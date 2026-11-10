"""Collect reviewed public municipal artifacts; omit full tile caches and host state."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT/"cases/two-city-vegetation"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace",type=Path,required=True)
    parser.add_argument("--output",type=Path,default=CASE/"evidence")
    args = parser.parse_args()
    records = []
    for city in ["helsinki","amsterdam"]:
        origin = args.workspace/"evidence"/city
        checks = json.loads((origin/"mcp.json").read_text(encoding="utf-8"))
        if checks["failures"] or checks["checks_passed"] != len(checks["checks"]) or len(set(checks["tools_exercised"])) != 21:
            raise ValueError("Incomplete or failed case evidence")
        for field, name in [("implementation_sha256","engine.py"),("server_sha256","server.py"),("data_code_sha256","data.py"),("interface_code_sha256","interface.py")]:
            canonical = subprocess.check_output(["git","show","HEAD:urban_mcp_vegetation/"+name],cwd=ROOT)
            if hashlib.sha256(canonical).hexdigest() != checks[field]:
                raise ValueError("Executing source differs from committed canonical bytes: "+name)
        output = args.output/city
        output.mkdir(parents=True,exist_ok=True)
        for name in ["native.json","native-sensitivity.json","native-comparison.json","mcp.json","mcp-tools.json","mcp-resources.json","mcp-prompts.json"]:
            shutil.copyfile(origin/name,output/name)
        shutil.copyfile(args.workspace/"inputs"/city/"manifest.json",output/"harvest.json")
        for key,label in [("native_baseline","baseline"),("native_sensitivity","sensitivity")]:
            result = args.workspace/"results"/city/checks[key]
            shutil.copyfile(result/"zone_metrics.csv",output/(label+".csv"))
            shutil.copyfile(result/"class_counts.csv",output/(label+"-classes.csv"))
            shutil.copyfile(result/"report.md",output/(label+"-report.md"))
        shutil.copyfile(args.workspace/"results"/city/checks["native_baseline"]/"map.png",output/"map.png")
        records.append({"city":city,"native_mcp_checks":checks["checks_passed"],"tools_exercised":21,
                        **{key:checks[key] for key in ["implementation_sha256","server_sha256","data_code_sha256","interface_code_sha256","input_manifest_sha256"]},
                        "artifacts":{name:sha(output/name) for name in ["baseline.csv","sensitivity.csv","baseline-classes.csv","sensitivity-classes.csv","map.png"]}})
    shutil.copyfile(args.workspace/"evidence/upstream-audit.json",args.output/"upstream-audit.json")
    document = {"code_commit_observed":subprocess.check_output(["git","rev-parse","HEAD"],cwd=ROOT,text=True).strip(),"runtime_lock_sha256":sha(ROOT/"adapters/vegetation/runtime.lock.txt"),"snapshots":json.loads((CASE/"snapshot.lock.json").read_text(encoding="utf-8")),"cities":records,"synthetic_regressions":{"suite":"urban_mcp_vegetation.test_contracts","tests":12,"municipal_observations":False},"limits":"Native/protocol evidence for the declared two cities and operations. Independent host observations and factual reviews are separate; final-product third-city qualification remains pending."}
    (args.output/"reproduction.json").write_text(json.dumps(document,indent=2)+"\n",encoding="utf-8",newline="\n")
    print(json.dumps(records,indent=2))


if __name__ == "__main__":
    main()
