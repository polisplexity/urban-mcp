# Historical vegetation and aggregate population in Helsinki and Amsterdam

Development branch for municipal case #35. Public inputs have been harvested and prepared in both cities. Native/protocol/host admission remains pending until its evidence is committed; this initial recipe and snapshot publication do not claim completed runtime or host verification.

The case reuses JordanGunn/gdal-mcp at `418f401c7987e388eaaee6ad13289798a1ff69b6` (MIT), Rasterio/GDAL/GeoPandas and its FastMCP 2.12.3 interface. It adds city harvesting/binding, explicit categorical zonal accounting, population reconciliation, threshold sensitivity, artifact reading and map rendering. See `recipe.json`, the pinned Docker runtime and the versioned blind task.

WorldCover v200 describes 2021. Vegetation includes cropland. The local 10 m nearest-neighbour analysis grid does not increase source resolution. Water and NoData are reported separately; class-code means are not a physical vegetation measure. Population belongs to 2025 administrative zones, not pixels; a flagged zone does not establish lack of park access, heat exposure, current canopy or causality. Helsinki and Amsterdam have different population dates and statistical reconciliation limits.

Data: ESA WorldCover / CC BY 4.0; Helsinki Service Map and population / CC BY 4.0; CBS Wijken en Buurten 2025 via PDOK / CC0. Exact rights/attribution, requests, sizes and hashes are included in the source manifests and pinned snapshots. Code licensing does not replace source terms.

Final-product qualification remains pending under `docs/product-qualification.md`. These are original-team development observations, not the independent third-city reproduction required for promotion.
