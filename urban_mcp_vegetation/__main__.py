"""Container CLI and agent-neutral stdio MCP entry point."""
import argparse
import asyncio
import json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["status", "harvest", "prepare", "analyze", "test", "serve"])
    parser.add_argument("--city", default="helsinki")
    parser.add_argument("--mode", choices=["live", "snapshot"], default="snapshot")
    parser.add_argument("--run-id", default="native")
    parser.add_argument("--threshold", type=float, default=.2)
    args = parser.parse_args()
    from . import data, engine
    if args.command == "serve":
        from .server import mcp
        mcp.run(transport="stdio", show_banner=False)
        return
    if args.command == "test":
        from .checks import run
        result = asyncio.run(run(args.city))
    elif args.command == "status": result = data.status()
    elif args.command == "harvest": result = data.harvest(args.city, args.mode)
    elif args.command == "prepare": result = engine.prepare(args.city)
    else: result = engine.analyze(args.city, args.run_id, args.threshold)
    print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
