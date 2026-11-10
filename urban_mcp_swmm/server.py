"""Reuse the original server; add data, municipal comparison and bounded evidence."""
import json
import re
import signal

from pyswmm_mcp import server as upstream
from mcp.server import MCPServer
from . import data,engine

mcp=MCPServer('urban_mcp_swmm',instructions='Start with swmm_status; harvest a named snapshot and prepare the city. Use baseline/capacity75 municipal runs for the 72-hour comparison, and the explicitly separate five-minute inspection model for interactive/control/hotstart tests. All IDs, paths, units and times must come from returned data. Original simulation_run performs a batch without municipal comparison binding; run_swmm_scenario adds that binding. Read complete comparison CSV pages until next_offset is null. Report network warnings/continuity, hourly regional rain, historic assets and all false admission flags. No field forecast or city-wide flood extent is admitted. Cleanup retention is disabled. Output inspection and interactive creation return counts/samples rather than unbounded ID arrays; retrieve all IDs using model_list_objects. Read resource families with read_swmm_resource. Interleave status between intentional failures for hosts with a failure circuit breaker.')

ORIGINAL_TOOLS=['model_inspect','model_list_objects','simulation_run','output_inspect','simulation_create','simulation_start',
    'simulation_observe','simulation_step','simulation_stop','simulation_save_hotstart','simulation_close','output_query_series',
    'output_query_snapshot','run_summary','simulation_run_start','simulation_task_status','simulation_task_cancel','run_cleanup']
for name in ORIGINAL_TOOLS:
    if name not in {'output_inspect','simulation_create'}:mcp.tool()(getattr(upstream,name))
for uri,name,fn,mime in [
    ('pyswmm://models','model-list',upstream.models_resource,'application/json'),
    ('pyswmm://runtime/status','runtime-status',upstream.runtime_status_resource,'application/json'),
    ('pyswmm://runs/{run_id}/summary','run-summary',upstream.run_summary_resource,'application/json'),
    ('pyswmm://sessions/{session_id}/status','session-status',upstream.session_status_resource,'application/json'),
    ('pyswmm://tasks/{task_id}/status','simulation-task-status',upstream.simulation_task_status_resource,'application/json'),
    ('pyswmm://runs/{run_id}/report','run-report',upstream.run_report_resource,'text/plain'),
    ('pyswmm://runs/{run_id}/output','output-metadata',upstream.output_metadata_resource,'application/json')]:
    mcp.resource(uri,name=name,mime_type=mime)(fn)


def compact(value):
    """Bound original metadata arrays without changing the solver or stored run."""
    value=dict(value)
    for key in ['nodes','links','subcatchments','outfalls','raingages','lid_controls']:
        if isinstance(value.get(key),list):
            items=value.pop(key);value[key+'_count']=len(items);value[key+'_sample']=items[:5]
    if isinstance(value.get('manifest'),dict):value['manifest']=compact(value['manifest'])
    return value


@mcp.tool()
def output_inspect(output_path:str)->dict:
    """Original output inspection with bounded ID counts/samples; complete IDs via model_list_objects. Binary output remains on disk."""
    return compact(upstream.output_inspect(output_path))


@mcp.tool()
def simulation_create(input_path:str,hotstart_path:str|None=None)->dict:
    """Original process-isolated interactive create/hotstart with bounded manifest counts/samples. Use the separate inspection.inp for control experiments."""
    return compact(upstream.simulation_create(input_path,hotstart_path))


@mcp.tool()
def swmm_status()->dict:
    """Discover cities, exact method, original runtime, licenses and pending qualification."""
    return data.status()


@mcp.tool()
def harvest_swmm_data(city:str,mode:str='snapshot')->dict:
    """Restore exact licensed sources, or reharvest pinned original publishers in a fresh workspace. No inferred pipes or synthetic rain."""
    return data.harvest(city,mode)


@mcp.tool()
def read_swmm_source(city:str,name:str='manifest.json',offset:int=0,limit:int=8000)->dict:
    """Page complete source manifest, requests, rights, recipe or original INP at ≤12000 characters. Raw SHA identifies original bytes; text may normalize decoding."""
    return data.read_source(city,name,offset,limit)


@mcp.tool()
def prepare_swmm_case(city:str)->dict:
    """Verify sources; bind largest complete observed August 2018 day with 24h warm-up/cool-down. Preserve source physics; declare all edits including 13 zero-area Tuindorp NaNs. Create baseline, diameter75 and separate five-minute inspection inputs."""
    return engine.prepare(city)


@mcp.tool()
def inspect_swmm_case(city:str)->dict:
    """Read quality, source IDs, units, window and deterministic target; no simulation implied."""
    folder=engine.prepared(city);s=engine.sections((folder/'baseline.inp').read_text());q=json.loads((folder/'quality.json').read_text())
    return {'quality':q,'inspection_ids':{'node':q['target']['from_node'],'link':q['target']['conduit_id'],
        'outfall':s['OUTFALLS'][0][0],'subcatchment':s['SUBCATCHMENTS'][0][0],'raingage':s['RAINGAGES'][0][0]},
        'input_paths':{n:city+'/'+n+'.inp' for n in ['baseline','capacity75','inspection']}}


@mcp.tool()
def run_swmm_scenario(city:str,scenario:str)->dict:
    """Execute a full 72-hour baseline or capacity75 through original PySWMM MCP isolated batch; retain native report/output and all node/outfall rows. Diameter75 is a hypothetical geometry loss, not observed blockage or literal sediment depth."""
    if scenario not in {'baseline','capacity75'}:raise ValueError('Choose baseline or capacity75')
    engine.prepared(city)
    result=upstream.simulation_run(city+'/'+scenario+'.inp',300)
    if upstream.run_summary(result['run_id'])['completion_status']!='COMPLETED':raise ValueError('Native batch not complete')
    full=engine.bind_run(city,scenario,result)
    # Detailed transformations remain available in inspect_swmm_case and summary pages.
    return {k:v for k,v in full.items() if k!='quality'}


@mcp.tool()
def compare_swmm_runs(city:str,baseline_run_id:str,scenario_run_id:str)->dict:
    """Compare every original node, ≥10 m³ reported overflow threshold and newly crossing IDs in complete comparison.csv. Preserve zero/rounded values, ponding and continuity limits."""
    return engine.compare(city,baseline_run_id,scenario_run_id)


@mcp.tool()
def read_swmm_artifact(run_id:str,name:str,offset:int=0,limit:int=8000)->dict:
    """Read complete municipal CSV/JSON in ≤12000-character pages; follow next_offset until null. No arbitrary paths."""
    return engine.artifact(run_id,name,offset,limit)


def original_resource(uri):
    if uri=='pyswmm://models':return upstream.models_resource()
    if uri=='pyswmm://runtime/status':return upstream.runtime_status_resource()
    m=re.fullmatch(r'pyswmm://(runs|sessions|tasks)/([A-Za-z0-9_-]{1,128})/(summary|status|report|output)',uri)
    if not m:raise ValueError('Use an advertised original resource URI with a returned ID')
    group,identifier,kind=m.groups()
    if group=='runs' and not re.fullmatch(r'[a-f0-9]{32}',identifier):raise ValueError('Invalid run ID')
    calls={('runs','summary'):upstream.run_summary_resource,('runs','report'):upstream.run_report_resource,
        ('runs','output'):upstream.output_metadata_resource,('sessions','status'):upstream.session_status_resource,
        ('tasks','status'):upstream.simulation_task_status_resource}
    if (group,kind) not in calls:raise ValueError('Unknown original resource family')
    return calls[(group,kind)](identifier)


@mcp.tool()
def read_swmm_resource(uri:str,offset:int=0,limit:int=8000)->dict:
    """Read actual original MCP resource functions through bounded text pages, including reports and binary-output metadata (not binary bytes)."""
    if type(offset)!=int or offset<0 or type(limit)!=int or not 1<=limit<=12000:raise ValueError('offset >=0; limit 1..12000')
    value=original_resource(uri);text=value if isinstance(value,str) else json.dumps(value,sort_keys=True,allow_nan=False)
    if offset>len(text):raise ValueError('Offset beyond resource')
    end=min(offset+limit,len(text))
    import hashlib
    return {'uri':uri,'offset':offset,'characters':len(text),'text_sha256':hashlib.sha256(text.encode()).hexdigest(),
        'next_offset':end if end<len(text) else None,'text':text[offset:end]}


@mcp.resource('swmm://cities/{city}/quality',name='municipal-quality',mime_type='application/json')
def quality_resource(city:str)->dict:
    folder=engine.prepared(city);return json.loads((folder/'quality.json').read_text())


@mcp.prompt()
def municipal_drainage_review(city:str)->str:
    data.config(city)
    return f'For {city}, restore sources, prepare and inspect quality. Execute baseline and capacity75; compare every node and read full CSV pages. Separately exercise original inspection, output, interactive/hotstart, asynchronous task/cancellation and resources. Review exact reported ≥10 m³ crossings, native continuity, hourly regional rain and historical assets. Keep forecast_admitted, calibration_revalidated and product_qualified false. Never infer 2D extent, damage, exposure or current system condition.'


def main():
    # Service.shutdown owns all spawned native workers. Container stop delivers
    # SIGTERM to this Python PID 1; avoid leaving a detached simulation behind.
    def terminate(signum,frame):raise SystemExit(128+signum)
    signal.signal(signal.SIGTERM,terminate)
    try:mcp.run()
    finally:
        if upstream._service is not None:upstream._service.shutdown()
