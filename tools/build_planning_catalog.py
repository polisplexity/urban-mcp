"""Import a sanitized research snapshot and explicitly authored data requirements.

Maintainer utility, not an engine runtime or a decision about its language.
"""
import argparse
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def dump(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("research", type=Path)
    args = parser.parse_args()
    research = args.research
    catalog = json.loads((research / "catalog.json").read_text(encoding="utf-8"))["repositories"]
    decisions = {r["repository"]: r for r in csv.DictReader((research / "integration-decisions.tsv").open(encoding="utf-8"), delimiter="|")}
    commits = {r["repository"]: r["commit"] for r in json.loads((research / "integration-source-audit-20261110.json").read_text(encoding="utf-8"))}
    assignments = {}
    for row in csv.DictReader((ROOT / "planning/tool-data-map.tsv").open(encoding="utf-8"), delimiter="|"):
        repo = row["repository"]
        if repo in assignments:
            raise ValueError(f"Duplicate mapping: {repo}")
        assignments[repo] = row
    expected = {r["repository"] for r in catalog} | {"external:palm", "external:telemac", "external:simstadt"}
    if set(assignments) != expected:
        raise ValueError(f"Mapping mismatch missing={expected-set(assignments)} unexpected={set(assignments)-expected}")
    rows = []
    for upstream in catalog:
        repo = upstream["repository"]
        mapping = assignments[repo]
        decision = decisions[repo]
        rows.append({
            "id": upstream["id"], "repository": repo, "url": upstream["url"],
            "category": upstream["category"], "kind": upstream["kind"],
            "source_commit_observed": commits[repo], "research_date": "2026-11-10",
            "data_profile": mapping["profile"], "data_note": mapping["note"],
            "scope_proposal": decision["dictamen"],
            "reuse": decision["traer"], "original_interface": decision["entrada"],
            "proposed_delta": decision["construir"],
            "implementation_proposal": decision["tecnologia_motivo"],
            "critical_limit": decision["no_duplicar_y_riesgo"],
            "acceptance_case_proposal": decision["prueba"],
            "license_detection": upstream.get("license_spdx_github"),
            "license_review": upstream["license_classification"],
            "execution_role": "reference" if decision["dictamen"] in ("referencia", "no-ejecutable") else "dependency" if decision["dictamen"] == "dependencia" else "candidate",
            "input_binding_status": "not_implemented", "engine_runtime_status": "not_verified",
            "reference_case_status": "not_verified", "real_city_status": "needs_input_review",
            "ready_to_run": False,
        })
    externals = json.loads((research / "external-sources.json").read_text(encoding="utf-8"))
    for item in externals:
        key = "external:" + item["id"]
        mapping = assignments[key]
        rows.append({"id": item["id"], "repository": key, "url": item["repository"],
            "category": item["category"], "kind": "external_engine", "source_commit_observed": None,
            "research_date": "2026-11-10", "data_profile": mapping["profile"], "data_note": mapping["note"],
            "scope_proposal": "especialista", "reuse": item["purpose"],
            "original_interface": "Version/API/CLI to be selected from upstream evidence",
            "proposed_delta": "Data preparation, existing runtime integration and reproducible cases, subject to review",
            "implementation_proposal": "Preserve the native engine; do not select a universal MCP framework",
            "critical_limit": "Source, data and runtime admission are pending; documented commands are not execution evidence",
            "acceptance_case_proposal": "Reproduce one upstream example before proposing a real-city case",
            "license_detection": None, "license_review": "exact_revision_review_required",
            "execution_role": "candidate", "input_binding_status": "not_implemented",
            "engine_runtime_status": "not_verified", "reference_case_status": "not_verified",
            "real_city_status": "needs_input_review", "ready_to_run": False})
    dump(ROOT / "registry/tools.json", {"schema_version": "0.1.0", "status": "rfc_proposal", "tools": rows})
    print(f"Imported {len(rows)} public candidates; no runtime promoted to ready.")


if __name__ == "__main__":
    main()
