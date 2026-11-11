Odense’s historical, uncalibrated Bellinge neighborhood model (Pedersen et al., 2021) uses regional DMI station 06120 hourly observations; both sources retain CC-BY-4.0. The hypothetical scenario reduces one conduit’s diameter to 75%. Uniform regional rainfall, unresolved local extremes and unproven 24-hour equilibration limit interpretation. This is a blind computational test.

All 1,020 nodes remain in the denominator. G70F030 (22 m³) and G70F100 (220 m³) reach the threshold in both runs; none newly cross. Listed flooding rows decrease from 17 to 14, while summed reported overflow remains 245 m³. Listed zeros reflect report rounding; ponding/re-entry gives node overflow and system loss distinct meanings. Each run has 15 elevation/depth warnings. Routing errors are 0.322%/0.323%; runoff errors are −0.003% each. JSON preserves report precision.

Required operations and seven resource families were exercised; only one short-report page was reviewed. Hotstart loading succeeded. The asynchronous test ended `CANCELLED`: “Simulation task was cancelled.” Outside-root and `MISSING` errors recovered. Cleanup removed zero runs; final status succeeded.

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