"""Preserve original SUMO models; bind a bounded hypothetical works experiment."""
from collections import Counter
import csv
from functools import lru_cache
import gzip
import importlib.metadata
import json
import math
from pathlib import Path
import subprocess
from threading import RLock
import xml.etree.ElementTree as ET

import sumolib
from . import data

LOCK = RLock()
MAX_PAGE = 12000


def xml_open(path):
    return gzip.open(path, "rb") if str(path).endswith(".gz") else Path(path).open("rb")


def write_csv(path, rows, fields=None):
    with Path(path).open("w", encoding="utf-8", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=fields or list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def xml_write(path, node):
    ET.ElementTree(node).write(path, encoding="utf-8", xml_declaration=True)


@lru_cache(maxsize=1)
def load_network(path):
    return sumolib.net.readNet(str(path), withPrograms=True)


def prepared(city):
    base, manifest = data.verify(city)
    folder = data.root()/"prepared"/city
    quality = json.loads((folder/"quality.json").read_text(encoding="utf-8"))
    if quality["input_manifest_sha256"] != data.sha(base/"manifest.json") or quality["implementation_sha256"] != data.sha(Path(__file__)):
        raise ValueError("Prepared source/method changed; use a fresh workspace")
    for name, expected in quality["files"].items():
        if data.sha(folder/name) != expected["sha256"]:
            raise ValueError("Prepared artifact integrity failure: "+name)
    return folder, quality, manifest


def prepare(city):
    with LOCK:
        cfg = data.config(city)
        folder = data.root()/"prepared"/city
        if folder.exists():
            return prepared(city)[1]
        base, manifest = data.verify(city)
        net = load_network(base/cfg["network"])
        vehicles, definitions, ids, frequencies = [], [], set(), Counter()
        source_counts = {}
        for name in cfg["routes"]:
            count = 0
            with xml_open(base/name) as stream:
                root = None
                for event, node in ET.iterparse(stream, events=("start", "end")):
                    if root is None:
                        root = node
                    if event != "end" or node is root or node not in root:
                        continue
                    if node.tag in {"vType", "vTypeDistribution", "route", "routeDistribution"}:
                        definitions.append(ET.tostring(node, encoding="unicode"))
                    elif node.tag == "vehicle":
                        count += 1
                        depart = float(node.attrib["depart"])
                        if cfg["begin"] <= depart < cfg["depart_end"]:
                            key = node.attrib["id"]
                            route = node.find("route")
                            if key in ids or route is None or "edges" not in route.attrib:
                                raise ValueError("Duplicate vehicle or unsupported non-explicit published route")
                            edges = route.attrib["edges"].split()
                            if not edges or any(not net.hasEdge(e) for e in edges):
                                raise ValueError("Published route has an unknown network edge")
                            ids.add(key)
                            in_window = cfg["cohort_begin"] <= depart < cfg["cohort_end"]
                            if in_window:
                                frequencies.update(set(edges))
                            vehicles.append({"id": key, "depart": depart, "in_window": in_window, "edges": edges, "xml": ET.tostring(node, encoding="unicode")})
                    else:
                        raise ValueError("Unsupported published route child: "+node.tag)
                    root.remove(node)
            source_counts[name] = count
        cap = data.recipe()["speed_cap_m_s"]
        candidates = []
        for key, frequency in frequencies.items():
            edge = net.getEdge(key)
            lanes = [lane for lane in edge.getLanes() if lane.allows("passenger") and lane.getSpeed() > cap]
            if edge.getLength() >= 100 and lanes:
                candidates.append((key, frequency, lanes))
        if not candidates:
            raise ValueError("No eligible published corridor edge")
        candidates.sort(key=lambda row: (-row[1], row[0]))
        selected, frequency, lanes = candidates[0]
        vehicles.sort(key=lambda row: (row["depart"], row["id"]))
        folder.mkdir(parents=True)
        with (folder/"routes.xml").open("w", encoding="utf-8", newline="\n") as output:
            output.write('<?xml version="1.0" encoding="UTF-8"?>\n<routes>\n')
            output.write("\n".join(definitions)+"\n")
            for row in vehicles:
                output.write(row["xml"]+"\n")
            output.write("</routes>\n")
        schedule = [{"vehicle_id": r["id"], "scheduled_depart": r["depart"], "evaluation_window": r["in_window"], "corridor_cohort": r["in_window"] and selected in r["edges"], "published_route_uses_selected_edge": selected in r["edges"]} for r in vehicles]
        write_csv(folder/"schedule.csv", schedule)
        quality = {"city":city, "network":str(base/cfg["network"]), "source_vehicle_counts":source_counts, "scheduled_vehicles":len(vehicles), "evaluation_window_vehicles":sum(r["in_window"] for r in vehicles), "corridor_cohort_vehicles":frequency, "target_edge":{"id":selected,"name":net.getEdge(selected).getName(),"length_m":net.getEdge(selected).getLength(),"published_cohort_routes":frequency,"lanes":[{"id":lane.getID(),"original_speed_m_s":lane.getSpeed(),"works_speed_m_s":cap} for lane in lanes]}, "network_edges":len(net.getEdges()), "network_nodes":len(net.getNodes()), "traffic_lights":len(net.getTrafficLights()), "network_boundary_xy":net.getBoundary(), "model_date":cfg["model_date"], "time":{k:cfg[k] for k in ["begin","cohort_begin","cohort_end","depart_end","end","step_length"]}, "seed":data.recipe()["seed"], "input_manifest_sha256":data.sha(base/"manifest.json"), "implementation_sha256":data.sha(Path(__file__)), "files":{name:{"sha256":data.sha(folder/name),"bytes":(folder/name).stat().st_size} for name in ["routes.xml","schedule.csv"]}, "limits":data.recipe()["limits"]+cfg["limits"]}
        if frequency != sum(r["corridor_cohort"] for r in schedule):
            raise ValueError("Selected corridor cohort mismatch")
        data.dump(folder/"quality.json", quality)
        return quality


def read_schedule(city):
    folder, _, _ = prepared(city)
    with (folder/"schedule.csv").open(encoding="utf-8", newline="") as stream:
        return [{**r,"scheduled_depart":float(r["scheduled_depart"]),"evaluation_window":r["evaluation_window"]=="True","corridor_cohort":r["corridor_cohort"]=="True","published_route_uses_selected_edge":r["published_route_uses_selected_edge"]=="True"} for r in csv.DictReader(stream)]


def make_run(city, run_id, scenario="baseline", inspection=False):
    data.token(run_id)
    if scenario not in {"baseline", "works30"}:
        raise ValueError("scenario must be baseline or works30")
    cfg = data.config(city)
    folder, quality, _ = prepared(city)
    base = data.root()/"inputs"/city
    output = data.root()/"results"/city/run_id
    output.mkdir(parents=True, exist_ok=False)
    additional = []
    for number, name in enumerate(cfg["additional"]):
        node = ET.parse(base/name).getroot()
        for element in node.iter():
            if "file" in element.attrib:
                element.set("file", str(output/("detectors-"+str(number)+".xml")))
        target = output/("additional-"+str(number)+".xml")
        xml_write(target, node)
        additional.append(str(target))
    if scenario == "works30":
        node = ET.Element("additional")
        sign = ET.SubElement(node,"variableSpeedSign",id="urban_mcp_works30",lanes=" ".join(l["id"] for l in quality["target_edge"]["lanes"]))
        ET.SubElement(sign,"step",time=str(cfg["cohort_begin"]),speed=str(data.recipe()["speed_cap_m_s"]))
        xml_write(output/"works.add.xml", node)
        additional.append(str(output/"works.add.xml"))
    end = cfg["begin"]+60 if inspection else cfg["end"]
    node = ET.Element("configuration")
    def options(group, values):
        element = ET.SubElement(node,group)
        for key,value in values.items():
            ET.SubElement(element,key,value=str(value))
    options("input",{"net-file":quality["network"],"route-files":str(folder/"routes.xml"),"additional-files":",".join(additional)})
    options("time",{"begin":cfg["begin"],"end":end,"step-length":cfg["step_length"]})
    options("processing",cfg["processing"])
    options("random_number",{"seed":data.recipe()["seed"]})
    options("output",{"tripinfo-output":str(output/"tripinfo.xml"),"tripinfo-output.write-unfinished":"true","tripinfo-output.write-undeparted":"true","summary-output":str(output/"simulation-summary.xml"),"summary-output.period":"60","statistic-output":str(output/"statistics.xml"),"fcd-output":str(output/"fcd.xml.gz"),"device.fcd.period":"10"})
    options("report",{"no-step-log":"true","log":str(output/"sumo.log"),"error-log":str(output/"sumo-errors.log")})
    xml_write(output/"run.sumocfg",node)
    spec={"city":city,"run_id":run_id,"scenario":scenario,"inspection":inspection,"begin":cfg["begin"],"end":end,"seed":data.recipe()["seed"],"input_manifest_sha256":quality["input_manifest_sha256"],"implementation_sha256":quality["implementation_sha256"],"config":str(output/"run.sumocfg")}
    data.dump(output/"run.json",spec)
    return output,spec


def trip_rows(city, output):
    records = {}
    for _, node in ET.iterparse(output/"tripinfo.xml",events=("end",)):
        if node.tag=="tripinfo":
            if node.attrib["id"] in records:
                raise ValueError("Duplicate tripinfo vehicle")
            records[node.attrib["id"]]=dict(node.attrib)
            node.clear()
    rows=[]
    for scheduled in read_schedule(city):
        key=scheduled["vehicle_id"]
        raw=records.get(key)
        depart=float(raw["depart"]) if raw else None
        arrival=float(raw["arrival"]) if raw else None
        state="not_recorded" if raw is None else "undeparted" if depart<0 else "unfinished" if arrival<0 else "arrived"
        rows.append({**scheduled,"state":state,"depart":depart,"arrival":arrival,**{field:float(raw[field]) if raw and field in raw and state=="arrived" else None for field in ["duration","waitingTime","timeLoss","departDelay","routeLength"]},"vaporized":raw.get("vaporized","") if raw else ""})
    if set(records)-{r["vehicle_id"] for r in rows}:
        raise ValueError("SUMO output contains unscheduled vehicles")
    return rows


def summarize(city, run_id):
    data.token(run_id)
    output=data.root()/"results"/city/run_id
    spec=json.loads((output/"run.json").read_text(encoding="utf-8"))
    if spec["inspection"]:
        raise ValueError("An inspection run is not a complete municipal scenario")
    _,quality,_=prepared(city)
    rows=trip_rows(city,output)
    cohort=[r for r in rows if r["corridor_cohort"]]
    complete=[r for r in cohort if r["state"]=="arrived"]
    stats=ET.parse(output/"statistics.xml").getroot()
    native_statistics={child.tag:dict(child.attrib) for child in stats if child.tag!="performance"}
    summary={**spec,"model_date":quality["model_date"],"target_edge":quality["target_edge"],"scheduled_vehicles":len(rows),"all_scheduled_states":dict(sorted(Counter(r["state"] for r in rows).items())),"corridor_cohort_vehicles":len(cohort),"corridor_cohort_states":{k:sum(r["state"]==k for r in cohort) for k in ["arrived","unfinished","undeparted","not_recorded"]},"completed_cohort_means":{field:sum(r[field] for r in complete)/len(complete) if complete else None for field in ["duration","waitingTime","timeLoss","departDelay"]},"native_statistics":native_statistics,"limits":quality["limits"],"runtime":{name:importlib.metadata.version(name) for name in ["eclipse-sumo","sumolib","traci","mcp"]},"artifacts":["summary.json","all-vehicles.csv","cohort.csv","tripinfo.xml","statistics.xml","simulation-summary.xml","fcd.xml.gz","report.md","map.png (after render)"]}
    write_csv(output/"all-vehicles.csv",rows)
    write_csv(output/"cohort.csv",cohort,fields=list(rows[0]))
    data.dump(output/"summary.json",summary)
    (output/"report.md").write_text(f"# {data.config(city)['name']}: {spec['scenario']}\n\nHistorical published-model experiment; {len(cohort)} scheduled corridor-cohort vehicles, {len(complete)} completed by the fixed horizon. Completion-only means must retain this denominator. This is not observed current traffic, revalidated calibration, or a city ranking.\n\n"+"\n".join("- "+v for v in quality["limits"])+"\n",encoding="utf-8",newline="\n")
    return {k:v for k,v in summary.items() if k!="config"}


def run(city, run_id, scenario="baseline"):
    output,spec=make_run(city,run_id,scenario)
    command=[sumolib.checkBinary("sumo"),"-c",spec["config"]]
    try:
        result=subprocess.run(command,capture_output=True,text=True,timeout=300,cwd=output)
        (output/"stdout.log").write_text(result.stdout,encoding="utf-8")
        (output/"stderr.log").write_text(result.stderr,encoding="utf-8")
        if result.returncode:
            raise RuntimeError("Native SUMO failed: "+result.stderr[-2000:])
        return summarize(city,run_id)
    except Exception as exc:
        data.dump(output/"failure.json",{"type":type(exc).__name__,"error":str(exc)})
        raise


def compare(city, baseline_id, scenario_id):
    data.config(city)
    for key in [baseline_id,scenario_id]:data.token(key)
    folders=[data.root()/"results"/city/key for key in [baseline_id,scenario_id]]
    before,after=[json.loads((p/"summary.json").read_text(encoding="utf-8")) for p in folders]
    if before["scenario"]!="baseline" or after["scenario"]!="works30" or any(before[k]!=after[k] for k in ["city","input_manifest_sha256","implementation_sha256","seed","begin","end","target_edge"]):
        raise ValueError("Compare one baseline and works30 on identical city/input/method/seed/horizon")
    cohorts=[]
    for folder in folders:
        with (folder/"cohort.csv").open(encoding="utf-8",newline="") as stream:cohorts.append({r["vehicle_id"]:r for r in csv.DictReader(stream)})
    if set(cohorts[0])!=set(cohorts[1]):raise ValueError("Scheduled comparison cohort changed")
    rows=[]
    for key in sorted(cohorts[0]):
        a,b=[c[key] for c in cohorts]
        matched=a["state"]==b["state"]=="arrived"
        delta=float(b["duration"])-float(a["duration"]) if matched else None
        rows.append({"vehicle_id":key,"baseline_state":a["state"],"works_state":b["state"],"matched_arrived":matched,"travel_time_delta_s":delta,"increased_over_30s":delta>data.recipe()["comparison_threshold_s"] if matched else None})
    path=folders[1]/"comparison.csv"
    write_csv(path,rows,["vehicle_id","baseline_state","works_state","matched_arrived","travel_time_delta_s","increased_over_30s"])
    deltas=[r["travel_time_delta_s"] for r in rows if r["matched_arrived"]]
    result={"city":city,"baseline_id":baseline_id,"scenario_id":scenario_id,"target_edge_id":before["target_edge"]["id"],"scheduled_corridor_cohort":len(rows),"baseline_states":before["corridor_cohort_states"],"works_states":after["corridor_cohort_states"],"matched_completed_cohort":len(deltas),"excluded_from_paired_comparison":len(rows)-len(deltas),"mean_matched_travel_time_delta_s":sum(deltas)/len(deltas) if deltas else None,"increased_over_30s":sum(r["increased_over_30s"] is True for r in rows),"decreased_over_30s":sum(v < -30 for v in deltas),"comparison_artifact":"comparison.csv","comparison_sha256":data.sha(path),"limits":"Paired completed-trip differences on the same scheduled corridor cohort and fixed seed; censored trips excluded explicitly. Historical scenario, not an observed causal effect or validated current forecast."}
    data.dump(folders[1]/"comparison.json",result)
    return result


def read_artifact(city,run_id,name="summary.json",offset=0,limit=8000):
    data.config(city);data.token(run_id)
    allowed={"summary.json","cohort.csv","all-vehicles.csv","comparison.csv","comparison.json","report.md","map.png","statistics.xml","simulation-summary.xml"}
    if name not in allowed:raise ValueError("Artifact name is not allowed")
    if type(offset) is not int or type(limit) is not int or offset<0 or not 1<=limit<=MAX_PAGE:raise ValueError("Page limit must be 1..12000 and offset nonnegative")
    path=data.root()/"results"/city/run_id/name
    receipt={"name":name,"bytes":path.stat().st_size,"sha256":data.sha(path)}
    if name=="map.png":return receipt
    text=path.read_text(encoding="utf-8")
    return {**receipt,"text":text[offset:offset+limit],"characters":len(text),"next_offset":offset+limit if offset+limit<len(text) else None}


def network_info(city,edge_id=None):
    _,quality,_=prepared(city)
    if edge_id is None:return {k:quality[k] for k in ["city","network_edges","network_nodes","traffic_lights","network_boundary_xy","target_edge","scheduled_vehicles","evaluation_window_vehicles","corridor_cohort_vehicles","time","seed","model_date","limits"]}
    net=load_network(quality["network"])
    if not net.hasEdge(edge_id):raise ValueError("Unknown source edge ID")
    edge=net.getEdge(edge_id)
    return {"city":city,"edge_id":edge_id,"name":edge.getName(),"length_m":edge.getLength(),"shape_xy":edge.getShape(),"lanes":[{"id":l.getID(),"speed_m_s":l.getSpeed(),"length_m":l.getLength(),"allows_passenger":l.allows("passenger")} for l in edge.getLanes()],"planned_route_membership_is_not_observed_traversal":True}


def render(city,run_id):
    data.token(run_id)
    _,quality,_=prepared(city)
    folder=data.root()/"results"/city/run_id
    summary=json.loads((folder/"summary.json").read_text(encoding="utf-8"))
    if (folder/"map.png").exists():raise ValueError("Map exists; preserve the observed artifact")
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.collections import LineCollection
    net=load_network(quality["network"])
    fig,axes=plt.subplots(1,2,figsize=(12,6),gridspec_kw={"width_ratios":[1.4,1]})
    axes[0].add_collection(LineCollection([e.getShape() for e in net.getEdges()],colors="#8c9a9f",linewidths=.35))
    edge=net.getEdge(quality["target_edge"]["id"])
    axes[0].add_collection(LineCollection([edge.getShape()],colors="#d44d3c",linewidths=3))
    axes[0].autoscale();axes[0].set_aspect("equal");axes[0].set_xlabel("Source network x (m)");axes[0].set_ylabel("Source network y (m)")
    axes[0].set_title("Published network and selected works corridor")
    states=summary["corridor_cohort_states"]
    axes[1].barh(list(states),list(states.values()),color="#287568")
    axes[1].set_xlabel("Scheduled corridor-cohort vehicles");axes[1].set_title(summary["scenario"]+": explicit completion states")
    fig.suptitle(data.config(city)["name"]+" · historical SUMO model experiment")
    fig.text(.02,.025,data.config(city)["attribution"]+"\n"+data.config(city)["license"]+" · hypothetical works; not current traffic or independently revalidated calibration.",fontsize=7)
    fig.tight_layout(rect=(0,.10,1,.95));fig.savefig(folder/"map.png",dpi=130,metadata={"Software":"Urban MCP pinned SUMO runtime"});plt.close(fig)
    return read_artifact(city,run_id,"map.png")
