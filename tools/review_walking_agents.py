"""Compare independent host artifacts with committed native evidence.

This checks artifacts/tool use. Human review of the final narrative is separate.
It must not label an answer correct merely because tables match.
"""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import re

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / "cases/two-city-walking"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--codex-suffix", default="v2")
    parser.add_argument("--hermes-suffix", default="final")
    parser.add_argument("--evidence-dir",type=Path,default=CASE/"evidence")
    parser.add_argument("--task",type=Path,default=CASE/"agent-task.md")
    parser.add_argument("--diagnostics",action="store_true",help="Require full diagnostic tool equality and independently check the answer's JSON claims")
    args = parser.parse_args()
    review_path=args.evidence_dir/"narrative-review.json"
    reviews=json.loads(review_path.read_text())["reviews"] if review_path.exists() else {}
    records = []
    for city in ["helsinki", "amsterdam"]:
        original = json.loads((args.evidence_dir/city/"native.json").read_text())
        advertised = {t["name"] for t in json.loads((args.evidence_dir/city/"mcp-tools.json").read_text())}
        for host, suffix in [("codex", args.codex_suffix), ("hermes", args.hermes_suffix)]:
            label = "walking-" + city + "-" + suffix
            private = ROOT / ".urban-mcp/agent-evidence" / (host + "-" + label)
            workspace = ROOT / ".urban-mcp" / (host + "-" + label)
            process = json.loads((private / "process.json").read_text())
            if process["exit_code"] != 0 or process["task_template_sha256"] != digest(args.task):
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
                if csv_hash != digest(args.evidence_dir/city/(label_name+".csv")):
                    raise ValueError("Agent/native CSV differs")
                hashes[label_name + "_csv_sha256"] = csv_hash
            if digest(baseline_path / "map.png") != digest(args.evidence_dir/city/"map.png"):
                raise ValueError("Agent/native map differs")
            source = json.loads((workspace / "inputs" / city / "manifest.json").read_text())
            export_call=next(c for c in trace["calls"] if c["tool"].removeprefix("mcp__urban_mcp_walking__")=="walking_export_graph" and c["arguments"].get("city")==city)
            export_id=export_call["arguments"]["run_id"]
            if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}",export_id):raise ValueError("Unsafe export run ID")
            export_path=workspace/"results"/city/export_id/"network.graphml"
            if digest(export_path) != source["files"]["network.graphml"]["sha256"]:
                raise ValueError("Agent GraphML export differs from input")
            hashes.update(map_sha256=digest(baseline_path / "map.png"), graphml_sha256=digest(export_path), graphml_export_run_id=export_id)
            answer = (private / "answer.md").read_text(encoding="utf-8")
            destination = args.evidence_dir/city
            diagnostics_record={}
            if args.diagnostics:
                native_comparison=json.loads((destination/"native-comparison.json").read_text())
                native_route=json.loads((destination/"native-route-diagnostics.json").read_text())
                compare_results=json.loads((private/"comparison-results.json").read_text())
                route_results=json.loads((private/"route-results.json").read_text())
                remote_comparison=next(r["result"] for r in compare_results if r["arguments"].get("baseline_id")=="agent-baseline" and r["arguments"].get("scenario_id")=="agent-closure")
                remote_route=next(r["result"] for r in route_results if r["arguments"].get("origin_id")==native_route["request"]["origin_id"] and r["arguments"].get("destination_id")==native_route["request"]["destination_id"] and r["arguments"].get("k")==2)
                semantic=lambda r:{k:v for k,v in r.items() if k not in {"baseline_id","scenario_id"}}
                if semantic(remote_comparison)!=semantic(native_comparison) or remote_route!=native_route["result"]:
                    raise ValueError("Agent full diagnostic tool results differ from native evidence")
                expected={"city":city,"route_origin_id":native_route["request"]["origin_id"],
                          **{k:native_comparison[k] for k in ["crossed_threshold_origin_ids","affected_still_within_origin_ids","newly_unreachable_origin_ids","baseline_routes_using_closed_link_origin_ids","scenario_routes_using_closed_link_origin_ids"]},
                          "path_membership":[{k:p[k] for k in ["rank","uses_closed_link","avoids_all_declared_closed_links"]} for p in native_route["result"]["paths"]],
                          "path_ranks_avoiding_declared_closed_links":native_route["result"]["path_ranks_avoiding_declared_closed_links"]}
                candidates=[]
                for match in re.finditer(r"```(?:json)?\s*(\{.*?\})\s*```",answer,re.DOTALL):
                    try:value=json.loads(match.group(1))
                    except ValueError:continue
                    if isinstance(value,dict) and value.get("city")==city:candidates.append(value)
                claims=candidates[0] if len(candidates)==1 else {}
                mismatches=[]
                for key,value in expected.items():
                    actual=claims.get(key)
                    if isinstance(value,list) and key!="path_membership":
                        correct=isinstance(actual,list) and sorted(actual,key=json.dumps)==sorted(value,key=json.dumps)
                    elif key=="path_membership":
                        keys=["rank","uses_closed_link","avoids_all_declared_closed_links"]
                        correct=isinstance(actual,list) and all(isinstance(p,dict) and type(p.get("rank")) is int and type(p.get("uses_closed_link")) is bool and type(p.get("avoids_all_declared_closed_links")) is bool for p in actual) and sorted([{k:p[k] for k in keys} for p in actual],key=lambda p:p["rank"])==value
                    else:correct=actual==value
                    if not correct:mismatches.append(key)
                diagnostics_record={"diagnostic_tool_results_match_native":True,
                                    "machine_claims":{"status":"passed" if not mismatches else "failed","observed":claims,"mismatched_fields":mismatches}}
                for name in ["comparison-results.json","route-results.json"]:
                    shutil.copyfile(private/name,destination/(host+"-"+name))
            for source_name, public_name in [("trace.json", host + "-trace.json"), ("answer.md", host + "-answer.md"), ("process.json", host + "-process.json")]:
                shutil.copyfile(private / source_name, destination / public_name)
            review=reviews.get(city+":"+host)
            if review and review["answer_sha256"]!=digest(private / "answer.md"):
                raise ValueError("Narrative review belongs to a different observed answer")
            records.append({"city": city, "host": host, "process_exit_code": process["exit_code"], "mcp_calls_recorded": len(trace["calls"]),
                            "advertised_tools_exercised": sorted(advertised), "artifacts_match_native": True, "artifact_hashes": hashes,
                            "answer_sha256": digest(private / "answer.md"), "answer_word_count": len(answer.split()),
                            **diagnostics_record,"narrative_review": review or {"status":"pending explicit primary-agent review; artifact checks alone do not admit prose"}})
    document = {"task":str(args.task.resolve().relative_to(ROOT)).replace("\\","/"),"task_template_sha256":digest(args.task),
                "task_contains_expected_numerical_answers": False, "workspaces": "Independent and initially empty for each city/host; original host authentication only",
                "hosts": records, "narrative_review": "See narrative-review.md; numerical artifact equality does not establish factual correctness of every sentence"}
    (args.evidence_dir/"agents.json").write_text(json.dumps(document, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps([{k: r[k] for k in ["city", "host", "mcp_calls_recorded", "artifacts_match_native", "answer_word_count"]} for r in records], indent=2))
    if args.diagnostics and any(r["machine_claims"]["status"]!="passed" for r in records):
        raise SystemExit("One or more answer claim objects failed independent checks; evidence preserved")


if __name__ == "__main__":
    main()
