"""Package reviewed ODbL case inputs; caches and unrelated files are excluded."""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path, default=ROOT / ".urban-mcp/walking")
    parser.add_argument("--tag", default="data-walking-20261110")
    args = parser.parse_args()
    release = ROOT / ".urban-mcp/releases" / args.tag
    release.mkdir(parents=True, exist_ok=True)
    lock = {}
    for city in ["helsinki", "amsterdam"]:
        folder = args.workspace / "inputs" / city
        manifest = json.loads((folder / "manifest.json").read_text(encoding="utf-8"))
        archive = release / (city + "-walking-20261110.zip")
        if archive.exists():
            raise ValueError("Release archive already exists; preserve published bytes")
        with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zipped:
            for name, expected in manifest["files"].items():
                path = (folder / name).resolve()
                if not path.is_relative_to(folder.resolve()) or digest(path) != expected["sha256"] or path.stat().st_size != expected["bytes"]:
                    raise ValueError("Input manifest does not match reviewed files")
                zipped.write(path, name)
            zipped.write(folder / "manifest.json", "manifest.json")
            zipped.writestr("ATTRIBUTION.txt", manifest["attribution"] + "\nDatabase and derived database: ODbL-1.0\nhttps://opendatacommons.org/licenses/odbl/1-0/\nSource responses, requests and exact file hashes are in manifest.json and raw/.\nGraph and POI calls have separate OSM timestamps; not a transactional snapshot or a complete city extract.\nCode license does not replace the data license.\n")
        lock[city] = {"file": archive.name, "url": f"https://github.com/polisplexity/urban-mcp/releases/download/{args.tag}/{archive.name}",
                      "sha256": digest(archive), "bytes": archive.stat().st_size, "manifest_sha256": digest(folder / "manifest.json"), "license": "ODbL-1.0"}
    (ROOT / "cases/two-city-walking/snapshot.lock.json").write_text(json.dumps(lock, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"directory": str(release), "assets": lock}, indent=2))


if __name__ == "__main__":
    main()
