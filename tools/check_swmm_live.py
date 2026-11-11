"""Harvest original publishers through actual MCP in a fresh data mount."""
import asyncio
import datetime as dt
import json
import os
from pathlib import Path
import sys
from mcp import ClientSession,StdioServerParameters
from mcp.client.stdio import stdio_client
from urban_mcp_swmm import data
from urban_mcp_swmm.checks import decode


async def main():
    results={}
    parameters=StdioServerParameters(command=sys.executable,args=['-m','urban_mcp_swmm','serve'],env=dict(os.environ))
    async with stdio_client(parameters) as streams:
        async with ClientSession(*streams) as session:
            await session.initialize()
            for city in ['odense','utrecht']:
                calls=[]
                for name,args in [('harvest_swmm_data',{'city':city,'mode':'live'}),('prepare_swmm_case',{'city':city})]:
                    r=await session.call_tool(name,args,read_timeout_seconds=300)
                    if r.is_error:raise RuntimeError(str(r.content))
                    calls.append({'tool':name,'arguments':args,'result':decode(r)})
                folder,manifest=data.verify(city);model=data.root()/'models'/city
                results[city]={'calls':calls,'manifest':manifest,'requests':json.loads((folder/'requests.json').read_text()),
                    'prepared_sha256':{name:data.sha(model/name) for name in ['baseline.inp','capacity75.inp','inspection.inp']}}
    out=data.root()/'evidence/live-mcp.json'
    data.dump(out,{'passed':True,'retrieved_at':dt.datetime.now(dt.timezone.utc).isoformat(),'cities':results,
        'scope':'Actual live publisher acquisition and preparation via MCP. Different raw DMI envelope/metadata request timestamps do not imply different observations or simulations. No LLM or new field validation is claimed.'})
    print(json.dumps({'passed':True,'cities':list(results),'output':str(out)}))


if __name__=='__main__':asyncio.run(main())
