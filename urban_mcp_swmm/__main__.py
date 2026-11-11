import argparse
import asyncio
import json


def main():
    p=argparse.ArgumentParser()
    p.add_argument('command',choices=['status','harvest','prepare','run','test','serve'])
    p.add_argument('--city',choices=['odense','utrecht'],default='odense')
    p.add_argument('--mode',choices=['snapshot','live'],default='snapshot')
    p.add_argument('--scenario',choices=['baseline','capacity75'],default='baseline')
    p.add_argument('--run-id',default='native-baseline')
    a=p.parse_args()
    from . import data,engine
    if a.command=='serve':
        from .server import main as serve
        serve();return
    if a.command=='test':
        from .checks import run
        result=asyncio.run(run(a.city))
    elif a.command=='status':result=data.status()
    elif a.command=='harvest':result=data.harvest(a.city,a.mode)
    elif a.command=='prepare':result=engine.prepare(a.city)
    else:result=engine.run_native(a.city,a.run_id,a.scenario)
    print(json.dumps(result,indent=2,allow_nan=False))


if __name__=='__main__':main()
