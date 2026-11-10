"""Acquisition, immutable input receipts and bounded snapshot restoration."""
from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import tempfile
from urllib.parse import urlparse
import urllib.request
import zipfile

import geopandas as gpd
import osmnx as ox
import requests
from shapely.geometry import Point

CASE = Path(__file__).resolve().parents[1] / "cases/two-city-walking"


def root():
    return Path(os.environ.get("URBAN_MCP_DATA", "/data")).resolve()


def recipe():
    return json.loads((CASE / "recipe.json").read_text(encoding="utf-8"))


def city_config(city):
    if city not in recipe()["cities"]:
        raise ValueError("city must be helsinki or amsterdam")
    return recipe()["cities"][city]


def dump(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    content = (json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode()
    fd, tmp = tempfile.mkstemp(dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(content)
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def study_polygon(city, buffered=False):
    cfg, rec = city_config(city), recipe()
    radius = rec["core_radius_m"] + (rec["network_buffer_m"] if buffered else 0)
    return gpd.GeoSeries([Point(cfg["center_lon"], cfg["center_lat"])], crs=4326).to_crs(cfg["analysis_crs"]).buffer(radius).to_crs(4326).iloc[0]


@contextmanager
def receipts(folder):
    """Capture actual public HTTP request/response bytes, not reconstructed queries."""
    folder.mkdir(parents=True, exist_ok=True)
    original = requests.Session.send
    ledger = json.loads((folder / "requests.json").read_text(encoding="utf-8")) if (folder / "requests.json").exists() else []

    def send(session, request, **kwargs):
        host = urlparse(request.url).hostname
        if host not in {"overpass-api.de", "overpass.kumi.systems", "overpass.private.coffee"}:
            raise ValueError(f"Unapproved acquisition host: {host}")
        response = original(session, request, **kwargs)
        index = f"{len(ledger):03d}"
        payload = response.content
        (folder / (index + ".response")).write_bytes(payload)
        body = request.body
        if isinstance(body, bytes):
            body = body.decode("utf-8")
        item = {"method": request.method, "url": request.url, "request_body": body,
                "status": response.status_code, "retrieved_at": datetime.now(timezone.utc).isoformat(),
                "response_file": index + ".response", "sha256": hashlib.sha256(payload).hexdigest(),
                "bytes": len(payload), "content_type": response.headers.get("Content-Type")}
        try:
            decoded = response.json()
            item["osm3s"] = decoded.get("osm3s")
            item["remark"] = decoded.get("remark")
            if response.ok and item["remark"]:
                raise RuntimeError("Overpass returned a remark; partial data must not be admitted")
        except ValueError:
            pass
        ledger.append(item)
        dump(folder / "requests.json", ledger)
        return response

    requests.Session.send = send
    try:
        yield ledger
    finally:
        requests.Session.send = original


def verify(city):
    city_config(city)
    base = root() / "inputs" / city
    manifest = json.loads((base / "manifest.json").read_text(encoding="utf-8"))
    if manifest["city"] != city or manifest["case"] != recipe()["id"]:
        raise ValueError("Input city/case mismatch")
    if manifest["recipe_sha256"] != sha(CASE / "recipe.json"):
        raise ValueError("Input recipe hash differs; use the recorded recipe or harvest anew")
    for name, expected in manifest["files"].items():
        path = (base / name).resolve()
        if not path.is_relative_to(base.resolve()) or not path.is_file() or sha(path) != expected["sha256"] or path.stat().st_size != expected["bytes"]:
            raise ValueError(f"Input integrity failure: {name}")
    return base, manifest


def status():
    cities = {}
    for city in recipe()["cities"]:
        try:
            _, manifest = verify(city)
            cities[city] = {"verified": True, "nodes": manifest["nodes"], "edges": manifest["edges"], "features": manifest["features"]}
        except (OSError, ValueError, KeyError) as error:
            cities[city] = {"verified": False, "reason": str(error)}
    return {"case": recipe()["id"], "cities": cities, "recipe": recipe()}


def harvest(city, mode="snapshot", resume=False, feature_query="bbox", feature_endpoint="primary"):
    city_config(city)
    if mode not in {"snapshot", "live"}:
        raise ValueError("mode must be snapshot or live")
    if feature_query not in {"bbox", "polygon"}:
        raise ValueError("feature_query must be bbox or polygon")
    if feature_endpoint not in {"primary", "private-coffee"}:
        raise ValueError("feature_endpoint must be primary or private-coffee")
    if mode == "snapshot":
        return restore(city)
    destination = root() / "inputs" / city
    if destination.exists():
        raise ValueError("Inputs already exist; use a fresh workspace to preserve receipts")
    rec = recipe()
    staging = root() / "staging" / city
    if staging.exists() and not resume:
        raise ValueError("Staging exists; inspect the failed acquisition, then use CLI --resume or a fresh workspace")
    if resume and (staging / "intent.json").exists():
        intent = json.loads((staging / "intent.json").read_text(encoding="utf-8"))
        if intent != {"city": city, "recipe_sha256": sha(CASE / "recipe.json")}:
            raise ValueError("Cannot resume a different city/recipe")
    staging.mkdir(parents=True, exist_ok=resume)
    dump(staging / "intent.json", {"city": city, "recipe_sha256": sha(CASE / "recipe.json")})
    ox.settings.cache_folder = staging / "cache"
    ox.settings.log_console = False
    ox.settings.requests_timeout = 180
    ox.settings.overpass_rate_limit = True
    ox.settings.overpass_url = "https://overpass-api.de/api"
    ox.settings.http_user_agent = "Urban-MCP municipal reproducibility study https://github.com/polisplexity/urban-mcp"
    ox.settings.useful_tags_way = list(dict.fromkeys(ox.settings.useful_tags_way + ["foot", "access", "oneway:foot", "sidewalk", "wheelchair", "bridge", "tunnel", "surface"]))
    ox.settings.useful_tags_node = list(dict.fromkeys(ox.settings.useful_tags_node + ["barrier", "access", "foot", "wheelchair"]))
    polygon = study_polygon(city, buffered=True)
    with receipts(staging / "raw") as acquired:
        graph = ox.graph_from_polygon(polygon, network_type="walk", simplify=False, retain_all=True, truncate_by_edge=True)
        if feature_endpoint == "private-coffee":
            ox.settings.overpass_url = "https://overpass.private.coffee/api"
            # This operator explicitly offers an endpoint without a slot limit.
            # Retain bounded requests/timeouts; never poll or bypass the primary's slots.
            ox.settings.overpass_rate_limit = False
        if feature_query == "polygon":
            features = ox.features_from_polygon(polygon, tags=rec["feature_tags"])
        else:
            # A short bounding-box request avoids repeating a long polygon in
            # every tag clause. The exact study polygon still filters features.
            features = ox.features_from_bbox(tuple(polygon.bounds), tags=rec["feature_tags"])
            features = features[features.geometry.intersects(polygon)]
    graph.graph.update(network_type="walk", city=city, snapshot_model="bidirectional unsimplified OSMnx walk")
    ox.save_graphml(graph, staging / "network.graphml")
    features = features.reset_index()
    # Keep only fields needed for this experiment, never contacts or images.
    keep = [c for c in ["element", "id", "amenity", "name", "access", "geometry"] if c in features]
    features[keep].to_file(staging / "features.geojson", driver="GeoJSON")
    gpd.GeoDataFrame({"role": ["core", "buffered_network"]}, geometry=[study_polygon(city), polygon], crs=4326).to_file(staging / "areas.geojson", driver="GeoJSON")
    manifest = {"case": rec["id"], "city": city, "retrieved_at": datetime.now(timezone.utc).isoformat(),
                "recipe_sha256": sha(CASE / "recipe.json"), "license": rec["license"], "license_url": rec["license_url"],
                "attribution": rec["attribution"], "nodes": len(graph), "edges": graph.number_of_edges(), "features": len(features),
                "http_requests": len(acquired), "osmnx": ox.__version__, "python": platform.python_version(),
                "feature_acquisition": feature_query + " request, filtered to buffered study polygon", "feature_endpoint": feature_endpoint,
                "files": {str(p.relative_to(staging)).replace("\\", "/"): {"sha256": sha(p), "bytes": p.stat().st_size} for p in sorted(staging.rglob("*")) if p.is_file() and "cache" not in p.parts}}
    dump(staging / "manifest.json", manifest)
    destination.parent.mkdir(parents=True, exist_ok=True)
    os.replace(staging, destination)
    verify(city)
    return manifest


def restore(city):
    if (root() / "inputs" / city).exists():
        base, manifest = verify(city)
        if (CASE / "snapshot.lock.json").exists():
            lock = json.loads((CASE / "snapshot.lock.json").read_text(encoding="utf-8"))[city]
            if data_sha := lock.get("manifest_sha256"):
                if sha(base / "manifest.json") != data_sha:
                    raise ValueError("Existing inputs differ from the locked snapshot; use a fresh workspace")
        return manifest
    lock = json.loads((CASE / "snapshot.lock.json").read_text(encoding="utf-8"))[city]
    url = lock["url"]
    if not url.startswith("https://github.com/polisplexity/urban-mcp/releases/download/"):
        raise ValueError("Snapshot URL must be a project release asset")
    root().mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=root()) as tmp:
        archive = Path(tmp) / "snapshot.zip"
        with urllib.request.urlopen(url, timeout=120) as response, archive.open("wb") as stream:
            total = 0
            while chunk := response.read(1024 * 1024):
                total += len(chunk)
                if total > lock["bytes"]:
                    raise ValueError("Snapshot exceeds locked size")
                stream.write(chunk)
        if total != lock["bytes"] or sha(archive) != lock["sha256"]:
            raise ValueError("Snapshot size or SHA-256 mismatch")
        unpack = Path(tmp) / "unpack"
        with zipfile.ZipFile(archive) as zipped:
            if sum(i.file_size for i in zipped.infolist()) > 250_000_000:
                raise ValueError("Snapshot expands beyond allowed limit")
            for item in zipped.infolist():
                if not (unpack / item.filename).resolve().is_relative_to(unpack.resolve()) or (item.external_attr >> 16) & 0o170000 == 0o120000:
                    raise ValueError("Unsafe snapshot member")
            zipped.extractall(unpack)
        destination = root() / "inputs" / city
        destination.parent.mkdir(parents=True, exist_ok=True)
        # Verify every member before publishing an input directory.
        manifest = json.loads((unpack / "manifest.json").read_text(encoding="utf-8"))
        if manifest["city"] != city or manifest["recipe_sha256"] != sha(CASE / "recipe.json"):
            raise ValueError("Snapshot case/recipe mismatch")
        for name, expected in manifest["files"].items():
            path = (unpack / name).resolve()
            if not path.is_relative_to(unpack.resolve()) or sha(path) != expected["sha256"] or path.stat().st_size != expected["bytes"]:
                raise ValueError("Snapshot input integrity failure")
        shutil.move(str(unpack), str(destination))
    return verify(city)[1]
