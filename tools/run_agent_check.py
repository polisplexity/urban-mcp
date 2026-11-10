"""Run the public blind task using an installed host and its own authentication.

No provider credential is read, copied, printed or provisioned by this script.
Hermes requires an independently configured test profile with this MCP enabled.
"""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess

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
    parser.add_argument("--capability",choices=["inventory","walking"],default="inventory")
    parser.add_argument("--city",choices=["helsinki","amsterdam"],default="helsinki")
    args=parser.parse_args()
    if not args.label.replace("-","").replace("_","").isalnum():raise SystemExit("Use a simple alphanumeric label")
    out=ROOT/".urban-mcp/agent-evidence"/(args.host+"-"+args.label)
    out.mkdir(parents=True,exist_ok=False)
    work=out/"work";work.mkdir()
    task="cases/two-city-walking/agent-task.md" if args.capability=="walking" else "cases/helsinki-service-inventory/agent-task.md"
    prompt=(ROOT/task).read_text(encoding="utf-8").replace("{{city}}",args.city)+"\nYour host name is "+args.host+".\n"
    name=server_name(args.capability)
    env=dict(os.environ)
    if args.host=="codex":
        executable=shutil.which("codex")
        if not executable:raise SystemExit("Install/configure Codex CLI with your account first")
        cfg=server_config(ROOT/".urban-mcp"/("codex-"+args.label),args.wsl_distro,args.capability)
        cfg.update(startup_timeout_sec=60,tool_timeout_sec=300,required=True,default_tools_approval_mode="approve")
        # Approval is scoped to this case server in this explicitly requested
        # benchmark; the agent shell remains read-only and is forbidden by task.
        command=[executable,"-a","never","exec","--ephemeral","--json","--skip-git-repo-check","-s","read-only","-C",str(work),"-c","mcp_servers="+toml_inline({name:cfg}),"-c",'web_search="disabled"',"-o",str(out/"answer.md"),"-"]
        stdin=prompt
    else:
        executable=args.hermes_executable or shutil.which("hermes")
        if not executable or not args.hermes_home:raise SystemExit("Use an installed Hermes and --hermes-home pointing to an isolated configured test profile")
        env["HERMES_HOME"]=str(Path(args.hermes_home).resolve())
        command=[executable,"chat","-Q","--ignore-rules","--source","tool","-t",name,"--max-turns","45","-q",prompt]
        stdin=None
    with (out/"events.log").open("w",encoding="utf-8") as stdout,(out/"stderr.log").open("w",encoding="utf-8") as stderr:
        result=subprocess.run(command,input=stdin,encoding="utf-8",env=env,cwd=work,stdout=stdout,stderr=stderr,timeout=900)
    print(json.dumps({"host":args.host,"exit_code":result.returncode,"evidence":str(out),"note":"Exit code alone is not admission: inspect tool calls, compare numeric/table artifacts and review claims."}))
    raise SystemExit(result.returncode)


if __name__ == "__main__":
    main()
