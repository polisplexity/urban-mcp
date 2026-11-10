"""Export only completed public-case MCP calls, never reasoning or host config."""
import argparse
import json
import hashlib
from pathlib import Path
from public_mcp_results import decode


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--events", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--server", default="urban_mcp_walking")
    parser.add_argument("--results-dir",type=Path,help="Export complete public comparison and closed-link route responses")
    args = parser.parse_args()
    calls, other_tools, comparisons, routes = [], [], [], []
    for line in args.events.read_text(encoding="utf-8").splitlines():
        try:
            event = json.loads(line)
        except ValueError:
            continue
        if event.get("type") != "item.completed":
            continue
        item = event.get("item", {})
        if item.get("type") == "mcp_tool_call":
            if item.get("server") != args.server:
                other_tools.append(item.get("server") + "/" + item.get("tool"))
                continue
            result = item.get("result")
            calls.append({"tool": item["tool"], "arguments": item.get("arguments"), "status": item.get("status"),
                          "error": item.get("error"), "response_recorded": result is not None,
                          "response_excerpt": json.dumps(result, ensure_ascii=False)[:800]})
            if args.results_dir and item.get("status")=="completed":
                target=comparisons if item["tool"]=="walking_compare" else routes if item["tool"]=="walking_route" and item.get("arguments",{}).get("closed_links") else None
                if target is not None:
                    target.append({"arguments":item.get("arguments"),"result":decode(result)})
        elif item.get("type") in {"command_execution", "web_search", "file_change"}:
            other_tools.append(item.get("type"))
    if other_tools:
        raise ValueError("Non-case tool use detected; review without exporting private content: " + str(other_tools))
    document = {"host": "Codex CLI", "calls": calls, "other_tool_use": other_tools,
                "note": "Only case MCP calls exported; no reasoning, authentication, private host configuration or system prompts."}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    if args.results_dir:
        args.results_dir.mkdir(parents=True,exist_ok=True)
        for name,values in [("comparison-results.json",comparisons),("route-results.json",routes)]:
            (args.results_dir/name).write_text(json.dumps(values,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
    print(json.dumps({"calls": len(calls), "tools": sorted({c["tool"] for c in calls})}))


if __name__ == "__main__":
    main()
