Helsinki’s strict **0.20 land-share threshold** flags **101 Vironniemi** and **301 Kallio**, with **51,906 published residents** attached to those zones.

| Zone ID and name | Vegetation / valid-land pixels | Land share | Population | Low at |
|---|---:|---:|---:|---|
| 101 Vironniemi | 3,794 / 20,425 | 18.5753% | 13,280 | Both thresholds |
| 301 Kallio | 3,858 / 26,876 | 14.3548% | 38,626 | Both thresholds |
| 103 Kampinmalmi | 9,161 / 43,218 | 21.1972% | 46,874 | 0.40 |
| 302 Alppiharju | 2,929 / 9,100 | 32.1868% | 11,463 | 0.40 |
| 303 Vallila | 7,172 / 26,109 | 27.4695% | 16,643 | 0.40 |
| 304 Pasila | 13,109 / 43,922 | 29.8461% | 17,182 | 0.40 |

At **0.40**, six zones are flagged, carrying **144,068 residents**. Four zones enter and none leave. The additional attached population is 92,162. This is threshold sensitivity using identical observations.

Both complete zone CSVs and all 408 class-count rows per run were read through `next_offset: null`. Every flag matched the unrounded vegetation-pixel/valid-land-pixel fraction using strict `<`; equality would not qualify.

Across the **34 analyzed zones**, vegetation occupies 1,405,954 of 2,147,273 valid land pixels: **65.48%**. Including permanent water gives **19.66%** of 7,150,383 valid surface pixels. Water accounts for 5,003,110 pixels; zone-assigned NoData is zero. No zones are water-only or missing population. Whole-grid raster statistics include pixels outside these zones and therefore have different totals.

Zone populations sum to **680,710**, versus the municipal **694,392**: an unresolved difference of **13,682**. No Helsinki rounding rule was exposed; published integers were retained without adjustment.

Evidence uses **ESA WorldCover 2021 v200**, tiles N57E024 and N60E024, Helsinki Service Map boundaries, and City of Helsinki Urban Research and Statistics / Statistics Finland population dated **2025-12-31**. All carry the declared **CC-BY-4.0** rights. Snapshot acquisition dates are November 10, 2026. Hash verification passed; preparation used nearest resampling into a 10 m EPSG:3067 grid with zero overlapping assigned centres. This grid does not improve source resolution.

Vegetation includes cropland and wetlands. Mapped tree-class area is approximately **117.41 km²**, which is not fractional canopy percentage. The historical land cover, later population and acquisition-date boundaries are temporally mismatched. Local classification accuracy remains unvalidated; InputQuality was not acquired.

Codex exercised all 21 advertised tools. Requested derivatives succeeded under `/data/results/helsinki/agent-baseline/`, including nearest COG overviews `[2,4]` and EPSG:3857 display reprojection. Buffers and simplification are geometric inspections. Raster queries extract bounding windows; numeric class-code means have no physical vegetation meaning.

All six invalid-input checks were rejected. Preflight and catalog URI failures remain in the trace; stored scientific justifications and encoded resource paths enabled recovery. Case, manifest and quality resources were retrieved. Codex exposes no MCP prompt interface, so the municipal workflow prompt could not be retrieved.

The baseline map receipt reports **190,912 bytes**, SHA-256 `1a050047e7bcf329c4c730d872599bf828a50a9c1647df794eb2244e382186cb`.

A bounded next action is a local vegetation and planting-feasibility review in zones 101 and 301, checking recent imagery, field conditions, ownership, utilities, boundary vintages and population reconciliation before investment. Product qualification remains pending.

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