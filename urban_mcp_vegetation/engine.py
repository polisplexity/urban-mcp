"""Categorical zonal accounting on native Rasterio/GDAL and GeoPandas APIs."""
from __future__ import annotations

import csv
import importlib.metadata
import json
import math
from pathlib import Path
import re
from threading import RLock

import geopandas as gpd
import numpy as np
import pandas as pd
import rasterio
from rasterio.enums import MergeAlg, Resampling
from rasterio.features import rasterize
from rasterio.transform import from_origin
from rasterio.warp import reproject

from . import data

_LOCK = RLock()


def token(value):
    if not isinstance(value, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,47}", value):
        raise ValueError("run_id must be 1-48 letters, digits, underscores or hyphens")
    return value


def class_catalog():
    spec = data.recipe()
    return {"classes": [{"code": int(code), "name": name, "included_in_vegetation": int(code) in spec["vegetation_classes"]} for code, name in spec["classes"].items()], "vegetation_classes": spec["vegetation_classes"], "nodata": 0, "water_class": 80, "denominator": "valid pixels excluding permanent water; report all-surface share separately", "limits": spec["limits"]}


def paths(city):
    data.city_config(city)
    return data.root() / "prepared" / city


def prepared(city):
    base, manifest = data.verify(city)
    folder = paths(city)
    quality = json.loads((folder / "quality.json").read_text(encoding="utf-8"))
    if quality["input_manifest_sha256"] != data.sha(base / "manifest.json") or quality["implementation_sha256"] != data.sha(Path(__file__)):
        raise ValueError("Prepared data identity changed; use a fresh workspace and prepare again")
    for name, receipt in quality["files"].items():
        if data.sha(folder / name) != receipt["sha256"] or (folder / name).stat().st_size != receipt["bytes"]:
            raise ValueError("Prepared integrity failure: " + name)
    return folder, quality, manifest


def prepare(city):
    with _LOCK:
        folder = paths(city)
        if folder.exists():
            return prepared(city)[1]
        base, manifest = data.verify(city)
        spec, cfg = data.recipe(), data.city_config(city)
        zones = gpd.read_file(base / "zones.geojson").sort_values("zone_id").reset_index(drop=True).to_crs(cfg["analysis_crs"])
        if len(zones) != manifest["zones"] or not zones.geometry.is_valid.all() or zones.zone_id.duplicated().any():
            raise ValueError("Zone geometry/identity changed")
        x0, y0, x1, y1 = zones.total_bounds
        res = spec["resolution_m"]
        left, top = math.floor(x0/res)*res, math.ceil(y1/res)*res
        width, height = math.ceil((x1-left)/res), math.ceil((top-y0)/res)
        if width * height > 30_000_000:
            raise ValueError("Study grid exceeds the admitted 30 million pixel budget")
        transform = from_origin(left, top, res, res)
        grid = np.zeros((height, width), dtype="uint8")
        for item in manifest["source_tiles"]:
            warped = np.zeros_like(grid)
            with rasterio.open(base / item["file"]) as source:
                reproject(rasterio.band(source, 1), warped, src_transform=source.transform, src_crs=source.crs, src_nodata=0, dst_transform=transform, dst_crs=cfg["analysis_crs"], dst_nodata=0, resampling=Resampling.nearest, num_threads=1)
            conflicts = (grid != 0) & (warped != 0) & (grid != warped)
            if conflicts.any():
                raise ValueError("Source tiles disagree on overlapping destination pixels")
            grid[warped != 0] = warped[warped != 0]
        labels = rasterize(((geometry, i+1) for i, geometry in enumerate(zones.geometry)), out_shape=grid.shape, transform=transform, fill=0, dtype="uint16", all_touched=False)
        occupancy = rasterize(((geometry, 1) for geometry in zones.geometry), out_shape=grid.shape, transform=transform, fill=0, dtype="uint16", all_touched=False, merge_alg=MergeAlg.add)
        if (occupancy > 1).any():
            raise ValueError("Zone polygons assign overlapping pixel centres; review boundaries before aggregation")
        if not set(np.unique(grid)).issubset({0, *map(int, spec["classes"])}):
            raise ValueError("Unknown land-cover class code")
        folder.mkdir(parents=True)
        zones["zone_index"] = np.arange(1, len(zones)+1)
        zones.to_file(folder / "zones_metric.gpkg", driver="GPKG")
        zones.to_crs(4326).to_file(folder / "zones.geojson", driver="GeoJSON")
        profile = {"driver": "GTiff", "height": height, "width": width, "count": 1, "crs": cfg["analysis_crs"], "transform": transform, "nodata": 0, "compress": "deflate", "tiled": True, "blockxsize": 256, "blockysize": 256}
        for name, pixels in [("landcover.tif", grid), ("zone_ids.tif", labels)]:
            with rasterio.open(folder / name, "w", dtype=pixels.dtype, **profile) as dst:
                dst.write(pixels, 1)
                dst.update_tags(attribution=spec["landcover"]["attribution"], landcover_year="2021", description="Categorical classes" if name == "landcover.tif" else "Rasterization indices, not population", resampling="nearest", assignment=spec["zone_assignment"])
        quality = {"city": city, "zones": len(zones), "grid": {"width": width, "height": height, "crs": cfg["analysis_crs"], "resolution_m": res, "transform": list(transform)}, "population": manifest["population"], "overlapping_pixel_centres": 0, "input_manifest_sha256": data.sha(base / "manifest.json"), "implementation_sha256": data.sha(Path(__file__)), "files": {name: {"sha256": data.sha(folder/name), "bytes": (folder/name).stat().st_size} for name in ["landcover.tif", "zone_ids.tif", "zones_metric.gpkg", "zones.geojson"]}, "paths": {name: str(folder/name) for name in ["landcover.tif", "zone_ids.tif", "zones_metric.gpkg", "zones.geojson"]}, "limits": spec["limits"]}
        data.dump(folder / "quality.json", quality)
        return quality


def counts_to_metrics(counts, vegetation_classes):
    """Explicit categorical denominators, including empty/all-water zones."""
    counts = {int(k): int(v) for k, v in counts.items()}
    if any(v < 0 for v in counts.values()) or not set(counts).issubset({0, *map(int, data.recipe()["classes"])}):
        raise ValueError("Invalid class counts")
    total = sum(counts.values())
    valid = total - counts.get(0, 0)
    land = valid - counts.get(80, 0)
    vegetation = sum(counts.get(code, 0) for code in vegetation_classes)
    return {"total_pixels": total, "valid_pixels": valid, "nodata_pixels": counts.get(0, 0), "water_pixels": counts.get(80, 0), "valid_land_pixels": land, "vegetation_pixels": vegetation, "tree_class_pixels": counts.get(10, 0), "vegetation_share_of_valid_land": vegetation / land if land else None, "vegetation_share_of_valid_all": vegetation / valid if valid else None, "tree_class_share_of_valid_land": counts.get(10, 0) / land if land else None, "valid_fraction_of_zone_pixels": valid / total if total else None, "class_counts": {str(k): counts.get(k, 0) for k in [0, *map(int, data.recipe()["classes"])]}}


def analyze(city, run_id, threshold=0.2):
    token(run_id)
    if not math.isfinite(threshold) or not 0 <= threshold <= 1:
        raise ValueError("threshold must be a finite fraction in 0..1")
    folder, quality, manifest = prepared(city)
    out = data.root() / "results" / city / run_id
    if out.exists():
        raise ValueError("run_id already exists; preserve evidence and choose a new ID")
    zones = gpd.read_file(folder / "zones_metric.gpkg").sort_values("zone_index")
    with rasterio.open(folder / "landcover.tif") as source, rasterio.open(folder / "zone_ids.tif") as zone_source:
        pixels, labels = source.read(1), zone_source.read(1)
    # Composite indices aggregate all zones in one pass without replacing GDAL geometry operations.
    histograms = np.bincount(labels.ravel().astype(np.int64)*256 + pixels.ravel(), minlength=(len(zones)+1)*256).reshape(len(zones)+1, 256)
    rows = []
    for zone in zones.itertuples():
        histogram = histograms[int(zone.zone_index)]
        metrics = counts_to_metrics({i: int(n) for i, n in enumerate(histogram) if n}, data.recipe()["vegetation_classes"])
        share = metrics["vegetation_share_of_valid_land"]
        population = None if pd.isna(zone.population) else int(zone.population)
        low = share < threshold if share is not None else None
        rows.append({"zone_id": str(zone.zone_id), "name": zone.name, "population": population, "water_zone": bool(zone.water_zone), **metrics, "low_vegetation": low, "polygon_area_m2": float(zone.geometry.area), "rasterized_zone_area_m2": metrics["total_pixels"] * data.recipe()["resolution_m"]**2})
    low_rows = [r for r in rows if r["low_vegetation"] is True]
    eligible = [r for r in rows if r["vegetation_share_of_valid_land"] is not None]
    summary = {"city": city, "run_id": run_id, "threshold": threshold, "threshold_rule": "vegetation_share_of_valid_land < threshold; equality is not low", "landcover_year": 2021, "population_date": data.city_config(city)["population_date"], "zone_count": len(rows), "eligible_zone_count": len(eligible), "no_valid_land_zone_ids": [r["zone_id"] for r in rows if r["valid_land_pixels"] == 0], "low_vegetation_zone_ids": [r["zone_id"] for r in low_rows], "low_vegetation_zone_count": len(low_rows), "population_in_low_vegetation_zones": sum(r["population"] for r in low_rows if r["population"] is not None), "low_zones_with_unknown_population": [r["zone_id"] for r in low_rows if r["population"] is None], "population_reconciliation": manifest["population"], "pooled_pixel_metrics": counts_to_metrics({i: int(n) for i, n in enumerate(histograms[1:].sum(axis=0)) if n}, data.recipe()["vegetation_classes"]), "zones": rows, "ranking_lowest_valid_land_share": [r["zone_id"] for r in sorted(eligible, key=lambda r: (r["vegetation_share_of_valid_land"], r["zone_id"]))], "input_manifest_sha256": quality["input_manifest_sha256"], "implementation_sha256": data.sha(Path(__file__)), "runtime": {name: importlib.metadata.version(name) for name in ["rasterio", "geopandas", "numpy", "shapely", "fastmcp", "matplotlib"]}, "limits": data.recipe()["limits"], "artifacts": ["summary.json", "zone_metrics.csv", "class_counts.csv", "zones.geojson", "report.md", "map.png (after render)"]}
    out.mkdir(parents=True)
    data.dump(out / "summary.json", summary)
    fields = [k for k in rows[0] if k != "class_counts"]
    with (out / "zone_metrics.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows({k: row[k] for k in fields} for row in rows)
    with (out / "class_counts.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=["zone_id", "class_code", "pixel_count"])
        writer.writeheader()
        writer.writerows({"zone_id": row["zone_id"], "class_code": code, "pixel_count": count} for row in rows for code, count in row["class_counts"].items())
    features = zones.to_crs(4326)
    rows_by_id = {r["zone_id"]: r for r in rows}
    for name in ["vegetation_share_of_valid_land", "vegetation_share_of_valid_all", "low_vegetation"]:
        features[name] = features.zone_id.map(lambda key: rows_by_id[key][name])
    features.to_file(out / "zones.geojson", driver="GeoJSON")
    report = f"# {data.city_config(city)['name']}: mapped vegetation experiment\n\n{len(low_rows)} of {len(eligible)} zones with valid non-water pixels are below the declared {threshold:.0%} vegetation land-share threshold. {summary['population_in_low_vegetation_zones']:,} published 2025 residents are attached to those zones; this is not population without green access or exposed to heat. Land cover represents 2021.\n\n" + "\n".join("- " + limit for limit in summary["limits"]) + "\n\n" + data.recipe()["landcover"]["attribution"] + ". CC-BY-4.0.\n"
    (out / "report.md").write_text(report, encoding="utf-8", newline="\n")
    return summary


def read_artifact(city, run_id, name="summary.json", offset=0, limit=20000):
    data.city_config(city)
    token(run_id)
    if name not in {"summary.json", "zone_metrics.csv", "class_counts.csv", "zones.geojson", "report.md", "map.png"}:
        raise ValueError("Artifact name is not allowed")
    if type(offset) is not int or type(limit) is not int or offset < 0 or not 1 <= limit <= 50000:
        raise ValueError("offset must be nonnegative and limit must be 1..50000")
    path = data.root() / "results" / city / run_id / name
    receipt = {"name": name, "bytes": path.stat().st_size, "sha256": data.sha(path)}
    if name == "map.png":
        return {**receipt, "note": "PNG remains in the mounted workspace"}
    text = path.read_text(encoding="utf-8")
    return {**receipt, "text": text[offset:offset+limit], "characters": len(text), "next_offset": offset+limit if len(text) > offset+limit else None}


def compare(city, baseline_id, scenario_id):
    data.city_config(city)
    for key in [baseline_id, scenario_id]:
        token(key)
    results = [json.loads((data.root() / "results" / city / key / "summary.json").read_text(encoding="utf-8")) for key in [baseline_id, scenario_id]]
    before, after = results
    if before["city"] != city or after["city"] != city or any(before[key] != after[key] for key in ["input_manifest_sha256", "implementation_sha256", "landcover_year", "population_date", "zones", "pooled_pixel_metrics"] if key != "zones"):
        raise ValueError("Compare the same city's inputs and method; this is threshold sensitivity only")
    if [{k: v for k, v in row.items() if k != "low_vegetation"} for row in before["zones"]] != [{k: v for k, v in row.items() if k != "low_vegetation"} for row in after["zones"]]:
        raise ValueError("Zone data changed; compare threshold sensitivity on identical observations")
    a, b = set(before["low_vegetation_zone_ids"]), set(after["low_vegetation_zone_ids"])
    return {"city": city, "baseline_id": baseline_id, "scenario_id": scenario_id, "threshold_before": before["threshold"], "threshold_after": after["threshold"], "newly_below_threshold_zone_ids": sorted(b-a), "no_longer_below_threshold_zone_ids": sorted(a-b), "population_in_low_zones_before": before["population_in_low_vegetation_zones"], "population_in_low_zones_after": after["population_in_low_vegetation_zones"], "interpretation": "Sensitivity to an exploratory classification threshold on the same 2021 raster; not land-cover change or causal population impact"}


def render(city, run_id):
    token(run_id)
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.colors import ListedColormap
    from matplotlib.patches import Patch
    folder, _, _ = prepared(city)
    output = data.root() / "results" / city / run_id
    summary = json.loads((output / "summary.json").read_text(encoding="utf-8"))
    path = output / "map.png"
    if path.exists():
        raise ValueError("Map already exists; preserve the observed artifact")
    palette = {0: "#eeeeee", 10: "#006400", 20: "#ffbb22", 30: "#ffff4c", 40: "#f096ff", 50: "#fa0000", 60: "#b4b4b4", 70: "#f0f0f0", 80: "#0064c8", 90: "#0096a0", 95: "#00cf75", 100: "#fae6a0"}
    with rasterio.open(folder / "landcover.tif") as source, rasterio.open(folder / "zone_ids.tif") as zone_source:
        scale = max(1, math.ceil(max(source.width, source.height)/1800))
        shape = (math.ceil(source.height/scale), math.ceil(source.width/scale))
        pixels = source.read(1, out_shape=shape, resampling=Resampling.nearest)
        labels = zone_source.read(1, out_shape=shape, resampling=Resampling.nearest)
        pixels[labels == 0] = 0
        indices = np.zeros_like(pixels)
        for i, code in enumerate(palette):
            indices[pixels == code] = i
        extent = [source.bounds.left, source.bounds.right, source.bounds.bottom, source.bounds.top]
    fig, axes = plt.subplots(1, 2, figsize=(13, 7), gridspec_kw={"width_ratios": [1.2, 1]})
    axes[0].imshow(indices, cmap=ListedColormap(list(palette.values())), vmin=-.5, vmax=len(palette)-.5, extent=extent, interpolation="nearest")
    zones = gpd.read_file(folder / "zones_metric.gpkg")
    zones.boundary.plot(ax=axes[0], color="#ffffff", linewidth=.3)
    axes[0].set_title("WorldCover 2021 classes and study zones")
    axes[0].set_xlabel("Easting (m)"); axes[0].set_ylabel("Northing (m)")
    rows = sorted([r for r in summary["zones"] if r["vegetation_share_of_valid_land"] is not None], key=lambda r: (r["vegetation_share_of_valid_land"], r["zone_id"]))[:12]
    axes[1].barh([r["name"] for r in rows][::-1], [100*r["vegetation_share_of_valid_land"] for r in rows][::-1], color="#287568")
    axes[1].axvline(summary["threshold"]*100, color="#b24737", linestyle="--", label="Exploratory threshold")
    axes[1].set_xlabel("Vegetation / valid non-water pixels (%)")
    axes[1].set_title("Lowest mapped land shares; no access inference")
    axes[1].legend(fontsize=8)
    axes[0].legend(handles=[Patch(color=palette[int(code)], label=name) for code, name in data.recipe()["classes"].items()], loc="upper left", fontsize=6)
    fig.suptitle(data.city_config(city)["name"] + " · historical vegetation and 2025 zone-population context")
    fig.text(.02, .02, data.recipe()["landcover"]["attribution"] + " · CC-BY-4.0\nNearest 10 m metric grid; polygon-centre approximation. Not current canopy, park access, NDVI or temperature.", fontsize=7)
    fig.tight_layout(rect=(0, .08, 1, .95))
    fig.savefig(path, dpi=130, metadata={"Software": "Urban MCP pinned vegetation runtime"})
    plt.close(fig)
    return read_artifact(city, run_id, "map.png")
