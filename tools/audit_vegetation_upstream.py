"""Execute two suspected upstream reprojection defects on a synthetic raster."""
import argparse
import asyncio
import hashlib
import json
from pathlib import Path
import tempfile

import numpy as np
import geopandas as gpd
import rasterio
from rasterio.transform import from_origin
from shapely.geometry import LineString

from src.shared.raster.reproject import Params
from src.tools.raster.reproject import _reproject
from src.shared.vector.simplify import simplify
from src.tools.raster.query import raster_query


async def audit():
    with tempfile.TemporaryDirectory() as temp:
        folder = Path(temp)
        source = folder/"fixture.tif"
        with rasterio.open(source, "w", driver="GTiff", width=100, height=100, count=1, dtype="uint8", crs="EPSG:3067", transform=from_origin(380000, 6670000, 10, 10), nodata=0) as dst:
            dst.write(np.full((100,100), 50, dtype="uint8"), 1)
        original_bounds = [380000, 6669000, 381000, 6670000]
        output = folder/"dimensions.tif"
        await _reproject(str(source), str(output), Params(dst_crs="EPSG:3067", resampling="nearest", width=20, height=20))
        with rasterio.open(output) as result:
            dimensions = {"requested_width_height": [20,20], "expected_preserved_extent": original_bounds, "observed_bounds": list(result.bounds), "observed_resolution": list(result.res)}
        output2 = folder/"bounds.tif"
        requested_bounds = [380100, 6669100, 380900, 6669900]
        await _reproject(str(source), str(output2), Params(dst_crs="EPSG:3067", resampling="nearest", bounds=requested_bounds))
        with rasterio.open(output2) as result:
            bounds = {"requested_bounds": requested_bounds, "observed_bounds": list(result.bounds)}
        assert dimensions["observed_bounds"] != original_bounds
        assert bounds["observed_bounds"] != requested_bounds
        line = folder/"line.gpkg"
        gpd.GeoDataFrame({"id":[1]},geometry=[LineString([(380000,6670000),(380010,6670001),(380020,6670020),(380030,6670001),(380040,6670000)])],crs=3067).to_file(line,driver="GPKG")
        simplify(str(line),folder/"dp.gpkg",5,method="douglas-peucker")
        simplify(str(line),folder/"vw.gpkg",5,method="visvalingam")
        equal = bool(gpd.read_file(folder/"dp.gpkg").geometry.geom_equals_exact(gpd.read_file(folder/"vw.gpkg").geometry,1e-9).all())
        assert equal
        query_fn = getattr(raster_query,'fn',raster_query)
        query_bounds = [379950,6669950,380050,6670050]
        await query_fn(str(source),query_bounds,output=str(folder/'partial.tif'))
        with rasterio.open(folder/'partial.tif') as result:
            partial = {'requested_bounds':query_bounds,'expected_clipped_bounds':[380000,6669950,380050,6670000],'observed_bounds':list(result.bounds),'observed_shape':[result.height,result.width]}
        assert partial['observed_bounds'] != partial['expected_clipped_bounds']
        return {"upstream": "JordanGunn/gdal-mcp", "commit": "418f401c7987e388eaaee6ad13289798a1ff69b6", "license": "MIT", "fixture": "Synthetic 100x100 EPSG:3067 raster, 10 m pixels, class 50, plus synthetic metric line; not municipal evidence", "source_sha256": {name:hashlib.sha256(Path('/opt/gdal-mcp/src/'+name).read_bytes()).hexdigest() for name in ['tools/raster/reproject.py','tools/raster/query.py','shared/vector/simplify.py']}, "explicit_dimensions_change_footprint": dimensions, "bounds_ignored": bounds, "partial_window_wrong_transform":partial, "visvalingam_label_aliases_douglas_peucker": {"source_finding":"The advertised visvalingam branch explicitly calls Shapely simplify, the same Douglas-Peucker implementation; it does not implement a true Visvalingam algorithm.","synthetic_outputs_identical":equal}, "profile_response": "Vegetation profile rejects partial/outside raster windows, explicit raster bounds/width/height, continuous categorical interpolation and the Visvalingam label. Uses bounded source windows, resolution, nearest/mode and Douglas-Peucker. Original numerical code remains unchanged."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = asyncio.run(audit())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8", newline="\n")
    print(json.dumps(result, indent=2))
