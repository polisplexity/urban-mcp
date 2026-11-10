"""Native per-zone oracle and every exposed operation through a real stdio MCP."""
from __future__ import annotations

import csv
import json
import math
import os
from pathlib import Path
import sys
import time
from urllib.parse import quote
from uuid import uuid4

import geopandas as gpd
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import numpy as np
from pydantic import AnyUrl
import rasterio
from rasterio.features import geometry_mask, geometry_window
from rasterio.windows import Window, bounds as window_bounds

from . import data, engine


def payload(result):
    value = result.structuredContent
    if value is None:
        value = json.loads(next(c.text for c in result.content if hasattr(c, "text")))
    return value["result"] if isinstance(value, dict) and set(value) == {"result"} else value


def semantic(summary):
    return {k: v for k, v in summary.items() if k != "run_id"}


async def run(city):
    prefix = "check-" + uuid4().hex[:8]
    evidence = {"city": city, "transport": "MCP SDK real stdio subprocess", "checks": [], "tools_exercised": [], "failures": []}
    out = data.root()/"evidence"/city
    out.mkdir(parents=True, exist_ok=True)

    def check(name, condition, detail=None):
        value = bool(condition)
        evidence["checks"].append({"name": name, "passed": value, "detail": detail})
        if not value:
            evidence["failures"].append(name)
        print(json.dumps({"check": name, "passed": value}), flush=True)

    quality = engine.prepare(city)
    folder, _, manifest = engine.prepared(city)
    baseline = engine.analyze(city, prefix+"-native")
    sensitivity = engine.analyze(city, prefix+"-native-sensitivity", .4)
    comparison = engine.compare(city, baseline["run_id"], sensitivity["run_id"])
    zones = gpd.read_file(folder/"zones_metric.gpkg").sort_values("zone_index")
    indexed = {r["zone_id"]: r for r in baseline["zones"]}
    mismatches = []
    # Separate per-polygon windows/masks and np.unique, not the composite label/bincount implementation.
    with rasterio.open(folder/"landcover.tif") as src:
        for zone in zones.itertuples():
            window = geometry_window(src, [zone.geometry])
            pixels = src.read(1, window=window)
            inside = geometry_mask([zone.geometry], pixels.shape, src.window_transform(window), invert=True, all_touched=False)
            codes, counts = np.unique(pixels[inside], return_counts=True)
            histogram = dict(zip(map(int, codes), map(int, counts)))
            total = sum(histogram.values())
            valid = total - histogram.get(0, 0)
            land = valid - histogram.get(80, 0)
            vegetated = sum(histogram.get(code, 0) for code in data.recipe()["vegetation_classes"])
            row = indexed[zone.zone_id]
            share = vegetated/land if land else None
            if row["total_pixels"] != total or row["valid_land_pixels"] != land or row["vegetation_pixels"] != vegetated or row["vegetation_share_of_valid_land"] != share or any(row["class_counts"][str(code)] != histogram.get(int(code),0) for code in row["class_counts"]):
                mismatches.append(zone.zone_id)
    check("every zone/class/denominator equals independent polygon-window oracle", not mismatches and len(indexed) == len(zones) > 0, mismatches)
    check("all zones retained including unknown population or all-water", baseline["zone_count"] == manifest["zones"] and {r["zone_id"] for r in baseline["zones"]} == set(zones.zone_id))
    check("unknown population stays null and is never a negative sentinel", sorted(r["zone_id"] for r in baseline["zones"] if r["population"] is None) == manifest["population"]["unknown_population_zone_ids"] and all(r["population"] is None or r["population"] >= 0 for r in baseline["zones"]))
    check("published municipal and zone population reconciliation is explicit", sum(r["population"] for r in baseline["zones"] if r["population"] is not None) == manifest["population"]["zone_population_sum"] and baseline["population_reconciliation"]["municipal_minus_zone_population"] == manifest["population"]["municipal_population"] - manifest["population"]["zone_population_sum"])
    for summary in [baseline, sensitivity]:
        expected_ids = sorted(r["zone_id"] for r in summary["zones"] if r["vegetation_share_of_valid_land"] is not None and r["vegetation_share_of_valid_land"] < summary["threshold"])
        check("strict threshold IDs agree with all actual row fractions / " + str(summary["threshold"]), summary["low_vegetation_zone_ids"] == expected_ids and sum(r["population"] for r in summary["zones"] if r["zone_id"] in expected_ids and r["population"] is not None) == summary["population_in_low_vegetation_zones"])
    check("water and NoData are excluded only from declared land denominator", all(r["valid_land_pixels"] + r["water_pixels"] == r["valid_pixels"] and r["valid_pixels"] + r["nodata_pixels"] == r["total_pixels"] for r in baseline["zones"]))
    check("all-water and empty classes remain unknown rather than low", all(r["low_vegetation"] is None for r in baseline["zones"] if r["valid_land_pixels"] == 0))
    check("threshold sensitivity preserves class-count bytes", data.sha(data.root()/"results"/city/baseline["run_id"]/"class_counts.csv") == data.sha(data.root()/"results"/city/sensitivity["run_id"]/"class_counts.csv"))
    check("raising threshold cannot remove a previously low-share zone", not comparison["no_longer_below_threshold_zone_ids"] and set(baseline["low_vegetation_zone_ids"]) <= set(sensitivity["low_vegetation_zone_ids"]))
    check("tree-class metric remains a distinct component", all(r["tree_class_pixels"] <= r["vegetation_pixels"] <= r["valid_land_pixels"] for r in baseline["zones"]))
    params = StdioServerParameters(command=sys.executable, args=["-m", "urban_mcp_vegetation", "serve"], env=dict(os.environ))
    work = data.root()/"results"/city/(prefix+"-upstream")
    work.mkdir(parents=True)
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as client:
            initial = await client.initialize()
            evidence["protocol_version"] = initial.protocolVersion
            tools = (await client.list_tools()).tools
            names = {t.name for t in tools}
            data.dump(out/"mcp-tools.json", [t.model_dump(mode="json") for t in tools])
            check("original 13 tools plus eight municipal tools are exposed", len(names) == 21)

            async def invoke(name, args=None, error=None):
                started = time.monotonic()
                result = await client.call_tool(name, args or {})
                evidence["tools_exercised"].append(name)
                message = " ".join(getattr(c,"text","") for c in result.content)
                correct = bool(result.isError) == bool(error) and (not error or error in message)
                check(name + (" / expected rejection" if error else " / call"), correct, {"seconds": round(time.monotonic()-started,3), "error": message if result.isError else None})
                if result.isError and not error:
                    raise RuntimeError(message)
                return None if result.isError else payload(result)

            await invoke("vegetation_status")
            await invoke("harvest_vegetation_data", {"city":city,"mode":"snapshot"})
            remote_quality = await invoke("prepare_vegetation_data", {"city":city})
            check("native/MCP preparation receipts identical", remote_quality == quality)
            classes = await invoke("vegetation_class_catalog")
            check("class catalog includes cropland but excludes water", {c["code"] for c in classes["classes"] if c["included_in_vegetation"]} == set(data.recipe()["vegetation_classes"]) and 80 not in classes["vegetation_classes"])
            remote = await invoke("analyze_vegetation", {"city":city,"run_id":prefix+"-mcp"})
            remote_sensitivity = await invoke("analyze_vegetation", {"city":city,"run_id":prefix+"-mcp-sensitivity","threshold":.4})
            check("complete native/MCP baseline zone diagnostics identical", semantic(remote) == semantic(baseline))
            check("complete native/MCP sensitivity diagnostics identical", semantic(remote_sensitivity) == semantic(sensitivity))
            remote_compare = await invoke("vegetation_compare", {"city":city,"baseline_id":remote["run_id"],"scenario_id":remote_sensitivity["run_id"]})
            normalize = lambda value: {k:v for k,v in value.items() if k not in {"baseline_id","scenario_id"}}
            check("native/MCP threshold comparison identical", normalize(remote_compare) == normalize(comparison))
            for filename in ["zone_metrics.csv","class_counts.csv"]:
                chunks, offset = [], 0
                while True:
                    artifact = await invoke("read_vegetation_artifact", {"city":city,"run_id":remote["run_id"],"name":filename,"offset":offset,"limit":2000})
                    chunks.append(artifact["text"])
                    if artifact["next_offset"] is None: break
                    offset = artifact["next_offset"]
                native_path = data.root()/"results"/city/baseline["run_id"]/filename
                check(filename + " exact native/MCP bytes and complete pagination", artifact["sha256"] == data.sha(native_path) and "".join(chunks) == native_path.read_text(encoding="utf-8"))
            native_map = engine.render(city, baseline["run_id"])
            remote_map = await invoke("render_vegetation_map", {"city":city,"run_id":remote["run_id"]})
            check("native/MCP rendered map bytes identical", native_map["sha256"] == remote_map["sha256"] and remote_map["bytes"] > 10000)
            raster, vector = folder/"landcover.tif", folder/"zones.geojson"
            info = await invoke("vector_info", {"uri":str(vector)})
            check("original vector_info matches source zone count", info["feature_count"] == len(zones))
            converted = work/"zones.gpkg"
            await invoke("vector_convert", {"uri":str(vector),"output":str(converted),"driver":"GPKG"})
            source_zones = gpd.read_file(vector)
            restored = gpd.read_file(converted)
            check("original conversion preserves zone IDs and geometry", restored.zone_id.tolist() == source_zones.zone_id.tolist() and restored.geometry.geom_equals_exact(source_zones.geometry,1e-9).all())

            async def justify(tool, domain, prompt, arguments, method):
                result = await client.get_prompt(prompt, {k:json.dumps(v) if isinstance(v,(dict,list)) else str(v) for k,v in arguments.items()})
                check(prompt + " / prompt", bool(result.messages))
                return await invoke("store_justification", {"tool_name":tool,"domain":domain,"prompt_name":prompt,"prompt_args":arguments,"justification":{"intent":"Historical categorical vegetation and aggregate municipal population context","alternatives":[],"choice":{"method":method,"rationale":"Use declared CRS, pixel grid and categorical semantics; do not infer access, canopy or temperature.","tradeoffs":"Exploratory, temporally mismatched source observations; preserve classification and boundary uncertainty."},"confidence":"high"}})

            crs = data.city_config(city)["analysis_crs"]
            metric = work/"zones_metric.gpkg"
            await justify("vector_reproject","crs_datum","justify_crs_selection",{"dst_crs":crs},crs)
            await invoke("vector_reproject", {"uri":str(vector),"output":str(metric),"dst_crs":crs})
            metric_zones = gpd.read_file(metric)
            check("original reprojection agrees with native projected geometries", metric_zones.geometry.geom_equals_exact(source_zones.to_crs(crs).geometry,1e-6).all())
            buffers = work/"buffers.gpkg"
            await invoke("vector_buffer", {"uri":str(metric),"output":str(buffers),"distance":100})
            buffer_zones = gpd.read_file(buffers)
            check("original 100 m buffer agrees with native area", buffer_zones.zone_id.tolist() == metric_zones.zone_id.tolist() and np.allclose(buffer_zones.area, metric_zones.buffer(100).area,rtol=.0001,atol=1))
            xmin,ymin,xmax,ymax = source_zones.total_bounds
            bbox = [xmin,ymin,(xmin+xmax)/2,(ymin+ymax)/2]
            clip = work/"clip.geojson"
            await invoke("vector_clip", {"uri":str(vector),"output":str(clip),"bounds":bbox})
            expected_clip = gpd.clip(source_zones,bbox)
            check("original clipping agrees with native zone subset", len(expected_clip)>0 and set(gpd.read_file(clip).zone_id)==set(expected_clip.zone_id))
            query_args = {"geometry":bbox,"purpose":"Bounded zone inspection in declared WGS84 coordinates"}
            await justify("vector_query","spatial_query","justify_query_extent",query_args,"Bounding window")
            query = await invoke("vector_query", {"uri":str(vector),"output":str(work/"query.geojson"),**query_args})
            check("original vector query agrees with native subset", set(gpd.read_file(work/"query.geojson").zone_id)==set(expected_clip.zone_id))
            check("original vector query resource is readable", bool((await client.read_resource(AnyUrl(query["query"]["uri"]))).contents))
            simplified = work/"simplified.gpkg"
            await invoke("vector_simplify", {"uri":str(metric),"output":str(simplified),"tolerance":20})
            check("original simplify agrees with native metric tolerance", gpd.read_file(simplified).geometry.geom_equals_exact(metric_zones.geometry.simplify(20,preserve_topology=True),1e-7).all())
            raster_info = await invoke("raster_info", {"uri":str(raster)})
            stats = await invoke("raster_stats", {"uri":str(raster),"params":{"include_histogram":True}})
            with rasterio.open(raster) as source:
                pixels = source.read(1)
                masked = source.read(1,masked=True)
                crop = Window(source.width//2,source.height//2,30,30)
                extent = list(window_bounds(crop,source.transform))
                expected_crop = source.read(window=crop)
                check("original raster metadata/statistics match native cells", raster_info["width"]==source.width and stats["band_stats"][0]["valid_count"]==masked.count() and np.isclose(stats["band_stats"][0]["mean"],masked.mean(),atol=1e-9,rtol=0))
            cog = work/"classes_cog.tif"
            await invoke("raster_convert", {"uri":str(raster),"output":str(cog),"options":{"driver":"COG","compression":"deflate","overviews":[2,4],"overview_resampling":"nearest"}})
            with rasterio.open(cog) as result:
                check("original COG preserves all categorical pixels and nearest overviews", np.array_equal(result.read(1),pixels) and result.overviews(1)==[2,4] and result.tags(ns="IMAGE_STRUCTURE").get("LAYOUT")=="COG")
            raster_query = {"geometry":extent,"purpose":"Exact 30 by 30 native categorical raster window in metres"}
            await justify("raster_query","spatial_query","justify_query_extent",raster_query,"Integer pixel window")
            query = await invoke("raster_query", {"uri":str(raster),"output":str(work/"tile.tif"),**raster_query})
            with rasterio.open(work/"tile.tif") as result:
                check("original raster query matches exact native window", np.array_equal(result.read(),expected_crop))
            check("original raster query resource is readable", bool((await client.read_resource(AnyUrl(query["query"]["uri"]))).contents))
            await justify("raster_reproject","crs_datum","justify_crs_selection",{"dst_crs":"EPSG:3857"},"Display only")
            await justify("raster_reproject","resampling","justify_resampling_method",{"method":"nearest"},"Categorical nearest")
            await invoke("raster_reproject", {"uri":str(raster),"output":str(work/"display.tif"),"dst_crs":"EPSG:3857","resampling":"nearest"})
            with rasterio.open(work/"display.tif") as result:
                check("original nearest reprojection preserves class domain", result.crs.to_epsg()==3857 and set(np.unique(result.read(1))) <= set(np.unique(pixels)))

            await invoke("analyze_vegetation", {"city":city,"run_id":"invalid","threshold":1.1},error="threshold must")
            await invoke("analyze_vegetation", {"city":city,"run_id":remote["run_id"]},error="already exists")
            await invoke("analyze_vegetation", {"city":city,"run_id":"../outside"},error="run_id must")
            await invoke("harvest_vegetation_data", {"city":"unknown"},error="Unknown city")
            await invoke("read_vegetation_artifact", {"city":city,"run_id":remote["run_id"],"name":"../../manifest.json"},error="not allowed")
            await invoke("read_vegetation_artifact", {"city":city,"run_id":remote["run_id"],"limit":100000},error="limit must")
            await invoke("vector_buffer", {"uri":str(vector),"output":str(work/"bad-buffer.gpkg"),"distance":100},error="degrees are not metres")
            await invoke("raster_reproject", {"uri":str(raster),"output":str(work/"bad-interpolation.tif"),"dst_crs":"EPSG:3857","resampling":"bilinear"},error="require nearest or mode")
            await invoke("raster_reproject", {"uri":str(raster),"output":str(work/"bad-dimensions.tif"),"dst_crs":crs,"resampling":"nearest","width":20,"height":20},error="Explicit bounds/width/height")
            await invoke("raster_reproject", {"uri":str(raster),"output":str(work/"bad-bounds.tif"),"dst_crs":crs,"resampling":"nearest","bounds":[0,0,100,100]},error="Explicit bounds/width/height")
            await invoke("raster_convert", {"uri":str(raster),"output":str(work/"bad-cog.tif"),"options":{"driver":"COG","overviews":[2]}},error="Categorical overviews require")
            await invoke("vector_info", {"uri":"/etc/passwd"},error="outside")
            resources = (await client.list_resources()).resources
            templates = (await client.list_resource_templates()).resourceTemplates
            data.dump(out/"mcp-resources.json", {"resources":[r.model_dump(mode="json") for r in resources],"templates":[t.model_dump(mode="json") for t in templates]})
            file_vector,file_raster = quote(str(vector),safe=""),quote(str(raster),safe="")
            uris = [str(r.uri) for r in resources] + [f"vegetation://{city}/manifest", f"vegetation://{city}/quality", "catalog://workspace/all/prepared", "catalog://workspace/vector/prepared", "catalog://workspace/raster/prepared", "catalog://workspace/summary/current", "catalog://workspace/by-crs/"+crs.split(":")[1], "reference://compression/available/all", "reference://crs/common/all", "reference://glossary/geospatial/all", "reference://resampling/available/all", "reference://resampling/guide/nearest", f"metadata://{file_vector}/format", f"metadata://{file_vector}/vector", f"metadata://{file_raster}/raster", f"metadata://{file_raster}/bands/current", f"metadata://{file_raster}/statistics"]
            for uri in uris:
                result = await client.read_resource(AnyUrl(uri))
                check("resource " + uri, bool(result.contents))
            prompts = (await client.list_prompts()).prompts
            data.dump(out/"mcp-prompts.json", [p.model_dump(mode="json") for p in prompts])
            result = await client.get_prompt("municipal_vegetation_review", {"city":city})
            check("municipal workflow prompt", bool(result.messages))
            check("every exposed original and added tool exercised", set(evidence["tools_exercised"]) == names, {"advertised":sorted(names),"exercised":sorted(set(evidence["tools_exercised"]))})
    evidence.update(checks_passed=sum(c["passed"] for c in evidence["checks"]), native_baseline=baseline["run_id"], native_sensitivity=sensitivity["run_id"], mcp_baseline=remote["run_id"], mcp_sensitivity=remote_sensitivity["run_id"], input_manifest_sha256=data.sha(data.root()/"inputs"/city/"manifest.json"), implementation_sha256=data.sha(Path(engine.__file__)))
    for filename, value in [("native.json",baseline),("native-sensitivity.json",sensitivity),("native-comparison.json",comparison),("mcp.json",evidence)]:
        data.dump(out/filename,value)
    if evidence["failures"]:
        raise AssertionError(evidence["failures"])
    return {"city":city,"checks_passed":evidence["checks_passed"],"tools_exercised":len(names),"evidence":str(out)}
