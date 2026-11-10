"""Exact source harvesting, rights and city-specific immutable snapshot admission."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import tempfile
from urllib.request import Request, urlopen
import zipfile

CASE = Path(__file__).resolve().parents[1] / "cases/two-city-sumo"


def root():
    return Path(os.environ.get("URBAN_MCP_DATA", "/data")).resolve()


def recipe():
    return json.loads((CASE / "recipe.json").read_text(encoding="utf-8"))


def config(city):
    if city not in recipe()["cities"]:
        raise ValueError("Unknown city; inspect sumo_status")
    return recipe()["cities"][city]


def token(value):
    if not isinstance(value, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,47}", value):
        raise ValueError("run_id must be 1-48 letters, digits, underscores or hyphens")
    return value


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024*1024), b""):
            h.update(chunk)
    return h.hexdigest()


def dump(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, name = tempfile.mkstemp(dir=path.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as stream:
            json.dump(value, stream, ensure_ascii=False, indent=2, allow_nan=False)
            stream.write("\n")
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def verify(city, folder=None):
    cfg = config(city)
    folder = Path(folder) if folder else root()/"inputs"/city
    manifest = json.loads((folder/"manifest.json").read_text(encoding="utf-8"))
    if manifest["city"] != city or manifest["recipe_sha256"] != sha(CASE/"recipe.json") or manifest["publisher_commit"] != cfg["publisher_commit"]:
        raise ValueError("Input city/recipe/publisher identity mismatch")
    expected = {a["file"]: a for a in cfg["assets"]}
    if set(manifest["files"]) != set(expected):
        raise ValueError("Input manifest file set differs from source contract")
    for name, asset in expected.items():
        path = (folder/name).resolve()
        receipt = manifest["files"][name]
        if not path.is_relative_to(folder.resolve()) or not path.is_file() or path.stat().st_size != asset["bytes"] or sha(path) != asset["sha256"] or receipt["sha256"] != asset["sha256"]:
            raise ValueError("Input integrity failure: "+name)
    return folder, manifest


def status():
    states = {}
    for city in recipe()["cities"]:
        try:
            _, manifest = verify(city)
            states[city] = {"verified": True, "publisher_commit": manifest["publisher_commit"]}
        except (OSError, ValueError, KeyError) as exc:
            states[city] = {"verified": False, "reason": str(exc)}
    return {"case": recipe()["id"], "cities": states, "recipe": recipe(), "product_qualified": False}


def harvest(city, mode="snapshot"):
    cfg = config(city)
    if mode == "snapshot":
        return restore(city)
    if mode != "live":
        raise ValueError("mode must be live or snapshot")
    destination, stage = root()/"inputs"/city, root()/"staging"/city
    if destination.exists() or stage.exists():
        raise ValueError("Inputs/staging exist; preserve the observation and use a fresh workspace")
    stage.mkdir(parents=True)
    ledger = []
    try:
        for asset in cfg["assets"]:
            entry = {"url": asset["url"], "retrieved_at": datetime.now(timezone.utc).isoformat()}
            ledger.append(entry)
            path = stage/asset["file"]
            path.parent.mkdir(parents=True, exist_ok=True)
            with urlopen(Request(asset["url"], headers={"User-Agent": "Urban-MCP municipal SUMO case"}), timeout=120) as response, path.open("xb") as output:
                entry.update(status=response.status, etag=response.headers.get("ETag"))
                size = 0
                while block := response.read(1024*1024):
                    size += len(block)
                    if size > asset["bytes"]:
                        raise ValueError("Source exceeds pinned size")
                    output.write(block)
            if path.stat().st_size != asset["bytes"] or sha(path) != asset["sha256"]:
                raise ValueError("Pinned source size/hash mismatch")
        manifest = {"city": city, "case": recipe()["id"], "recipe_sha256": sha(CASE/"recipe.json"), "publisher_repository": cfg["publisher_repository"], "publisher_commit": cfg["publisher_commit"], "acquired_at": datetime.now(timezone.utc).isoformat(), "license": cfg["license"], "attribution": cfg["attribution"], "files": {a["file"]: {k:a[k] for k in ["url", "bytes", "sha256"]} for a in cfg["assets"]}, "requests": ledger}
        dump(stage/"manifest.json", manifest)
        verify(city, stage)
        destination.parent.mkdir(parents=True, exist_ok=True)
        os.replace(stage, destination)
        return manifest
    except Exception as exc:
        dump(stage/"failure.json", {"error": str(exc), "requests": ledger})
        raise


def restore(city):
    config(city)
    lock = json.loads((CASE/"snapshot.lock.json").read_text(encoding="utf-8"))[city]
    destination = root()/"inputs"/city
    if destination.exists():
        folder, manifest = verify(city)
        if sha(folder/"manifest.json") != lock["manifest_sha256"]:
            raise ValueError("Existing inputs differ from the public snapshot")
        return {"city": city, "mode": "existing_locked_snapshot", "files": len(manifest["files"])}
    root().mkdir(parents=True, exist_ok=True)
    archive = root()/(city+"-snapshot.zip")
    with urlopen(Request(lock["url"], headers={"User-Agent":"Urban-MCP snapshot reproduction"}), timeout=120) as response, archive.open("wb") as output:
        size = 0
        while block := response.read(1024*1024):
            size += len(block)
            if size > lock["bytes"]:
                raise ValueError("Snapshot size exceeds lock")
            output.write(block)
    if archive.stat().st_size != lock["bytes"] or sha(archive) != lock["sha256"]:
        raise ValueError("Snapshot size/hash mismatch")
    stage = root()/"restore"/city
    stage.mkdir(parents=True, exist_ok=False)
    with zipfile.ZipFile(archive) as source:
        names = source.namelist()
        if len(names) != len(set(names)) or len(names) > 100 or sum(i.file_size for i in source.infolist()) > 200_000_000:
            raise ValueError("Snapshot duplicate/member/expansion limit")
        for info in source.infolist():
            name = PurePosixPath(info.filename)
            target = (stage/str(name)).resolve()
            if name.is_absolute() or ".." in name.parts or "\\" in info.filename or not target.is_relative_to(stage.resolve()) or info.is_dir() or (info.external_attr >> 16) & 0o170000 == 0o120000:
                raise ValueError("Unsafe snapshot member")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.read(info))
    _, manifest = verify(city, stage)
    if sha(stage/"manifest.json") != lock["manifest_sha256"]:
        raise ValueError("Snapshot manifest mismatch")
    destination.parent.mkdir(parents=True, exist_ok=True)
    os.replace(stage, destination)
    return {"city":city, "mode":"locked_public_snapshot", "files":len(manifest["files"])}
