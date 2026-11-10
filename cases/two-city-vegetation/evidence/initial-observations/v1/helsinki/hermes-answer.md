summary.json fully read (next_offset=null at second page). All data is complete. Now I have everything needed to verify the low-share flags and write the municipal brief.

VERIFICATION OF LOW-SHARE FLAGS (threshold 0.20, rule: strictly less than):
- Zone 101 (Vironniemi): vegetation_share_of_valid_land = 0.1858, 0.1858 < 0.20 = TRUE, flagged=True. CORRECT.
- Zone 301 (Kallio): vegetation_share_of_valid_land = 0.1435, 0.1435 < 0.20 = TRUE, flagged=True. CORRECT.
- Zone 103 (Kampinmalmi): 0.2120 < 0.20 = FALSE, flagged=False. CORRECT (not low at 0.20).
- Zone 302 (Alppiharju): 0.3219 < 0.20 = FALSE, flagged=False. CORRECT.

HOST FEATURE GAP: The server exposes only one resource (vegetation://case). Resources like vegetation://manifest, vegetation://quality are NOT advertised. This is a host feature gap -- those resource URIs were not in list_resources output.

Now I have all evidence. Let me write the municipal brief and final JSON.

---

MUNICIPAL BRIEF: HELSINKI MAPPED VEGETATION AND ZONE POPULATION (2021/2025)

Source and Observation Dates

This analysis is based on ESA WorldCover v200, a modeled land-cover classification derived from 2021 Sentinel satellite data (CC-BY-4.0). It is not a current vegetation inventory, NDVI measure, canopy percentage, park-access metric, temperature indicator, or any other live observation. Zone population figures are published 2025 aggregate counts from City of Helsinki Urban Research and Statistics / Statistics Finland (CC-BY-4.0), dated 2025-12-31. These two datasets are four years apart in time; zone boundaries in the population file may not exactly match the 2021 land-cover observation period. Residents are not located within specific pixels; population attached to a zone is not population lacking green access or exposed to heat stress.

Denominator and Classes

Vegetation share is computed over valid-land pixels only, excluding both permanent water (class 80) and NoData (code 0) from the denominator. Vegetation classes are: Tree cover (10), Shrubland (20), Grassland (30), Cropland (40), Herbaceous wetland (90), Mangroves (95), Moss and lichen (100). The tree-class pixel count is a 2021 WorldCover class-code count, not a fractional canopy cover or lidar canopy percentage. At city scale, 5,003,110 of 7,150,383 total pixels are permanent water, reflecting Helsinki's extensive coastal and island geography; Laajasalo (zone 603) has 3,306,360 water pixels but 82.9% vegetation share of its valid land. All 34 zones have zero NoData pixels and zero missing-population entries.

Population Reconciliation

The sum of published zone populations is 680,710. The municipal register records 694,392 residents. The gap of 13,682 persons is not attributable to any specific zone; it is a known structural difference between municipal totals and district sums, inherent in how population is published, not an error in this analysis.

Low-Share Zones at Threshold 0.20

The analysis flags zones whose vegetation share of valid land is strictly below 0.20. At this threshold, two zones are flagged:

Zone 101 Vironniemi: vegetation share = 18.6% (3,794 vegetation pixels / 20,425 valid-land pixels). Tree-class pixels = 2,799 (13.7% of valid land). Of its 40,293 total pixels, 19,868 are water. Published population = 13,280.

Zone 301 Kallio: vegetation share = 14.4% (3,858 / 26,876). Tree-class pixels = 3,557 (13.2% of valid land). Of its 37,342 total pixels, 10,466 are water. Published population = 38,626.

Combined published population in these two zones = 51,906. This is not a count of residents without vegetation access.

Threshold Sensitivity

Using an exploratory threshold of 0.40 (double the baseline, applied to the same 2021 raster -- this is not evidence of vegetation change over time), four additional zones become flagged: 103 Kampinmalmi (21.2%, pop. 46,874), 302 Alppiharju (32.2%, pop. 11,463), 303 Vallila (27.5%, pop. 16,643), 304 Pasila (29.8%, pop. 17,182). The aggregate attached population rises to 144,068. No zones move from low to not-low when raising the threshold.

The next-ranked zone not flagged at 0.20 is Kampinmalmi at 21.2%, which is 1.2 percentage points above the 20% threshold. Any modest measurement uncertainty in the 10 m classification could move it across that line; the classification accuracy of WorldCover is global and not locally validated.

Bounded Possible Next Municipal Action

A bounded, evidence-grounded next step would be for the City of Helsinki to commission local field verification in zones 101 and 301 -- specifically checking whether the low WorldCover tree-class fraction (around 14% in both zones) reflects genuine absence of tree cover or is an artifact of dense built-up area and narrow streets being misclassified at 10 m resolution. This verification should use current aerial imagery, existing city tree-register data, or lidar canopy models if available. The 2021 WorldCover observation is four years old; actual conditions may differ. Only after field validation can the classification be used to prioritize tree-planting or greening interventions in those zones.

No claim is made here that residents in these zones lack park access, experience higher air temperatures, or face individual heat exposure.

---

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
