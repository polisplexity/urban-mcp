"""Run the public blind task using an installed host and its own authentication.

No provider credential is copied, printed or provisioned by this script.
Only registered MCP names are retained from the host's configuration,
to disable unrelated registrations in this process without editing host config.
Hermes requires an independently configured test profile with this MCP enabled.
"""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import re
import tomllib
import hashlib
import time
from datetime import datetime, timezone

from client_config import ROOT, server_config, server_name


def toml_inline(value):
    if isinstance(value,dict):return "{"+",".join(json.dumps(k)+"="+toml_inline(v) for k,v in value.items())+"}"
    return json.dumps(value)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("host",choices=["codex","hermes"])
    parser.add_argument("--wsl-distro")
    parser.add_argument("--hermes-home",help="An isolated, already-authenticated Hermes test profile")
    parser.add_argument("--hermes-executable",help="Explicit path when Hermes is not on PATH")
    parser.add_argument("--label",default="trial",help="New label preserves earlier runs and observations")
    parser.add_argument("--capability",choices=["inventory","walking","vegetation","sumo","swmm"],default="inventory")
    parser.add_argument("--city",choices=["helsinki","amsterdam","bologna","ingolstadt","odense","utrecht"],default="helsinki")
    parser.add_argument("--task",help="Versioned public task path relative to this repository")
    parser.add_argument("--max-turns",type=int,help="Hermes turn budget; default 65 for vegetation, 45 for earlier cases")
    args=parser.parse_args()
    allowed={"sumo":{"bologna","ingolstadt"},"swmm":{"odense","utrecht"}}
    if args.city not in allowed.get(args.capability,{"helsinki","amsterdam"}):
        raise ValueError("City is not supported by the selected capability")
    if not args.label.replace("-","").replace("_","").isalnum():raise SystemExit("Use a simple alphanumeric label")
    out=ROOT/".urban-mcp/agent-evidence"/(args.host+"-"+args.label)
    out.mkdir(parents=True,exist_ok=False)
    work=out/"work";work.mkdir()
    task=args.task or {"walking":"cases/two-city-walking/agent-task.md","inventory":"cases/helsinki-service-inventory/agent-task.md","vegetation":"cases/two-city-vegetation/agent-task-v2.md","sumo":"cases/two-city-sumo/agent-task.md","swmm":"cases/two-city-swmm/agent-task-v2.md"}[args.capability]
    task_path=(ROOT/task).resolve()
    if not task_path.is_relative_to((ROOT/"cases").resolve()) or task_path.suffix!=".md":
        raise ValueError("Use a public Markdown task inside cases/")
    prompt=(ROOT/task).read_text(encoding="utf-8").replace("{{city}}",args.city)+"\nYour host name is "+args.host+".\n"
    name=server_name(args.capability)
    env=dict(os.environ)
    started_at=datetime.now(timezone.utc).isoformat()
    started=time.monotonic()
    source_commit=subprocess.check_output(["git","rev-parse","HEAD"],cwd=ROOT,text=True).strip()
    task_hash=hashlib.sha256(task_path.read_bytes()).hexdigest()
    if args.host=="codex":
        executable=shutil.which("codex")
        if not executable:raise SystemExit("Install/configure Codex CLI with your account first")
        cfg=server_config(ROOT/".urban-mcp"/("codex-"+args.label),args.wsl_distro,args.capability)
        cfg.update(startup_timeout_sec=60,tool_timeout_sec=420 if args.capability in {"sumo","swmm"} else 300,required=True,default_tools_approval_mode="approve")
        config_path=Path(os.environ.get("CODEX_HOME",str(Path.home()/".codex")))/"config.toml"
        host_config=tomllib.loads(config_path.read_text(encoding="utf-8")) if config_path.exists() else {}
        registrations=list(host_config.get("mcp_servers",{}))
        del host_config
        overrides=[]
        for registered_name in registrations:
            if registered_name!=name:
                if not re.fullmatch(r"[A-Za-z0-9_-]+",registered_name):
                    raise ValueError("A registered MCP name cannot be safely represented as a CLI configuration key")
                overrides.extend(["-c","mcp_servers."+registered_name+".enabled=false"])
        del registrations
        # Approval is scoped to this case server in this explicitly requested
        # benchmark; the agent shell remains read-only and is forbidden by task.
        command=[executable,"-a","never","exec","--ephemeral","--json","--skip-git-repo-check","-s","read-only","-C",str(work),"-c","mcp_servers="+toml_inline({name:cfg}),*overrides,"-c","features.apps=false","-c","features.plugins=false","-c",'web_search="disabled"',"-o",str(out/"answer.md"),"-"]
        stdin=prompt
    else:
        executable=args.hermes_executable or shutil.which("hermes")
        if not executable or not args.hermes_home:raise SystemExit("Use an installed Hermes and --hermes-home pointing to an isolated configured test profile")
        env["HERMES_HOME"]=str(Path(args.hermes_home).resolve())
        turns=args.max_turns or (100 if args.capability in {"sumo","swmm"} else 65 if args.capability=="vegetation" else 45)
        if not 1 <= turns <= 100:raise ValueError("max-turns must be 1..100")
        command=[executable,"chat","-Q","--ignore-rules","--source","tool","-t",name,"--max-turns",str(turns),"-q",prompt]
        stdin=None
    with (out/"events.log").open("w",encoding="utf-8") as stdout,(out/"stderr.log").open("w",encoding="utf-8") as stderr:
        result=subprocess.run(command,input=stdin,encoding="utf-8",env=env,cwd=work,stdout=stdout,stderr=stderr,timeout=1800 if args.capability in {"sumo","swmm"} else 900)
    (out/"process.json").write_text(json.dumps({"host":args.host,"city":args.city,"capability":args.capability,"exit_code":result.returncode,
        "started_at":started_at,"elapsed_seconds":round(time.monotonic()-started,3),"submitted_prompt_sha256":hashlib.sha256(prompt.encode()).hexdigest(),
        "task_path":task,"task_template_sha256":task_hash,
        "code_commit":source_commit},indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"host":args.host,"exit_code":result.returncode,"evidence":str(out),"note":"Exit code alone is not admission: inspect tool calls, compare numeric/table artifacts and review claims."}))
    raise SystemExit(result.returncode)


if __name__ == "__main__":
    main()
