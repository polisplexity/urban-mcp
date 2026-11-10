"""The same implementations are callable natively and through MCP."""
import argparse
import json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["status", "harvest", "prepare", "inventory", "serve", "test"])
    parser.add_argument("--mode", choices=["live", "snapshot"], default="snapshot")
    parser.add_argument("--run-id", default="native")
    parser.add_argument("--service-id", type=int, action="append", default=[])
    args = parser.parse_args()
    from urban_mcp_case import sources
    if args.command == "harvest":
        result = sources.harvest_live() if args.mode == "live" else sources.harvest_snapshot()
    elif args.command == "serve":
        from urban_mcp_case.server import mcp
        mcp.run(transport="stdio", show_banner=False)
        return
    elif args.command == "test":
        from urban_mcp_case.mcp_check import main as check
        check()
        return
    else:
        from urban_mcp_case import analysis
        if args.command == "prepare":
            result = analysis.prepare()
        elif args.command == "inventory":
            result = analysis.inventory(args.service_id, args.run_id)
        else:
            result = analysis.status()
    print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
