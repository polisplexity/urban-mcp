"""Publish bounded reviewed evidence; bulk output and private host state stay ignored."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

ROOT=Path(__file__).resolve().parents[1]
CASE=ROOT/"cases/two-city-sumo"


def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--city",choices=["bologna","ingolstadt"],required=True)
    p.add_argument("--workspace",type=Path,required=True);p.add_argument("--source-commit",required=True)
    a=p.parse_args();checks=json.loads((a.workspace/"evidence"/a.city/"latest.json").read_text())
    if checks["quick_protocol_only"] or not checks["passed"] or checks["failures"] or len(checks["tools_exercised"])!=13: raise ValueError("Incomplete protocol evidence")
    out=CASE/"evidence"/a.city;out.mkdir(parents=True,exist_ok=True)
    checks["runtime_source_commit"]=a.source_commit
    shutil.copyfile(a.workspace/"inputs"/a.city/"manifest.json",out/"harvest.json")
    copied={}
    for role,label in [("native-baseline","baseline"),("native-works30","works")]:
        folder=a.workspace/"results"/a.city/checks["runs"][role]
        summary=json.loads((folder/"summary.json").read_text())
        canonical=subprocess.check_output(["git","show",a.source_commit+":urban_mcp_sumo/engine.py"],cwd=ROOT)
        if hashlib.sha256(canonical).hexdigest()!=summary["implementation_sha256"]:raise ValueError("Native implementation differs from recorded source commit")
        for name in ["summary.json","cohort.csv","all-vehicles.csv","statistics.xml","simulation-summary.xml","sumo-errors.log"]:
            target=out/(label+"-"+name)
            shutil.copyfile(folder/name,target);copied[target.name]=sha(target)
        if label=="works":
            for name in ["comparison.csv","comparison.json","map.png"]:
                shutil.copyfile(folder/name,out/name);copied[name]=sha(out/name)
    # Bind every executing backend byte, not a later documentation-only HEAD.
    checks["source_sha256"]={}
    for name in ["data.py","engine.py","server.py","compat.py","checks.py","__main__.py"]:
        canonical=subprocess.check_output(["git","show",a.source_commit+":urban_mcp_sumo/"+name],cwd=ROOT)
        if (ROOT/"urban_mcp_sumo"/name).read_bytes()!=canonical: raise ValueError("Executing source has changed since test: "+name)
        checks["source_sha256"][name]=hashlib.sha256(canonical).hexdigest()
    checks["artifact_sha256"]=copied
    (out/"native-mcp.json").write_text(json.dumps(checks,indent=2)+"\n",encoding="utf-8",newline="\n")
    print(json.dumps({"city":a.city,"checks":len(checks["checks"]),"passed":checks["passed"],"artifacts":len(copied)}))


if __name__=="__main__": main()
