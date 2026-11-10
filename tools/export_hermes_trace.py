"""Export only public-case tool calls from an isolated Hermes test database.

Never export system prompts, model configuration, credentials or reasoning.
The selected session must contain the exact public test task.
"""
import argparse
import json
from pathlib import Path
import sqlite3


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state-db",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--task",default="cases/helsinki-service-inventory/agent-task.md")
    parser.add_argument("--city",choices=["helsinki","amsterdam"],default="helsinki")
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
    calls=[];by_id={}
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
    document={"host":"Hermes","model":selected["model"],"started_at":selected["started_at"],"ended_at":selected["ended_at"],"calls":calls,"note":"A null ended_at is retained as recorded by the host; process exit and artifacts are checked separately. No private configuration or reasoning exported."}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(document,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"host":"Hermes","model":selected["model"],"calls":len(calls),"tools":sorted(set(str(c["tool"]) for c in calls))}))


if __name__=="__main__":main()
