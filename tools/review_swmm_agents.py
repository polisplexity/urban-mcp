"""Review complete observed host payloads against committed native evidence."""
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
import re
import subprocess

ROOT=Path(__file__).resolve().parents[1];CASE=ROOT/'cases/two-city-swmm'
TOOLS={'model_inspect','model_list_objects','simulation_run','output_inspect','simulation_create','simulation_start','simulation_observe',
    'simulation_step','simulation_stop','simulation_save_hotstart','simulation_close','output_query_series','output_query_snapshot','run_summary',
    'simulation_run_start','simulation_task_status','simulation_task_cancel','run_cleanup','swmm_status','harvest_swmm_data','read_swmm_source',
    'prepare_swmm_case','inspect_swmm_case','run_swmm_scenario','compare_swmm_runs','read_swmm_artifact','read_swmm_resource'}


def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def exact(actual,expected):
    if type(expected) is float:return type(actual) in {int,float} and math.isfinite(actual) and math.isclose(actual,expected,rel_tol=0,abs_tol=1e-6)
    if type(actual) is not type(expected):return False
    if isinstance(expected,dict):return set(actual)==set(expected) and all(exact(actual[k],v) for k,v in expected.items())
    if isinstance(expected,list):return len(actual)==len(expected) and all(exact(a,b) for a,b in zip(actual,expected))
    return actual==expected
def success(call):
    r=call.get('result')
    if call.get('status')!='completed' or r is None:return False
    if isinstance(r,dict):return not (r.get('isError') or r.get('is_error') or ('error' in r and 'state' not in r))
    return not isinstance(r,str) or not r.startswith(('Error','Tool execution failed'))


def pages(calls,tool,args,path):
    text=path.read_bytes().decode('utf-8-sig');offsets={};raw=sha(path)
    for call in calls:
        if call['tool']!=tool or not success(call) or not all(call['arguments'].get(k)==v for k,v in args.items()):continue
        a=call['arguments'];r=call['result'];off=a.get('offset',0);limit=a.get('limit',8000)
        nxt=off+limit if off+limit<len(text) else None
        expected={'name':path.name,'bytes':path.stat().st_size,'sha256':raw,'offset':off,'next_offset':nxt,'characters':len(text),'text':text[off:off+limit]}
        if r!=expected:raise ValueError('Observed page differs from actual bytes: '+str(args)+' at '+str(off))
        offsets[off]={'offset':off,'next_offset':nxt,'characters':len(r['text']),'text_sha256':hashlib.sha256(r['text'].encode()).hexdigest()}
    off=0;chain=[]
    while True:
        if off not in offsets:raise ValueError('Missing complete observed page '+str(args)+' at '+str(off))
        chain.append(offsets[off]);off=offsets[off]['next_offset']
        if off is None:break
    return {'tool':tool,'arguments':args,'file_sha256':raw,'pages':chain,'all_pages_match':True}


def expected_claims(city):
    out=CASE/'evidence'/city;a=load(out/'baseline-summary.json');b=load(out/'capacity75-summary.json');c=load(out/'comparison.json')
    crossed=sorted(r['node_id'] for r in csv.DictReader((out/'comparison.csv').open()) if r['newly_at_or_above_10m3']=='True')
    return {'city':city,'target_conduit_id':c['target']['conduit_id'],'event_day':a['quality']['event']['wet_day'],
        'event_day_mm':a['quality']['event']['event_day_mm'],'forcing_total_mm':a['quality']['event']['forcing_total_mm'],
        'source_nodes':a['nodes'],'baseline_listed_flooding_nodes':a['listed_flooding_nodes'],'scenario_listed_flooding_nodes':b['listed_flooding_nodes'],
        'baseline_nodes_at_or_above_10m3':c['baseline_nodes_at_or_above_10m3'],'scenario_nodes_at_or_above_10m3':c['scenario_nodes_at_or_above_10m3'],
        'newly_at_or_above_10m3':c['newly_at_or_above_10m3'],'newly_crossing_node_ids':crossed,
        'baseline_sum_reported_node_flood_volume_m3':a['sum_reported_node_flood_volume_m3'],'scenario_sum_reported_node_flood_volume_m3':b['sum_reported_node_flood_volume_m3'],
        'delta_sum_reported_node_flood_volume_m3':c['delta_sum_reported_node_flood_volume_m3'],
        'baseline_system_flooding_loss_m3':a['system_flooding_loss_m3'],'scenario_system_flooding_loss_m3':b['system_flooding_loss_m3'],
        'routing_continuity_error_percent':[a['routing_continuity_error_percent'],b['routing_continuity_error_percent']],
        'runoff_continuity_error_percent':[a['runoff_continuity_error_percent'],b['runoff_continuity_error_percent']],
        'warning_counts':[len(a['warnings']),len(b['warnings'])],'comparison_sha256':sha(out/'comparison.csv'),
        'controls_physically_actuated':False,'calibration_revalidated':False,'forecast_admitted':False,'product_qualified':False}


def review(host,city,workspace,observations):
    out=CASE/'evidence'/city;trace=load(observations/'trace.json');process=load(observations/'process.json');answer=(observations/'answer.md').read_text(encoding='utf-8')
    calls=trace['calls'];passed=[c for c in calls if success(c)];checks=[];page_receipts=[]
    def check(name,value):checks.append({'name':name,'passed':bool(value)})
    check('host process exited zero',process['exit_code']==0)
    task=ROOT/process['task_path'];check('exact public task at launch',sha(task)==process['task_template_sha256'])
    prompt=task.read_text(encoding='utf-8').replace('{{city}}',city)+'\nYour host name is '+host+'.\n'
    check('submitted task and host identity',hashlib.sha256(prompt.encode()).hexdigest()==process['submitted_prompt_sha256'])
    discovery={'list_resources','list_mcp_resources','list_mcp_resource_templates'}
    check('no unrelated tools',not trace.get('other_tool_use') and {c['tool'] for c in calls}<=TOOLS|discovery)
    successful={c['tool'] for c in passed}
    check('all 27 tool families succeeded',TOOLS<=successful)
    native=load(out/'native-mcp.json')
    for name in ['data.py','engine.py','server.py','checks.py']:
        blob=subprocess.check_output(['git','show',process['code_commit']+':urban_mcp_swmm/'+name],cwd=ROOT)
        check('frozen host/native source '+name,hashlib.sha256(blob).hexdigest()==native['source_sha256'][name])
    byscenario={}
    for scenario in ['baseline','capacity75']:
        observed=[c['result'] for c in passed if c['tool']=='run_swmm_scenario' and c['arguments'].get('city')==city and c['arguments'].get('scenario')==scenario]
        check('one completed municipal '+scenario,len(observed)==1)
        if len(observed)!=1:continue
        r=observed[0];byscenario[scenario]=r;expected=load(out/(scenario+'-summary.json'));folder=workspace/'municipal'/r['run_id']
        for key in ['city','scenario','nodes','listed_flooding_nodes','nodes_at_or_above_10m3','sum_reported_node_flood_volume_m3','system_flooding_loss_m3','routing_continuity_error_percent','runoff_continuity_error_percent','report_precipitation_mm','warnings','forecast_admitted']:
            check('actual '+scenario+' '+key,exact(r.get(key),expected[key]))
        for name in ['nodes.csv','outfalls.csv']:check('complete '+scenario+' '+name,sha(folder/name)==sha(out/(scenario+'-'+name)))
        check('original source quality binding '+scenario,load(folder/'summary.json')['quality']==expected['quality'])
        original=r['original_result']
        check('original native metadata '+scenario,original['engine_version']=='5.2.4' and original['system_units']=='SI' and original['flow_units']=='CMS')
        check('original balances agree with report '+scenario,abs(original['runoff_error']-r['runoff_continuity_error_percent'])<=.00051 and abs(original['flow_routing_error']-r['routing_continuity_error_percent'])<=.00051)
    if set(byscenario)=={'baseline','capacity75'}:
        rid=byscenario['capacity75']['run_id'];folder=workspace/'municipal'/rid
        expected=load(out/'comparison.json');actual=load(folder/'comparison.json')
        ignored={'baseline_run_id','scenario_run_id'}
        check('complete comparison response equals native',{k:v for k,v in actual.items() if k not in ignored}=={k:v for k,v in expected.items() if k not in ignored} and any(c['tool']=='compare_swmm_runs' and c['result']==actual for c in passed))
        check('complete comparison artifact',sha(folder/'comparison.csv')==sha(out/'comparison.csv'))
        requirements=[('read_swmm_source',{'city':city,'name':name},workspace/'sources'/city/name) for name in ['manifest.json','requests.json','rights.json']]
        requirements.append(('read_swmm_source',{'city':city,'name':'recipe.json'},CASE/'recipe.json'))
        requirements.extend(('read_swmm_artifact',{'run_id':rid,'name':name},folder/name) for name in ['comparison.csv','comparison.json','nodes.csv','outfalls.csv'])
        for tool,args,path in requirements:
            try:page_receipts.append(pages(calls,tool,args,path));check('all observed pages '+str(args),True)
            except ValueError as exc:checks.append({'name':str(exc),'passed':False})
    check('all five object listings',{c['arguments'].get('object_type') for c in passed if c['tool']=='model_list_objects'}=={'node','link','subcatchment','raingage','lid_control'})
    for tool in ['output_query_series','output_query_snapshot']:
        check('four result types '+tool,{c['arguments'].get('object_type') for c in passed if c['tool']==tool}=={'node','link','subcatchment','system'})
    check('all four approved model-control families',any(c['tool']=='simulation_step' and all(c['arguments'].get(k) for k in ['link_target_settings','node_generated_inflows','outfall_stages','raingage_total_precipitation']) for c in passed))
    check('hotstart state actually loaded',any(c['tool']=='simulation_create' and c['result'].get('hotstart_loaded') is True for c in passed))
    required_live={'nodes':{'depth','flooding'},'links':{'flow'},'subcatchments':{'rainfall','runoff'},
        'raingages':{'rainfall','total_precip'},'system':{'runoff_stats','routing_stats'}}
    live_seen={key:set() for key in required_live}
    for c in passed:
        if c['tool'] not in {'simulation_observe','simulation_step'}:continue
        observation=c['arguments'].get('observe') or {}
        for kind in required_live:
            if kind=='system':live_seen[kind].update(observation.get(kind,[]))
            else:
                for item in observation.get(kind,[]):live_seen[kind].update(item.get('fields',[]))
    missing_live={key:sorted(fields-live_seen[key]) for key,fields in required_live.items() if fields-live_seen[key]}
    check('native asynchronous cancellation observed',any(c['tool'] in {'simulation_task_status','simulation_task_cancel'} and c['result'].get('state')=='CANCELLED' for c in passed))
    observed_resources={}
    session_resource_states=[]
    for c in passed:
        if c['tool']!='read_swmm_resource':continue
        uri=c['arguments']['uri'];parts=uri.removeprefix('pyswmm://').split('/')
        if parts[0]=='runs' and len(parts)==3:family='runs/'+parts[2]
        elif parts[0] in {'sessions','tasks'} and len(parts)==3:family=parts[0]+'/status'
        else:family='/'.join(parts)
        observed_resources[family]=True
        if family=='sessions/status':
            try:session_resource_states.append(json.loads(c['result']['text'])['state'])
            except (ValueError,KeyError):session_resource_states.append('unproven')
    families={'models','runtime/status','runs/summary','runs/report','runs/output','sessions/status','tasks/status'}
    check('seven original resource families',families<=set(observed_resources))
    quality=load(out/'quality.json');canonical=json.dumps(quality,sort_keys=True,allow_nan=False);uri=f'swmm://cities/{city}/quality'
    offsets={};quality_matches=True
    for c in passed:
        if c['tool']!='read_swmm_resource' or c['arguments'].get('uri')!=uri:continue
        off=c['arguments'].get('offset',0);limit=c['arguments'].get('limit',8000);end=min(off+limit,len(canonical));r=c['result']
        expected={'uri':uri,'offset':off,'characters':len(canonical),'text_sha256':hashlib.sha256(canonical.encode()).hexdigest(),
            'next_offset':end if end<len(canonical) else None,'text':canonical[off:end]}
        quality_matches=quality_matches and r==expected;offsets[off]=r['next_offset']
    off=0;seen=set()
    while off in offsets and off not in seen:
        seen.add(off);off=offsets[off]
        if off is None:break
    check('complete municipal quality resource equals native',quality_matches and off is None)
    check('cleanup preserved all runs',any(c['tool']=='run_cleanup' and c['result'].get('removed_runs')==0 for c in passed))
    check('final status successful',bool(passed) and passed[-1]['tool']=='swmm_status')
    check('public model-query oracle passed',load(observations/'query-oracle.json')['passed'] is True)
    blocks=re.findall(r'```json\s*(\{.*?\})\s*```',answer,re.S)
    try:claims=json.loads(blocks[0]) if len(blocks)==1 else {}
    except ValueError:claims={}
    expected=expected_claims(city);claim_errors=[k for k,v in expected.items() if not exact(claims.get(k),v)]
    if set(claims)!=set(expected):claim_errors.append('exact_field_set')
    prose=re.sub(r'```json\s*\{.*?\}\s*```','',answer,flags=re.S).strip()
    return {'host':host,'city':city,'source_commit':process['code_commit'],'task_path':process['task_path'],'task_sha256':sha(task),
        'trace_sha256':sha(observations/'trace.json'),'process_sha256':sha(observations/'process.json'),'answer_sha256':sha(observations/'answer.md'),
        'tool_calls':len(calls),'successful_tool_families':len(TOOLS&successful),'failed_or_recovered_calls':[{'index':i,'tool':c['tool'],'arguments':c['arguments']} for i,c in enumerate(calls) if not success(c)],
        'host_provided_discovery_helpers':sorted(successful&discovery),
        'checks':checks,'checks_passed':all(c['passed'] for c in checks),'missing_tools':sorted(TOOLS-successful),
        'structured_claims':{'passed':not claim_errors,'mismatched_fields':claim_errors,'observed':claims},
        'complete_pages':page_receipts,'query_oracle_sha256':sha(observations/'query-oracle.json'),
        'task_ordering':{'session_resource_states':session_resource_states,'session_status_read_before_close':any(s in {'OPEN','STARTED','RUNNING','ENDED'} for s in session_resource_states)},
        'fine_grained_task_coverage':{'required_live_fields_exercised':not missing_live,'missing_live_fields':missing_live,
            'note':'Separate from 27 function-family/numeric/page acceptance. Supplementary observations may test omissions but do not rewrite this run.'},
        'prose_word_count':len(prose.split()),'prose_length_passed':len(prose.split())<=180,
        'narrative_factual_review':'Separate manual answer-hash-bound review required; no automatic prose admission.',
        'forecast_admitted':False,'calibration_revalidated':False,'product_qualified':False}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--host',choices=['codex','hermes'],required=True);p.add_argument('--city',choices=['odense','utrecht'],required=True)
    p.add_argument('--workspace',required=True,type=Path);p.add_argument('--observations',required=True,type=Path);p.add_argument('--output',required=True,type=Path);a=p.parse_args()
    result=review(a.host,a.city,a.workspace,a.observations);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({'host':a.host,'city':a.city,'checks_passed':result['checks_passed'],'claims_passed':result['structured_claims']['passed'],'failed_checks':[c['name'] for c in result['checks'] if not c['passed']],'claims_errors':result['structured_claims']['mismatched_fields'],'prose_words':result['prose_word_count']}))
    raise SystemExit(0 if result['checks_passed'] and result['structured_claims']['passed'] else 1)


if __name__=='__main__':main()
