"""Fetch pinned small reference assets for review; do not execute the engine."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
from urllib.request import urlopen
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def check_asset(data, asset):
    if len(data) != asset["bytes"] or hashlib.sha256(data).hexdigest() != asset["sha256"]:
        raise ValueError(f"Asset integrity mismatch: {asset['file']}")


def check_sumo_references(folder):
    config = ET.parse(folder / "hello.sumocfg").getroot()
    for tag in ("net-file", "route-files", "gui-settings-file"):
        for item in config.iter(tag):
            for value in item.attrib["value"].split(","):
                if Path(value).name != value or not (folder / value).is_file():
                    raise ValueError(f"Unresolved/unsafe native config reference: {value}")
    edges = {item.attrib["id"] for item in ET.parse(folder / "hello.net.xml").getroot().iter("edge")}
    for route in ET.parse(folder / "hello.rou.xml").getroot().iter("route"):
        for edge in route.attrib.get("edges", "").split():
            if edge not in edges:
                raise ValueError(f"Route uses unknown edge: {edge}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fetch-for-review", action="store_true", help="Download public assets into ignored cache; does not admit rights or execute SUMO")
    args = parser.parse_args()
    case = json.loads((ROOT / "cases/sumo-reference-hello/case.json").read_text())
    cache = ROOT / ".urban-mcp/cases" / case["id"] / "inputs"
    if not args.fetch_for_review:
        print(json.dumps({"mode": "plan_only", "assets": case["assets"], "execution_ready": False, "blockers": case["blockers"]}, indent=2))
        return 0
    cache.mkdir(parents=True, exist_ok=True)
    for asset in case["assets"]:
        name = asset["file"]
        if Path(name).name != name or "/" in name or "\\" in name:
            raise ValueError("Asset file must be a basename")
        url = urlsplit(asset["url"])
        expected_prefix = f"/eclipse-sumo/sumo/{case['source_commit']}/tests/complex/tutorial/hello/data/"
        if url.scheme != "https" or url.netloc != "raw.githubusercontent.com" or not url.path.startswith(expected_prefix):
            raise ValueError("This review fetcher only supports the pinned upstream reference case")
        target = cache / name
        if target.is_file():
            data = target.read_bytes()
        else:
            with urlopen(asset["url"], timeout=20) as response:
                data = response.read(1048577)
            check_asset(data, asset)
            target.write_bytes(data)
        check_asset(data, asset)
    check_sumo_references(cache)
    receipt = {"status": "reference_assets_verified", "assets": len(case["assets"]), "case": case["id"], "checks": ["pinned byte length and SHA-256", "native relative references", "route edge IDs"], "execution_ready": False, "engine_executed": False, "blockers": case["blockers"]}
    (cache.parent / "data-review-receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
