Amsterdam’s historical screening flags **26 of 111 zones below 0.20**, attaching **217,945 published residents**. Exact source IDs and attached populations are:

WK0363AA: 9,145; WK0363AB: 19,485; WK0363AC: 6,505; WK0363AD: 4,345; WK0363AE: 4,760; WK0363AF: 9,940; WK0363AG: 5,710; WK0363AH: 7,570; WK0363BB: 1,765; WK0363EC: 5,475; WK0363EH: 12,945; WK0363EM: 10,045; WK0363EP: 6,250; WK0363EQ: 4,710; WK0363ES: 6,910; WK0363ET: 7,675; WK0363EU: 7,400; WK0363KF: 12,550; WK0363MA: 20,760; WK0363ME: 10,000; WK0363MF: 12,045; WK0363MJ: 16,090; WK0363MK: 1,535; WK0363NB: 12,010; WK0363NM: 1,910; WK0363NP: 410.

**Below 0.40**, all 26 remain and these 39 enter, adding **340,020 known residents**, for **557,965 across 65 zones**:

WK036399: unknown; WK0363AJ: 8,005; WK0363AK: 15,525; WK0363BA: 30; WK0363ED: 11,785; WK0363EE: 19,130; WK0363EG: 2,330; WK0363EJ: 8,195; WK0363EK: 8,220; WK0363EL: 6,560; WK0363EN: 5,945; WK0363ER: 6,730; WK0363EV: 1,825; WK0363FC: 10,370; WK0363FG: 14,450; WK0363FH: 6,145; WK0363FK: 18,625; WK0363FN: 11,755; WK0363KA: 11,585; WK0363KB: 3,745; WK0363KD: 12,565; WK0363KE: 15,000; WK0363KG: 7,810; WK0363KH: 11,665; WK0363KJ: 8,640; WK0363KK: 15,125; WK0363KL: 5,200; WK0363KP: 4,835; WK0363MB: 5,820; WK0363MC: 10,560; WK0363MD: 8,745; WK0363ML: 8,485; WK0363NC: 12,545; WK0363NK: 9,470; WK0363NN: 3,420; WK0363SC: 8,035; WK0363SD: 5,740; WK0363TE: 7,775; WK0363TH: 7,630.

Both thresholds use strict inequality; equality is excluded. This is sensitivity on identical observations, not temporal change. Both complete 111-row CSVs and all 1,332 class-count rows were read through null `next_offset`. Every fraction, flag, ID list and population sum reconciled.

Sources are ESA WorldCover 2021 v200, asset `ESA_WorldCover_10m_2021_v200_N51E003_Map.tif` (CC-BY-4.0; © ESA WorldCover project 2021 / Contains modified Copernicus Sentinel data (2021) processed by ESA WorldCover consortium), and CBS Wijken en Buurten 2025 via PDOK (CC0-1.0). The hash-verified snapshot was acquired 2026-11-10. Population represents 2025-01-01; the 2025 boundaries and population differ temporally from 2021 land cover.

Nearest resampling produced the declared 10 m EPSG:28992 grid, with zero overlapping assigned pixel centres. Vegetation includes tree, shrub, grass, cropland, herbaceous wetland, mangrove and moss/lichen classes. Zone-assigned vegetation totals **1,084,317/1,968,573 valid non-water pixels (55.08%)**, versus **1,084,317/2,436,583 valid all-surface pixels (44.50%)**. Water contributes 468,010 pixels; NoData contributes zero. Cells represent 100 m²; boundary rasterization remains approximate. Mapped tree-class area is **46.2433 km²**, not canopy percentage. InputQuality was not acquired; NoData coverage supplies no classification-confidence estimate.

No zone lacks valid land or is entirely mapped water. WK036399 has 16,297 land pixels and fraction **4,247/16,297 = 0.26060011**. Its population remains unknown and is excluded from the 0.40 population sum. Known zone population totals **934,515**, versus municipal **934,526**, a **+11** difference. District counts are randomly rounded to multiples of five; missing counts remain null.

Codex exercised all 21 tools. Derivatives stayed in the baseline directory. Buffers are geometric inspections, raster queries extract bounding windows, class-code means have no physical vegetation meaning, and EPSG:3857 serves display only. Unknown-city, invalid-threshold, unsafe-ID/path, degree-buffer and categorical-interpolation tests were rejected. Case, manifest and quality resources were retrieved. Host prompt retrieval was unavailable; preflight rejections and manually authored justification recoveries remain recorded. The map receipt reports 291,736 bytes, SHA-256 `84c5e22dbce61f377c24b4ba255b03ed31b3261dbc1adb44046f76d4b0b048e4`.

A bounded municipal next step is reviewing WK0363AD and WK0363AE against dated aerial imagery, field observations, ownership and planting constraints before selecting a pilot. Validate classifications, shorelines, boundaries and updated population locally. These results establish neither park access, current vegetation, NDVI, temperature, individual heat exposure, causality nor a validated city ranking. Product qualification remains pending.

```json
{
  "city": "amsterdam",
  "landcover_year": 2021,
  "population_date": "2025-01-01",
  "zone_count": 111,
  "low_zone_ids_at_020": [
    "WK0363AA", "WK0363AB", "WK0363AC", "WK0363AD", "WK0363AE",
    "WK0363AF", "WK0363AG", "WK0363AH", "WK0363BB", "WK0363EC",
    "WK0363EH", "WK0363EM", "WK0363EP", "WK0363EQ", "WK0363ES",
    "WK0363ET", "WK0363EU", "WK0363KF", "WK0363MA", "WK0363ME",
    "WK0363MF", "WK0363MJ", "WK0363MK", "WK0363NB", "WK0363NM",
    "WK0363NP"
  ],
  "low_zone_ids_at_040": [
    "WK036399", "WK0363AA", "WK0363AB", "WK0363AC", "WK0363AD",
    "WK0363AE", "WK0363AF", "WK0363AG", "WK0363AH", "WK0363AJ",
    "WK0363AK", "WK0363BA", "WK0363BB", "WK0363EC", "WK0363ED",
    "WK0363EE", "WK0363EG", "WK0363EH", "WK0363EJ", "WK0363EK",
    "WK0363EL", "WK0363EM", "WK0363EN", "WK0363EP", "WK0363EQ",
    "WK0363ER", "WK0363ES", "WK0363ET", "WK0363EU", "WK0363EV",
    "WK0363FC", "WK0363FG", "WK0363FH", "WK0363FK", "WK0363FN",
    "WK0363KA", "WK0363KB", "WK0363KD", "WK0363KE", "WK0363KF",
    "WK0363KG", "WK0363KH", "WK0363KJ", "WK0363KK", "WK0363KL",
    "WK0363KP", "WK0363MA", "WK0363MB", "WK0363MC", "WK0363MD",
    "WK0363ME", "WK0363MF", "WK0363MJ", "WK0363MK", "WK0363ML",
    "WK0363NB", "WK0363NC", "WK0363NK", "WK0363NM", "WK0363NN",
    "WK0363NP", "WK0363SC", "WK0363SD", "WK0363TE", "WK0363TH"
  ],
  "population_in_low_zones_at_020": 217945,
  "population_in_low_zones_at_040": 557965,
  "no_valid_land_zone_ids": [],
  "unknown_population_zone_ids": [
    "WK036399"
  ],
  "municipal_minus_zone_population": 11,
  "newly_below_threshold_zone_ids": [
    "WK036399", "WK0363AJ", "WK0363AK", "WK0363BA", "WK0363ED",
    "WK0363EE", "WK0363EG", "WK0363EJ", "WK0363EK", "WK0363EL",
    "WK0363EN", "WK0363ER", "WK0363EV", "WK0363FC", "WK0363FG",
    "WK0363FH", "WK0363FK", "WK0363FN", "WK0363KA", "WK0363KB",
    "WK0363KD", "WK0363KE", "WK0363KG", "WK0363KH", "WK0363KJ",
    "WK0363KK", "WK0363KL", "WK0363KP", "WK0363MB", "WK0363MC",
    "WK0363MD", "WK0363ML", "WK0363NC", "WK0363NK", "WK0363NN",
    "WK0363SC", "WK0363SD", "WK0363TE", "WK0363TH"
  ],
  "no_longer_below_threshold_zone_ids": []
}
```