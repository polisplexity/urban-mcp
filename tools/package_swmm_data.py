"""Package already verified, permitted publisher inputs; exclude original NC rain."""
import argparse
import gzip
import hashlib
import io
import json
from pathlib import Path
import tarfile


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--sources',required=True,type=Path)
    p.add_argument('--output',required=True,type=Path)
    p.add_argument('--release-tag',default='data-swmm-20261110')
    a=p.parse_args();a.output.mkdir(parents=True,exist_ok=True);cities={}
    for city in ['odense','utrecht']:
        folder=a.sources/city;m=json.loads((folder/'manifest.json').read_text())
        allowed=[f['name'] for f in m['files']]+['manifest.json']
        for f in m['files']:
            b=(folder/f['name']).read_bytes()
            if hashlib.sha256(b).hexdigest()!=f['sha256'] or len(b)!=f['bytes']:raise ValueError('Source changed')
        content=io.BytesIO()
        with tarfile.open(fileobj=content,mode='w') as t:
            for name in sorted(allowed):
                b=(folder/name).read_bytes();info=tarfile.TarInfo(name);info.size=len(b);info.mode=0o644;info.mtime=0
                t.addfile(info,io.BytesIO(b))
        name=city+'-swmm-sources.tar.gz';out=a.output/name
        out.write_bytes(gzip.compress(content.getvalue(),mtime=0))
        cities[city]={'url':f'https://github.com/polisplexity/urban-mcp/releases/download/{a.release_tag}/{name}',
            'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'bytes':out.stat().st_size,
            'manifest_sha256':hashlib.sha256((folder/'manifest.json').read_bytes()).hexdigest()}
    lock={'schema_version':'0.1.0','release_tag':a.release_tag,'cities':cities,
        'rights':'Model CC-BY-4.0; DMI CC-BY-4.0; KNMI CC0 with publisher attribution/no-endorsement notice. Code MIT does not relicense inputs.',
        'exclusions':'No Bellinge rain-gauge collection, learned GNN weights, proprietary utilities data, calibration claims or generated simulation outputs.'}
    (a.output/'snapshot.lock.json').write_text(json.dumps(lock,indent=2)+'\n')
    print(json.dumps(lock,indent=2))


if __name__=='__main__':main()
