"""Verify supplementary observed live fields through direct original PySWMM."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import tempfile

from pyswmm import Simulation,Subcatchments


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--city',required=True);p.add_argument('--trace',required=True,type=Path);p.add_argument('--answer',required=True,type=Path);p.add_argument('--input',required=True,type=Path);p.add_argument('--output',required=True,type=Path);a=p.parse_args()
    trace=json.loads(a.trace.read_text());calls=trace['calls']
    inspect=next(c['result'] for c in calls if c['tool']=='inspect_swmm_case');identifier=inspect['inspection_ids']['subcatchment']
    def observed(tool):
        matches=[c for c in calls if c['tool']==tool and isinstance(c.get('result'),dict) and 'observation' in c['result']]
        assert len(matches)==1
        c=matches[0];assert c['arguments']['observe']=={'subcatchments':[{'id':identifier,'fields':['rainfall','runoff']}]}
        return c['result']['observation']
    initial=observed('simulation_observe');after=observed('simulation_step')
    with tempfile.TemporaryDirectory() as directory:
        inp=Path(directory)/'model.inp';shutil.copyfile(a.input,inp)
        with Simulation(str(inp)) as sim:
            sim.start();sub=Subcatchments(sim)[identifier]
            native_initial={'rainfall':sub.rainfall,'runoff':sub.runoff,'current_time':sim.current_time.isoformat()}
            sim.step_advance(30);next(iter(sim))
            native_after={'rainfall':sub.rainfall,'runoff':sub.runoff,'current_time':sim.current_time.isoformat()}
    checks=[]
    for label,obs,native in [('initial',initial,native_initial),('after_step',after,native_after)]:
        checks.append({'name':label+' native clock','passed':obs['current_time']==native['current_time']})
        for field in ['rainfall','runoff']:checks.append({'name':label+' '+field,'passed':obs['subcatchments'][identifier][field]==native[field]})
    closed=any(c['tool']=='simulation_close' and isinstance(c.get('result'),dict) and c['result'].get('state')=='CLOSED' for c in calls)
    checks.append({'name':'session closed','passed':closed})
    answer=a.answer.read_text();blocks=re.findall(r'```json\s*(\{.*?\})\s*```',answer,re.S);claims=json.loads(blocks[0]) if len(blocks)==1 else {}
    expected={'city':a.city,'subcatchment_id':identifier,'initial_rainfall':native_initial['rainfall'],'initial_runoff':native_initial['runoff'],
        'after_step_rainfall':native_after['rainfall'],'after_step_runoff':native_after['runoff'],'session_closed':True,'forecast_admitted':False}
    checks.append({'name':'actual answer JSON','passed':claims==expected})
    read_open=any(c['tool']=='read_swmm_resource' and isinstance(c.get('result'),dict) and '/sessions/' in c['arguments'].get('uri','') for c in calls)
    result={'city':a.city,'passed':all(c['passed'] for c in checks),'checks':checks,'trace_sha256':sha(a.trace),'answer_sha256':sha(a.answer),'input_sha256':sha(a.input),
        'native_initial':native_initial,'native_after_step':native_after,'subcatchment_id':identifier,'open_resource_read_in_this_supplement':read_open,
        'scope':'Live rainfall/runoff observations at initialization and 30 s versus direct original PySWMM, not a new municipal forecast or a replacement for full-task observations.'}
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'city':a.city,'passed':result['passed'],'checks':len(checks),'open_resource_read_in_this_supplement':read_open}))
    raise SystemExit(0 if result['passed'] else 1)


if __name__=='__main__':main()
