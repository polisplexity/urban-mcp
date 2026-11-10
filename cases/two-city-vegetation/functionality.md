# Operation-by-operation admission

Original tools retain the pinned upstream numerical implementation, subject to profile guards. New municipal tools join that same FastMCP server. Public Rasterio/GDAL/GeoPandas APIs perform analysis; there is no agent framework in the backend. Every row is exercised in both deterministic city suites. Host tool attempts, completed results and prose verdicts remain separate in [the dossier](evidence/README.md).

| Tool | Reused or built | Verified bounded behavior |
| --- | --- | --- |
| `vector_info` | Original | Zone schema/CRS, counts and bounds |
| `vector_convert` | Original | GeoJSON/GPKG geometry and IDs; equivalent polygon/multipolygon topology accepted |
| `vector_reproject` | Original | Metric/geographic transform and geometry equivalence with justified CRS |
| `vector_buffer` | Original + guard | 100 m geometric buffer; degrees refused; no access interpretation |
| `vector_clip` | Original | Bounded intersection/IDs against native |
| `vector_query` | Original | Attribute/spatial selection against native |
| `vector_simplify` | Original + guards | 20 m Douglas–Peucker; Visvalingam alias and degrees refused |
| `raster_info` | Original | CRS/grid/domain/NoData |
| `raster_stats` | Original | Numeric statistics against native; category mean is not vegetation |
| `raster_convert` | Original + guard | COG, nearest overviews `[2,4]`, preserved base pixels/CRS |
| `raster_query` | Original + guard | Inside-source window pixels/transform; no polygon-mask claim; partial extents refused |
| `raster_reproject` | Original + guards | Nearest display reprojection to EPSG:3857, valid classes and explicit NoData border; unsupported dimensions/bounds and continuous interpolation refused |
| `store_justification` | Original | Reflection-gated rationale storage/reuse; not scientific endorsement |
| `vegetation_status` | Built | Empty-workspace discovery, recipe/cities/input integrity/qualification |
| `harvest_vegetation_data` | Built | Live sources or size/hash-locked snapshot; exact rights/provenance and input protection |
| `prepare_vegetation_data` | Built | Native-grid crops → nearest local grid → centre-based zone labels; overlap/unknown-code rejection; method/data hashes |
| `vegetation_class_catalog` | Built | All 11 codes, explicit vegetation including cropland, tree-class meaning and denominators |
| `analyze_vegetation` | Built | Every zone's class counts, land/all-surface shares, strict flags, missing population and reconciliation; bounded response plus full artifacts |
| `vegetation_compare` | Built | Same city/data/method with 0.20/0.40 thresholds: exact newly/no-longer-low IDs; changed observations refused |
| `read_vegetation_artifact` | Built | Allowlist, SHA/bytes and ≤12,000-character pages; reconstructed full summaries equal native; unsafe paths refused |
| `render_vegetation_map` | Built | Actual classes/zone outlines/lowest shares with attribution; native/MCP PNG equality; receipt does not claim agent visual inspection |

Vegetation adds resource `vegetation://case`, templates `vegetation://{city}/manifest` and `vegetation://{city}/quality`, and prompt `municipal_vegetation_review`. The deterministic suite also fetches original catalog, per-file metadata, format/CRS/compression/glossary/resampling resource families and all original justification prompts. Schemas and named checks are in each city's `mcp-tools.json`, `mcp-resources.json`, `mcp-prompts.json`, `mcp.json`. Host discovery helpers vary; they are not part of the 21 numerical/case tools.

The production path rasterizes labels once and counts by label/class. The oracle independently opens polygon windows, masks geometry and uses `numpy.unique`. Every integer count and strict flag must match. Tests cover full native/MCP equality, paged CSVs, unchanged class counts under sensitivity, exact v1 numerical bytes and population joins. Synthetic tests cover all-water/empty zones absent from these observations. The source `water_zone` flag is not an eligibility rule: even Groot water has mapped land and becomes low at 0.40 with unknown population.

Not admitted: arbitrary new cities/options/formats, all upstream algorithms, remote multi-user deployment, local classification accuracy, current canopy, NDVI, thermal modeling, accessibility, resident pixel locations or autonomous municipal decisions. [Independent-person qualification](../../docs/product-qualification.md) remains pending.
