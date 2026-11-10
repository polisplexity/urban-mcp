"""Package only admitted public input crops/receipts; never caches or host state."""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / "cases/two-city-vegetation"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--tag", default="data-vegetation-20261110")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    locks = {}
    for city in json.loads((CASE/"recipe.json").read_text(encoding="utf-8"))["cities"]:
        folder = args.workspace / "inputs" / city
        manifest = json.loads((folder/"manifest.json").read_text(encoding="utf-8"))
        if manifest["city"] != city or manifest["recipe_sha256"] != sha(CASE/"recipe.json"):
            raise ValueError("Input recipe/city identity changed")
        names = ["manifest.json", *manifest["files"]]
        for name, expected in manifest["files"].items():
            path = (folder/name).resolve()
            if not path.is_relative_to(folder.resolve()) or path.stat().st_size != expected["bytes"] or sha(path) != expected["sha256"]:
                raise ValueError("Input differs from the acquisition receipt")
        name = city + "-vegetation-20261110.zip"
        target = args.output/name
        if target.exists():
            raise ValueError("Archive already exists; preserve the published bytes")
        with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
            for member in sorted(names):
                info = zipfile.ZipInfo(member, date_time=(1980, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                z.writestr(info, (folder/member).read_bytes())
        locks[city] = {"url": f"https://github.com/polisplexity/urban-mcp/releases/download/{args.tag}/{name}", "bytes": target.stat().st_size, "sha256": sha(target), "manifest_sha256": sha(folder/"manifest.json")}
    (CASE/"snapshot.lock.json").write_text(json.dumps(locks, indent=2)+"\n", encoding="utf-8", newline="\n")
    (args.output/"SHA256SUMS").write_text("".join(value["sha256"]+"  "+Path(value["url"]).name+"\n" for value in locks.values()), encoding="utf-8", newline="\n")
    print(json.dumps(locks, indent=2))


if __name__ == "__main__":
    main()
