"""Plot original model geometry and native report rows, never flood extents."""
import argparse
import csv
import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.lines import Line2D

from urban_mcp_swmm.engine import sections


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--city',required=True);p.add_argument('--workspace',type=Path,default=Path('/data'));p.add_argument('--evidence',type=Path,required=True);a=p.parse_args()
    source=a.workspace/'sources'/a.city/'model.inp';s=sections(source.read_text(encoding='utf-8-sig'))
    quality=json.loads((a.evidence/'quality.json').read_text());xy={r[0]:(float(r[1]),float(r[2])) for r in s['COORDINATES']}
    vertices={}
    for r in s.get('VERTICES',[]):vertices.setdefault(r[0],[]).append((float(r[1]),float(r[2])))
    edges={r[0]:r for section in ['CONDUITS','PUMPS','ORIFICES','WEIRS','OUTLETS'] for r in s.get(section,[])}
    lines=[];missing=[]
    for key,r in edges.items():
        if r[1] not in xy or r[2] not in xy:missing.append(key);continue
        lines.append([xy[r[1]],*vertices.get(key,[]),xy[r[2]]])
    fig,axes=plt.subplots(1,2,figsize=(14,7),layout='constrained',facecolor='#f5f2e8')
    target=quality['target']['conduit_id'];edge=edges[target]
    for axis,scenario,title in zip(axes,['baseline','capacity75'],['Original effective diameter','Hypothetical diameter × 0.75'],strict=True):
        rows=list(csv.DictReader((a.evidence/(scenario+'-nodes.csv')).open()));high=[];low=[]
        axis.set_facecolor('#f5f2e8');axis.add_collection(LineCollection(lines,colors='#a4afae',linewidths=.5,zorder=1))
        for row in rows:
            if row['node_id'] not in xy:continue
            if float(row['flood_volume_m3'])>=10:high.append(row)
            elif row['listed_flooding']=='True':low.append(row)
        if low:axis.scatter(*zip(*(xy[r['node_id']] for r in low)),s=20,color='#237f9d',zorder=3)
        if high:
            axis.scatter(*zip(*(xy[r['node_id']] for r in high)),s=50,color='#b24631',zorder=4)
            for i,r in enumerate(high):
                axis.annotate(r['node_id']+'\n'+r['flood_volume_m3']+' m³',xy[r['node_id']],xytext=(20,30 if i%2==0 else -36),textcoords='offset points',fontsize=8,color='#7f291e',arrowprops={'arrowstyle':'-','color':'#7f291e','lw':.6})
        points=[xy[edge[1]],*vertices.get(target,[]),xy[edge[2]]]
        axis.plot(*zip(*points),color='#dc921e',linewidth=3,zorder=5)
        axis.scatter(*xy[edge[1]],s=120,facecolor='none',edgecolor='#dc921e',linewidth=1.4,zorder=6)
        axis.autoscale();axis.set_aspect('equal');axis.set_title(title+'\n'+str(len(high))+' nodes ≥10 m³; '+str(len(low))+' other listed rows',fontsize=11,loc='left')
        axis.set_xlabel('Original model X');axis.set_ylabel('Original model Y');axis.ticklabel_format(style='plain',useOffset=False)
        axis.spines[['top','right']].set_visible(False)
    handles=[Line2D([],[],color='#b24631',marker='o',linestyle='',label='Reported overflow ≥10 m³'),Line2D([],[],color='#237f9d',marker='o',linestyle='',label='Other listed overflow row (may round to zero)'),Line2D([],[],color='#dc921e',linewidth=3,label='Source-selected conduit')]
    axes[0].legend(handles=handles,loc='lower left',fontsize=7,framealpha=.9)
    name='Bellinge / Odense' if a.city=='odense' else 'Tuindorp development / Utrecht'
    fig.suptitle(name+' — historical model experiment\n'+quality['event']['start_local'][:10]+' to '+quality['event']['end_local'][:10]+'; original model coordinates, no CRS inferred',fontsize=14,x=.02,ha='left')
    fig.supxlabel('Native reported node overflow, not 2D inundation or current condition. Regional hourly rain; no new calibration. Model data CC BY 4.0.',fontsize=9)
    output=a.evidence/'model-overflow.png';fig.savefig(output,dpi=150,metadata={'Software':'Urban MCP / Matplotlib'});plt.close(fig)
    receipt={'city':a.city,'sha256':hashlib.sha256(output.read_bytes()).hexdigest(),'bytes':output.stat().st_size,
        'source_model_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'coordinate_nodes':len(xy),'drawn_links':len(lines),'links_missing_endpoint_coordinates':missing,
        'inputs':{name:hashlib.sha256((a.evidence/name).read_bytes()).hexdigest() for name in ['baseline-nodes.csv','capacity75-nodes.csv','quality.json']},
        'meaning':'Original model geometry and native rounded overflow rows; no flood polygon, geographic CRS or field validation inferred.'}
    (a.evidence/'map-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({'city':a.city,'output':str(output),'bytes':receipt['bytes']}))


if __name__=='__main__':main()
