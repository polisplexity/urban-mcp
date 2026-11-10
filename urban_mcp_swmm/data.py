"""Exact licensed model acquisition and independently sourced observed forcing."""
from pathlib import Path
import datetime as dt
import hashlib
import io
import json
import os
import re
import tarfile
import urllib.request
import zipfile

CASE=Path('/opt/urban-mcp/cases/two-city-swmm')
if not CASE.exists():CASE=Path(__file__).resolve().parents[1]/'cases/two-city-swmm'


def root():return Path(os.environ.get('URBAN_MCP_SWMM_ROOT','/data'))
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def dump(path,value):
    Path(path).parent.mkdir(parents=True,exist_ok=True)
    Path(path).write_text(json.dumps(value,indent=2,allow_nan=False)+'\n',encoding='utf-8')
def recipe():return json.loads((CASE/'recipe.json').read_text())
def config(city):
    if city not in recipe()['cities']:raise ValueError('Choose odense or utrecht')
    return recipe()['cities'][city]
def token(value):
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{0,63}',value):raise ValueError('Use a simple identifier of at most 64 characters')
    return value
def status():
    return {'capability':'historical-drainage-capacity','cities':list(recipe()['cities']),
        'upstream_mcp':'foundanotusedname/pyswmm-mcp@a4db37b45d3b30dcfbd80fc0162a8238e727a80f',
        'native':'EPA SWMM 5.2.4 / PySWMM 2.2.0 / swmm-toolkit 0.17.0',
        'framework':'official Python MCP SDK 2.3.0, original MCPServer',
        'scenarios':['baseline','capacity75'],'forecast_admitted':False,'calibration_revalidated':False,
        'product_qualified':False,'qualification':'Independent person and third city required.',
        'method':recipe()['method'],'available_sources':[c for c in recipe()['cities'] if (root()/'sources'/c/'manifest.json').exists()]}


def fetch(url,requests,headers=None,max_bytes=12_000_000):
    with urllib.request.urlopen(urllib.request.Request(url,headers=headers or {}),timeout=90) as response:
        content=response.read(max_bytes+1)
        if len(content)>max_bytes:raise ValueError('Source exceeds declared acquisition bound')
        requests.append({'url':url,'retrieved_at':dt.datetime.now(dt.timezone.utc).isoformat(),
            'http_status':response.status,'bytes':len(content),'sha256':hashlib.sha256(content).hexdigest(),
            'etag':response.headers.get('ETag'),'content_range':response.headers.get('Content-Range')})
        if headers and 'Range' in headers and response.status!=206:raise ValueError('Publisher did not honor byte range')
        return content


class RemoteZip(io.RawIOBase):
    """Read only ZIP directory and selected model, with version-consistent ranges."""
    def __init__(self,url,size,requests):
        self.url,self.size,self.requests,self.pos=url,size,requests,0
        with urllib.request.urlopen(urllib.request.Request(url,method='HEAD'),timeout=45) as r:
            if int(r.headers['Content-Length'])!=size:raise ValueError('Publisher archive size changed')
            self.etag=r.headers['ETag']
    def seekable(self):return True
    def tell(self):return self.pos
    def seek(self,offset,whence=0):
        self.pos=offset if whence==0 else self.pos+offset if whence==1 else self.size+offset
        if not 0<=self.pos<=self.size:raise ValueError('Invalid ZIP seek')
        return self.pos
    def read(self,n=-1):
        if n<0:n=self.size-self.pos
        if not n:return b''
        end=min(self.size-1,self.pos+n-1)
        b=fetch(self.url,self.requests,{'Range':f'bytes={self.pos}-{end}','If-Range':self.etag})
        if len(b)!=end-self.pos+1 or self.requests[-1]['etag']!=self.etag:raise ValueError('ZIP ranges changed version')
        self.pos+=len(b);return b


def weather_fingerprint(city,path):
    if city=='utrecht':return sha(path)
    value=json.loads(Path(path).read_text())
    # Keep original response bytes; only the envelope timeStamp is excluded
    # from the independently recorded content fingerprint of the observations.
    records=sorted(value['features'],key=lambda f:f['id'])
    return hashlib.sha256(json.dumps(records,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()


def verify(city):
    c=config(city);folder=root()/'sources'/city
    manifest=json.loads((folder/'manifest.json').read_text())
    for f in manifest['files']:
        p=folder/f['name']
        if sha(p)!=f['sha256'] or p.stat().st_size!=f['bytes']:raise ValueError('Source artifact integrity failed: '+f['name'])
    if sha(folder/'model.inp')!=c['model']['sha256']:raise ValueError('Original model differs from recipe')
    if weather_fingerprint(city,folder/c['weather']['filename'])!=c['weather']['content_sha256']:raise ValueError('Observation content differs from locked experiment; create a reviewed new recipe')
    return folder,manifest


def harvest(city,mode='snapshot'):
    c=config(city);folder=root()/'sources'/city
    if mode not in {'snapshot','live'}:raise ValueError('mode must be snapshot or live')
    if folder.exists():
        verify(city)
        if mode=='live':raise ValueError('Live harvest requires a fresh city source directory')
        return {'city':city,'already_present':True,'manifest_sha256':sha(folder/'manifest.json')}
    folder.mkdir(parents=True)
    requests=[]
    try:
        if mode=='snapshot':
            lock=json.loads((CASE/'snapshot.lock.json').read_text())['cities'][city]
            archive=fetch(lock['url'],requests,max_bytes=15_000_000)
            if hashlib.sha256(archive).hexdigest()!=lock['sha256']:raise ValueError('Snapshot archive hash mismatch')
            with tarfile.open(fileobj=io.BytesIO(archive),mode='r:gz') as t:
                for member in t.getmembers():
                    if not member.isfile() or '/' in member.name or member.name.startswith('.'):raise ValueError('Unexpected snapshot member')
                    (folder/member.name).write_bytes(t.extractfile(member).read())
            verify(city)
            dump(folder/'snapshot-restore.json',{'requests':requests,'archive_sha256':lock['sha256']})
        else:
            m=c['model']
            if city=='odense':
                archive=fetch(m['url'],requests)
                if hashlib.sha256(archive).hexdigest()!=m['archive_sha256']:raise ValueError('Original model archive changed')
                with zipfile.ZipFile(io.BytesIO(archive)) as z:model=z.read(m['member'])
            else:
                with zipfile.ZipFile(RemoteZip(m['url'],m['archive_bytes'],requests)) as z:model=z.read(m['member'])
            if hashlib.sha256(model).hexdigest()!=m['sha256']:raise ValueError('Original input model changed')
            (folder/'model.inp').write_bytes(model)
            w=c['weather'];b=fetch(w['url'],requests);(folder/w['filename']).write_bytes(b)
            if weather_fingerprint(city,folder/w['filename'])!=w['content_sha256']:raise ValueError('Observed weather changed; retain failed acquisition and review a new recipe')
            for asset in c['metadata']:
                (folder/asset['filename']).write_bytes(fetch(asset['url'],requests,max_bytes=2_000_000))
            dump(folder/'rights.json',{'model':c['model']['rights'],'weather':w['rights'],'attribution':c['attribution'],
                'excluded':'Original Bellinge rain-gauge collection CC-BY-NC-4.0 is not redistributed or used. All original hydraulic parameters remain historical.'})
            dump(folder/'requests.json',requests)
            files=[{'name':p.name,'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(folder.iterdir()) if p.is_file()]
            dump(folder/'manifest.json',{'city':city,'mode':mode,'files':files,'model_member':m['member'],
                'model_license':m['rights'],'weather_license':w['rights'],'weather_content_sha256':w['content_sha256']})
            verify(city)
    except Exception as exc:
        dump(folder/'acquisition-failure.json',{'error':str(exc),'requests':requests});raise
    return {'city':city,'mode':mode,'manifest_sha256':sha(folder/'manifest.json'),'sources':len(verify(city)[1]['files'])}


def page(path,offset=0,limit=8000):
    if type(offset)!=int or offset<0 or type(limit)!=int or not 1<=limit<=12000:raise ValueError('offset >= 0; limit 1..12000')
    b=Path(path).read_bytes();s=b.decode('utf-8-sig')
    if offset>len(s):raise ValueError('Offset exceeds text length')
    end=min(offset+limit,len(s))
    return {'name':Path(path).name,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'offset':offset,
        'next_offset':end if end<len(s) else None,'characters':len(s),'text':s[offset:end]}


def read_source(city,name='manifest.json',offset=0,limit=8000):
    folder,manifest=verify(city)
    if name=='recipe.json':return page(CASE/name,offset,limit)
    allowed={x['name'] for x in manifest['files']}|{'manifest.json','snapshot-restore.json'}
    if name not in allowed or name.endswith('.zip'):raise ValueError('Choose a named textual source from manifest.json; raw ZIP is not a text endpoint')
    return page(folder/name,offset,limit)
