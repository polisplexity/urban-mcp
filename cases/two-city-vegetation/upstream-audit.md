# Executable source review

Reviewed original code: [JordanGunn/gdal-mcp at 418f401](https://github.com/JordanGunn/gdal-mcp/tree/418f401c7987e388eaaee6ad13289798a1ff69b6), MIT. The Dockerfile verifies the archive SHA, installs its API and reuses the original FastMCP 2.12.3 server, path validation, justification middleware, 13 tools and resources/prompts. Rasterio 1.4.3/GDAL reads, warps and windows rasters; GeoPandas/Pyogrio/PROJ handle vectors. The four existing [compatibility patches](../../adapters/municipal_inventory/apply_compat.py) are retained for installed and original-test source. Numerical algorithms are not replaced under original tool names.

Original raster statistics summarize numeric values. They do not define vegetation classes, a non-water denominator, administrative zone membership, population joins or a municipal comparison. `raster_query` extracts a bounding window, not polygon-masked zonal statistics. These missing municipal operations are the new Python module, separate tools and explicit recipe. Python keeps arrays, GeoPandas and existing FastMCP in one process; there is no numerical rewrite in Go or agent-specific backend.

## Defects reproduced from source

[Executable audit](../../tools/audit_vegetation_upstream.py), [observed output/source hashes](evidence/upstream-audit.json). Fixture: synthetic 100 × 100 cells of class 50 at 10 m in EPSG:3067 plus a metric line. This is not municipal evidence.

| Original source/option | Observed failure | Profile behavior |
| --- | --- | --- |
| `tools/raster/reproject.py`: explicit dimensions | 20 × 20 retains 10 m transform, shrinking the original 1 km footprint to 200 m | Reject explicit width/height; use resolution |
| Same: explicit bounds | Requested crop bounds ignored; output retains original extent | Reject explicit bounds |
| `tools/raster/query.py`: partially outside source | Data clips to 5 × 5 but retains an unclipped transform; expected `[380000,6669950,380050,6670000]`, observed `[379950,6670000,380000,6670050]` | Reject outside/partial extents; admit inside-source windows |
| `shared/vector/simplify.py`: Visvalingam label | Branch calls Shapely's same Douglas–Peucker implementation; fixture outputs identical | Reject that label; admit explicit Douglas–Peucker |

Scientific guards also require nearest/mode resampling and categorical overviews, and metre-based projected CRS for buffer/simplify. Numeric class-code means are inspection metadata, not vegetation indices. Guards run before original reflection middleware; admitted calls still pass original path/justification checks. An early appended guard could be preempted by justification requests; its correction is preserved in [development failures](evidence/development-failures.json).

The two-city native/stdio suite exercises all 21 tools and every resource/prompt family, independently compares every zone/class and tests these rejections. The original 69 tests pass with `GDAL_MCP_WORKSPACES` unset, their expected empty-workspace environment. Twelve synthetic regressions cover semantic edge cases and snapshot integrity. This does not admit all GDAL/Rasterio functionality, arbitrary inputs, HTTP transport or local classification accuracy. [Operation coverage](functionality.md).
