"""Export only public-case tool calls from an isolated Hermes test database.

Never export system prompts, model configuration, credentials or reasoning.
The selected session must contain the exact public test task.
"""
import argparse
import json
from pathlib import Path
import sqlite3
import re
from public_mcp_results import decode


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state-db",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--task",default="cases/helsinki-service-inventory/agent-task.md")
    parser.add_argument("--city",choices=["helsinki","amsterdam"],default="helsinki")
    parser.add_argument("--answer-output",type=Path)
    parser.add_argument("--results-dir",type=Path,help="Export complete selected public walking tool responses")
    parser.add_argument("--allow-incomplete-results",action="store_true",help="Preserve failed/truncated historical diagnostic exports explicitly; never admits them as complete results")
    args=parser.parse_args()
    task=(Path(__file__).resolve().parents[1]/args.task).read_text(encoding="utf-8").replace("{{city}}",args.city).strip()
    connection=sqlite3.connect(args.state_db.resolve().as_uri()+"?mode=ro",uri=True)
    connection.row_factory=sqlite3.Row
    selected=None
    for session in connection.execute("select id,model,started_at,ended_at from sessions order by started_at desc"):
        users=connection.execute("select content from messages where session_id=? and role='user'",(session["id"],)).fetchall()
        if any(task in (row["content"] or "") for row in users):
            selected=session;break
    if selected is None:raise SystemExit("No session matches the public case task; nothing exported")
    calls=[];by_id={};comparisons=[];routes=[];analyses=[];artifacts=[]
    for message in connection.execute("select role,tool_name,tool_call_id,tool_calls,content from messages where session_id=? order by id",(selected["id"],)):
        if message["tool_calls"]:
            for raw in json.loads(message["tool_calls"]):
                fn=raw.get("function",{})
                arguments=fn.get("arguments",{})
                call={"tool":fn.get("name"),"arguments":json.loads(arguments) if isinstance(arguments,str) else arguments}
                calls.append(call);by_id[raw.get("id")]=call
        if message["role"]=="tool":
            call=by_id.get(message["tool_call_id"])
            if call is not None:
                content=message["content"] or ""
                call["response_excerpt"]=content[:800]
                call["response_recorded"]=True
                if args.results_dir:
                    target=comparisons if call["tool"] in {"mcp__urban_mcp_walking__walking_compare","mcp__urban_mcp_vegetation__vegetation_compare"} else analyses if call["tool"]=="mcp__urban_mcp_vegetation__analyze_vegetation" and call["arguments"].get("run_id") in {"agent-baseline","agent-sensitivity"} else artifacts if call["tool"] in {"mcp__urban_mcp_vegetation__read_vegetation_artifact","mcp__urban_mcp_vegetation__render_vegetation_map"} else routes if call["tool"]=="mcp__urban_mcp_walking__walking_route" and call["arguments"].get("closed_links") else None
                    if target is not None:
                        if re.search(r'\{\s*"error"\s*:',content):
                            continue
                        try:
                            target.append({"arguments":call["arguments"],"result":decode(content)})
                        except ValueError as exc:
                            if not args.allow_incomplete_results:raise
                            target.append({"arguments":call["arguments"],"result":None,"payload_export_error":str(exc),"observed_public_excerpt":content[:2000],"admitted_as_complete":False})
    document={"host":"Hermes","model":selected["model"],"started_at":selected["started_at"],"ended_at":selected["ended_at"],"calls":calls,"note":"A null ended_at is retained as recorded by the host; process exit and artifacts are checked separately. No private configuration or reasoning exported."}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(document,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    if args.answer_output:
        final=connection.execute("select content from messages where session_id=? and role='assistant' and (tool_calls is null or tool_calls='' or tool_calls='[]') order by id desc limit 1",(selected["id"],)).fetchone()
        if final is None:raise ValueError("No final assistant answer recorded")
        args.answer_output.parent.mkdir(parents=True,exist_ok=True)
        args.answer_output.write_text(final["content"]+"\n",encoding="utf-8")
    if args.results_dir:
        args.results_dir.mkdir(parents=True,exist_ok=True)
        for name,values in [("comparison-results.json",comparisons),("route-results.json",routes),("analysis-results.json",analyses),("artifact-results.json",artifacts)]:
            (args.results_dir/name).write_text(json.dumps(values,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
    print(json.dumps({"host":"Hermes","model":selected["model"],"calls":len(calls),"tools":sorted(set(str(c["tool"]) for c in calls))}))


if __name__=="__main__":main()
