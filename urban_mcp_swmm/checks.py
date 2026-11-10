"""Real two-city native oracle, stdio MCP and complete operation coverage."""
import csv
import datetime as dt
import hashlib
import json
import math
import os
from pathlib import Path
import re
import sys
import time

from mcp import ClientSession,StdioServerParameters
from mcp.client.stdio import stdio_client
from . import data,engine


def decode(result):
    if result.structured_content is not None:
        value=result.structured_content
        return value['result'] if set(value)=={'result'} else value
    blocks=[x.text for x in result.content if x.type=='text']
    return json.loads(blocks[0]) if len(blocks)==1 else blocks


def independent_flood_report(path):
    """Read the EPA text table without swmm-api or adapter summary functions."""
    text=path.read_text(encoding='cp1252');tail=text.split('Node Flooding Summary',1)[1]
    tail=tail.split('Node Inflow Quality',1)[0].split('Outfall Loading Summary',1)[0]
    if 'No nodes were flooded.' in tail:return {}
    rows={}
    for line in tail.splitlines():
        p=line.split()
        if len(p)==7 and re.fullmatch(r'\d+:\d+',p[4]):
            rows[p[0]]={'volume_m3':float(p[5])*1000,'peak_m3_s':float(p[2]),'hours':float(p[1])}
    if not rows:raise AssertionError('Independent flooding table not found')
    return rows


async def run(city):
    data.config(city);stamp=time.strftime('%Y%m%dT%H%M%S')+'-'+os.urandom(3).hex()
    receipt={'city':city,'checks':[],'calls':[],'native':{},'mcp':{},'source_sha256':{p.name:data.sha(p) for p in Path(__file__).parent.glob('*.py')},
        'started_at':dt.datetime.now(dt.timezone.utc).isoformat(),'scope':'Computational/native/MCP reproduction; no LLM or field-validation claim.'}
    evidence=data.root()/'evidence'/city/stamp;evidence.mkdir(parents=True,exist_ok=False)
    def check(name,condition,details=None):
        receipt['checks'].append({'name':name,'passed':bool(condition),'details':details})
        if not condition:raise AssertionError(name+': '+str(details))
    native={}
    try:
        data.harvest(city);prepared=engine.prepare(city);folder=engine.prepared(city)
        source,_=data.verify(city);original=engine.sections((source/'model.inp').read_text(encoding='utf-8-sig'))
        base=engine.sections((folder/'baseline.inp').read_text());scenario=engine.sections((folder/'capacity75.inp').read_text())
        preserved=set(original)-{'OPTIONS','RAINGAGES','SUBCATCHMENTS'}
        for name in sorted(preserved):
            if name=='TIMESERIES':check('preserved source '+name,base[name][72:]==original[name])
            else:check('preserved source '+name,base[name]==original[name])
        check('all original subcatchment fields except reviewed zero-area NaN',all(a==b or (float(a[3])==0 and a[4].lower()=='nan' and b[4]=='0' and a[:4]+a[5:]==b[:4]+b[5:]) for a,b in zip(original['SUBCATCHMENTS'],base['SUBCATCHMENTS'],strict=True)))
        check('scenario changes exactly one XSECTIONS record',sum(a!=b for a,b in zip(base['XSECTIONS'],scenario['XSECTIONS'],strict=True))==1)
        check('scenario preserves all other sections',all(base[k]==scenario[k] for k in base if k!='XSECTIONS'))
        check('complete hourly forcing',prepared['event']['hourly_intervals']==72)
        check('no silent calibration/forecast/qualification',all(prepared[k] is False for k in ['forecast_admitted','calibration_revalidated','product_qualified']))
        for name in ['baseline','capacity75']:
            result=engine.run_native(city,stamp+'-'+name,name);native[name]=result
            p=data.root()/'native'/city/(stamp+'-'+name)
            manual=independent_flood_report(p/'model.rpt')
            rows=list(csv.DictReader((p/'nodes.csv').open()))
            check('independent native flooding table '+name,{r['node_id']:float(r['flood_volume_m3']) for r in rows if r['listed_flooding']=='True'}=={k:v['volume_m3'] for k,v in manual.items()})
            check('native complete node denominator '+name,len(rows)==sum(prepared['counts'][k] for k in ['junctions','storage','outfalls']))
            check('native observed rainfall conserved '+name,abs(result['report_precipitation_mm']-prepared['event']['forcing_total_mm'])<=.001)
            receipt['native'][name]={'run_id':result['native_run_id'],'summary':result}
        params=StdioServerParameters(command=sys.executable,args=['-m','urban_mcp_swmm','serve'],env=dict(os.environ))
        with (evidence/'mcp-stderr.log').open('w') as err:
            async with stdio_client(params,errlog=err) as streams:
                async with ClientSession(*streams) as client:
                    await client.initialize()
                    tools=(await client.list_tools()).tools
                    from .server import ORIGINAL_TOOLS
                    expected=set(ORIGINAL_TOOLS)|{'swmm_status','harvest_swmm_data','read_swmm_source','prepare_swmm_case','inspect_swmm_case','run_swmm_scenario','compare_swmm_runs','read_swmm_artifact','read_swmm_resource'}
                    check('27 actual advertised tools',{t.name for t in tools}==expected)
                    async def call(tool,args=None,error=False):
                        raw=await client.call_tool(tool,args or {},read_timeout_seconds=360)
                        value=decode(raw) if not raw.is_error else [x.text for x in raw.content if x.type=='text']
                        receipt['calls'].append({'tool':tool,'arguments':args or {},'is_error':raw.is_error,'result':value})
                        check(('reject ' if error else 'execute ')+tool,bool(raw.is_error)==error)
                        return value
                    await call('swmm_status');await call('harvest_swmm_data',{'city':city});await call('prepare_swmm_case',{'city':city})
                    inspect=await call('inspect_swmm_case',{'city':city});ids=inspect['inspection_ids'];input_path=city+'/inspection.inp'
                    for name in ['manifest.json','requests.json','rights.json','recipe.json']:
                        off=0
                        while True:
                            page=await call('read_swmm_source',{'city':city,'name':name,'offset':off,'limit':12000})
                            off=page['next_offset']
                            if off is None:break
                    model=await call('model_inspect',{'input_path':input_path})
                    check('native engine original model identity',str(model['engine_version']).startswith('5.2.4'))
                    for typ in ['node','link','subcatchment','raingage','lid_control']:
                        await call('model_list_objects',{'input_path':input_path,'object_type':typ})
                    short=await call('simulation_run',{'input_path':input_path})
                    await call('run_summary',{'run_id':short['run_id']})
                    await call('output_inspect',{'output_path':short['artifacts']['output']})
                    mcp_results={}
                    for name in ['baseline','capacity75']:
                        result=await call('run_swmm_scenario',{'city':city,'scenario':name});mcp_results[name]=result
                        p=data.root()/'municipal'/result['run_id'];np=data.root()/'native'/city/native[name]['native_run_id']
                        # Compare complete tables and every displayed numeric column, not just a headline.
                        for file in ['nodes.csv','outfalls.csv']:
                            ar=list(csv.DictReader((np/file).open()));br=list(csv.DictReader((p/file).open()))
                            check('native/MCP full '+name+' '+file,ar==br)
                        for key in ['nodes','listed_flooding_nodes','nodes_at_or_above_10m3','sum_reported_node_flood_volume_m3','system_flooding_loss_m3','routing_continuity_error_percent','runoff_continuity_error_percent','report_precipitation_mm','warnings']:
                            check('native/MCP '+name+' '+key,result[key]==native[name][key])
                        receipt['mcp'][name]=result
                    comparison=await call('compare_swmm_runs',{'city':city,'baseline_run_id':mcp_results['baseline']['run_id'],'scenario_run_id':mcp_results['capacity75']['run_id']})
                    receipt['comparison']=comparison
                    for name in ['comparison.csv','comparison.json','nodes.csv','outfalls.csv','summary.json','binding.json']:
                        off=0;text='';rid=mcp_results['capacity75']['run_id'];path=data.root()/'municipal'/rid/name
                        while True:
                            page=await call('read_swmm_artifact',{'run_id':rid,'name':name,'offset':off,'limit':12000});text+=page['text']
                            check('page bound '+name,len(page['text'])<=12000 and page['sha256']==data.sha(path))
                            off=page['next_offset']
                            if off is None:break
                        check('complete actual '+name,text==path.read_bytes().decode('utf-8-sig'))
                    out=mcp_results['baseline']['original_result']['artifacts']['output']
                    from pyswmm import Output
                    from swmm.toolkit.shared_enum import NodeAttribute,LinkAttribute,SubcatchAttribute,SystemAttribute
                    node=ids['node'];link=ids['link'];sub=ids['subcatchment']
                    for typ,obj,attr in [('node',node,'depth'),('link',link,'flow'),('subcatchment',sub,'rainfall'),('system','system','outfall_flow')]:
                        series=await call('output_query_series',{'output_path':out,'object_type':typ,'object_id':obj,'attribute':attr,'max_points':10})
                        receipt.setdefault('series',{})[typ]=series
                        snapshot=await call('output_query_snapshot',{'output_path':out,'object_type':typ,'object_ids':[obj],'attributes':[attr],'target_time':prepared['event']['start_local'][:10]+'T01:00:00'})
                        receipt.setdefault('snapshots',{})[typ]=snapshot
                        np=data.root()/'native'/city/native['baseline']['native_run_id']/'model.out'
                        with Output(str(np)) as native_output:
                            enum={'node':NodeAttribute.INVERT_DEPTH,'link':LinkAttribute.FLOW_RATE,'subcatchment':SubcatchAttribute.RAINFALL,'system':SystemAttribute.OUTFALL_FLOWS}[typ]
                            native_values=(native_output.system_series(enum) if typ=='system' else getattr(native_output,{'node':'node_series','link':'link_series','subcatchment':'subcatch_series'}[typ])(obj,enum))
                        check('native binary series '+typ,series['original_point_count']==len(native_values) and all(math.isclose(p['value'],native_values[dt.datetime.fromisoformat(p['time'])],rel_tol=1e-5,abs_tol=1e-6) for p in series['points']))
                        check('native binary snapshot '+typ,math.isclose(snapshot['values'][obj][attr],native_values[dt.datetime.fromisoformat(snapshot['report_time'])],rel_tol=1e-5,abs_tol=1e-6))
                    session=await call('simulation_create',{'input_path':input_path});sid=session['session_id']
                    await call('simulation_start',{'session_id':sid})
                    observe={'nodes':[{'id':node,'fields':['depth','flooding','head']}],
                        'links':[{'id':link,'fields':['flow','target_setting']}],
                        'subcatchments':[{'id':sub,'fields':['rainfall','runoff']}],
                        'raingages':[{'id':ids['raingage'],'fields':['rainfall','total_precip']}],
                        'system':['runoff_stats','routing_stats']}
                    await call('simulation_observe',{'session_id':sid,'observe':observe})
                    await call('simulation_step',{'session_id':sid,'advance_seconds':30,'observe':observe,
                        'link_target_settings':[{'id':link,'value':1.0}],
                        'node_generated_inflows':[{'id':node,'value':0.0}],
                        'outfall_stages':[{'id':ids['outfall'],'value':0.0}],
                        'raingage_total_precipitation':[{'id':ids['raingage'],'value':0.0}]})
                    hot=await call('simulation_save_hotstart',{'session_id':sid})
                    await client.read_resource('pyswmm://sessions/'+sid+'/status')
                    await call('read_swmm_resource',{'uri':'pyswmm://sessions/'+sid+'/status'})
                    await call('simulation_stop',{'session_id':sid});await call('simulation_close',{'session_id':sid})
                    receipt['hotstart']=hot
                    restored=await call('simulation_create',{'input_path':input_path,'hotstart_path':hot['artifacts']['hotstart']})
                    check('native hotstart state loaded',restored['hotstart_loaded'] is True)
                    await call('simulation_close',{'session_id':restored['session_id']})
                    task=await call('simulation_run_start',{'input_path':city+'/baseline.inp'})
                    tid=task['task_id'];await call('simulation_task_status',{'task_id':tid})
                    await client.read_resource('pyswmm://tasks/'+tid+'/status')
                    await call('read_swmm_resource',{'uri':'pyswmm://tasks/'+tid+'/status'})
                    await call('simulation_task_cancel',{'task_id':tid})
                    for _ in range(30):
                        state=await call('simulation_task_status',{'task_id':tid})
                        if state['state'] in {'CANCELLED','COMPLETED','ERROR'}:break
                        import anyio
                        await anyio.sleep(.1)
                    check('running native task cancelled',state['state']=='CANCELLED')
                    for uri in ['pyswmm://models','pyswmm://runtime/status','pyswmm://runs/'+short['run_id']+'/summary','pyswmm://runs/'+short['run_id']+'/report','pyswmm://runs/'+short['run_id']+'/output','swmm://cities/'+city+'/quality']:
                        value=await client.read_resource(uri);check('actual resource '+uri,bool(value.contents))
                        if uri.startswith('pyswmm:'):await call('read_swmm_resource',{'uri':uri})
                    resources=await client.list_resources();templates=await client.list_resource_templates();prompts=await client.list_prompts()
                    check('two static and six resource templates',len(resources.resources)==2 and len(templates.resource_templates)==6)
                    check('municipal prompt discovery',[p.name for p in prompts.prompts]==['municipal_drainage_review'])
                    prompt=await client.get_prompt('municipal_drainage_review',{'city':city});check('actual municipal prompt',bool(prompt.messages))
                    await call('model_inspect',{'input_path':'../outside.inp'},True)
                    await call('swmm_status')
                    await call('output_query_series',{'output_path':out,'object_type':'node','object_id':'MISSING','attribute':'depth'},True)
                    await call('swmm_status')
                    await call('simulation_step',{'session_id':sid,'advance_seconds':30},True)
                    await call('swmm_status')
                    await call('read_swmm_artifact',{'run_id':mcp_results['capacity75']['run_id'],'name':'../model.out'},True)
                    await call('swmm_status')
                    cleanup=await call('run_cleanup');receipt['cleanup']=cleanup
                    check('all advertised tools actually successful',expected=={c['tool'] for c in receipt['calls'] if not c['is_error']})
        receipt['passed']=True
    except BaseException as exc:
        receipt['passed']=False;receipt['failure']=repr(exc);raise
    finally:
        receipt['finished_at']=dt.datetime.now(dt.timezone.utc).isoformat();receipt['check_count']=len(receipt['checks'])
        data.dump(evidence/'native-mcp.json',receipt)
        data.dump(data.root()/'evidence'/city/'latest.json',{'path':str(evidence/'native-mcp.json'),'passed':receipt.get('passed',False)})
    return {'city':city,'passed':receipt['passed'],'checks':len(receipt['checks']),'tools':len(expected),'receipt':str(evidence/'native-mcp.json')}
