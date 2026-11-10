"""GeoPandas municipal operations; GDAL/Rasterio retain geospatial computation."""
from __future__ import annotations

import html
import json
from pathlib import Path
import re

import geopandas as gpd
import numpy as np
import pandas as pd
import rasterio
from rasterio.features import rasterize
from rasterio.transform import from_origin
from shapely.geometry import shape

from urban_mcp_case.sources import active_folder, data_root, digest, recipe, rows_for, write_json


def slug(value):
    if not re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9_-]{0,47}", value):
        raise ValueError("run_id must be 1-48 letters, digits, underscores or hyphens")
    return value


def status():
    result = {"case": recipe()["id"], "municipality": recipe()["municipality"], "limits": recipe()["limits"], "inputs": "missing", "prepared": False}
    try:
        _, receipt = active_folder()
        quality = data_root() / "prepared/quality.json"
        q = json.loads(quality.read_text(encoding="utf-8")) if quality.is_file() else {}
        result.update(inputs="verified", snapshot=receipt["snapshot"], prepared=q.get("snapshot") == receipt["snapshot"] and q.get("preparation_code_sha256") == digest(Path(__file__)))
    except (ValueError, OSError) as exc:
        result["blocker"] = str(exc)
    return result


def prepare():
    folder, receipt = active_folder()
    spec = recipe()
    out = data_root() / "prepared"
    out.mkdir(exist_ok=True)
    districts_raw = rows_for(folder, receipt, "districts")
    units_raw = rows_for(folder, receipt, "units")
    services = rows_for(folder, receipt, "services")
    if len(districts_raw) != 34 or any(d["municipality"] != "helsinki" for d in districts_raw):
        raise ValueError("The admitted district contract requires exactly 34 Helsinki districts")
    districts = gpd.GeoDataFrame([
        {"district_id": str(d["origin_id"]), "name": d["name"].get("en", d["name"].get("fi")), "geometry": shape(d["boundary"])} for d in districts_raw
    ], crs="EPSG:4326")
    if not districts.geometry.is_valid.all() or districts.district_id.duplicated().any():
        raise ValueError("Invalid or duplicate district geometry/identity; review source instead of silently repairing")
    population = json.loads((folder / "population.json").read_text(encoding="utf-8"))
    if population["id"] != ["Osa-alue", "Ikä", "Vuosi", "Tiedot"] or population["size"] != [35, 1, 1, 1] or list(population["dimension"]["Vuosi"]["category"]["index"]) != [spec["population_year"]]:
        raise ValueError("Population dimensions/year changed")
    area_index = population["dimension"]["Osa-alue"]["category"]["index"]
    values = population["value"]
    pop_by_id = {code[4:7]: values[index] for code, index in area_index.items() if code != "0910000000"}
    if set(pop_by_id) != set(districts.district_id) or any(not isinstance(n, int) or n < 0 for n in pop_by_id.values()):
        raise ValueError("Population and geometry district identifiers do not match")
    districts["population_2025"] = districts.district_id.map(pop_by_id)
    municipality_population = values[area_index["0910000000"]]
    accepted, rejected = [], []
    for u in units_raw:
        loc = u.get("location")
        if u.get("municipality") != "helsinki":
            raise ValueError("Service source returned another municipality")
        if not loc or loc.get("type") != "Point":
            rejected.append({"unit_id": u["id"], "reason": "no_point_location"})
            continue
        point = shape(loc)
        if point.is_empty or not point.is_valid or not (-180 <= point.x <= 180 and -90 <= point.y <= 90):
            rejected.append({"unit_id": u["id"], "reason": "invalid_coordinate"})
            continue
        accepted.append({"unit_id": u["id"], "name": u["name"].get("en", u["name"].get("fi", str(u["id"]))), "service_ids": ",".join(map(str, sorted(u.get("services", [])))), "geometry": point})
    units = gpd.GeoDataFrame(accepted, crs="EPSG:4326")
    if units.unit_id.duplicated().any():
        raise ValueError("Duplicate unit identifiers")
    joined = gpd.sjoin(units, districts[["district_id", "geometry"]], how="left", predicate="within")
    ambiguous = joined.loc[joined.unit_id.duplicated(keep=False), "unit_id"].unique().tolist()
    if ambiguous:
        joined.loc[joined.unit_id.isin(ambiguous), "district_id"] = None
        joined = joined.drop_duplicates("unit_id")
    units = joined.drop(columns="index_right").copy()
    units["district_id"] = units.district_id.fillna("")
    units.to_file(out / "units.geojson", driver="GeoJSON")
    districts.to_file(out / "districts.geojson", driver="GeoJSON")
    units.to_crs(spec["analysis_crs"]).to_file(out / "units_metric.gpkg", driver="GPKG")
    districts.to_crs(spec["analysis_crs"]).to_file(out / "districts_metric.gpkg", driver="GPKG")
    write_json(out / "services.json", services)
    write_json(out / "rejected.json", rejected)
    projected = districts.to_crs(spec["analysis_crs"])
    x0, y0, x1, y1 = projected.total_bounds
    res = spec["district_raster_resolution_m"]
    transform = from_origin(x0, y1, res, res)
    width, height = int(np.ceil((x1-x0)/res)), int(np.ceil((y1-y0)/res))
    pixels = rasterize(((g, int(i)) for g, i in zip(projected.geometry, projected.district_id)), out_shape=(height, width), transform=transform, fill=0, dtype="uint16")
    with rasterio.open(out / "district_ids.tif", "w", driver="GTiff", height=height, width=width, count=1, dtype="uint16", crs=spec["analysis_crs"], transform=transform, nodata=0, compress="deflate") as dst:
        dst.write(pixels, 1)
        dst.update_tags(description="Cartographic district identifier; categorical, not population. Cell-centre rasterization at 100 m.", source="City of Helsinki Service Map; CC BY 4.0")
    quality = {"snapshot": receipt["snapshot"], "registry_units": len(units_raw), "valid_point_units": len(units), "rejected_units": len(rejected), "unmatched_point_units": int((units.district_id == "").sum()), "ambiguous_point_units": len(ambiguous), "districts": len(districts), "municipality_population_2025": municipality_population, "district_population_sum": int(districts.population_2025.sum()), "population_not_in_district_rows": int(municipality_population-districts.population_2025.sum()), "analysis_crs": spec["analysis_crs"], "limits": spec["limits"]}
    quality["datasets"] = {name: str(out/name) for name in ("units.geojson", "districts.geojson", "units_metric.gpkg", "districts_metric.gpkg", "district_ids.tif", "services.json", "rejected.json")}
    quality["population_reconciliation"] = f"{quality['population_not_in_district_rows']} is the arithmetic difference between the municipal total and the 34 selected statistical district rows in this snapshot. It is not a point-in-polygon result for residents; no resident coordinates were acquired. Do not infer that these residents live outside the polygons or lack services."
    quality["prepared_assets"] = [{"file": name, "sha256": digest(out/name), "bytes": (out/name).stat().st_size} for name in quality["datasets"]]
    quality["preparation_code_sha256"] = digest(Path(__file__))
    write_json(out / "quality.json", quality)
    return quality


def prepared():
    _, receipt = active_folder()
    folder = data_root() / "prepared"
    if not (folder / "quality.json").is_file():
        raise ValueError("Prepared data missing: run prepare_municipal_data first")
    quality = json.loads((folder / "quality.json").read_text(encoding="utf-8"))
    if quality.get("preparation_code_sha256") != digest(Path(__file__)):
        raise ValueError("Preparation implementation changed; prepare the admitted snapshot again")
    if quality["snapshot"] != receipt["snapshot"]:
        raise ValueError("Prepared data belongs to an older snapshot; prepare the active version")
    for asset in quality["prepared_assets"]:
        path = folder / asset["file"]
        if not path.is_file() or digest(path) != asset["sha256"]:
            raise ValueError("Prepared asset changed; prepare the admitted snapshot again")
    return folder, quality


def service_catalog(search="", limit=20):
    if not 1 <= limit <= 100 or len(search) > 120:
        raise ValueError("limit must be 1..100 and search at most 120 characters")
    folder, _ = prepared()
    rows = json.loads((folder / "services.json").read_text(encoding="utf-8"))
    matches = [{"id": s["id"], "names": s["name"]} for s in rows if search.casefold() in " ".join(s["name"].values()).casefold()]
    return {"total_matches": len(matches), "results": matches[:limit], "truncated": len(matches) > limit, "selection_semantics": "Exact service IDs attached by the source; counts do not expand a hierarchy."}


def inventory(service_ids=None, run_id="native"):
    slug(run_id)
    folder, quality = prepared()
    services = json.loads((folder / "services.json").read_text(encoding="utf-8"))
    allowed = {s["id"] for s in services}
    chosen = sorted(set(service_ids or []))
    if any(not isinstance(i, int) or isinstance(i, bool) or i not in allowed for i in chosen) or len(chosen) > 100:
        raise ValueError("Choose at most 100 existing numeric IDs from service_catalog; unknown IDs are not silently ignored")
    units = gpd.read_file(folder / "units.geojson")
    districts = gpd.read_file(folder / "districts.geojson")
    if chosen:
        keep = units.service_ids.fillna("").map(lambda ids: bool(set(map(int, ids.split(","))) & set(chosen)) if ids else False)
        units = units.loc[keep].copy()
    counts = units.loc[units.district_id != ""].groupby("district_id").size()
    districts["registered_units"] = districts.district_id.map(counts).fillna(0).astype(int)
    districts["units_per_10000_residents"] = districts.registered_units / districts.population_2025.replace(0, np.nan) * 10000
    table = districts.drop(columns="geometry").sort_values("district_id")
    out = data_root() / "results" / run_id
    out.mkdir(parents=True, exist_ok=True)
    table.to_csv(out / "district_inventory.csv", index=False, float_format="%.6f")
    districts.to_file(out / "district_inventory.geojson", driver="GeoJSON")
    units.to_file(out / "selected_units.geojson", driver="GeoJSON")
    labels = {s["id"]: s["name"].get("en", s["name"].get("fi")) for s in services}
    summary = {"case": recipe()["id"], "snapshot": quality["snapshot"], "municipality": "Helsinki", "population_year": 2025, "municipality_population": quality["municipality_population_2025"], "population_not_in_district_rows": quality["population_not_in_district_rows"], "districts": len(districts), "selected_service_ids": chosen, "selected_services": {str(i): labels[i] for i in chosen}, "selected_point_units": len(units), "assigned_point_units": int((units.district_id != "").sum()), "unmatched_point_units": int((units.district_id == "").sum()), "districts_with_zero_registered_units": table.loc[table.registered_units == 0, "district_id"].tolist(), "quality": quality, "limitations": recipe()["limits"], "artifacts": ["summary.json", "district_inventory.csv", "district_inventory.geojson", "selected_units.geojson", "report.html"]}
    summary["output_directory"] = str(out)
    write_json(out / "summary.json", summary)
    render_report(out, districts, units, summary, table)
    return summary


def render_report(out, districts, units, summary, table):
    projected = districts.to_crs(recipe()["analysis_crs"])
    x0, y0, x1, y1 = projected.total_bounds
    scale = 760 / max(x1-x0, y1-y0)
    def xy(x, y):
        return f"{20+(x-x0)*scale:.2f},{20+(y1-y)*scale:.2f}"
    shapes = []
    maximum = max(1, int(districts.registered_units.max()))
    for _, row in projected.iterrows():
        polygons = list(row.geometry.geoms) if row.geometry.geom_type == "MultiPolygon" else [row.geometry]
        d = " ".join("M" + " L".join(xy(x,y) for x,y,*_ in ring.coords) + " Z" for polygon in polygons for ring in [polygon.exterior, *polygon.interiors])
        opacity = .15 + .75*row.registered_units/maximum
        title = html.escape(f"{row['name']}: {row.registered_units} locations; population 2025: {row.population_2025}")
        shapes.append(f'<path d="{d}" fill="#137c85" fill-opacity="{opacity:.3f}" stroke="white" stroke-width=".6" fill-rule="evenodd"><title>{title}</title></path>')
    for point in units.to_crs(recipe()["analysis_crs"]).geometry:
        x,y=xy(point.x,point.y).split(",")
        shapes.append(f'<circle cx="{x}" cy="{y}" r="1.1" fill="#132f49" fill-opacity=".65"/>')
    limits = "".join("<li>"+html.escape(s)+"</li>" for s in summary["limitations"])
    content = '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Helsinki municipal inventory</title><style>body{font:16px system-ui;max-width:1100px;margin:40px auto;padding:0 20px;color:#142d3c;background:#f8faf9}h1{font-size:36px}svg{max-width:100%;background:#e7eef1}table{border-collapse:collapse;font-size:13px}th,td{padding:7px;border-bottom:1px solid #ccd7dc;text-align:left}code{overflow-wrap:anywhere}</style><h1>Helsinki · registered service locations</h1>'
    content += f'<p>{summary["selected_point_units"]} selected point locations · {summary["districts"]} districts · population at 31 December 2025: {summary["municipality_population"]:,}.</p><p>Service IDs: {html.escape(str(summary["selected_services"]))}. Snapshot: <code>{html.escape(summary["snapshot"])}</code>. Hover over a district for counts.</p>'
    content += '<p>'+html.escape(summary["quality"]["population_reconciliation"])+f' Registry quality: {summary["quality"]["rejected_units"]} entries without usable point geometry; {summary["quality"]["unmatched_point_units"]} valid points without a unique district.</p>'
    content += '<svg viewBox="0 0 800 800" role="img" aria-label="Helsinki districts and registered service points">'+"".join(shapes)+'</svg>'
    content += '<h2>District inventory</h2>'+table.to_html(index=False,escape=True,float_format=lambda x:f"{x:.2f}")+'<h2>Scope and limitations</h2><ul>'+limits+'</ul><p>Sources: City of Helsinki Service Map; City of Helsinki Urban Research and Statistics / Statistics Finland. CC BY 4.0. Analysis and transformations: Urban MCP contributors. No institutional endorsement implied.</p></html>'
    (out/"report.html").write_text(content,encoding="utf-8")


def read_artifact(run_id, name="summary.json"):
    slug(run_id)
    if name not in {"summary.json", "district_inventory.csv"}:
        raise ValueError("Inline artifacts are summary.json or district_inventory.csv; maps and GeoJSON are file artifacts")
    path = data_root() / "results" / run_id / name
    if not path.is_file():
        raise ValueError("Artifact missing: execute inventory_by_district for this run_id")
    if path.stat().st_size > 100_000:
        raise ValueError("Artifact is too large for inline delivery")
    return {"name": name, "sha256": digest(path), "content": json.loads(path.read_text(encoding="utf-8")) if name.endswith(".json") else path.read_text(encoding="utf-8")}
