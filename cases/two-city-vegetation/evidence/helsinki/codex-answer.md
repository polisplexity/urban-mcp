Using only the vegetation MCP, codex restored the public Helsinki snapshot and verified its inputs. The evidence combines ESA WorldCover **2021 v200** Map tiles N57E024/N60E024 with Helsinki Service Map boundaries and Aluesarjat population dated **2025-12-31**. The snapshot was acquired on 2026-11-10. Sources carry CC-BY-4.0 attribution to ESA WorldCover and City of Helsinki Urban Research and Statistics / Statistics Finland.

At the strict **land-share < 0.20** threshold, two zones qualify: **101 Vironniemi and 301 Kallio**, with **51,906 attached residents**. Raising the exploratory threshold to **0.40** produces six zones and **144,068 attached residents**:

| Source ID | Zone | Vegetation land-share | Population |
|---|---|---:|---:|
| 101 | Vironniemi | 18.58% | 13,280 |
| 103 | Kampinmalmi | 21.20% | 46,874 |
| 301 | Kallio | 14.35% | 38,626 |
| 302 | Alppiharju | 32.19% | 11,463 |
| 303 | Vallila | 27.47% | 16,643 |
| 304 | Pasila | 29.85% | 17,182 |

IDs **103, 302, 303 and 304** newly qualify; none leave. This is threshold sensitivity on identical historical observations. Displayed percentages are rounded; every flag was checked using the unrounded fraction.

Both complete zone CSVs and all **408 baseline class-count records** were read through terminal pages with `next_offset: null`. Across the 34 represented zones, there are **2,147,273 valid land pixels**, **5,003,110 water pixels**, and **zero NoData pixels**. All zones have valid land and are eligible. Vegetation occupies **65.48% of valid land**, or **19.66% of all valid surface**, including water in that denominator. Vegetation includes cropland and other declared vegetation classes. Mapped tree-class area is **117.4097 km²**; this does not measure fractional canopy percentage.

No zone population is missing. Missing values would remain null. The Helsinki recipe declares no rounding rule, so no rounding correction was applied. Zone population totals **680,710**, leaving **13,682** relative to the municipal **694,392**; that difference remains unresolved.

All 21 advertised tools were exercised. Inspection derivatives include metric reprojection, a 100 m geometric buffer, bounded vector clip/query, 20 m simplification, categorical COG with nearest overviews `[2,4]`, a raster window, and nearest EPSG:3857 display reprojection. Numeric class-code statistics carry no physical vegetation interpretation; raster queries extract bounding windows. All requested negative tests were rejected, including the partially outside raster rectangle. The baseline PNG receipt matched: **190,912 bytes**.

Case, manifest and quality resources were retrieved. **Host gap:** codex exposed no prompt-invocation API, preventing municipal workflow prompt inspection. Server-requested scientific justifications were explicitly authored, stored and successfully retried.

A bounded next municipal action is a local review of candidate planting opportunities in zones 101 and 301. Before selecting sites, validate current conditions, classification accuracy, boundaries, ownership, utilities and planting feasibility. The 2021 land cover, 2025 population and acquisition-date boundaries differ temporally. These results establish neither park access, current vegetation, NDVI, temperature, individual heat exposure, causality nor a validated city ranking. Product qualification remains pending.

```json
{
  "city": "helsinki",
  "landcover_year": 2021,
  "population_date": "2025-12-31",
  "zone_count": 34,
  "low_zone_ids_at_020": ["101", "301"],
  "low_zone_ids_at_040": ["101", "103", "301", "302", "303", "304"],
  "population_in_low_zones_at_020": 51906,
  "population_in_low_zones_at_040": 144068,
  "no_valid_land_zone_ids": [],
  "unknown_population_zone_ids": [],
  "municipal_minus_zone_population": 13682,
  "newly_below_threshold_zone_ids": ["103", "302", "303", "304"],
  "no_longer_below_threshold_zone_ids": []
}
```