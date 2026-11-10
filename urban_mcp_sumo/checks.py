"""Independent native XML/CSV oracles and the complete scoped MCP contract."""
import ast
import asyncio
from collections import Counter
import csv
import gzip
import json
import math
import os
from pathlib import Path
import re
import sys
from uuid import uuid4
import xml.etree.ElementTree as ET

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from pydantic import AnyUrl
import sumolib
import traci

from . import data, engine
from .compat import install_traci_stderr

TOOLS = {"get_sumo_info", "control_simulation", "query_simulation_state", "run_analysis",
         "sumo_status", "harvest_sumo_data", "read_sumo_source", "prepare_sumo_case",
         "sumo_network_info", "run_sumo_scenario", "compare_sumo_runs",
         "read_sumo_artifact", "render_sumo_map"}


def payload(result):
    value = result.structuredContent
    if value is None:
        text = next(c.text for c in result.content if hasattr(c, "text"))
        try: value = json.loads(text)
        except ValueError: value = text
    return value["result"] if isinstance(value, dict) and set(value) == {"result"} else value


def semantic(value):
    """Ignore run identity/absolute output paths, never numeric model outputs."""
    return {k:v for k,v in value.items() if k not in {"run_id", "baseline_id", "scenario_id", "config"}}


def row_oracle(city, run_id):
    folder = data.root()/"results"/city/run_id
    with (data.root()/"prepared"/city/"schedule.csv").open(newline="") as stream:
        schedule = list(csv.DictReader(stream))
    raw = {n.attrib["id"]: n.attrib for n in ET.parse(folder/"tripinfo.xml").getroot() if n.tag == "tripinfo"}
    teleport_ids = set(re.findall(r"Teleporting vehicle '([^']+)'", (folder/"sumo-errors.log").read_text()))
    with (folder/"all-vehicles.csv").open(newline="") as stream:
        actual = {r["vehicle_id"]:r for r in csv.DictReader(stream)}
    errors = []
    cohort = {}
    for source in schedule:
        key = source["vehicle_id"]; trip = raw.get(key); row = actual.get(key)
        state = "not_recorded"
        if trip:
            state = ("undeparted" if float(trip["depart"]) < 0 else "unfinished" if float(trip["arrival"]) < 0
                     else "removed" if trip.get("vaporized") else "arrived")
        correct = row is not None and row["state"] == state and (row["teleport_warning_seen"] == "True") == (key in teleport_ids)
        for field in ["duration", "waitingTime", "timeLoss", "departDelay", "routeLength", "scheduled_to_arrival_s"]:
            expected = (float(trip["arrival"])-float(source["scheduled_depart"]) if field == "scheduled_to_arrival_s" else float(trip[field])) if state == "arrived" else None
            correct = correct and (math.isclose(float(row[field]), expected, abs_tol=1e-8, rel_tol=0) if expected is not None else row[field] == "")
        if not correct: errors.append(key)
        if source["corridor_cohort"] == "True": cohort[key] = row
    if set(actual) != {r["vehicle_id"] for r in schedule} or set(raw)-set(actual): errors.append("identity-set")
    return errors, cohort


async def run(city):
    quick = os.environ.get("URBAN_MCP_SUMO_QUICK") == "1"
    prefix = "check-"+uuid4().hex[:8]
    evidence = {"city":city, "quick_protocol_only":quick, "transport":"MCP SDK stdio subprocess", "checks":[], "tools_exercised":[], "failures":[], "runs":{}}
    out = data.root()/"evidence"/city; out.mkdir(parents=True,exist_ok=True)
    def check(name, condition, detail=None):
        evidence["checks"].append({"name":name,"passed":bool(condition),"detail":detail})
        if not condition: evidence["failures"].append(name)
        print(json.dumps({"check":name,"passed":bool(condition)}),flush=True)
    data.harvest(city,"snapshot")
    quality = engine.prepare(city); cfg = data.config(city)
    check("source snapshots and mandatory signal files verified", bool(data.verify(city)) and quality["traffic_lights"] > 0)
    # Check every original selected vehicle subtree, including type, stop, route
    # and behavior attributes; serialization whitespace is not a model input.
    def signature(node): return (node.tag, tuple(sorted(node.attrib.items())), tuple(signature(c) for c in node))
    original = {}
    for name in cfg["routes"]:
        with engine.xml_open(data.root()/"inputs"/city/name) as stream:
            root = None
            for event,node in ET.iterparse(stream,events=("start","end")):
                if root is None: root=node
                if event == "end" and node is not root and node in root:
                    if node.tag == "vehicle" and cfg["begin"] <= float(node.attrib["depart"]) < cfg["depart_end"]:
                        original[node.attrib["id"]] = signature(node)
                    root.remove(node)
    prepared = {n.attrib["id"]:signature(n) for n in ET.parse(data.root()/"prepared"/city/"routes.xml").getroot() if n.tag == "vehicle"}
    check("every selected vehicle preserves original attributes and complete route/stop subtree", original == prepared, {"vehicles":len(original)})
    native = []
    if not quick:
        for scenario in ["baseline","works30"]:
            result = await asyncio.to_thread(engine.run,city,prefix+"-native-"+scenario,scenario)
            native.append(result)
            evidence["runs"]["native-"+scenario] = result["run_id"]
            errors,cohort = row_oracle(city,result["run_id"])
            check(scenario+": every trip state and metric matches native tripinfo/teleport log", not errors, {"rows":result["scheduled_vehicles"],"mismatches":errors})
            check(scenario+": all censored states retained in cohort denominator", sum(result["corridor_cohort_states"].values()) == len(cohort) == quality["corridor_cohort_vehicles"])
            check(scenario+": teleport log reconciles native event counter and no forecast admitted", result["model_quality"]["teleport_log_reconciles_native_events"] and result["model_quality"]["forecast_admitted"] is False)
        comparison = engine.compare(city,native[0]["run_id"],native[1]["run_id"])
        pairs = [row_oracle(city,r["run_id"])[1] for r in native]
        expected = {}; censored=0; teleported=0
        for key,a in pairs[0].items():
            b = pairs[1][key]
            if a["state"] != "arrived" or b["state"] != "arrived": censored+=1
            elif a["teleport_warning_seen"] == "True" or b["teleport_warning_seen"] == "True": teleported+=1
            else: expected[key] = round(float(b["arrival"])-float(a["arrival"]),8)
        with (data.root()/"results"/city/native[1]["run_id"]/"comparison.csv").open(newline="") as stream: rows=list(csv.DictReader(stream))
        check("full keyed comparison independently reconciles eligible/censored/teleport pairs", len(rows)==len(pairs[0]) and {r["vehicle_id"]:float(r["scheduled_to_arrival_delta_s"]) for r in rows if r["eligible_paired_comparison"]=="True"}==expected and comparison["excluded_censored_pairs"]==censored and comparison["excluded_teleport_identified_completed_pairs"]==teleported)
        check("every strict threshold flag matches arrival-difference oracle", all((r["increased_over_30s"]==str(expected[r["vehicle_id"]]>30)) if r["vehicle_id"] in expected else r["increased_over_30s"]=="" for r in rows) and comparison["increased_over_30s"]==sum(v>30 for v in expected.values()))
        native_map=engine.render(city,native[1]["run_id"])
        config=ET.parse(data.root()/"results"/city/native[1]["run_id"]/"run.sumocfg").getroot()
        check("native config preserves seed, begin, end, step and publisher processing", all(config.find("time/"+k).attrib["value"]==str(cfg[v]) for k,v in [("begin","begin"),("end","end"),("step-length","step_length")]) and config.find("random_number/seed").attrib["value"]==str(data.recipe()["seed"]) and all(config.find("processing/"+k).attrib["value"]==str(v) for k,v in cfg["processing"].items()) and config.find("random_number/random") is None)
        sign=ET.parse(data.root()/"results"/city/native[1]["run_id"]/"works.add.xml").getroot().find("variableSpeedSign")
        check("works limits only selected faster passenger lanes at declared absolute time", sign.attrib["lanes"].split()==[l["id"] for l in quality["target_edge"]["lanes"]] and float(sign.find("step").attrib["time"])==cfg["cohort_begin"] and float(sign.find("step").attrib["speed"])==data.recipe()["speed_cap_m_s"])
    params=StdioServerParameters(command=sys.executable,args=["-m","urban_mcp_sumo","serve"],env=dict(os.environ))
    with (out/(prefix+"-mcp-stderr.log")).open("w") as errlog:
        async with stdio_client(params,errlog=errlog) as (read,write):
            async with ClientSession(read,write) as session:
                await session.initialize()
                listed=await session.list_tools()
                check("exact scoped thirteen-tool discovery", {t.name for t in listed.tools}==TOOLS)
                async def call(name,arguments=None,error=False):
                    result=await session.call_tool(name,arguments or {},read_timeout_seconds=__import__("datetime").timedelta(seconds=420))
                    check(name+(": expected rejection" if error else ": protocol success"),bool(result.isError)==error)
                    if not error and not result.isError: evidence["tools_exercised"].append(name)
                    return payload(result)
                async def pages(name,args,path):
                    offset=0; chunks=[];count=0
                    while True:
                        result=await call(name,{**args,"offset":offset,"limit":12000})
                        chunks.append(result["text"]);count+=1
                        if result["next_offset"] is None: break
                        if result["next_offset"] <= offset: raise ValueError("Non-advancing page")
                        offset=result["next_offset"]
                    check("complete paged "+path.name,"".join(chunks)==path.read_text(encoding="utf-8") and result["sha256"]==data.sha(path),{"pages":count,"sha256":result["sha256"]})
                await call("get_sumo_info")
                await call("sumo_status")
                await call("harvest_sumo_data",{"city":city,"mode":"snapshot"})
                await pages("read_sumo_source",{"city":city,"name":"manifest.json"},data.root()/"inputs"/city/"manifest.json")
                license_name=next(n["file"] for n in cfg["assets"] if "license" in n["file"].lower())
                await pages("read_sumo_source",{"city":city,"name":license_name},data.root()/"inputs"/city/license_name)
                await call("prepare_sumo_case",{"city":city})
                await call("sumo_network_info",{"city":city})
                edge=await call("sumo_network_info",{"city":city,"edge_id":quality["target_edge"]["id"]})
                check("exact original edge geometry and lanes returned",edge["edge_id"]==quality["target_edge"]["id"] and len(edge["shape_xy"])>1)
                resources=await session.list_resources(); templates=await session.list_resource_templates(); prompts=await session.list_prompts()
                check("resource and prompt discovery",len(resources.resources)==1 and len(templates.resourceTemplates)==2 and len(prompts.prompts)==1)
                for uri in ["sumo://case",f"sumo://{city}/manifest",f"sumo://{city}/quality"]:
                    check("read resource "+uri,bool((await session.read_resource(AnyUrl(uri))).contents))
                check("render municipal prompt",bool((await session.get_prompt("municipal_sumo_review",{"city":city})).messages))
                for name,args in [("prepare_sumo_case",{"city":"unknown"}),("run_sumo_scenario",{"city":city,"run_id":"../escape"}),("run_sumo_scenario",{"city":city,"run_id":prefix+"-bad","scenario":"invent"}),("read_sumo_source",{"city":city,"name":"../../secret"}),("read_sumo_artifact",{"city":city,"run_id":"any","name":"../../secret"}),("query_simulation_state",{"target":"vehicle_list"})]:
                    await call(name,args,error=True)
                inspect_id=prefix+"-inspection"
                connected=await call("control_simulation",{"action":"connect","params":{"city":city,"run_id":inspect_id}})
                await call("control_simulation",{"action":"connect","params":{"city":city,"run_id":prefix+"-double"}},error=True)
                stepped=await call("control_simulation",{"action":"step","params":{"step":cfg["begin"]+30}})
                check("absolute inspection time, not number of calls",stepped["absolute_simulation_time"]==cfg["begin"]+30)
                active=await call("query_simulation_state",{"target":"vehicle_list"})
                vehicle_ids=ast.literal_eval(active.split(": ",1)[1]);check("nonempty live vehicle query",len(vehicle_ids)>0)
                sim=ast.literal_eval((await call("query_simulation_state",{"target":"simulation"})).split(": ",1)[1])
                variables={}
                for variable in ["speed","position","acceleration","lane","route"]:
                    variables[variable]=(await call("query_simulation_state",{"target":"vehicle_variable","params":{"vehicle_id":vehicle_ids[0],"variable":variable}})).split(": ",1)[1]
                for step in [cfg["begin"]+29,cfg["begin"]+61]:
                    await call("control_simulation",{"action":"step","params":{"step":step}},error=True)
                await call("control_simulation",{"action":"disconnect"})
                analysis=await call("run_analysis",{"fcd_file":str(data.root()/"results"/city/inspect_id/"fcd.xml.gz")})
                speeds=[]
                with gzip.open(data.root()/"results"/city/inspect_id/"fcd.xml.gz","rb") as stream:
                    for _,node in ET.iterparse(stream,events=("end",)):
                        if node.tag=="vehicle": speeds.append(float(node.attrib["speed"]))
                        node.clear()
                check("original FCD sample count/mean matches independent gzip XML oracle",f"Total Data Points: {len(speeds)}" in analysis and f"Average Speed: {sum(speeds)/len(speeds):.2f} m/s" in analysis)
                # Independent direct TraCI connection, original native binary,
                # same input and seed; compare all five variables and per-step counters.
                install_traci_stderr()
                folder,spec=engine.make_run(city,prefix+"-oracle",inspection=True)
                traci.start([sumolib.checkBinary("sumo"),"-c",spec["config"]],label="oracle",stdout=__import__("subprocess").DEVNULL)
                conn=traci.getConnection("oracle")
                try:
                    conn.simulationStep(cfg["begin"]+30)
                    key=vehicle_ids[0]
                    expected_vars={"speed":str(conn.vehicle.getSpeed(key)),"position":str(conn.vehicle.getPosition(key)),"acceleration":str(conn.vehicle.getAcceleration(key)),"lane":conn.vehicle.getLaneID(key),"route":str(list(conn.vehicle.getRoute(key)))}
                    expected_sim={"time":conn.simulation.getTime(),"loaded_vehicles":conn.simulation.getLoadedNumber(),"departed_vehicles":conn.simulation.getDepartedNumber(),"arrived_vehicles":conn.simulation.getArrivedNumber(),"min_expected_vehicles":conn.simulation.getMinExpectedNumber()}
                    check("original MCP live IDs, five variables and per-step counters equal independent native TraCI",vehicle_ids==list(conn.vehicle.getIDList()) and variables==expected_vars and sim==expected_sim)
                finally: conn.close()
                if not quick:
                    mcp_runs=[]
                    for scenario in ["baseline","works30"]:
                        result=await call("run_sumo_scenario",{"city":city,"run_id":prefix+"-mcp-"+scenario,"scenario":scenario})
                        mcp_runs.append(result);evidence["runs"]["mcp-"+scenario]=result["run_id"]
                        check(scenario+": complete native/MCP summaries identical",semantic(result)==semantic(native[len(mcp_runs)-1]))
                        for name in ["all-vehicles.csv","cohort.csv"]:
                            check(scenario+": native/MCP "+name+" byte identical",data.sha(data.root()/"results"/city/result["run_id"]/name)==data.sha(data.root()/"results"/city/native[len(mcp_runs)-1]["run_id"]/name))
                    compared=await call("compare_sumo_runs",{"city":city,"baseline_id":mcp_runs[0]["run_id"],"scenario_id":mcp_runs[1]["run_id"]})
                    check("complete native/MCP comparison identical",semantic(compared)==semantic(comparison))
                    await pages("read_sumo_artifact",{"city":city,"run_id":mcp_runs[1]["run_id"],"name":"comparison.csv"},data.root()/"results"/city/mcp_runs[1]["run_id"]/"comparison.csv")
                    rendered=await call("render_sumo_map",{"city":city,"run_id":mcp_runs[1]["run_id"]})
                    check("native/MCP map bytes identical",rendered==native_map)
                    await call("read_sumo_artifact",{"city":city,"run_id":mcp_runs[1]["run_id"],"name":"map.png"})
                    await call("compare_sumo_runs",{"city":city,"baseline_id":mcp_runs[1]["run_id"],"scenario_id":mcp_runs[0]["run_id"]},error=True)
                # Intentionally leave an owned inspection open. EOF must reap it.
                await call("control_simulation",{"action":"connect","params":{"city":city,"run_id":prefix+"-cleanup"}})
    await asyncio.sleep(1)
    live=[]
    for comm in Path("/proc").glob("[0-9]*/comm"):
        try:
            if comm.read_text().strip()=="sumo" and "Z" not in (comm.parent/"stat").read_text().split()[2]: live.append(comm.parent.name)
        except OSError: pass
    check("MCP EOF reaps owned native inspection process",not live,live)
    evidence["tools_exercised"]=sorted(set(evidence["tools_exercised"]))
    check("quick protocol subset executed" if quick else "all thirteen advertised tool families executed",set(evidence["tools_exercised"])==(TOOLS-{"run_sumo_scenario","compare_sumo_runs","read_sumo_artifact","render_sumo_map"} if quick else TOOLS))
    evidence["passed"]=not evidence["failures"]
    data.dump(out/(prefix+".json"),evidence)
    data.dump(out/"latest.json",evidence)
    if evidence["failures"]: raise RuntimeError("SUMO checks failed: "+str(evidence["failures"]))
    return evidence
