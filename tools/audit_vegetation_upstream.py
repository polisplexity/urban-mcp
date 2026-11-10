"""Execute two suspected upstream reprojection defects on a synthetic raster."""
import argparse
import asyncio
import hashlib
import json
from pathlib import Path
import tempfile

import numpy as np
import rasterio
from rasterio.transform import from_origin

from src.shared.raster.reproject import Params
from src.tools.raster.reproject import _reproject


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
        return {"upstream": "JordanGunn/gdal-mcp", "commit": "418f401c7987e388eaaee6ad13289798a1ff69b6", "license": "MIT", "fixture": "Synthetic 100x100 EPSG:3067 raster, 10 m pixels, class 50; not municipal evidence", "source_sha256": hashlib.sha256(Path("/opt/gdal-mcp/src/tools/raster/reproject.py").read_bytes()).hexdigest(), "explicit_dimensions_change_footprint": dimensions, "bounds_ignored": bounds, "profile_response": "Vegetation profile rejects explicit bounds/width/height; uses resolution and categorical nearest/mode. Original numerical code remains unchanged."}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = asyncio.run(audit())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8", newline="\n")
    print(json.dumps(result, indent=2))
