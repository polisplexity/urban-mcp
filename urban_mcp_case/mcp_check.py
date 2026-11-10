"""Exercise every exposed tool over a real stdio MCP subprocess, with native checks."""
from __future__ import annotations

import asyncio
import json
import math
import os
from pathlib import Path
import sys
import time
from urllib.parse import quote

import geopandas as gpd
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import numpy as np
from pydantic import AnyUrl
import rasterio
from rasterio.windows import Window, bounds as window_bounds

from urban_mcp_case import analysis, sources


def payload(result):
    data = getattr(result, "structuredContent", None)
    if data is None:
        data = json.loads(next(c.text for c in result.content if hasattr(c, "text")))
    if isinstance(data, dict) and set(data) == {"result"}:
        data = data["result"]
    return data


async def run():
    root = sources.data_root()
    out = root / "evidence"
    out.mkdir(parents=True, exist_ok=True)
    work = root / "results/protocol"
    work.mkdir(parents=True, exist_ok=True)
    evidence = {"transport": "stdio subprocess", "checks": [], "tools_exercised": [], "failures": [], "limits": sources.recipe()["limits"]}
    def record(name, passed, detail=None):
        evidence["checks"].append({"name": name, "passed": bool(passed), "detail": detail})
        if not passed:
            evidence["failures"].append(name)
        print(json.dumps({"check": name, "passed": bool(passed)}, ensure_ascii=False), flush=True)

    params = StdioServerParameters(command=sys.executable, args=["-m", "urban_mcp_case", "serve"], env=dict(os.environ))
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as client:
            initial = await client.initialize()
            evidence["protocol_version"] = initial.protocolVersion
            tools = (await client.list_tools()).tools
            sources.write_json(out / "mcp-tools.json", [t.model_dump(mode="json") for t in tools])
            async def invoke(name, args=None, expected_error=False, expected_message=None):
                started = time.monotonic()
                result = await client.call_tool(name, args or {})
                evidence["tools_exercised"].append(name)
                correct = bool(result.isError) == expected_error
                if expected_message:
                    correct = correct and expected_message in " ".join(getattr(c,"text","") for c in result.content)
                record(name + (" / expected rejection" if expected_error else " / call"), correct, {"seconds": round(time.monotonic()-started, 3), "error": result.model_dump(mode="json") if result.isError else None})
                return None if result.isError else payload(result)

            await invoke("municipal_status")
            # The same acquisition entrypoint is tested offline against the pinned archive.
            if (sources.CASE / "snapshot.lock.json").is_file():
                await invoke("harvest_municipal_sources", {"mode": "snapshot"})
            else:
                await invoke("harvest_municipal_sources", {"mode": "invalid"}, expected_error=True)
            quality = await invoke("prepare_municipal_data")
            if quality is None:
                raise RuntimeError("Preparation failed; inspect the recorded MCP error")
            catalog = await invoke("service_catalog", {"search": "librar", "limit": 100})
            sources.write_json(out / "library-catalog.json", catalog)
            # Select the source's exact general library category, not every book-related service.
            exact = [s["id"] for s in catalog["results"] if any(n.casefold() in {"public libraries", "yleiset kirjastot"} for n in s["names"].values())]
            record("general library category found", len(exact) == 1, exact)
            if not exact:
                raise RuntimeError("Review the service taxonomy; no general library ID selected")
            native = analysis.inventory(exact, "native-library")
            summary = await invoke("inventory_by_district", {"service_ids": exact, "run_id": "protocol-library"})
            def semantic(result):
                result = json.loads(json.dumps(result))
                result.pop("output_directory", None)
                result["quality"].pop("prepared_assets", None)
                return result
            record("municipal native/MCP results identical", semantic(summary) == semantic(native))
            await invoke("read_case_artifact", {"run_id": "protocol-library", "name": "district_inventory.csv"})
            await invoke("inventory_by_district", {"service_ids": [999999999], "run_id": "invalid"}, expected_error=True, expected_message="unknown IDs")
            await invoke("read_case_artifact", {"run_id": "../outside"}, expected_error=True, expected_message="run_id")
            await invoke("service_catalog", {"limit": 1000}, expected_error=True, expected_message="limit")
            await invoke("vector_info", {"uri": "missing.geojson"}, expected_error=True, expected_message="Cannot open vector")
            await invoke("vector_info", {"uri": "/etc/passwd"}, expected_error=True)
            units = root / "results/protocol-library/selected_units.geojson"
            vector = gpd.read_file(units)
            info = await invoke("vector_info", {"uri": str(units)})
            record("vector metadata agrees with native", info["feature_count"] == len(vector))
            await invoke("vector_buffer", {"uri": str(units), "output": str(work/"invalid-degree-buffer.gpkg"), "distance": 500}, expected_error=True, expected_message="degrees are not metres")
            converted = work / "libraries.gpkg"
            await invoke("vector_convert", {"uri": str(units), "output": str(converted), "driver": "GPKG"})
            restored = gpd.read_file(converted)
            record("vector conversion preserves IDs and geometry", restored.unit_id.tolist() == vector.unit_id.tolist() and restored.geometry.geom_equals_exact(vector.geometry, 1e-10).all())

            async def justify(tool, domain, prompt_name, prompt_args, method, rationale):
                prompt = await client.get_prompt(prompt_name, {k: json.dumps(v) if isinstance(v, (dict,list)) else str(v) for k,v in prompt_args.items()})
                record(prompt_name + " / prompt", bool(prompt.messages))
                return await invoke("store_justification", {"tool_name": tool, "domain": domain, "prompt_name": prompt_name, "prompt_args": prompt_args, "justification": {"intent": "Reproducible Helsinki municipal cartography", "alternatives": [], "choice": {"method": method, "rationale": rationale, "tradeoffs": "Scope restricted to the published case; no accessibility or population-grid claim."}, "confidence": "high"}})

            metric = work / "libraries_metric.gpkg"
            await justify("vector_reproject", "crs_datum", "justify_crs_selection", {"dst_crs": "EPSG:3067"}, "EPSG:3067", "ETRS-TM35FIN uses metres and covers Finland; buffers are geometric distances, not walking times.")
            await invoke("vector_reproject", {"uri": str(units), "output": str(metric), "dst_crs": "EPSG:3067"})
            expected = vector.to_crs("EPSG:3067")
            projected = gpd.read_file(metric)
            record("vector reprojection agrees with native coordinates", np.allclose(projected.geometry.x, expected.geometry.x, rtol=0, atol=1e-6) and np.allclose(projected.geometry.y, expected.geometry.y, rtol=0, atol=1e-6))
            buffer_path = work / "library_buffers.gpkg"
            await invoke("vector_buffer", {"uri": str(metric), "output": str(buffer_path), "distance": 500.0})
            buffered = gpd.read_file(buffer_path)
            areas = buffered.geometry.area
            record("500 metre buffer area within 1 percent of circle", len(buffered) == len(projected) > 0 and set(buffered.unit_id) == set(projected.unit_id) and bool(np.allclose(areas, math.pi*500**2, rtol=.01)))
            await invoke("vector_buffer", {"uri": str(metric), "output": str(work / "bad-buffer.gpkg"), "distance": -1}, expected_error=True, expected_message="greater than 0")
            districts = gpd.read_file(root / "prepared/districts.geojson")
            bbox = [24.90, 60.15, 24.98, 60.20]
            clipped = work / "libraries_clipped.geojson"
            await invoke("vector_clip", {"uri": str(units), "output": str(clipped), "bounds": bbox})
            native_clip = gpd.clip(vector, bbox)
            record("vector clipping preserves the expected subset", len(native_clip) > 0 and set(gpd.read_file(clipped).unit_id) == set(native_clip.unit_id))
            query_path = work / "library_query.geojson"
            query_args = {"geometry": bbox, "purpose": "Inspect registered libraries inside the city-centre bounding box"}
            await justify("vector_query", "spatial_query", "justify_query_extent", query_args, "Bounding box", "Coordinates are WGS84 longitude/latitude and select a city-centre inspection extent.")
            query = await invoke("vector_query", {"uri": str(units), "output": str(query_path), **query_args})
            record("vector query agrees with native extent selection", set(gpd.read_file(query_path).unit_id) == set(native_clip.unit_id))
            if query:
                resource = await client.read_resource(AnyUrl(query["query"]["uri"]))
                record("query result resource", bool(resource.contents))
            simplified = work / "districts_simplified.gpkg"
            await invoke("vector_simplify", {"uri": str(root / "prepared/districts_metric.gpkg"), "output": str(simplified), "tolerance": 20.0})
            original = gpd.read_file(root / "prepared/districts_metric.gpkg")
            simple = gpd.read_file(simplified)
            record("simplification agrees with native tolerance and IDs", simple.district_id.tolist() == original.district_id.tolist() and simple.geometry.geom_equals_exact(original.geometry.simplify(20, preserve_topology=True), 1e-8).all())

            raster = root / "prepared/district_ids.tif"
            await invoke("raster_info", {"uri": str(raster)})
            stats = await invoke("raster_stats", {"uri": str(raster), "params": {"include_histogram": True}})
            with rasterio.open(raster) as src:
                cells = src.read(1, masked=True)
                source_array = src.read(1)
                crop = Window(10, 10, 30, 30)
                extent = list(window_bounds(crop, src.transform))
                expected_crop = src.read(window=crop)
                record("raster statistics agree with native masked cells", stats["band_stats"][0]["valid_count"] == cells.count() and np.isclose(stats["band_stats"][0]["mean"], cells.mean(), rtol=0, atol=1e-8))
            cog = work / "district_ids_cog.tif"
            await invoke("raster_convert", {"uri": str(raster), "output": str(cog), "options": {"driver": "COG", "compression": "deflate", "overviews": [2,4], "overview_resampling": "nearest"}})
            with rasterio.open(cog) as src:
                record("COG conversion preserves categorical pixels", np.array_equal(src.read(1), source_array))
                record("COG layout and overviews preserved", src.tags(ns="IMAGE_STRUCTURE").get("LAYOUT") == "COG" and src.overviews(1) == [2,4])
            raster_query_args = {"geometry": extent, "purpose": "Extract a 30 by 30 pixel cartographic district-ID tile in metric coordinates"}
            await justify("raster_query", "spatial_query", "justify_query_extent", raster_query_args, "Native raster window", "Extent is derived from an integer native pixel window; the raster is categorical district IDs.")
            tile = work / "district_tile.tif"
            await invoke("raster_query", {"uri": str(raster), "output": str(tile), **raster_query_args})
            with rasterio.open(tile) as src:
                record("raster query pixels match native window", np.array_equal(src.read(), expected_crop))
            await justify("raster_reproject", "crs_datum", "justify_crs_selection", {"dst_crs": "EPSG:3857"}, "EPSG:3857", "Web-display derivative only; preserve EPSG:3067 for metric analysis.")
            await justify("raster_reproject", "resampling", "justify_resampling_method", {"method": "nearest"}, "nearest", "District identifiers are categorical; interpolation must not invent district codes.")
            warped = work / "district_web.tif"
            await invoke("raster_reproject", {"uri": str(raster), "output": str(warped), "dst_crs": "EPSG:3857", "resampling": "nearest"})
            with rasterio.open(warped) as src:
                record("raster reprojection preserves class domain", src.crs.to_epsg() == 3857 and np.count_nonzero(src.read(1)) > 0 and set(np.unique(src.read(1))) <= set(np.unique(source_array)))
            invalid_query = {"geometry": [1,1,0,0], "purpose": "Deliberate invalid extent contract test"}
            await justify("raster_query", "spatial_query", "justify_query_extent", invalid_query, "Negative test", "This deliberately invalid extent must be rejected; it is not an analysis extent.")
            await invoke("raster_query", {"uri": str(raster), **invalid_query}, expected_error=True, expected_message="Bounding box must satisfy")

            resources = (await client.list_resources()).resources
            templates = (await client.list_resource_templates()).resourceTemplates
            sources.write_json(out / "mcp-resources.json", {"resources": [r.model_dump(mode="json") for r in resources], "templates": [t.model_dump(mode="json") for t in templates]})
            file_vector = quote(str(units), safe="")
            file_raster = quote(str(raster), safe="")
            uris = [str(r.uri) for r in resources] + [
                "catalog://workspace/all/prepared", "catalog://workspace/vector/prepared", "catalog://workspace/raster/prepared", "catalog://workspace/summary/current", "catalog://workspace/by-crs/3067",
                "reference://compression/available/all", "reference://crs/common/all", "reference://glossary/geospatial/all", "reference://resampling/available/all", "reference://resampling/guide/nearest",
                f"metadata://{file_vector}/format", f"metadata://{file_vector}/vector", f"metadata://{file_raster}/raster", f"metadata://{file_raster}/bands/current", f"metadata://{file_raster}/statistics",
            ]
            for uri in uris:
                try:
                    resource = await client.read_resource(AnyUrl(uri))
                    record("resource " + uri, bool(resource.contents))
                except Exception as exc:
                    record("resource " + uri, False, str(exc))
            prompts = (await client.list_prompts()).prompts
            sources.write_json(out / "mcp-prompts.json", [p.model_dump(mode="json") for p in prompts])
            task = await client.get_prompt("municipal_inventory_task", {"service_query": "library"})
            record("municipal workflow prompt", bool(task.messages))
            called = set(evidence["tools_exercised"])
            record("every exposed tool exercised", called == {t.name for t in tools}, {"untested": sorted({t.name for t in tools}-called), "count": len(tools)})
    evidence["tools_exercised"] = sorted(set(evidence["tools_exercised"]))
    evidence["status"] = "passed" if not evidence["failures"] else "failed"
    sources.write_json(out / "mcp-check.json", evidence)
    return evidence


def main():
    result = asyncio.run(run())
    print(json.dumps({"status": result["status"], "checks": len(result["checks"]), "tools": len(result["tools_exercised"]), "failures": result["failures"]}, ensure_ascii=False, indent=2))
    if result["failures"]:
        raise SystemExit(1)
