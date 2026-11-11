Codex reviewed the historical, uncalibrated Bellinge neighborhood model (Pedersen et al., 2021; DOI 10.11583/DTU.12513428.v2) with regional DMI 06120 hourly observations. Both sources are CC-BY-4.0; excluded CC-BY-NC-4.0 local gauges were unused. Capacity75 hypothetically reduced one conduit’s diameter by 25%.

Across all 1,020 nodes, no node newly crossed 10 m³; summed reported overflow remained 245 m³. Listed flooding rows decreased from 17 to 14; displayed zeros can conceal overflow. System loss and node overflow have distinct meanings under ponding/re-entry. Each run retained 15 elevation/depth warnings. Report-derived routing errors were 0.322%/0.323%; runoff errors were −0.003% each. Historical physics, regional hourly forcing and unverified warm-up limit interpretation.

Required interfaces, isolated controls, hotstart and seven resource families were exercised. The separate five-minute run’s routing error was −25.009%; only one report-resource page was reviewed. Cancellation ended `CANCELLED` (“Simulation task was cancelled”) and was excluded from municipal evidence. Two URI errors and both deliberate invalid requests recovered. Cleanup removed nothing; final status succeeded. This is computational evidence, without field validation.

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
  "baseline_sum_reported_node_flood_volume_m3": 245,
  "scenario_sum_reported_node_flood_volume_m3": 245,
  "delta_sum_reported_node_flood_volume_m3": 0,
  "baseline_system_flooding_loss_m3": 245,
  "scenario_system_flooding_loss_m3": 245,
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