"""Public input acquisition and immutable city-specific snapshot admission."""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import tempfile
from urllib.parse import urlencode, urlsplit
from urllib.request import Request, urlopen
import zipfile

import geopandas as gpd
import numpy as np
import rasterio
from rasterio.windows import Window, from_bounds
from shapely.geometry import shape

from urban_mcp_case.sources import collect_pages, get_json

CASE = Path(__file__).resolve().parents[1] / "cases/two-city-vegetation"


def root():
    return Path(os.environ.get("URBAN_MCP_DATA", "/data")).resolve()


def recipe():
    return json.loads((CASE / "recipe.json").read_text(encoding="utf-8"))


def city_config(city):
    if city not in recipe()["cities"]:
        raise ValueError("Unknown city; inspect vegetation_status for configured cases")
    return recipe()["cities"][city]


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def dump(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    content = (json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode()
    fd, temp = tempfile.mkstemp(dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(content)
        os.replace(temp, path)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)


def fetch(url, path, ledger, max_bytes=350_000_000):
    host = urlsplit(url).hostname
    if host not in {"esa-worldcover.s3.eu-central-1.amazonaws.com", "service.pdok.nl"}:
        raise ValueError("Acquisition URL is outside the public recipe hosts")
    path.parent.mkdir(parents=True, exist_ok=True)
    entry = {"url": url, "method": "GET", "retrieved_at": datetime.now(timezone.utc).isoformat()}
    ledger.append(entry)
    try:
        with urlopen(Request(url, headers={"User-Agent": "Urban-MCP municipal vegetation case"}), timeout=90) as response:
            entry.update(status=response.status, etag=response.headers.get("ETag"), last_modified=response.headers.get("Last-Modified"))
            expected = int(response.headers["Content-Length"]) if response.headers.get("Content-Length") else None
            if expected is not None and expected > max_bytes:
                raise ValueError("Source exceeds acquisition size limit")
            size = 0
            with path.open("xb") as stream:
                while chunk := response.read(1024 * 1024):
                    size += len(chunk)
                    if size > max_bytes:
                        raise ValueError("Source exceeds acquisition size limit")
                    stream.write(chunk)
            if expected is not None and size != expected:
                raise ValueError("Source download is truncated")
            entry.update(bytes=size, sha256=sha(path), file=path.name)
    except Exception as exc:
        entry["error"] = type(exc).__name__ + ": " + str(exc)
        raise
    return entry


def municipal_inputs(city, folder, ledger):
    cfg = city_config(city)
    raw = folder / "raw"
    raw.mkdir()
    if city == "helsinki":
        districts, receipt = collect_pages("districts", cfg["district_url"], raw)
        ledger.append({"source": "Helsinki Service Map", **receipt})
        metadata_bytes, metadata, retries = get_json(cfg["population_url"])
        (raw / "population-metadata.json").write_bytes(metadata_bytes)
        variables = {v["code"]: v for v in metadata["variables"]}
        areas = [code for code, label in zip(variables["Osa-alue"]["values"], variables["Osa-alue"]["valueTexts"]) if code == "0910000000" or code.startswith("091") and "peruspiiri" in label]
        if len(districts) != 34 or len(areas) != 35 or "2025" not in variables["Vuosi"]["values"]:
            raise ValueError("Helsinki's admitted district/year contract changed")
        query = {"query": [{"code": k, "selection": {"filter": "item", "values": v}} for k, v in [("Osa-alue", areas), ("Ikä", ["ALL"]), ("Vuosi", ["2025"]), ("Tiedot", ["lkm"])]], "response": {"format": "json-stat2"}}
        dump(raw / "population-query.json", query)
        payload, population, more_retries = get_json(cfg["population_url"], query)
        (raw / "population.json").write_bytes(payload)
        ledger.append({"source": "Helsinki PxWeb", "url": cfg["population_url"], "query": query, "retries": retries + more_retries})
        if population["id"] != ["Osa-alue", "Ikä", "Vuosi", "Tiedot"] or population["size"] != [35, 1, 1, 1] or list(population["dimension"]["Vuosi"]["category"]["index"]) != ["2025"]:
            raise ValueError("Population dimensions changed")
        index = population["dimension"]["Osa-alue"]["category"]["index"]
        by_id = {code[4:7]: population["value"][i] for code, i in index.items() if code != "0910000000"}
        records = [{"zone_id": str(d["origin_id"]), "name": d["name"].get("en", d["name"].get("fi")), "population": by_id[str(d["origin_id"])], "water_zone": False, "geometry": shape(d["boundary"])} for d in districts if d["municipality"] == "helsinki"]
        if len(records) != len(districts) or set(by_id) != {r["zone_id"] for r in records}:
            raise ValueError("District and population identities disagree")
        municipal_population = population["value"][index["0910000000"]]
        zones = gpd.GeoDataFrame(records, crs=4326)
    else:
        filter_xml = '<fes:Filter xmlns:fes="http://www.opengis.net/fes/2.0"><fes:PropertyIsEqualTo><fes:ValueReference>gemeentecode</fes:ValueReference><fes:Literal>GM0363</fes:Literal></fes:PropertyIsEqualTo></fes:Filter>'
        objects = {}
        for layer in ["wijken", "gemeenten"]:
            props = "geom,gemeentecode,gemeentenaam,aantalInwoners,jaar,water,oppervlakteTotaalInHa,oppervlakteLandInHa,oppervlakteWaterInHa"
            if layer == "wijken":
                props += ",wijkcode,wijknaam"
            params = {"service": "WFS", "version": "2.0.0", "request": "GetFeature", "typeNames": "wijkenbuurten:" + layer, "srsName": "EPSG:28992", "outputFormat": "application/json", "count": 1000, "propertyName": props, "filter": filter_xml}
            path = raw / (layer + ".geojson")
            fetch(cfg["wfs_url"] + "?" + urlencode(params), path, ledger, 20_000_000)
            obj = json.loads(path.read_text(encoding="utf-8"))
            if obj.get("numberMatched") != len(obj["features"]) or len(obj["features"]) >= 1000 or any(link.get("rel") == "next" for link in obj.get("links", [])):
                raise ValueError("WFS response is incomplete or exceeds bounded request")
            if any(f["properties"]["gemeentecode"] != "GM0363" or f["properties"]["jaar"] != 2025 for f in obj["features"]):
                raise ValueError("WFS returned another municipality/year")
            objects[layer] = obj["features"]
        records = []
        for f in objects["wijken"]:
            p = f["properties"]
            n = p["aantalInwoners"]
            records.append({"zone_id": p["wijkcode"], "name": p["wijknaam"], "population": int(n) if n is not None and n >= 0 else None, "water_zone": p["water"] == "JA", "geometry": shape(f["geometry"])})
        zones = gpd.GeoDataFrame(records, crs=28992).to_crs(4326)
        totals = [f["properties"]["aantalInwoners"] for f in objects["gemeenten"] if f["properties"]["water"] == "NEE"]
        if len(totals) != 1 or totals[0] < 0:
            raise ValueError("Municipal population total is missing or ambiguous")
        municipal_population = totals[0]
    if zones.empty or zones.zone_id.duplicated().any() or not zones.geometry.is_valid.all() or zones.geometry.is_empty.any() or any(n is not None and not (isinstance(n, int) and n >= 0) for n in records_population(records)):
        raise ValueError("Invalid district geometry, population or identity")
    zones = zones.sort_values("zone_id").reset_index(drop=True)
    zones.to_file(folder / "zones.geojson", driver="GeoJSON")
    population_sum = sum(r["population"] for r in records if r["population"] is not None)
    return zones, {"municipal_population": int(municipal_population), "zone_population_sum": int(population_sum), "municipal_minus_zone_population": int(municipal_population - population_sum), "population_date": cfg["population_date"], "unknown_population_zone_ids": sorted(r["zone_id"] for r in records if r["population"] is None)}


def records_population(records):
    return [r["population"] for r in records]


def verify(city, base=None):
    city_config(city)
    base = Path(base) if base else root() / "inputs" / city
    manifest = json.loads((base / "manifest.json").read_text(encoding="utf-8"))
    if manifest["city"] != city or manifest["case"] != recipe()["id"] or manifest["recipe_sha256"] != sha(CASE / "recipe.json"):
        raise ValueError("Input city/case/recipe identity mismatch")
    required = {"zones.geojson", "requests.json", *(item["file"] for item in manifest["source_tiles"])}
    if not manifest["source_tiles"] or not required.issubset(manifest["files"]):
        raise ValueError("Input manifest omits required files")
    for name, expected in manifest["files"].items():
        path = (base / name).resolve()
        if not path.is_relative_to(base.resolve()) or not path.is_file() or path.stat().st_size != expected["bytes"] or sha(path) != expected["sha256"]:
            raise ValueError("Input integrity failure: " + name)
    return base, manifest


def status():
    cities = {}
    for city in recipe()["cities"]:
        try:
            _, manifest = verify(city)
            cities[city] = {"verified": True, "zones": manifest["zones"], "population": manifest["population"]}
        except (OSError, ValueError, KeyError) as exc:
            cities[city] = {"verified": False, "reason": str(exc)}
    return {"case": recipe()["id"], "cities": cities, "recipe": recipe(), "product_qualified": False}


def harvest(city, mode="snapshot"):
    city_config(city)
    if mode == "snapshot":
        return restore(city)
    if mode != "live":
        raise ValueError("mode must be live or snapshot")
    destination = root() / "inputs" / city
    folder = root() / "staging" / city
    if destination.exists() or folder.exists():
        raise ValueError("Inputs/staging already exist; inspect failures and use a fresh workspace")
    folder.mkdir(parents=True)
    ledger = []
    try:
        zones, population = municipal_inputs(city, folder, ledger)
        west, south, east, north = zones.total_bounds
        # Include a small source margin for the projected-grid nearest warp.
        bounds = [west - .002, south - .002, east + .002, north + .002]
        source_tiles = []
        for latitude in range(3 * math.floor(bounds[1] / 3), 3 * math.floor(bounds[3] / 3) + 1, 3):
            for longitude in range(3 * math.floor(bounds[0] / 3), 3 * math.floor(bounds[2] / 3) + 1, 3):
                tile = f"{'N' if latitude >= 0 else 'S'}{abs(latitude):02d}{'E' if longitude >= 0 else 'W'}{abs(longitude):03d}"
                filename = f"ESA_WorldCover_10m_2021_v200_{tile}_Map.tif"
                full_path = root() / "source-cache" / filename
                if full_path.exists():
                    raise ValueError("Use a fresh source-cache for an independently receipted live acquisition")
                entry = fetch(recipe()["landcover"]["base_url"] + filename, full_path, ledger)
                with rasterio.open(full_path) as source:
                    if source.crs != rasterio.crs.CRS.from_epsg(4326) or source.count != 1 or source.dtypes != ("uint8",):
                        raise ValueError("WorldCover source CRS/band/type mismatch")
                    crop = (max(bounds[0], source.bounds.left), max(bounds[1], source.bounds.bottom), min(bounds[2], source.bounds.right), min(bounds[3], source.bounds.top))
                    w = from_bounds(*crop, transform=source.transform)
                    col, row = math.floor(w.col_off), math.floor(w.row_off)
                    window = Window(col, row, math.ceil(w.col_off + w.width) - col, math.ceil(w.row_off + w.height) - row).intersection(Window(0, 0, source.width, source.height))
                    pixels = source.read(1, window=window)
                    valid_codes = set(np.unique(pixels).tolist())
                    if not valid_codes.issubset({0, *map(int, recipe()["classes"])}):
                        raise ValueError("Unexpected WorldCover class codes")
                    profile = source.profile.copy()
                    profile.update(driver="GTiff", height=pixels.shape[0], width=pixels.shape[1], transform=source.window_transform(window), nodata=0, compress="deflate", tiled=True, blockxsize=256, blockysize=256)
                    name = "source-" + tile + ".tif"
                    with rasterio.open(folder / name, "w", **profile) as dst:
                        dst.write(pixels, 1)
                        dst.update_tags(source_url=entry["url"], source_sha256=entry["sha256"], attribution=recipe()["landcover"]["attribution"], license="CC-BY-4.0", year="2021")
                    source_tiles.append({"file": name, "upstream": dict(entry), "window": [int(x) for x in [window.col_off, window.row_off, window.width, window.height]], "source_nodata": source.nodata, "source_bounds": list(source.bounds), "crop_transform": list(profile["transform"])})
        dump(folder / "requests.json", ledger)
        manifest = {"case": recipe()["id"], "city": city, "acquired_at": datetime.now(timezone.utc).isoformat(), "recipe_sha256": sha(CASE / "recipe.json"), "zones": len(zones), "population": population, "source_tiles": source_tiles, "licenses": [recipe()["landcover"], *city_config(city)["licenses"]], "files": {str(p.relative_to(folder)).replace("\\", "/"): {"bytes": p.stat().st_size, "sha256": sha(p)} for p in sorted(folder.rglob("*")) if p.is_file()}}
        dump(folder / "manifest.json", manifest)
        verify(city, folder)
        destination.parent.mkdir(parents=True, exist_ok=True)
        os.replace(folder, destination)
        return manifest
    except Exception as exc:
        dump(folder / "requests.json", ledger)
        dump(folder / "failure.json", {"type": type(exc).__name__, "message": str(exc)})
        raise


def restore(city):
    city_config(city)
    lock = json.loads((CASE / "snapshot.lock.json").read_text(encoding="utf-8"))[city]
    destination = root() / "inputs" / city
    if destination.exists():
        base, manifest = verify(city)
        if sha(base / "manifest.json") != lock["manifest_sha256"]:
            raise ValueError("Existing inputs differ from the locked public snapshot")
        return {"city": city, "mode": "existing_locked_snapshot", "zones": manifest["zones"]}
    root().mkdir(parents=True, exist_ok=True)
    archive = root() / (city + "-snapshot.zip")
    with urlopen(Request(lock["url"], headers={"User-Agent": "Urban-MCP snapshot reproduction"}), timeout=90) as response:
        payload = response.read(lock["bytes"] + 1)
    if len(payload) != lock["bytes"] or hashlib.sha256(payload).hexdigest() != lock["sha256"]:
        raise ValueError("Published snapshot size/hash mismatch")
    archive.write_bytes(payload)
    stage = root() / "restore" / city
    if stage.exists():
        raise ValueError("Restore staging exists; inspect and use a fresh workspace")
    stage.mkdir(parents=True)
    with zipfile.ZipFile(archive) as z:
        names = z.namelist()
        if len(names) != len(set(names)) or len(names) > 100 or sum(i.file_size for i in z.infolist()) > 250_000_000:
            raise ValueError("Snapshot member/count/expansion limit exceeded")
        for info in z.infolist():
            name = PurePosixPath(info.filename)
            target = (stage / str(name)).resolve()
            if name.is_absolute() or ".." in name.parts or "\\" in info.filename or not target.is_relative_to(stage.resolve()) or info.is_dir() or (info.external_attr >> 16) & 0o170000 == 0o120000:
                raise ValueError("Unsafe snapshot member")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(z.read(info))
    _, manifest = verify(city, stage)
    if sha(stage / "manifest.json") != lock["manifest_sha256"]:
        raise ValueError("Snapshot manifest hash mismatch")
    destination.parent.mkdir(parents=True, exist_ok=True)
    os.replace(stage, destination)
    return {"city": city, "mode": "locked_public_snapshot", "zones": manifest["zones"]}
