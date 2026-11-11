"""Execute isolated original methods; distinguish them from full server tests."""
import argparse
import ast
import asyncio
import contextlib
import hashlib
import importlib.metadata
import importlib.util
import io
import json
from pathlib import Path
import posixpath
import tarfile
import tempfile
from types import SimpleNamespace
import urllib.request

PINS={
    'klab':('https://codeload.github.com/kLabUM/SWMM-MCP-PUB/tar.gz/0c299b24196d1c8c32e92e8d4437958f237e4a88','12c81335d1b4b3c104bd6642abe8e72889d778938ef46c8eba120fb72d85c024', ['LICENSE','server.py','utils/ModelManager.py']),
    'workflow':('https://codeload.github.com/Zhonghao1995/agentic-swmm-workflow/tar.gz/a3bf4f23469cf4252955901176c86b9c94578963','ea87680174c39102978a3367e2bd79c03b912d3a1872568b1e166eefba0e2756',['LICENSE','mcp/swmm-runner/server.js','skills/swmm-runner/scripts/swmm_runner.py'])}


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',required=True,type=Path);a=p.parse_args()
    a.output.parent.mkdir(parents=True,exist_ok=True);cache=a.output.parent/'reviewed-upstreams';cache.mkdir(exist_ok=True)
    evidence={'scope':'Isolated original AST methods with explicit stubs and original generic CLI functions. These are not full alternative MCP-server executions. Selected PySWMM MCP original suite/native/city/host results are recorded separately.', 'archives':{},'files':{},'checks':[]}
    def check(name,condition,observed):
        evidence['checks'].append({'name':name,'passed':bool(condition),'observed':observed})
        if not condition:raise AssertionError(name)
    for name,(url,expected,selected) in PINS.items():
        request=urllib.request.urlopen(url,timeout=90);b=request.read(25_000_001)
        if len(b)>25_000_000 or hashlib.sha256(b).hexdigest()!=expected:raise ValueError('Original archive hash changed')
        target=cache/name;target.mkdir(exist_ok=True)
        with tarfile.open(fileobj=io.BytesIO(b),mode='r:gz') as t:
            for member in t.getmembers():
                relative='/'.join(member.name.split('/')[1:])
                if relative in selected and member.isfile():
                    out=target/relative;out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(t.extractfile(member).read())
                    evidence['files'][name+'/'+relative]={'sha256':sha(out),'bytes':out.stat().st_size}
        evidence['archives'][name]={'url':url,'sha256':expected,'bytes':len(b),'selected_files':selected}
    manager=cache/'klab/utils/ModelManager.py';tree=ast.parse(manager.read_text())
    cls=next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name=='ModelManager')
    selected=[n for n in cls.body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef)) and n.name in {'duplicate_model','run_model'}]
    node=ast.ClassDef(name='ModelManager',bases=[],keywords=[],body=selected,decorator_list=[])
    commands=[];native_calls=[]
    fake_os=SimpleNamespace(path=SimpleNamespace(join=posixpath.join,exists=lambda p:True),system=lambda cmd:commands.append(cmd) or 1)
    namespace={'os':fake_os,'MODELS_DIRECTORY':'/synthetic/models','Simulation':lambda *args:native_calls.append(args),'log_info':lambda *args:None}
    exec(compile(ast.fix_missing_locations(ast.Module(body=[node],type_ignores=[])),str(manager),'exec'),namespace)
    original=namespace['ModelManager']();original._fetch_models=lambda:None;original._editable_models=[];original._ModelManager__models=['partial']
    result=original.duplicate_model('with spaces','../outside; literal')
    check('original duplicate passes unquoted/unvalidated operands to shell',commands==['cp /synthetic/models/with spaces.inp /synthetic/models/../outside; literal.inp'],{'intercepted_command':commands[0],'shell_executed':False})
    check('original duplicate reports new model despite failed copy',result=='../outside; literal' and original._editable_models==[result],{'copy_exit_code_stub':1,'returned':result})
    result=asyncio.run(original.run_model('partial'))
    check('original run skips native execution when any output exists',result=='Model already ran.' and not native_calls,{'returned':result,'native_invocations':len(native_calls),'partial_output_stub':True})
    server=cache/'klab/server.py';tree=ast.parse(server.read_text())
    fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='add_storage');fn.decorator_list=[]
    from swmm_api import SwmmInput
    from swmm_api.input_file.sections import Storage
    model=SwmmInput.read_text('[OPTIONS]\nFLOW_UNITS CMS\n[JUNCTIONS]\nJ 0 2 0 0 0\n')
    namespace={'mm':SimpleNamespace(get=lambda *args:model,update_inp=lambda *args:None),'Storage':Storage}
    exec(compile(ast.fix_missing_locations(ast.Module(body=[fn],type_ignores=[])),str(server),'exec'),namespace)
    failure=None
    try:namespace['add_storage']('synthetic-metric','J',100.0)
    except AttributeError as exc:failure=str(exc)
    check('original storage creation fails against tested parser property',failure is not None and 'no setter' in failure,{'parser_version':importlib.metadata.version('swmm-api'),'error':failure,'full_original_locked_stack_tested':False})
    model['STORAGE']=Storage.create_section()
    result=namespace['add_storage']('synthetic-metric','J',100.0)
    area=model.STORAGE['J'].data[0];correct=100*.028316846592/2
    check('original cuft storage argument is treated as native metric volume',area==50 and abs(area-correct)>1,{'argument_cuft':100,'source_depth_m':2,'actual_area_m2':area,'converted_area_m2':correct,'result':result,'native_solver_executed':False})
    file=cache/'workflow/skills/swmm-runner/scripts/swmm_runner.py'
    spec=importlib.util.spec_from_file_location('reviewed_original_swmm_runner',file);runner=importlib.util.module_from_spec(spec);spec.loader.exec_module(runner)
    with tempfile.TemporaryDirectory() as directory:
        directory=Path(directory);left=directory/'a.rpt';right=directory/'b.rpt'
        left.write_text('Flow Routing Continuity\nContinuity Error (%) ..... 0.1\nNode Flooding Summary\nJ 0.1\n')
        right.write_text('Flow Routing Continuity\nContinuity Error (%) ..... 0.1\nNode Flooding Summary\nJ 999.0\n')
        stdout=io.StringIO()
        with contextlib.redirect_stdout(stdout):runner.cmd_compare(SimpleNamespace(rpt=str(left),rpt2=str(right)))
        observed=json.loads(stdout.getvalue())
        check('original workflow compare returns continuity only',set(observed)=={'a','b','a_err','b_err'}, {'keys':sorted(observed),'different_flooding_rows_compared':False,'a_err':observed['a_err'],'b_err':observed['b_err']})
        errors=directory/'error.rpt';errors.write_text('  ERROR 209: undefined object\nContinuity Error (%) ..... 0.1\n')
        detected=runner.scan_rpt_for_errors(errors)
        check('original workflow detects native report error despite exit ambiguity',detected==['ERROR 209: undefined object'],{'detected':detected})
    evidence['selected_upstream_files']={str(p.relative_to('/opt/pyswmm-mcp')):sha(p) for p in Path('/opt/pyswmm-mcp').glob('src/pyswmm_mcp/*.py')}
    evidence['linux_watchdog_patch']=json.loads(Path('/opt/linux-watchdog-receipt.json').read_text())
    evidence['runtime']=[]
    for name in ['mcp','mcp-types','pyswmm','swmm-toolkit','swmm-api','pyswmm-mcp','pydantic']:
        d=importlib.metadata.distribution(name)
        evidence['runtime'].append({'package':name,'version':d.version,'license_expression':d.metadata.get('License-Expression'),
            'license_files':[{'path':str(f),'sha256':sha(d.locate_file(f))} for f in d.files if 'license' in str(f).lower() and d.locate_file(f).is_file()]})
    evidence['native_cli']={'path':'/opt/native/bin/runswmm','sha256':sha('/opt/native/bin/runswmm'),'library_sha256':sha('/opt/native/bin/libswmm5.so'),
        'source_version':'5.2.4','source_commit':'07c371f8a0d477da1d9d4e7c0d75719664f62fec','source_files':{str(p.relative_to('/opt/epa')):sha(p) for p in [Path('/opt/epa/src/solver/gage.c'),Path('/opt/epa/src/solver/statsrpt.c'),Path('/opt/epa/src/solver/report.c'),Path('/opt/epa/src/solver/swmm5.c')]}}
    evidence['passed']=True;evidence['check_count']=len(evidence['checks'])
    a.output.write_text(json.dumps(evidence,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'passed':True,'isolated_original_checks':len(evidence['checks']),'output':str(a.output)}))


if __name__=='__main__':main()
