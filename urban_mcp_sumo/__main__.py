"""Native CLI and agent-neutral stdio profile entry point."""
import argparse
import asyncio
import json


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("command",choices=["status","harvest","prepare","run","test","serve"])
    parser.add_argument("--city",default="bologna")
    parser.add_argument("--mode",choices=["snapshot","live"],default="snapshot")
    parser.add_argument("--run-id",default="native-baseline")
    parser.add_argument("--scenario",choices=["baseline","works30"],default="baseline")
    args=parser.parse_args()
    from . import data,engine
    if args.command=="serve":
        import anyio
        from .server import serve
        anyio.run(serve)
        return
    if args.command=="test":
        from .checks import run
        result=asyncio.run(run(args.city))
    elif args.command=="status":result=data.status()
    elif args.command=="harvest":result=data.harvest(args.city,args.mode)
    elif args.command=="prepare":result=engine.prepare(args.city)
    else:result=engine.run(args.city,args.run_id,args.scenario)
    print(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False))


if __name__=="__main__":main()
