"""Package permitted exact original sources; caches and generated simulations excluded."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import zipfile

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from urban_mcp_sumo import data


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace",type=Path,required=True)
    parser.add_argument("--output-dir",type=Path,required=True)
    parser.add_argument("--release-tag",default="data-sumo-20261110")
    args=parser.parse_args()
    args.output_dir.mkdir(parents=True,exist_ok=True)
    lock={}
    for city in ["bologna","ingolstadt"]:
        folder,manifest=data.verify(city,args.workspace/"inputs"/city)
        name=city+"-sumo-20261110.zip"
        target=args.output_dir/name
        with zipfile.ZipFile(target,"w",compression=zipfile.ZIP_DEFLATED,compresslevel=6) as archive:
            for filename in sorted(["manifest.json",*manifest["files"]]):
                info=zipfile.ZipInfo(filename,date_time=(2026,11,10,0,0,0))
                info.create_system=3;info.external_attr=0o100644<<16;info.compress_type=zipfile.ZIP_DEFLATED
                archive.writestr(info,(folder/filename).read_bytes())
        lock[city]={"url":f"https://github.com/polisplexity/urban-mcp/releases/download/{args.release_tag}/{name}","bytes":target.stat().st_size,"sha256":data.sha(target),"manifest_sha256":data.sha(folder/"manifest.json")}
    data.dump(data.CASE/"snapshot.lock.json",lock)
    (args.output_dir/"SHA256SUMS").write_text("".join(f"{entry['sha256']}  {city}-sumo-20261110.zip\n" for city,entry in lock.items()),encoding="utf-8",newline="\n")
    print(json.dumps(lock,indent=2))


if __name__=="__main__":main()
