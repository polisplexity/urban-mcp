Codex used the historical, uncalibrated Bellinge neighborhood model `7_SWMM/BellingeSWMM_v021_nopervious.inp` (Pedersen et al., 2021, DOI 10.11583/DTU.12513428.v2) and DMI station 06120 regional hourly observations. Both retain CC-BY-4.0; excluded original local rainfall is CC-BY-NC-4.0. Uniform rainfall, changed dates/threads and unproven 24-hour warm-up equilibrium limit interpretation. Capacity75 hypothetically reduces one diameter to 75%.

Across all 1,020 nodes, none newly crossed 10 m³. Both reported node-volume sums are 245 m³; listed flooding rows fell 17→14. Rounded zeros can overflow. System loss separately reports 245 m³ each; ponding/re-entry prevents general equivalence. Each run has 15 geometry warnings; routing continuity is 0.322%/0.323%, runoff −0.003% each.

Required pages and seven resource families were read, with one report page and output metadata. Controls and hotstart loading succeeded. Stop and loaded-session start/observe failed; closure reported “Session operation interrupted.” URI errors and deliberate failures recovered. Asynchronous baseline ended `CANCELLED`: “Simulation task was cancelled”; excluded. Short-report routing was −25.009% despite summary zero. Cleanup removed nothing; final status succeeded. This remains a blind computational test without field validation.

```json
{
  "city": "odense",
  "target_conduit_id": "G75F65Y_G75S541_l1",
  "event_day": "2018-08-12",
  "event_day_mm": 19.7,
  "forcing_total_mm": 31.0,
  "source_nodes": 1020,
  "baseline_listed_flooding_nodes": 17,
  "scenario_listed_flooding_nodes": 14,
  "baseline_nodes_at_or_above_10m3": 2,
  "scenario_nodes_at_or_above_10m3": 2,
  "newly_at_or_above_10m3": 0,
  "newly_crossing_node_ids": [],
  "baseline_sum_reported_node_flood_volume_m3": 245.0,
  "scenario_sum_reported_node_flood_volume_m3": 245.0,
  "delta_sum_reported_node_flood_volume_m3": 0.0,
  "baseline_system_flooding_loss_m3": 245.0,
  "scenario_system_flooding_loss_m3": 245.0,
  "routing_continuity_error_percent": [0.322, 0.323],
  "runoff_continuity_error_percent": [-0.003, -0.003],
  "warning_counts": [15, 15],
  "comparison_sha256": "f510fd2292163995a67bcabee19e948d340fa58884e08d253bdd3ca96d6b7b06",
  "controls_physically_actuated": false,
  "calibration_revalidated": false,
  "forecast_admitted": false,
  "product_qualified": false
}
```