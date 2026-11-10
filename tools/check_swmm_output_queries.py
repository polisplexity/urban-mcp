"""Compare every observed host series/snapshot value to an independent EPA output."""
import argparse
import datetime as dt
import hashlib
import json
import math
from pathlib import Path

from pyswmm import Output
from swmm.toolkit.output_metadata import OutputMetadata
from swmm.toolkit.shared_enum import NodeAttribute,LinkAttribute,SubcatchAttribute,SystemAttribute

ATTRS={'node':{'depth':NodeAttribute.INVERT_DEPTH},'link':{'flow':LinkAttribute.FLOW_RATE},
    'subcatchment':{'rainfall':SubcatchAttribute.RAINFALL},'system':{'outfall_flow':SystemAttribute.OUTFALL_FLOWS}}


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def close(a,b):return type(a) in {int,float} and math.isfinite(a) and math.isclose(a,b,rel_tol=1e-5,abs_tol=1e-6)


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--trace',required=True,type=Path);p.add_argument('--native-output',required=True,type=Path);p.add_argument('--output',required=True,type=Path);a=p.parse_args()
    trace=json.loads(a.trace.read_text());checks=[]
    def check(name,value):
        checks.append({'name':name,'passed':bool(value)})
    covered=set()
    with Output(str(a.native_output)) as native:
        for i,call in enumerate(trace['calls']):
            tool=call['tool'];args=call.get('arguments',{});r=call.get('result')
            if tool not in {'output_query_series','output_query_snapshot'} or not isinstance(r,dict) or 'object_type' not in r:continue
            typ=args['object_type'];attributes=[args['attribute']] if tool.endswith('series') else args['attributes']
            ids=[args['object_id']] if tool.endswith('series') else args['object_ids']
            for obj in ids:
                for attr in attributes:
                    enum=ATTRS[typ][attr];covered.add((tool,typ))
                    values=(native.system_series(enum) if typ=='system' else getattr(native,{'node':'node_series','link':'link_series','subcatchment':'subcatch_series'}[typ])(obj,enum))
                    unit=OutputMetadata(native.handle).get_attribute_metadata(enum)[1]
                    label=f'call {i} {tool} {typ}/{obj}/{attr}'
                    if tool.endswith('series'):
                        start=dt.datetime.fromisoformat(args['start_time']) if args.get('start_time') else min(values)
                        end=dt.datetime.fromisoformat(args['end_time']) if args.get('end_time') else max(values)
                        expected={t:v for t,v in values.items() if start<=t<=end}
                        check(label+' original count',type(r['original_point_count']) is int and r['original_point_count']==len(expected))
                        check(label+' returned count',type(r['returned_point_count']) is int and r['returned_point_count']==len(r['points'])==min(len(expected),args.get('max_points',500)))
                        check(label+' every observed value',all(dt.datetime.fromisoformat(v['time']) in expected and close(v['value'],expected[dt.datetime.fromisoformat(v['time'])]) for v in r['points']))
                        times=[v['time'] for v in r['points']]
                        check(label+' ordered endpoints',times==sorted(set(times)) and times[0]==min(expected).isoformat() and times[-1]==max(expected).isoformat())
                        check(label+' unit',r['unit']==unit)
                    else:
                        target=dt.datetime.fromisoformat(args['target_time']);report=max(t for t in values if t<=target)
                        check(label+' report timestamp',r['report_time']==report.isoformat() and r['time_match']=='at_or_before')
                        check(label+' value',close(r['values'][obj][attr],values[report]))
                        check(label+' unit',r['units'][attr]==unit)
    expected={(name,typ) for name in ['output_query_series','output_query_snapshot'] for typ in ATTRS}
    check('all four object types in both query families',covered==expected)
    result={'passed':all(c['passed'] for c in checks),'checks':checks,'check_count':len(checks),'trace_sha256':sha(a.trace),
        'native_output_sha256':sha(a.native_output),'scope':'Actual host query responses versus separately compiled EPA native binary; no agent reasoning or expected-answer replay.'}
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'passed':result['passed'],'checks':len(checks),'failed':[c['name'] for c in checks if not c['passed']]}))
    raise SystemExit(0 if result['passed'] else 1)


if __name__=='__main__':main()
