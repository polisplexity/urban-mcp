"""Preserve original SWMM hydraulics; bind observations and a declared scenario."""
import collections
import csv
import datetime as dt
import hashlib
import io
import json
import math
from pathlib import Path
import re
import shutil
import subprocess
import zipfile
from zoneinfo import ZoneInfo

from . import data


def sections(text):
    result={};section=None
    for line in text.splitlines():
        s=line.split(';')[0].strip()
        if s.startswith('['):section=s.strip('[]').upper();result[section]=[]
        elif s and section:result[section].append(s.split())
    return result


def observations(city,folder):
    result=[]
    if city=='odense':
        obj=json.loads((folder/'rainfall.json').read_text())
        for f in obj['features']:
            p=f['properties'];start=dt.datetime.fromisoformat(p['from']);end=dt.datetime.fromisoformat(p['to'])
            if p['stationId']!='06120' or p['parameterId']!='acc_precip' or p['timeResolution']!='hour' or end-start!=dt.timedelta(hours=1):raise ValueError('Unexpected DMI observation identity/interval')
            if p['validity'] is not True or type(p['value']) not in {int,float} or not math.isfinite(p['value']) or p['value']<0:raise ValueError('Missing/invalid DMI rainfall is not zero')
            if f['geometry']['coordinates']!=[10.3304,55.4748]:raise ValueError('DMI station position changed')
            result.append((start,float(p['value']),False))
    else:
        with zipfile.ZipFile(folder/'rainfall.zip') as z:
            lines=z.read('uurgeg_260_2011-2020.txt').decode().splitlines()
        header=[v.strip() for v in next(l for l in lines if l.startswith('# STN,') and 'YYYYMMDD' in l).lstrip('# ').split(',')]
        for line in lines:
            if not re.match(r'^\s*260,',line):continue
            p=dict(zip(header,[v.strip() for v in line.split(',')],strict=True))
            if not '20180730'<=p['YYYYMMDD']<='20180903':continue
            if p['RH']=='':raise ValueError('Missing KNMI rainfall is not zero')
            raw=int(p['RH']);hour=int(p['HH'])
            if raw < -1 or not 1<=hour<=24:raise ValueError('Unexpected KNMI rainfall or interval')
            # HH=24 ends at next-day 00:00 UTC. SWMM VOLUME uses interval START.
            end=dt.datetime.strptime(p['YYYYMMDD'],'%Y%m%d').replace(tzinfo=dt.timezone.utc)+dt.timedelta(hours=hour)
            result.append((end-dt.timedelta(hours=1),0.025 if raw==-1 else raw/10,raw==-1))
    result.sort()
    if len({r[0] for r in result})!=len(result):raise ValueError('Duplicate observation timestamps require source review')
    return result


def event(city,folder):
    zone=ZoneInfo(data.config(city)['timezone']);obs=observations(city,folder)
    local=[(t.astimezone(zone).replace(tzinfo=None),v,trace) for t,v,trace in obs]
    bytime={t:(v,trace) for t,v,trace in local};candidates=[]
    for day in sorted({t.date() for t,_,_ in local if t.year==2018 and t.month==8}):
        start=dt.datetime.combine(day-dt.timedelta(days=1),dt.time())
        hours=[start+dt.timedelta(hours=i) for i in range(72)]
        if all(t in bytime for t in hours):
            # Trace lower bound, rather than imputed midpoint, selects the day.
            total=sum(0 if bytime[t][1] else bytime[t][0] for t in hours[24:48])
            candidates.append((total,day,start,hours))
    if not candidates:raise ValueError('No complete 72-hour observed forcing window')
    total,day,start,hours=min(candidates,key=lambda x:(-x[0],x[1]))
    rain=[(t,*bytime[t]) for t in hours];traces=sum(int(x[2]) for x in rain)
    return rain,{'wet_day':day.isoformat(),'selection_day_lower_bound_mm':round(total,6),
        'event_day_mm':round(sum(v for t,v,_ in rain if t.date()==day),6),
        'start_local':start.isoformat(),'end_local':(start+dt.timedelta(hours=72)).isoformat(),
        'timezone':data.config(city)['timezone'],'hourly_intervals':72,
        'forcing_total_mm':round(sum(v for _,v,_ in rain),6),'trace_intervals':traces,
        'trace_midpoint_mm':0.025,'trace_total_uncertainty_mm':round(traces*0.025,6),
        'complete_candidate_days':len(candidates),'warmup_hours':24,'cooldown_hours':24,
        'observation_kind':data.config(city)['weather']['description']}


def make_model(city,text,rain,info):
    start=dt.datetime.fromisoformat(info['start_local']);end=dt.datetime.fromisoformat(info['end_local'])
    opts={'START_DATE':start.strftime('%m/%d/%Y'),'START_TIME':'00:00:00','REPORT_START_DATE':start.strftime('%m/%d/%Y'),
        'REPORT_START_TIME':'00:00:00','END_DATE':end.strftime('%m/%d/%Y'),'END_TIME':'00:00:00','THREADS':'1'}
    src=sections(text)
    if dict(src['OPTIONS'])['FLOW_UNITS']!='CMS':raise ValueError('This municipal method requires source CMS metric units')
    if any(x[0]=='OBS_RAIN' for x in src.get('TIMESERIES',[])):raise ValueError('Observation timeseries ID collision')
    out=[];section='';repairs=[];changes=[]
    for line in text.splitlines():
        s=line.split(';')[0].strip();tok=s.split();before=line
        if s.startswith('['):section=s.strip('[]').upper()
        elif tok:
            if section=='OPTIONS' and tok[0] in opts:line=f'{tok[0]} {opts[tok[0]]}'
            if section=='RAINGAGES':line=f'{tok[0]} VOLUME 1:00 1.0 TIMESERIES OBS_RAIN'
            if section=='SUBCATCHMENTS' and any(t.lower()=='nan' for t in tok):
                if city!='utrecht' or float(tok[3])!=0 or tok[4].lower()!='nan' or sum(t.lower()=='nan' for t in tok)!=1:raise ValueError('Unreviewed non-finite source parameter')
                line=re.sub(r'\bnan\b','0',line,flags=re.I);repairs.append(tok[0])
        if line!=before:changes.append({'section':section,'before':before,'after':line})
        out.append(line)
    if city=='utrecht' and len(repairs)!=13:raise ValueError('Source zero-area normalization set changed')
    if not any(l.strip().upper()=='[TIMESERIES]' for l in out):out.append('[TIMESERIES]')
    i=next(i for i,l in enumerate(out) if l.strip().upper()=='[TIMESERIES]')+1
    out[i:i]=[f'OBS_RAIN {t:%m/%d/%Y} {t:%H:%M} {v:.6f}' for t,v,_ in rain]
    return '\n'.join(out)+'\n',{'edits':changes,'zero_area_nan_normalized_ids':repairs,'inserted_observation_rows':72,
        'physical_parameter_policy':'Original hydraulic/hydrologic/control/DWF values preserved except declared zero-area NaN normalization and scenario diameter.'}


def select_target(src):
    area=collections.defaultdict(float)
    for row in src['SUBCATCHMENTS']:area[row[2]]+=float(row[3])
    shapes={r[0]:r for r in src['XSECTIONS']}
    candidates=[]
    for c in src['CONDUITS']:
        x=shapes[c[0]]
        if x[1]=='CIRCULAR' and float(x[2])>0 and float(c[3])>0 and area[c[1]]>0:
            candidates.append((area[c[1]],c[0],c,x))
    if not candidates:raise ValueError('No eligible source conduit with directly contributing subcatchments')
    a,_,c,x=min(candidates,key=lambda v:(-v[0],v[1]))
    return {'conduit_id':c[0],'from_node':c[1],'to_node':c[2],'source_diameter_m':float(x[2]),
        'scenario_diameter_m':float(x[2])*0.75,'directly_contributing_area_ha':a,'eligible_conduits':len(candidates),
        'selection':'Largest sum of source subcatchment areas directly assigned to the upstream node; positive-length circular conduit; tie by source ID. No result-based tuning.'}


def prepare(city):
    folder,manifest=data.verify(city);out=data.root()/'models'/city
    rain,info=event(city,folder);text=(folder/'model.inp').read_text(encoding='utf-8-sig')
    baseline,transform=make_model(city,text,rain,info);src=sections(baseline);target=select_target(src)
    lines=[];section=''
    for line in baseline.splitlines():
        s=line.split(';')[0].strip()
        if s.startswith('['):section=s.strip('[]').upper()
        tok=s.split()
        if section=='XSECTIONS' and tok and tok[0]==target['conduit_id']:
            tok[2]=format(target['scenario_diameter_m'],'.12g');line=' '.join(tok)
        lines.append(line)
    modified='\n'.join(lines)+'\n'
    inspection=baseline
    inspection_end=dt.datetime.fromisoformat(info['start_local'])+dt.timedelta(minutes=5)
    inspection=re.sub(r'^END_DATE\s+.*$',f'END_DATE {inspection_end:%m/%d/%Y}',inspection,flags=re.M)
    inspection=re.sub(r'^END_TIME\s+.*$',f'END_TIME {inspection_end:%H:%M:%S}',inspection,flags=re.M)
    expected={'baseline.inp':baseline.encode(),'capacity75.inp':modified.encode(),'inspection.inp':inspection.encode()}
    source_bind={'original_model_sha256':data.sha(folder/'model.inp'),'weather_content_sha256':data.weather_fingerprint(city,folder/data.config(city)['weather']['filename']),
        'recipe_sha256':data.sha(data.CASE/'recipe.json'),'method_source_sha256':data.sha(Path(__file__))}
    quality={'city':city,'scope':data.config(city)['scope'],'source_binding':source_bind,'event':info,'target':target,
        'transformations':transform,'counts':{k.lower():len(src.get(k,[])) for k in ['SUBCATCHMENTS','JUNCTIONS','OUTFALLS','STORAGE','CONDUITS','PUMPS','ORIFICES','WEIRS','RAINGAGES']},
        'allow_ponding':dict(src['OPTIONS'])['ALLOW_PONDING'],'flow_units':'CMS','length_units':'m','area_units':'ha',
        'coordinate_reference':data.config(city)['coordinate_reference'],
        'flood_volume_report_resolution_m3':1,'node_volume_threshold_m3':10,
        'forecast_admitted':False,'calibration_revalidated':False,'product_qualified':False,
        'limits':data.recipe()['limitations']}
    if out.exists():
        if json.loads((out/'quality.json').read_text())!=quality or any((out/n).read_bytes()!=b for n,b in expected.items()):raise ValueError('Prepared case differs; preserve it and use a fresh workspace')
    else:
        out.mkdir(parents=True)
        for n,b in expected.items():(out/n).write_bytes(b)
        data.dump(out/'quality.json',quality)
        with (out/'rainfall.csv').open('w',newline='') as f:
            w=csv.writer(f);w.writerow(['interval_start_local','rainfall_mm','trace_midpoint_used']);w.writerows((t.isoformat(),v,str(trace).lower()) for t,v,trace in rain)
    return {**quality,'baseline_input_path':city+'/baseline.inp','scenario_input_path':city+'/capacity75.inp',
        'inspection_input_path':city+'/inspection.inp','quality_sha256':data.sha(out/'quality.json')}


def prepared(city):
    prepare(city)
    return data.root()/'models'/city


def summarize(city,scenario,report,output,out):
    from swmm_api import read_rpt_file
    # The original EPA CLI emits a literal single-byte superscript 3 in its
    # cubic-unit headings. Preserve bytes and decode that report as CP1252.
    text=Path(report).read_text(encoding='cp1252')
    errors=re.findall(r'^\s*ERROR\s+\d+:.*$',text,re.M)
    if errors or 'Analysis ended on:' not in text or 'Flow Routing Continuity' not in text:raise ValueError('Native report incomplete or contains errors: '+'; '.join(errors))
    r=read_rpt_file(report,encoding='cp1252');q=json.loads((prepared(city)/'quality.json').read_text());src=sections((prepared(city)/(scenario+'.inp')).read_text())
    node_ids=sorted(x[0] for k in ['JUNCTIONS','STORAGE','OUTFALLS','DIVIDERS'] for x in src.get(k,[]))
    depths=r.node_depth_summary;flood=r.node_flooding_summary
    if depths is None or set(depths.index)!=set(node_ids):raise ValueError('Native node summary does not cover original node set')
    if flood is None and 'No nodes were flooded.' not in text:raise ValueError('Missing flooding table cannot be interpreted as zero')
    floodrows={} if flood is None else flood.to_dict(orient='index')
    if not set(floodrows)<=set(node_ids):raise ValueError('Unknown flooded node')
    rows=[]
    for node in node_ids:
        f=floodrows.get(node)
        rows.append({'node_id':node,'listed_flooding':node in floodrows,
            'flood_volume_m3':0.0 if f is None else float(f['Total_Flood_Volume_10^6 ltr'])*1000,
            'flood_hours':0.0 if f is None else float(f['Hours_Flooded']),
            'peak_flood_rate_m3_s':0.0 if f is None else float(f['Maximum_Rate_CMS']),
            'maximum_depth_m':float(depths.loc[node,'Maximum_Depth_Meters'])})
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    with (out/'nodes.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    with (out/'outfalls.csv').open('w',newline='') as f:
        cols=['outfall_id','maximum_flow_m3_s','total_volume_m3'];w=csv.writer(f);w.writerow(cols)
        table=r.outfall_loading_summary
        expected={x[0] for x in src['OUTFALLS']}
        if table is None or not expected<=set(table.index):raise ValueError('Incomplete native outfall summary')
        for key in sorted(expected):w.writerow([key,float(table.loc[key,'Max_Flow_CMS']),float(table.loc[key,'Total_Volume_10^6 ltr'])*1000])
    summary={'city':city,'scenario':scenario,'nodes':len(rows),'listed_flooding_nodes':len(floodrows),
        'nodes_at_or_above_10m3':sum(x['flood_volume_m3']>=10 for x in rows),
        'sum_reported_node_flood_volume_m3':round(sum(x['flood_volume_m3'] for x in rows),6),
        'system_flooding_loss_m3':r.flow_routing_continuity['Flooding Loss']['Volume_10^6 ltr']*1000,
        'routing_continuity_error_percent':r.flow_routing_continuity['Continuity Error (%)'],
        'runoff_continuity_error_percent':r.runoff_quantity_continuity['Continuity Error (%)'],
        'report_precipitation_mm':r.runoff_quantity_continuity['Total Precipitation']['Depth_mm'],
        'warnings':re.findall(r'^\s*WARNING.*$',text,re.M),'quality':q,
        'rounding':'Native report node volumes: 0.001 million litres = 1 m3 resolution, ±0.5 m3 per displayed node. Listed rows may display zero. System loss and summed overflowing-node volumes differ with ponding/re-entry and rounding.',
        'report_sha256':data.sha(report),'output_sha256':data.sha(output),
        'artifacts':{n:{'sha256':data.sha(out/n),'bytes':(out/n).stat().st_size} for n in ['nodes.csv','outfalls.csv']},
        'forecast_admitted':False}
    data.dump(out/'summary.json',summary);return summary


def run_native(city,run_id,scenario):
    data.token(run_id)
    if scenario not in {'baseline','capacity75'}:raise ValueError('Unknown scenario')
    folder=prepared(city);out=data.root()/'native'/city/run_id;out.mkdir(parents=True,exist_ok=False)
    inp=out/'model.inp';shutil.copyfile(folder/(scenario+'.inp'),inp)
    with (out/'native.log').open('w') as log:
        proc=subprocess.run(['runswmm',str(inp),str(out/'model.rpt'),str(out/'model.out')],stdout=log,stderr=subprocess.STDOUT,timeout=300)
    if proc.returncode:raise ValueError('Original EPA CLI exited '+str(proc.returncode))
    result=summarize(city,scenario,out/'model.rpt',out/'model.out',out)
    return {**result,'native_run_id':run_id}


def bind_run(city,scenario,result):
    run_id=result['run_id'];out=data.root()/'municipal'/run_id;out.mkdir(parents=True,exist_ok=False)
    summary=summarize(city,scenario,data.root()/'runs'/result['artifacts']['report'],data.root()/'runs'/result['artifacts']['output'],out)
    data.dump(out/'binding.json',{'city':city,'scenario':scenario,'run_id':run_id,'original_result':result})
    return {**summary,'run_id':run_id,'original_result':result}


def compare(city,baseline_run_id,scenario_run_id):
    def load(run_id,scenario):
        if not re.fullmatch(r'[a-f0-9]{32}',run_id):raise ValueError('Use the returned original MCP run ID')
        p=data.root()/'municipal'/run_id;binding=json.loads((p/'binding.json').read_text());summary=json.loads((p/'summary.json').read_text())
        if binding['city']!=city or binding['scenario']!=scenario:raise ValueError('Comparison city/scenario mismatch')
        for name,receipt in summary['artifacts'].items():
            if data.sha(p/name)!=receipt['sha256']:raise ValueError('Run artifact changed')
        return p,summary
    a,sa=load(baseline_run_id,'baseline');b,sb=load(scenario_run_id,'capacity75')
    if sa['quality']!=sb['quality']:raise ValueError('Source/method binding differs')
    def read(p):return {r['node_id']:r for r in csv.DictReader((p/'nodes.csv').open())}
    ar,br=read(a),read(b)
    if set(ar)!=set(br):raise ValueError('Node denominator mismatch')
    out=b/'comparison.csv';rows=[]
    for node in sorted(ar):
        x,y=ar[node],br[node];av,bv=float(x['flood_volume_m3']),float(y['flood_volume_m3'])
        rows.append({'node_id':node,'baseline_flood_volume_m3':av,'scenario_flood_volume_m3':bv,'delta_flood_volume_m3':round(bv-av,6),
            'baseline_at_or_above_10m3':av>=10,'scenario_at_or_above_10m3':bv>=10,'newly_at_or_above_10m3':av<10<=bv,
            'baseline_listed_flooding':x['listed_flooding'],'scenario_listed_flooding':y['listed_flooding']})
    with out.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    result={'city':city,'baseline_run_id':baseline_run_id,'scenario_run_id':scenario_run_id,'nodes':len(rows),
        'threshold_m3':10,'newly_at_or_above_10m3':sum(r['newly_at_or_above_10m3'] for r in rows),
        'baseline_nodes_at_or_above_10m3':sa['nodes_at_or_above_10m3'],'scenario_nodes_at_or_above_10m3':sb['nodes_at_or_above_10m3'],
        'baseline_sum_reported_node_flood_volume_m3':sa['sum_reported_node_flood_volume_m3'],
        'scenario_sum_reported_node_flood_volume_m3':sb['sum_reported_node_flood_volume_m3'],
        'delta_sum_reported_node_flood_volume_m3':round(sb['sum_reported_node_flood_volume_m3']-sa['sum_reported_node_flood_volume_m3'],6),
        'routing_continuity_error_percent':[sa['routing_continuity_error_percent'],sb['routing_continuity_error_percent']],
        'target':sa['quality']['target'],'comparison_csv':{'sha256':data.sha(out),'bytes':out.stat().st_size,'rows':len(rows)},
        'forecast_admitted':False,'calibration_revalidated':False,'product_qualified':False}
    data.dump(b/'comparison.json',result);return result


def artifact(run_id,name,offset=0,limit=8000):
    if not re.fullmatch(r'[a-f0-9]{32}',run_id):raise ValueError('Use returned MCP run ID')
    if name not in {'nodes.csv','outfalls.csv','summary.json','binding.json','comparison.csv','comparison.json'}:raise ValueError('Choose an admitted municipal artifact')
    return data.page(data.root()/'municipal'/run_id/name,offset,limit)
