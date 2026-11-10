"""Export complete public SUMO tool observations, never host reasoning or secrets."""
import argparse
import json
from pathlib import Path
import sqlite3

ROOT=Path(__file__).resolve().parents[1]


def decode(value):
    if isinstance(value,str):
        # A host may wrap a complete JSON response in an untrusted-result tag.
        start=value.find("{")
        if start>=0:
            try: return decode(json.JSONDecoder().raw_decode(value[start:])[0])
            except ValueError: pass
        return value
    if not isinstance(value,dict): return value
    for key in ["structuredContent","structured_content"]:
        if value.get(key) is not None: return decode(value[key])
    if set(value)=={"result"}: return decode(value["result"])
    if "content" in value:
        text=[b["text"] for b in value["content"] if b.get("type")=="text"]
        if len(text)==1: return decode(text[0])
    return value


def export_codex(events):
    calls=[]
    for line in events.read_text(encoding="utf-8").splitlines():
        try: event=json.loads(line)
        except ValueError: continue
        if event.get("type")!="item.completed": continue
        item=event.get("item",{})
        if item.get("type")=="mcp_tool_call":
            if item.get("server")!="urban_mcp_sumo": raise ValueError("Non-case MCP use; no private content exported")
            calls.append({"tool":item["tool"],"arguments":item.get("arguments",{}),"status":item.get("status"),"error":item.get("error"),"result":decode(item.get("result"))})
        elif item.get("type") in {"command_execution","web_search","file_change"}:
            raise ValueError("Non-case tool use; review without exporting private content")
    return {"host":"Codex CLI","calls":calls,"other_tool_use":[]},None


def export_hermes(db,city):
    task=(ROOT/"cases/two-city-sumo/agent-task.md").read_text().replace("{{city}}",city).strip()
    conn=sqlite3.connect(db.resolve().as_uri()+"?mode=ro",uri=True);conn.row_factory=sqlite3.Row
    selected=None
    for session in conn.execute("select id,model,started_at,ended_at from sessions order by started_at desc"):
        users=conn.execute("select content from messages where session_id=? and role='user'",(session["id"],))
        if any(task in (r["content"] or "") for r in users): selected=session;break
    if selected is None: raise ValueError("No exact public task match; nothing exported")
    calls=[]; by_id={}
    for msg in conn.execute("select role,tool_call_id,tool_calls,content from messages where session_id=? order by id",(selected["id"],)):
        if msg["tool_calls"]:
            for raw in json.loads(msg["tool_calls"]):
                fn=raw.get("function",{}); name=fn.get("name","")
                if not name.startswith("mcp__urban_mcp_sumo__"): raise ValueError("Non-case tool use; no private content exported")
                args=fn.get("arguments",{})
                call={"tool":name.removeprefix("mcp__urban_mcp_sumo__"),"arguments":json.loads(args) if isinstance(args,str) else args,"status":"no_response","result":None}
                calls.append(call);by_id[raw.get("id")]=call
        if msg["role"]=="tool" and msg["tool_call_id"] in by_id:
            call=by_id[msg["tool_call_id"]]; body=msg["content"] or ""
            value=decode(body)
            call.update(result=value,status="failed" if isinstance(value,dict) and "error" in value else "completed")
    final=conn.execute("select content from messages where session_id=? and role='assistant' and (tool_calls is null or tool_calls='' or tool_calls='[]') order by id desc limit 1",(selected["id"],)).fetchone()
    return {"host":"Hermes","model":selected["model"],"started_at":selected["started_at"],"ended_at":selected["ended_at"],"calls":calls,"other_tool_use":[]},final["content"] if final else None


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("host",choices=["codex","hermes"]);p.add_argument("--events",type=Path);p.add_argument("--state-db",type=Path)
    p.add_argument("--city",choices=["bologna","ingolstadt"],required=True);p.add_argument("--output",type=Path,required=True);p.add_argument("--answer-output",type=Path)
    a=p.parse_args()
    document,answer=export_codex(a.events) if a.host=="codex" else export_hermes(a.state_db,a.city)
    document.update(city=a.city,note="Complete public SUMO tool payloads only. Expected validation failures are retained. No reasoning, private configuration, credentials or system prompts exported. A null host ended_at is preserved; process exit is reviewed separately.")
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(document,ensure_ascii=False,indent=2,allow_nan=False)+"\n",encoding="utf-8",newline="\n")
    if a.answer_output:
        if answer is None: raise ValueError("No final assistant answer recorded")
        a.answer_output.write_text(answer+"\n",encoding="utf-8",newline="\n")
    print(json.dumps({"host":a.host,"city":a.city,"calls":len(document["calls"]),"tools":sorted({c["tool"] for c in document["calls"]})}))


if __name__=="__main__": main()
