"""Verify full observed host payloads, paging, outputs and claims against native evidence."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import re
import shutil
import subprocess

ROOT=Path(__file__).resolve().parents[1];CASE=ROOT/"cases/two-city-sumo"
TOOLS={"get_sumo_info","control_simulation","query_simulation_state","run_analysis","sumo_status","harvest_sumo_data","read_sumo_source","prepare_sumo_case","sumo_network_info","run_sumo_scenario","compare_sumo_runs","read_sumo_artifact","render_sumo_map"}


def load(path):return json.loads(path.read_text(encoding="utf-8"))
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def semantic(value):return {k:v for k,v in value.items() if k not in {"config","run_id","baseline_id","scenario_id"}}


def expected_claims(baseline,works,comparison):
    return {"city":baseline["city"],"target_edge_id":baseline["target_edge"]["id"],"target_lane_ids":[l["id"] for l in baseline["target_edge"]["lanes"]],"scheduled_vehicles":baseline["scheduled_vehicles"],**{k:comparison[k] for k in ["scheduled_corridor_cohort","baseline_states","works_states","matched_completed_cohort","eligible_paired_comparison","excluded_censored_pairs","excluded_teleport_identified_completed_pairs","increased_over_30s","mean_matched_scheduled_to_arrival_delta_s","mean_matched_in_network_duration_delta_s","mean_matched_insertion_delay_delta_s","comparison_sha256"]},"baseline_native_teleport_events":baseline["model_quality"]["native_teleport_events"],"works_native_teleport_events":works["model_quality"]["native_teleport_events"],"baseline_native_collisions":baseline["model_quality"]["native_collisions"],"works_native_collisions":works["model_quality"]["native_collisions"],"calibration_revalidated":False,"forecast_admitted":False,"new_random_demand_generated":False}


def exact(actual,expected):
    if type(expected) is float:
        return type(actual) in {int,float} and math.isfinite(actual) and math.isclose(actual,expected,abs_tol=1e-5,rel_tol=0)
    if type(actual) is not type(expected):return False
    if isinstance(expected,dict):return set(actual)==set(expected) and all(exact(actual[k],v) for k,v in expected.items())
    if isinstance(expected,list):return len(actual)==len(expected) and all(exact(a,b) for a,b in zip(actual,expected))
    return actual==expected


def claims(answer,expected):
    candidates=[]
    for match in re.finditer(r"```json\s*(\{.*?\})\s*```",answer,re.DOTALL):
        try: value=json.loads(match.group(1))
        except ValueError:continue
        if isinstance(value,dict) and value.get("city")==expected["city"]:candidates.append(value)
    observed=candidates[0] if len(candidates)==1 else {}
    errors=[k for k,v in expected.items() if not exact(observed.get(k),v)]
    if set(observed)!=set(expected):errors.append("exact_field_set")
    return {"passed":not errors,"mismatched_fields":errors,"observed":observed}


def pages(calls,tool,args,path):
    text=path.read_text(encoding="utf-8");observed={}
    for call in calls:
        if call["tool"]!=tool or not all(call["arguments"].get(k)==v for k,v in args.items()):continue
        result=call.get("result")
        if not isinstance(result,dict) or "text" not in result:continue
        offset=call["arguments"].get("offset",0);limit=call["arguments"].get("limit",8000)
        if type(offset) is not int or type(limit) is not int or offset<0 or not 1<=limit<=12000:raise ValueError("Invalid page request")
        nxt=offset+limit if offset+limit<len(text) else None
        expected={"name":args["name"],"bytes":path.stat().st_size,"sha256":sha(path),"text":text[offset:offset+limit],"characters":len(text),"next_offset":nxt}
        if result!=expected:raise ValueError("Observed page differs from complete backend bytes: "+str(args)+" at "+str(offset))
        observed[offset]={"offset":offset,"characters":len(result["text"]),"next_offset":nxt,"text_sha256":hashlib.sha256(result["text"].encode()).hexdigest()}
    offset=0;chain=[]
    while True:
        if offset not in observed:raise ValueError("Incomplete observed pages: "+str(args)+" missing "+str(offset))
        page=observed[offset];chain.append(page)
        if page["next_offset"] is None:break
        offset=page["next_offset"]
    return {"source":tool,"arguments":args,"sha256":sha(path),"pages":chain,"all_pages_match":True}


def success(call):
    value=call.get("result")
    return call.get("status")=="completed" and value is not None and not (isinstance(value,dict) and (value.get("error") or value.get("isError"))) and not (isinstance(value,str) and value.startswith(("Error","Analysis error")))


def review(host,city,workspace,observations):
    out=CASE/"evidence"/city
    baseline=load(out/"baseline-summary.json");works=load(out/"works-summary.json");comparison=load(out/"comparison.json")
    trace=load(observations/"trace.json");process=load(observations/"process.json");answer=(observations/"answer.md").read_text(encoding="utf-8")
    calls=trace["calls"];passed=[c for c in calls if success(c)]
    errors=[]
    def check(name,condition):
        if not condition:errors.append(name)
    check("host exit",process["exit_code"]==0)
    task=ROOT/process["task_path"]
    check("task at launch",sha(task)==process["task_template_sha256"])
    submitted=task.read_text(encoding="utf-8").replace("{{city}}",city)+"\nYour host name is "+host+".\n"
    check("exact submitted public task",hashlib.sha256(submitted.encode()).hexdigest()==process["submitted_prompt_sha256"])
    for name in ["engine.py","server.py","data.py","compat.py"]:
        canonical=subprocess.check_output(["git","show",process["code_commit"]+":urban_mcp_sumo/"+name],cwd=ROOT)
        check("launch source "+name,hashlib.sha256(canonical).hexdigest()==load(out/"native-mcp.json")["source_sha256"][name])
    check("all thirteen successful tool families",{c["tool"] for c in passed}==TOOLS)
    check("no unrelated tool use",not trace.get("other_tool_use"))
    for run_id,native in [("agent-baseline",baseline),("agent-works",works)]:
        actual=load(workspace/"results"/city/run_id/"summary.json")
        check(run_id+" summary equals native",semantic(actual)==semantic(native))
        responses=[c["result"] for c in passed if c["tool"]=="run_sumo_scenario" and c["arguments"].get("run_id")==run_id]
        check(run_id+" complete actual scenario response",len(responses)==1 and semantic(responses[0])==semantic(native))
        for name in ["all-vehicles.csv","cohort.csv"]:
            label="baseline" if run_id=="agent-baseline" else "works"
            check(run_id+" "+name+" equals native",sha(workspace/"results"/city/run_id/name)==sha(out/(label+"-"+name)))
    compared=[c["result"] for c in passed if c["tool"]=="compare_sumo_runs"]
    check("complete actual comparison response",len(compared)==1 and semantic(compared[0])==semantic(comparison))
    check("actual map equals native",sha(workspace/"results"/city/"agent-works/map.png")==sha(out/"map.png"))
    map_receipt={"name":"map.png","bytes":(out/"map.png").stat().st_size,"sha256":sha(out/"map.png")}
    # Rendering itself returns the complete receipt requested by the task.
    # An optional separate read must agree; it is not a second image viewing.
    check("actual map receipt observed",any(c["tool"]=="render_sumo_map" and c["result"]==map_receipt for c in passed) and all(c["result"]==map_receipt for c in passed if c["tool"]=="read_sumo_artifact" and c["arguments"].get("name")=="map.png"))
    check("all five original variables queried",{c["arguments"].get("params",{}).get("variable") for c in passed if c["tool"]=="query_simulation_state" and c["arguments"].get("target")=="vehicle_variable"}=={"speed","position","acceleration","lane","route"})
    check("original connection lifecycle exercised",{c["arguments"].get("action") for c in passed if c["tool"]=="control_simulation"}=={"connect","step","disconnect"})
    cfg=load(CASE/"recipe.json")["cities"][city]
    check("absolute live step",any(c["tool"]=="control_simulation" and c["arguments"].get("action")=="step" and c["arguments"].get("params",{}).get("step")==cfg["begin"]+30 and c["result"].get("absolute_simulation_time")==cfg["begin"]+30 for c in passed))
    required=[("read_sumo_artifact",{"city":city,"run_id":"agent-works","name":"comparison.csv"},workspace/"results"/city/"agent-works/comparison.csv"),
              ("read_sumo_artifact",{"city":city,"run_id":"agent-works","name":"comparison.json"},workspace/"results"/city/"agent-works/comparison.json")]
    for run_id in ["agent-baseline","agent-works"]:
        required.append(("read_sumo_artifact",{"city":city,"run_id":run_id,"name":"summary.json"},workspace/"results"/city/run_id/"summary.json"))
    for name in ["manifest.json",cfg["config"],next(n["file"] for n in cfg["assets"] if "license" in n["file"].lower())]:
        required.append(("read_sumo_source",{"city":city,"name":name},workspace/"inputs"/city/name))
    paging=[]
    for tool,args,path in required:
        try:paging.append(pages(calls,tool,args,path))
        except ValueError as exc:errors.append(str(exc))
    rejected=[c for c in calls if not success(c)]
    check("deliberate errors retained",len(rejected)>=4)
    check("invalid city tested",any(c["arguments"].get("city") not in {None,"bologna","ingolstadt"} for c in rejected))
    check("invalid scenario tested",any(c["tool"]=="run_sumo_scenario" and c["arguments"].get("scenario") not in {None,"baseline","works30"} for c in rejected))
    check("artifact traversal tested",any(c["tool"]=="read_sumo_artifact" and ".." in c["arguments"].get("name","") for c in rejected))
    check("disconnected query tested",any(c["tool"]=="query_simulation_state" and "No active inspection session" in str(c.get("result")) for c in rejected))
    # A later successful status call establishes recovery after each deliberate error.
    check("recovery after each rejected call",all(any(success(c) and c["tool"]=="sumo_status" for c in calls[i+1:]) for i,c in enumerate(calls) if not success(c)))
    checked_claims=claims(answer,expected_claims(baseline,works,comparison))
    check("final JSON claims",checked_claims["passed"])
    record={"host":host,"city":city,"computational_workflow_passed":not errors,"errors":errors,"successful_tools":sorted({c["tool"] for c in passed}),"tool_calls":len(calls),"failed_or_rejected_calls":len(rejected),"source_commit_at_launch":process["code_commit"],"task_sha256":process["task_template_sha256"],"answer_sha256":sha(observations/"answer.md"),"trace_sha256":sha(observations/"trace.json"),"process_sha256":sha(observations/"process.json"),"complete_observed_pages":paging,"structured_claims":checked_claims,"prose_review":"Separate explicit hash-bound narrative-review.json; this script does not invent a prose verdict."}
    for source,label in [("trace.json","trace.json"),("answer.md","answer.md"),("process.json","process.json")]:shutil.copyfile(observations/source,out/(host+"-"+label))
    (out/(host+"-review.json")).write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8",newline="\n")
    return record


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("host",choices=["codex","hermes"]);p.add_argument("--city",choices=["bologna","ingolstadt"],required=True)
    p.add_argument("--workspace",type=Path,required=True);p.add_argument("--observations",type=Path,required=True);a=p.parse_args()
    record=review(a.host,a.city,a.workspace,a.observations)
    print(json.dumps({k:record[k] for k in ["host","city","computational_workflow_passed","errors"]},indent=2))
    if not record["computational_workflow_passed"]:raise SystemExit(1)


if __name__=="__main__":main()
