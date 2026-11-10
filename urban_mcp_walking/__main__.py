"""Container commands; the MCP transport remains agent independent."""
import argparse
import json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["status", "harvest", "analyze", "test", "serve"])
    parser.add_argument("--city", choices=["helsinki", "amsterdam"], default="helsinki")
    parser.add_argument("--mode", choices=["live", "snapshot"], default="snapshot")
    parser.add_argument("--resume", action="store_true", help="Resume an inspected failed live harvest using its cache and append-only HTTP receipts")
    parser.add_argument("--feature-query", choices=["bbox", "polygon"], default="bbox")
    parser.add_argument("--feature-endpoint", choices=["primary", "private-coffee"], default="primary")
    args = parser.parse_args()
    from . import data
    if args.command == "status":
        result = data.status()
    elif args.command == "harvest":
        result = data.harvest(args.city, args.mode, args.resume, args.feature_query, args.feature_endpoint)
    elif args.command == "analyze":
        from .engine import analyze
        result = analyze(args.city, "native")
    elif args.command == "test":
        import asyncio
        from .checks import run
        result = asyncio.run(run(args.city))
    else:
        from .server import mcp
        mcp.run(transport="stdio", show_banner=False)
        return
    print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))


if __name__ == "__main__":
    main()
