"""Export only completed public-case MCP calls, never reasoning or host config."""
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--events", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--server", default="urban_mcp_walking")
    args = parser.parse_args()
    calls, other_tools = [], []
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
        elif item.get("type") in {"command_execution", "web_search", "file_change"}:
            other_tools.append(item.get("type"))
    if other_tools:
        raise ValueError("Non-case tool use detected; review without exporting private content: " + str(other_tools))
    document = {"host": "Codex CLI", "calls": calls, "other_tool_use": other_tools,
                "note": "Only case MCP calls exported; no reasoning, authentication, private host configuration or system prompts."}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(document, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"calls": len(calls), "tools": sorted({c["tool"] for c in calls})}))


if __name__ == "__main__":
    main()
