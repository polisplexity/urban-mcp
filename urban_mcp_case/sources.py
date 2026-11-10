"""Bounded, versioned acquisition of the admitted Helsinki recipe."""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import time
from urllib.parse import urlsplit
from urllib.request import Request, urlopen
import uuid
import zipfile

CASE = Path(__file__).resolve().parents[1] / "cases/helsinki-service-inventory"
MAX_RESPONSE = 12_000_000


def recipe():
    return json.loads((CASE / "recipe.json").read_text(encoding="utf-8"))


def data_root():
    return Path(os.environ.get("URBAN_MCP_DATA", "/data")).resolve()


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(obj, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    temporary = path.parent / ("." + uuid.uuid4().hex + ".tmp")
    descriptor = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
        stream.write(text)
    temporary.replace(path)


def get_json(url, payload=None):
    parsed = urlsplit(url)
    if parsed.scheme != "https" or parsed.hostname not in {"api.hel.fi", "stat.hel.fi"} or parsed.username or parsed.password:
        raise ValueError("Source URL is outside the admitted HTTPS recipe")
    body = json.dumps(payload, ensure_ascii=False).encode() if payload is not None else None
    headers = {"User-Agent": "Urban-MCP/0.1 (public reproducible municipal research)", "Accept": "application/json"}
    if body:
        headers["Content-Type"] = "application/json"
    failures = []
    for attempt in range(3):
        try:
            with urlopen(Request(url, data=body, headers=headers), timeout=30) as response:
                content = response.read(MAX_RESPONSE + 1)
            if len(content) > MAX_RESPONSE:
                raise ValueError("Source response exceeds the declared size limit")
            return content, json.loads(content), failures
        except (OSError, TimeoutError) as exc:
            failures.append({"attempt": attempt + 1, "error_type": type(exc).__name__})
            if attempt == 2:
                raise RuntimeError(f"Source acquisition failed after bounded retries: {url}") from exc
            time.sleep(attempt + 1)


def collect_pages(name, url, folder):
    pages, rows, ids = [], [], set()
    visited, expected = set(), None
    while url:
        if url in visited or len(visited) >= 200:
            raise ValueError("Pagination cycle or page limit exceeded")
        visited.add(url)
        content, obj, failures = get_json(url)
        if expected is None:
            expected = obj["count"]
        if obj["count"] != expected:
            raise ValueError(f"{name}: count changed during acquisition; take a new snapshot")
        for row in obj["results"]:
            if row["id"] in ids:
                raise ValueError(f"{name}: duplicate ID across pages; snapshot is incomplete")
            ids.add(row["id"])
            rows.append(row)
        filename = f"{name}-{len(pages)+1:04d}.json"
        path = folder / filename
        path.write_bytes(content)
        pages.append({"file": filename, "url": url, "sha256": digest(path), "bytes": len(content), "records": len(obj["results"]), "retries": failures})
        url = obj["next"]
    if len(rows) != expected:
        raise ValueError(f"{name}: expected {expected} rows, obtained {len(rows)}")
    return rows, {"expected": expected, "obtained": len(rows), "duplicates": 0, "complete_pagination": True, "pages": pages}


def harvest_live():
    spec = recipe()
    root = data_root()
    version = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:6]
    folder = root / "sources" / version
    folder.mkdir(parents=True)
    receipt = {"case": spec["id"], "mode": "live", "snapshot": version, "acquired_at": datetime.now(timezone.utc).isoformat(), "sources": {}, "licenses": spec["licenses"], "failed": [], "complete": False}
    try:
        for name in ("units", "districts", "services"):
            _, receipt["sources"][name] = collect_pages(name, spec["sources"][name], folder)
        url = spec["sources"]["population_metadata"]
        content, metadata, retries = get_json(url)
        (folder / "population-metadata.json").write_bytes(content)
        variables = {v["code"]: v for v in metadata["variables"]}
        areas = [code for code, label in zip(variables["Osa-alue"]["values"], variables["Osa-alue"]["valueTexts"]) if code == "0910000000" or code.startswith("091") and "peruspiiri" in label]
        if len(areas) != 35 or spec["population_year"] not in variables["Vuosi"]["values"]:
            raise ValueError("Population metadata no longer matches the admitted 34-district/year contract")
        query = {"query": [{"code": k, "selection": {"filter": "item", "values": v}} for k, v in [("Osa-alue", areas), ("Ikä", ["ALL"]), ("Vuosi", [spec["population_year"]]), ("Tiedot", ["lkm"])]], "response": {"format": "json-stat2"}}
        write_json(folder / "population-query.json", query)
        content, _, pop_retries = get_json(url, query)
        (folder / "population.json").write_bytes(content)
        receipt["sources"]["population"] = {"url": url, "query_file": "population-query.json", "retries": retries + pop_retries, "pages": [{"file": name, "sha256": digest(folder / name), "bytes": (folder / name).stat().st_size} for name in ("population-metadata.json", "population-query.json", "population.json")]}
        receipt["complete"] = True
    except Exception as exc:
        receipt["failed"].append({"error_type": type(exc).__name__, "message": str(exc)})
        write_json(folder / "harvest.json", receipt)
        raise
    write_json(folder / "harvest.json", receipt)
    write_json(root / "active.json", {"snapshot": version})
    return {"snapshot": version, "receipt": str(folder / "harvest.json"), "counts": {k: v.get("obtained") for k, v in receipt["sources"].items()}, "complete": True}


def active_folder():
    root = data_root()
    pointer = root / "active.json"
    if not pointer.is_file():
        raise ValueError("Missing admitted inputs: run harvest_municipal_sources or the harvest CLI first")
    version = json.loads(pointer.read_text())["snapshot"]
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", version):
        raise ValueError("Invalid snapshot identifier")
    folder = root / "sources" / version
    return folder, verify_folder(folder)


def verify_folder(folder):
    receipt = json.loads((folder / "harvest.json").read_text(encoding="utf-8"))
    if not receipt["complete"] or receipt["failed"]:
        raise ValueError("Snapshot contains acquisition failures")
    for source in receipt["sources"].values():
        for page in source["pages"]:
            if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", page["file"]):
                raise ValueError("Invalid source asset filename")
            path = folder / page["file"]
            if not path.is_file() or path.stat().st_size != page["bytes"] or digest(path) != page["sha256"]:
                raise ValueError(f"Snapshot integrity mismatch: {page['file']}")
    return receipt


def rows_for(folder, receipt, name):
    rows = []
    for page in receipt["sources"][name]["pages"]:
        rows.extend(json.loads((folder / page["file"]).read_text(encoding="utf-8"))["results"])
    return rows


def harvest_snapshot():
    lock_path = CASE / "snapshot.lock.json"
    if not lock_path.is_file():
        raise ValueError("Public snapshot has not been published yet; use live acquisition")
    lock = json.loads(lock_path.read_text(encoding="utf-8"))
    root = data_root()
    root.mkdir(parents=True, exist_ok=True)
    archive = root / "snapshot.zip"
    if not archive.is_file() or digest(archive) != lock["sha256"]:
        with urlopen(Request(lock["url"], headers={"User-Agent": "Urban-MCP/0.1"}), timeout=60) as response:
            content = response.read(lock["bytes"] + 1)
        if len(content) != lock["bytes"] or hashlib.sha256(content).hexdigest() != lock["sha256"]:
            raise ValueError("Published snapshot integrity mismatch")
        archive.write_bytes(content)
    folder = root / "sources" / lock["snapshot"]
    folder.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive) as z:
        if sum(i.file_size for i in z.infolist()) > 50_000_000:
            raise ValueError("Snapshot exceeds extraction limit")
        for info in z.infolist():
            name = info.filename
            if PurePosixPath(name).name != name or "\\" in name or info.is_dir():
                raise ValueError("Snapshot member must be a plain filename")
            (folder / name).write_bytes(z.read(info))
    receipt = verify_folder(folder)
    write_json(root / "active.json", {"snapshot": lock["snapshot"]})
    return {"snapshot": lock["snapshot"], "mode": "pinned_public_snapshot", "complete": receipt["complete"], "receipt": str(folder / "harvest.json")}
