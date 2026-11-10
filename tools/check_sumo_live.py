"""Optional network acquisition review through real MCP, outside routine CI."""
import asyncio
import json
import os
from pathlib import Path
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from urban_mcp_sumo import data
from urban_mcp_sumo.checks import payload


async def main():
    if (data.root()/"inputs").exists():
        raise ValueError("Use a fresh data mount; preserve previous live/snapshot observations")
    records=[]
    params=StdioServerParameters(command=sys.executable,args=["-m","urban_mcp_sumo","serve"],env=dict(os.environ))
    async with stdio_client(params) as (read,write):
        async with ClientSession(read,write) as session:
            await session.initialize()
            for city in data.recipe()["cities"]:
                result=await session.call_tool("harvest_sumo_data",{"city":city,"mode":"live"})
                if result.isError:raise RuntimeError(payload(result))
                receipt=payload(result)
                result=await session.call_tool("prepare_sumo_case",{"city":city})
                if result.isError:raise RuntimeError(payload(result))
                quality=payload(result);folder,manifest=data.verify(city)
                if receipt["input_manifest_sha256"]!=data.sha(folder/"manifest.json") or quality["input_manifest_sha256"]!=receipt["input_manifest_sha256"]:
                    raise ValueError("Source/prepare response differs from actual live data")
                records.append({"city":city,"harvest_response":receipt,"prepared_files":quality["files"],"scheduled_vehicles":quality["scheduled_vehicles"],"corridor_cohort_vehicles":quality["corridor_cohort_vehicles"],"all_asset_hashes_verified":True,"request_count":len(manifest["requests"]),"all_requests_http_200":all(r["status"]==200 for r in manifest["requests"])})
    document={"transport":"Actual MCP SDK stdio subprocess, live publisher acquisition and preparation","observations":records,"source_sha256":{name:data.sha(Path(__import__("urban_mcp_sumo").__file__).parent/name) for name in ["engine.py","server.py","data.py","compat.py"]},"scope":"No simulation or LLM is run by this optional acquisition review; final native/host experiments are separate.","passed":all(r["all_asset_hashes_verified"] and r["all_requests_http_200"] for r in records)}
    data.dump(data.root()/"evidence/live-mcp.json",document)
    print(json.dumps(document,indent=2))


if __name__=="__main__":asyncio.run(main())
