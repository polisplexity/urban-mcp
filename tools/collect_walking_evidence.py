"""Collect compact reviewed public-case artifacts; never copy caches or host state."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / "cases/two-city-walking"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path, default=ROOT / ".urban-mcp/walking-reproduction")
    parser.add_argument("--audit", type=Path, default=ROOT / ".urban-mcp/walking/evidence/upstream-audit.json")
    args = parser.parse_args()
    records = []
    for city in ["helsinki", "amsterdam"]:
        folder = args.workspace / "evidence" / city
        checks = json.loads((folder / "mcp.json").read_text())
        if checks["failures"] or checks["checks_passed"] != len(checks["checks"]) or len(set(checks["tools_exercised"])) != 15:
            raise ValueError("Case evidence is incomplete or has failures")
        out = CASE / "evidence" / city
        out.mkdir(parents=True, exist_ok=True)
        for name in ["mcp.json", "mcp-tools.json", "native.json", "native-comparison.json"]:
            shutil.copyfile(folder / name, out / name)
        manifest = args.workspace / "inputs" / city / "manifest.json"
        shutil.copyfile(manifest, out / "harvest.json")
        for key, label in [("native_baseline", "baseline"), ("native_scenario", "closure")]:
            result = args.workspace / "results" / city / checks[key]
            shutil.copyfile(result / "accessibility.csv", out / (label + ".csv"))
            shutil.copyfile(result / "report.md", out / (label + "-report.md"))
        map_path = args.workspace / "results" / city / checks["mcp_baseline"] / "map.png"
        shutil.copyfile(map_path, out / "map.png")
        records.append({"city": city, "checks_passed": checks["checks_passed"], "tool_count": 15,
                        "manifest_sha256": digest(manifest), "implementation_sha256": checks["implementation_sha256"],
                        "baseline_csv_sha256": digest(out / "baseline.csv"), "closure_csv_sha256": digest(out / "closure.csv"), "map_sha256": digest(out / "map.png")})
    audit = json.loads(args.audit.read_text())
    if not any("same_node_set" in o for o in audit["observations"]):
        raise ValueError("Re-run the audit with the bounded-area native comparison")
    shutil.copyfile(args.audit, CASE / "evidence/upstream-audit.json")
    canonical = subprocess.run(["git", "show", "HEAD:urban_mcp_walking/engine.py"], cwd=ROOT, capture_output=True, check=True).stdout
    canonical_sha = hashlib.sha256(canonical).hexdigest()
    if any(r["implementation_sha256"] != canonical_sha for r in records):
        raise ValueError("Executing engine bytes differ from the committed canonical source")
    document = {"method": "Fresh public-release restoration in Docker followed by native oracle and MCP stdio subprocess checks in both cities",
                "code_commit_observed": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
                "canonical_engine_sha256": canonical_sha, "runtime_lock_sha256": digest(ROOT / "adapters/walking/runtime.lock.txt"),
                "snapshots": json.loads((CASE / "snapshot.lock.json").read_text()), "cities": records,
                "synthetic_integrity_regressions": {"suite": "urban_mcp_walking.test_contracts", "tests": 6, "separate_from_city_evidence": True},
                "limits": "Only the documented operations, two study areas, source observations and parameters. Host evidence and narrative review are recorded separately."}
    (CASE / "evidence/reproduction.json").write_text(json.dumps(document, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(records, indent=2))


if __name__ == "__main__":
    main()
