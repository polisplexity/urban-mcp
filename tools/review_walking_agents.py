"""Compare independent host artifacts with committed native evidence.

This checks artifacts/tool use. Human review of the final narrative is separate.
It must not label an answer correct merely because tables match.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / "cases/two-city-walking"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--codex-suffix", default="v2")
    parser.add_argument("--hermes-suffix", default="final")
    args = parser.parse_args()
    review_path=CASE / "evidence/narrative-review.json"
    reviews=json.loads(review_path.read_text())["reviews"] if review_path.exists() else {}
    records = []
    for city in ["helsinki", "amsterdam"]:
        original = json.loads((CASE / "evidence" / city / "native.json").read_text())
        advertised = {t["name"] for t in json.loads((CASE / "evidence" / city / "mcp-tools.json").read_text())}
        for host, suffix in [("codex", args.codex_suffix), ("hermes", args.hermes_suffix)]:
            label = "walking-" + city + "-" + suffix
            private = ROOT / ".urban-mcp/agent-evidence" / (host + "-" + label)
            workspace = ROOT / ".urban-mcp" / (host + "-" + label)
            process = json.loads((private / "process.json").read_text())
            if process["exit_code"] != 0 or process["task_template_sha256"] != digest(CASE / "agent-task.md"):
                raise ValueError("Process/task mismatch")
            trace = json.loads((private / "trace.json").read_text())
            names = {c["tool"].removeprefix("mcp__urban_mcp_walking__") for c in trace["calls"]}
            if not advertised.issubset(names):
                raise ValueError(f"{host}/{city} did not exercise every advertised tool: {advertised - names}")
            if host == "hermes" and any(not c["tool"].startswith("mcp__urban_mcp_walking__") for c in trace["calls"]):
                raise ValueError("Unrelated Hermes tool use")
            baseline_path = workspace / "results" / city / "agent-baseline"
            closure_path = workspace / "results" / city / "agent-closure"
            baseline = json.loads((baseline_path / "summary.json").read_text())
            if {k: v for k, v in baseline.items() if k != "run_id"} != {k: v for k, v in original.items() if k != "run_id"}:
                raise ValueError("Agent/native baseline summary mismatch")
            hashes = {}
            for label_name, folder in [("baseline", baseline_path), ("closure", closure_path)]:
                csv_hash = digest(folder / "accessibility.csv")
                if csv_hash != digest(CASE / "evidence" / city / (label_name + ".csv")):
                    raise ValueError("Agent/native CSV differs")
                hashes[label_name + "_csv_sha256"] = csv_hash
            if digest(baseline_path / "map.png") != digest(CASE / "evidence" / city / "map.png"):
                raise ValueError("Agent/native map differs")
            source = json.loads((workspace / "inputs" / city / "manifest.json").read_text())
            if digest(baseline_path / "network.graphml") != source["files"]["network.graphml"]["sha256"]:
                raise ValueError("Agent GraphML export differs from input")
            hashes.update(map_sha256=digest(baseline_path / "map.png"), graphml_sha256=digest(baseline_path / "network.graphml"))
            answer = (private / "answer.md").read_text(encoding="utf-8")
            destination = CASE / "evidence" / city
            for source_name, public_name in [("trace.json", host + "-trace.json"), ("answer.md", host + "-answer.md"), ("process.json", host + "-process.json")]:
                shutil.copyfile(private / source_name, destination / public_name)
            review=reviews.get(city+":"+host)
            if review and review["answer_sha256"]!=digest(private / "answer.md"):
                raise ValueError("Narrative review belongs to a different observed answer")
            records.append({"city": city, "host": host, "process_exit_code": process["exit_code"], "mcp_calls_recorded": len(trace["calls"]),
                            "advertised_tools_exercised": sorted(advertised), "artifacts_match_native": True, "artifact_hashes": hashes,
                            "answer_sha256": digest(private / "answer.md"), "answer_word_count": len(answer.split()),
                            "narrative_review": review or {"status":"pending explicit primary-agent review; artifact checks alone do not admit prose"}})
    document = {"task": "cases/two-city-walking/agent-task.md", "task_template_sha256": digest(CASE / "agent-task.md"),
                "task_contains_expected_numerical_answers": False, "workspaces": "Independent and initially empty for each city/host; original host authentication only",
                "hosts": records, "narrative_review": "See narrative-review.md; numerical artifact equality does not establish factual correctness of every sentence"}
    (CASE / "evidence/agents.json").write_text(json.dumps(document, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps([{k: r[k] for k in ["city", "host", "mcp_calls_recorded", "artifacts_match_native", "answer_word_count"]} for r in records], indent=2))


if __name__ == "__main__":
    main()
