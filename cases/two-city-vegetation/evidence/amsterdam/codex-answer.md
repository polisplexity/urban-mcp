Amsterdam’s 111 supplied zones contain **26 zones below 0.20**, with **217,945 published residents attached**. At 0.40, **65 zones** are flagged, with **557,965 known residents attached**, plus one unknown population. These are exploratory thresholds applied to identical historical observations.

Sources are ESA WorldCover 2021 v200, tile N51E003 Map (CC-BY-4.0), and CBS Wijken en Buurten 2025 via PDOK (CC0-1.0). Acquisition receipts date from 10 November 2026; population refers to 1 January 2025. The restored snapshot passed integrity checks. The analysis uses nearest resampling onto the declared 10 m EPSG:28992 grid, with pixel-centre zone assignment and zero overlapping assigned centres.

The following are all baseline low-share zones and their published populations:

| Source zone ID | Population |
|---|---:|
| WK0363AA | 9145 |
| WK0363AB | 19485 |
| WK0363AC | 6505 |
| WK0363AD | 4345 |
| WK0363AE | 4760 |
| WK0363AF | 9940 |
| WK0363AG | 5710 |
| WK0363AH | 7570 |
| WK0363BB | 1765 |
| WK0363EC | 5475 |
| WK0363EH | 12945 |
| WK0363EM | 10045 |
| WK0363EP | 6250 |
| WK0363EQ | 4710 |
| WK0363ES | 6910 |
| WK0363ET | 7675 |
| WK0363EU | 7400 |
| WK0363KF | 12550 |
| WK0363MA | 20760 |
| WK0363ME | 10000 |
| WK0363MF | 12045 |
| WK0363MJ | 16090 |
| WK0363MK | 1535 |
| WK0363NB | 12010 |
| WK0363NM | 1910 |
| WK0363NP | 410 |

At 0.40, all baseline zones remain flagged, and these 39 join them:

| Additional source zone ID | Population |
|---|---:|
| WK036399 | null |
| WK0363AJ | 8005 |
| WK0363AK | 15525 |
| WK0363BA | 30 |
| WK0363ED | 11785 |
| WK0363EE | 19130 |
| WK0363EG | 2330 |
| WK0363EJ | 8195 |
| WK0363EK | 8220 |
| WK0363EL | 6560 |
| WK0363EN | 5945 |
| WK0363ER | 6730 |
| WK0363EV | 1825 |
| WK0363FC | 10370 |
| WK0363FG | 14450 |
| WK0363FH | 6145 |
| WK0363FK | 18625 |
| WK0363FN | 11755 |
| WK0363KA | 11585 |
| WK0363KB | 3745 |
| WK0363KD | 12565 |
| WK0363KE | 15000 |
| WK0363KG | 7810 |
| WK0363KH | 11665 |
| WK0363KJ | 8640 |
| WK0363KK | 15125 |
| WK0363KL | 5200 |
| WK0363KP | 4835 |
| WK0363MB | 5820 |
| WK0363MC | 10560 |
| WK0363MD | 8745 |
| WK0363ML | 8485 |
| WK0363NC | 12545 |
| WK0363NK | 9470 |
| WK0363NN | 3420 |
| WK0363SC | 8035 |
| WK0363SD | 5740 |
| WK0363TE | 7775 |
| WK0363TH | 7630 |

Every flag was checked against vegetation pixels divided by valid-land pixels using strict `<`; equality is not low. Both complete zone CSVs and all 1,332 baseline class-count records were read through their final pages and reconciled.

Within these zones, 1,084,317 vegetation pixels divided by 1,968,573 valid-land pixels gives **55.0814%**. The all-surface denominator includes 468,010 water pixels: 2,436,583 valid pixels, giving **44.5015%**. NoData is zero. Vegetation includes cropland, grassland, wetlands and other declared vegetation classes. Mapped tree-class area is **46.2433 km²**, not canopy percentage.

Groot water, WK036399, has 16,297 valid-land pixels and a 26.0600% land share; its source water label does not exclude it. Its population remains null. Known zone populations sum to 934,515 versus municipal population 934,526, a difference of 11. Published zone counts are randomly rounded to multiples of five.

All 21 advertised tools were exercised. Inspection derivatives stayed under `/data/results/amsterdam/agent-baseline/`. All seven requested invalid-input tests were rejected, including the partially outside raster window. Numeric class-code statistics are not physical vegetation indicators; raster queries extract rectangular windows. The baseline map receipt confirms 291,736 bytes. Case, manifest and quality resources were retrieved. Codex lacks prompt retrieval, so the municipal workflow prompt could not be fetched; manually authored justifications following returned preflight metadata were accepted.

A bounded next action is recent-imagery and field review of WK0363AD and WK0363AE before considering small planting or depaving projects. Validate classification, boundaries, ownership, utilities, soil and maintenance feasibility locally. The 2021 classification and 2025 population describe different periods; attached population does not locate residents within vegetation pixels. Product qualification remains pending.

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
  "unknown_population_zone_ids": ["WK036399"],
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