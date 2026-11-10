"""Execute isolated original-method probes; these are not municipal simulations."""
import argparse
import ast
import datetime
import hashlib
import json
import logging
from pathlib import Path
from types import SimpleNamespace
import tempfile
from typing import Any, Dict, List, Optional
from unittest.mock import patch
from urllib.request import urlopen
import xml.etree.ElementTree as ET


def method(text, cls, name, namespace):
    tree=ast.parse(text)
    node=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name==cls)
    fn=next(n for n in node.body if isinstance(n,ast.FunctionDef) and n.name==name)
    fn.decorator_list=[]
    exec(compile(ast.Module(body=[fn],type_ignores=[]),"<original-method-probe>","exec"),namespace)
    return namespace[name]


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--output",type=Path,required=True);a=p.parse_args()
    records=[];checks=[]
    def fetch(repo,commit,path):
        url=f"https://raw.githubusercontent.com/{repo}/{commit}/{path}"
        with urlopen(url,timeout=60) as response: raw=response.read()
        records.append({"repository":repo,"commit":commit,"path":path,"url":url,"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest()})
        return raw.decode()
    def check(name,condition,observed):
        checks.append({"name":name,"passed":bool(condition),"observed":observed})
        if not condition:raise AssertionError(name)
    # Execute installed, unmodified XRDS functions with synthetic native stubs.
    from mcp_tools import simulation,vehicle
    from utils.connection import connection_manager
    command=[]
    with tempfile.TemporaryDirectory() as tmp:
        cfg=Path(tmp)/"seeded.sumocfg";cfg.write_text('<configuration><random_number><seed value="37"/></random_number></configuration>')
        with patch.object(simulation,"find_sumo_binary",return_value="sumo"),patch.object(simulation,"run_with_adaptive_timeout",side_effect=lambda fn,**kw:fn()),patch.object(simulation.traci,"start",side_effect=lambda cmd,**kw:command.extend(cmd)),patch.object(simulation.traci,"simulationStep"),patch.object(simulation.traci.vehicle,"getIDCount",return_value=0),patch.object(simulation.traci,"close"):
            simulation.run_simple_simulation(str(cfg),steps=1)
        check("original simple execution adds --random despite explicit seed", "--random" in command,{"command_without_private_path":["<synthetic-config>" if s==str(cfg) else s for s in command]})
        connection_manager._connected=True
        with patch.object(simulation.traci,"start") as native:
            value=connection_manager.connect("different.sumocfg")
        check("original already-connected call does not open requested model",value is None and not native.called,{"new_native_start_calls":native.call_count})
        connection_manager._connected=False
        check("original disconnected vehicle list is empty rather than a diagnostic",vehicle.get_vehicles()==[],{"value":vehicle.get_vehicles()})
        original=Path('/opt/sumo-mcp/src/mcp_tools/simulation.py').read_bytes()
        records.append({"repository":"XRDS76354/SUMO-MCP-Server","commit":"6b62a25c1b13751d636309a03e4388594fcd7620","path":"src/mcp_tools/simulation.py","sha256":hashlib.sha256(original).hexdigest(),"installed_from":"checksum-pinned complete original archive"})
        commit="2ad1d91a02f442218d54f2b1aec25c3b813ed5df"
        source=fetch("mw-jeong/AgentSUMO",commit,"agentsumo_mcp/baseline/simulation_runner.py")
        fetch("mw-jeong/AgentSUMO",commit,"LICENSE")
        copied=[]
        namespace={"Path":Path,"Optional":Optional,"List":List,"Dict":Dict,"Any":Any,"datetime":datetime,"logger":logging.getLogger(__name__),"get_working_directory":lambda:Path(tmp),"get_output_path":lambda _:Path(tmp),"ensure_vehicle_types_default":lambda _:None,"copy_additional_files":lambda files,*args:copied.append(list(files)) or list(files),"Element":ET.Element,"SubElement":ET.SubElement,"ElementTree":ET.ElementTree}
        run=method(source,"SimulationRunner","run",namespace)
        stub=SimpleNamespace(_generate_output_filenames=lambda *a:{},_copy_input_files=lambda *a:{},_has_rerouter=lambda *a:False,_validate_additional_files=lambda *a:[],_generate_additional_file=lambda *a:"synthetic.add.xml",_generate_config_file=lambda *a:"synthetic.sumocfg",_run_simulation_traci=lambda *a,**kw:{},_prepare_result=lambda *a:{"status":"synthetic-stub"})
        for policy in ["baseline","works"]:
            result=run(stub,net_file="/synthetic/city.net.xml",additional_files=["required-WAUT.add.xml"],policy_type=policy)
            if result.get("status")!="synthetic-stub":raise ValueError(result)
        check("original AgentSUMO baseline drops supplied additional files",copied==[[],["required-WAUT.add.xml"]],{"baseline":copied[0],"other_policy":copied[1],"backend":"stubbed; not the full server"})
        make=method(source,"SimulationRunner","_generate_config_file",namespace)
        generated=make(stub,Path(tmp),{"net_file":"city.net.xml","route_file":"routes.xml","trip_file":None},["required-WAUT.add.xml"],"output.add.xml",{"tripinfo":"trip.xml","summary":"summary.xml"},27000,"probe")
        check("original generated AgentSUMO config always begins at zero",ET.parse(generated).find("time/begin").attrib["value"]=="0",{"begin":0,"required_original_ingolstadt_begin":24300})
        # Static statement, deliberately separate from executed method probes.
        rerouting='"--device.rerouting.probability", "1.0"' in source
        check("original AgentSUMO source contains forced rerouting probability",rerouting,{"source_level_only":True,"probability":1.0})
        legacy=fetch("shikharvashistha/sumo-mcp","619abcbcc91cb2ddbfbdc09d25dc7819f4e2551e","server.py")
        fake=SimpleNamespace(vehicle=SimpleNamespace(getRouteID=lambda _:"route-identifier"))
        fn=method(legacy,"SUMOConnection","get_vehicle_route_edges",{"List":List,"traci":fake,"logger":logging.getLogger(__name__)})
        result=fn(SimpleNamespace(),"synthetic-vehicle")
        check("legacy original route-edges method returns route identifier string",result=="route-identifier",{"returned_type":type(result).__name__,"value":result})
    document={"probe_scope":"Synthetic isolated original methods with explicit stubs; not full AgentSUMO/legacy MCP execution, field validation or municipal observations.","original_methods_unmodified":True,"sources":records,"checks":checks,"passed":all(c["passed"] for c in checks)}
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(document,indent=2)+"\n")
    print(json.dumps({"checks":len(checks),"passed":document["passed"]}))


if __name__=="__main__":main()
