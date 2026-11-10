"""Verify observed host responses, complete paged CSVs and artifacts independently.

Narrative review is explicit and hash-bound; this script never invents a prose verdict.
Private host databases/events/configuration are not copied to the public dossier.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from urban_mcp_vegetation.interface import public_summary

CASE = ROOT / "cases/two-city-vegetation"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def semantic(value):
    return {k: v for k, v in value.items() if k not in {"run_id", "baseline_id", "scenario_id"}}


def expected_claims(baseline, sensitivity, comparison):
    return {
        "city": baseline["city"], "landcover_year": baseline["landcover_year"],
        "population_date": baseline["population_date"], "zone_count": baseline["zone_count"],
        "low_zone_ids_at_020": baseline["low_vegetation_zone_ids"],
        "low_zone_ids_at_040": sensitivity["low_vegetation_zone_ids"],
        "population_in_low_zones_at_020": baseline["population_in_low_vegetation_zones"],
        "population_in_low_zones_at_040": sensitivity["population_in_low_vegetation_zones"],
        "no_valid_land_zone_ids": baseline["no_valid_land_zone_ids"],
        "unknown_population_zone_ids": baseline["population_reconciliation"]["unknown_population_zone_ids"],
        "municipal_minus_zone_population": baseline["population_reconciliation"]["municipal_minus_zone_population"],
        **{k: comparison[k] for k in ["newly_below_threshold_zone_ids", "no_longer_below_threshold_zone_ids"]},
    }


def check_claims(answer, expected):
    candidates = []
    for match in re.finditer(r"```json\s*(\{.*?\})\s*```", answer, re.DOTALL):
        try:
            value = json.loads(match.group(1))
        except ValueError:
            continue
        if isinstance(value, dict) and value.get("city") == expected["city"]:
            candidates.append(value)
    observed = candidates[0] if len(candidates) == 1 else {}
    mismatches = []
    for key, value in expected.items():
        actual = observed.get(key)
        if isinstance(value, list):
            correct = isinstance(actual, list) and all(type(v) is str for v in actual) and sorted(actual) == sorted(value)
        else:
            correct = type(actual) is type(value) and actual == value
        if not correct:
            mismatches.append(key)
    if set(observed) != set(expected):
        mismatches.append("exact_field_set")
    return {"status": "failed" if mismatches else "passed", "observed": observed, "mismatched_fields": mismatches}


def review_pages(results, workspace, city):
    receipts = []
    for run_id, name in [("agent-baseline", "zone_metrics.csv"), ("agent-sensitivity", "zone_metrics.csv"), ("agent-baseline", "class_counts.csv")]:
        path = workspace / "results" / city / run_id / name
        text = path.read_text(encoding="utf-8")
        selected = [r for r in results if r["arguments"].get("run_id") == run_id and r["arguments"].get("name", "summary.json") == name and "text" in r["result"]]
        pages = {}
        for row in selected:
            args, result = row["arguments"], row["result"]
            offset, limit = args.get("offset", 0), args.get("limit", 8000)
            if type(offset) is not int or type(limit) is not int or offset < 0 or not 1 <= limit <= 12000:
                raise ValueError("Invalid observed page request")
            next_offset = offset + limit if len(text) > offset + limit else None
            if result != {"name": name, "bytes": path.stat().st_size, "sha256": digest(path), "text": text[offset:offset+limit], "characters": len(text), "next_offset": next_offset}:
                raise ValueError(f"Observed artifact page differs: {city}/{run_id}/{name}/{offset}")
            pages[offset] = {"offset": offset, "requested_limit": limit, "characters": len(result["text"]), "text_sha256": hashlib.sha256(result["text"].encode()).hexdigest(), "next_offset": next_offset}
        offset, chain = 0, []
        while True:
            if offset not in pages:
                raise ValueError(f"Host did not read the entire required CSV: {city}/{run_id}/{name}, missing {offset}")
            page = pages[offset]
            chain.append(page)
            if page["next_offset"] is None:
                break
            offset = page["next_offset"]
        receipts.append({"run_id": run_id, "name": name, "sha256": digest(path), "all_observed_pages_match_native_artifact": True, "pages": chain})
    return receipts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--suffix", default="v2")
    args = parser.parse_args()
    task = CASE / "agent-task-v2.md"
    review_path = CASE / "evidence/narrative-review.json"
    reviews = load(review_path)["reviews"] if review_path.exists() else {}
    records = []
    for city in ["helsinki", "amsterdam"]:
        destination = CASE / "evidence" / city
        native = [load(destination / n) for n in ["native.json", "native-sensitivity.json", "native-comparison.json"]]
        advertised = {t["name"] for t in load(destination / "mcp-tools.json")}
        for host in ["codex", "hermes"]:
            label = f"{host}-vegetation-{city}-{args.suffix}"
            private = ROOT / ".urban-mcp/agent-evidence" / label
            workspace = ROOT / ".urban-mcp" / label
            process, trace = load(private / "process.json"), load(private / "trace.json")
            if process["exit_code"] != 0 or process["task_template_sha256"] != digest(task):
                raise ValueError("Process/task mismatch")
            code_checks = load(destination / "mcp.json")
            for field, filename in [("implementation_sha256", "engine.py"), ("server_sha256", "server.py"), ("data_code_sha256", "data.py"), ("interface_code_sha256", "interface.py")]:
                launched = subprocess.check_output(["git", "show", process["code_commit"]+":urban_mcp_vegetation/"+filename], cwd=ROOT)
                if hashlib.sha256(launched).hexdigest() != code_checks[field]:
                    raise ValueError("Host launch source and executing native source differ")
            names = {c["tool"].removeprefix("mcp__urban_mcp_vegetation__") for c in trace["calls"]}
            if not advertised.issubset(names) or trace.get("other_tool_use"):
                raise ValueError(f"Missing or unrelated tools: {host}/{city}/{advertised - names}")
            if host == "hermes" and any(not c["tool"].startswith("mcp__urban_mcp_vegetation__") for c in trace["calls"]):
                raise ValueError("Unrelated Hermes tool use")
            successful = {c["tool"].removeprefix("mcp__urban_mcp_vegetation__") for c in trace["calls"] if c.get("response_recorded") and c.get("status", "completed") == "completed" and not c.get("error") and not re.search(r'\{\s*"error"\s*:', c.get("response_excerpt", ""))}
            if not advertised.issubset(successful):
                raise ValueError(f"Tools attempted but lacking an observed successful response: {advertised-successful}")
            hashes = {}
            for run, expected, prefix in [("agent-baseline", native[0], "baseline"), ("agent-sensitivity", native[1], "sensitivity")]:
                folder = workspace / "results" / city / run
                if semantic(load(folder / "summary.json")) != semantic(expected):
                    raise ValueError(f"Agent/native full summary mismatch: {host}/{city}/{run}")
                for name, public_name in [("zone_metrics.csv", prefix+".csv"), ("class_counts.csv", prefix+"-classes.csv")]:
                    if digest(folder / name) != digest(destination / public_name):
                        raise ValueError("Agent/native CSV mismatch")
                    hashes[public_name] = digest(folder / name)
            map_path = workspace / "results" / city / "agent-baseline/map.png"
            if digest(map_path) != digest(destination / "map.png"):
                raise ValueError("Agent/native map mismatch")
            hashes["map.png"] = digest(map_path)
            selected = load(private / "analysis-results.json")
            for run, expected in [("agent-baseline", native[0]), ("agent-sensitivity", native[1])]:
                actual = [r["result"] for r in selected if r["arguments"].get("run_id") == run]
                if len(actual) != 1 or semantic(actual[0]) != semantic(public_summary(expected)):
                    raise ValueError("Actual bounded MCP response incomplete or differs from native")
            comparisons = [r["result"] for r in load(private / "comparison-results.json") if r["arguments"].get("baseline_id") == "agent-baseline" and r["arguments"].get("scenario_id") == "agent-sensitivity"]
            if len(comparisons) != 1 or semantic(comparisons[0]) != semantic(native[2]):
                raise ValueError("Actual MCP comparison differs from native")
            pages = review_pages(load(private / "artifact-results.json"), workspace, city)
            answer = (private / "answer.md").read_text(encoding="utf-8")
            claims = check_claims(answer, expected_claims(*native))
            review = reviews.get(city+":"+host)
            if review and review["answer_sha256"] != digest(private / "answer.md"):
                raise ValueError("Narrative review belongs to a different answer")
            for name in ["answer.md", "trace.json", "process.json", "analysis-results.json", "comparison-results.json"]:
                shutil.copyfile(private / name, destination / (host+"-"+name))
            records.append({"city": city, "host": host, "source_commit_at_launch": process["code_commit"], "process_exit_code": 0,
                            "mcp_calls_recorded": len(trace["calls"]), "advertised_tools_exercised": sorted(advertised), "advertised_tools_with_successful_response": sorted(advertised & successful),
                            "artifacts_match_native": True, "actual_mcp_analysis_and_comparison_match_native": True,
                            "artifact_sha256": hashes, "observed_csv_pages": pages, "machine_claims": claims,
                            "answer_sha256": digest(private / "answer.md"), "prose_word_count": len(answer.split("```json")[0].split()),
                            "narrative_review": review or {"status": "pending_explicit_factual_review"}})
    document = {"task": "cases/two-city-vegetation/agent-task-v2.md", "task_template_sha256": digest(task), "task_contains_expected_numerical_answers": False,
                "workspaces": "Separate initially empty workspaces for each city/host; existing host authentication only; public source snapshot restored through MCP",
                "hosts": records, "qualification": "Original-team host observations do not satisfy independent-person third-city product qualification"}
    (CASE / "evidence/agents.json").write_text(json.dumps(document, indent=2)+"\n", encoding="utf-8", newline="\n")
    print(json.dumps([{k: r[k] for k in ["city", "host", "mcp_calls_recorded", "artifacts_match_native", "machine_claims"]} for r in records], indent=2))
    if any(r["machine_claims"]["status"] != "passed" for r in records):
        raise SystemExit("Failed structured answer claims; observations preserved")


if __name__ == "__main__":
    main()
