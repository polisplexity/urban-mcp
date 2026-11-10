All expected rejections now captured cleanly:

1. Unknown city -> "Unknown city; inspect vegetation_status for configured cases" [PASS]
2. threshold=1.5 -> "threshold must be a finite fraction in 0..1" [PASS]
3. threshold=-0.1 -> "threshold must be a finite fraction in 0..1" [PASS]
4. Unsafe artifact name "../../etc/passwd" -> "Artifact name is not allowed" [PASS]
5. Unsafe run_id "../../etc/shadow" -> "run_id must be 1-48 letters, digits, underscores or hyphens" [PASS]
6. Geographic-degree buffer (distance=0.001 on EPSG:4326 source) -> "This municipal profile requires a projected CRS in metres; degrees are not metres" [PASS]
7. Bilinear interpolation of categorical data -> "Categorical land-cover classes require nearest or mode; continuous interpolation invents class values" [PASS]
8. Out-of-bounds raster query -> "Raster query extent must stay fully within source bounds..." [PASS]

Host gap to report: The `municipal_vegetation_review` prompt is exposed by list_prompts and was retrieved successfully, providing detailed workflow guidance for Helsinki. This is correctly available.

Now I have all data needed. Let me verify the threshold checks against actual fractions from the CSV data:

Threshold checks (strict less-than, not equality):
- Zone 101 (Vironniemi): vegetation_share_of_valid_land=0.18575 < 0.20 -> low=True [CORRECT]
- Zone 301 (Kallio): vegetation_share_of_valid_land=0.14355 < 0.20 -> low=True [CORRECT]
- Zone 103 (Kampinmalmi): vegetation_share_of_valid_land=0.21197 >= 0.20 -> low=False at 0.20, True at 0.40 [CORRECT]
- Zone 302 (Alppiharju): vegetation_share_of_valid_land=0.32187 >= 0.20 -> False at 0.20; 0.32187 < 0.40 -> True at 0.40 [CORRECT]
- Zone 303 (Vallila): vegetation_share_of_valid_land=0.27469 >= 0.20 -> False at 0.20; 0.27469 < 0.40 -> True at 0.40 [CORRECT]
- Zone 304 (Pasila): vegetation_share_of_valid_land=0.29846 >= 0.20 -> False at 0.20; 0.29846 < 0.40 -> True at 0.40 [CORRECT]

Water zone check: All zones show water_zone=False in the CSV. Zones 101, 102, 601, 603, 603, 704 etc. have large water_pixels but water_zone=False - the source label water_zone=False does not prove zero valid-land pixels. The denominator correctly uses valid_land_pixels (excluding class 80 and NoData). Zone 603 (Laajasalo) is a good example: water_zone=False, water_pixels=3306360, valid_land_pixels=168888, vegetation_share_of_valid_land=0.829 - correctly not flagged as low.

Now I have everything needed to write the municipal brief and produce the final JSON:

---

MUNICIPAL BRIEF: Helsinki Vegetation Land-Share Screening, 2021 WorldCover

Source and method: ESA WorldCover 2021 v200 (CC-BY-4.0), nearest-neighbour warped to a 10 m local metric grid in EPSG:3067. Vegetation classes are codes 10 (tree cover), 20 (shrubland), 30 (grassland), 40 (cropland), 90 (herbaceous wetland), 95 (mangroves) and 100 (moss/lichen). Class 80 (permanent water) and NoData (0) are excluded from the land-share denominator. Zones: 34 Helsinki administrative districts. Population source: City of Helsinki / Statistics Finland, reference date 2025-12-31. The analysis raster is from 2021; zone boundaries and population are from 2025 acquisition; temporal mismatch of four years is inherent and cannot be resolved without updated land-cover data.

Denominator note: The land-share fraction (vegetation_share_of_valid_land) counts vegetation pixels over valid non-water land pixels. Helsinki has extremely large water coverage: pooled across all zones, 5003110 of 7150383 total pixels (70%) are permanent water (class 80); the city-wide valid land pixel count is only 2147273. Zones like Laajasalo (603), Ullanlinna (102), and Vuosaari (704) contain very large water extents but are labelled water_zone=False - that label does not exclude them from analysis; their valid_land_pixels are positive and their land-share fractions are computed correctly over those land pixels.

Low-share zones at threshold 0.20 (exploratory, not a policy standard; strict less-than):
- Zone 101 (Vironniemi): vegetation_share_of_valid_land=0.1858 (19 of 20425 valid land pixels are vegetation; large water area of 19868 pixels excluded from denominator); population 13280 (rounded).
- Zone 301 (Kallio): vegetation_share_of_valid_land=0.1435 (3858 vegetation pixels of 26876 valid land pixels); population 38626 (rounded).
Combined attached population at 0.20 threshold: 51906.

Threshold sensitivity (same 2021 raster, not vegetation change over time): raising to 0.40 adds zones 103 (Kampinmalmi, 0.212), 302 (Alppiharju, 0.322), 303 (Vallila, 0.275) and 304 (Pasila, 0.299). Combined attached population at 0.40: 144068. The four newly-flagged zones are all above 0.20, so they are not low at the exploratory threshold.

What the tree-class share measures: Tree cover pixels (class 10) are 1174097 of 2147273 valid land pixels across all zones - a city-wide tree-class share of 0.547. This measures the proportion of the 10 m analysis grid assigned to the tree-cover category in the 2021 WorldCover model. It is not fractional canopy cover, is not a current field measurement, and is not validated locally. Zone 101 has tree_class_share_of_valid_land=0.137, zone 301 has 0.132.

Population reconciliation: Municipal register total 694392; zone sum 680710; difference 13682 (1.97%). No zones have missing (null) population. Helsinki's figures are not randomly rounded (unlike Amsterdam's CBS data). The 13682 gap may reflect population residing in unassigned boundaries, institutional quarters, or rounding in the municipal source.

No zones have zero valid land pixels; no zones have missing population.

Bounded possible next action: Before any municipal intervention is considered, local field validation is required to confirm whether the mapped tree-class deficit in zones 101 and 301 reflects genuine land conditions in 2026 versus 2021 WorldCover classification uncertainty, misclassification of impervious surfaces, or changed land use since acquisition. A planting or greening study should use updated, locally validated land-cover data aligned with current zone boundaries. The 2021 WorldCover global accuracy is not per-zone local validation.

The analysis does not indicate park access deficits, current vegetation coverage, NDVI, air temperature, individual heat exposure or any causal relationship between low mapped land-share and resident wellbeing.

---

Now the final JSON:

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
