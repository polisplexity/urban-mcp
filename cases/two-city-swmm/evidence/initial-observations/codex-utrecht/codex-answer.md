The historical Tuindorp development model (Garzón Díaz et al., CC-BY-4.0) used KNMI 260 De Bilt regional hourly observations (CC0-1.0; no KNMI endorsement). The hypothetical diameter multiplier of 0.75 affected only `c_906791`.

Complete tables retained all 311 nodes: none reached 10 m³ in either run. Reported node overflow sums and system flooding losses were both zero; these remain distinct quantities. Each run produced 16 minimum-elevation-drop warnings, with routing/runoff continuity errors of −0.134%/−0.098%.

Decisive limits include neighborhood coverage, uniform hourly rainfall, ±0.225 mm trace uncertainty, a 24-hour initialization warm-up, 13 declared zero-area NaN normalizations, and SWMM changing from 5.1.015 to 5.2.4. This is computational reproduction without field validation.

Separate inspection controls and hotstart tests completed; loading preserved the initial clock. The asynchronous test ended `CANCELLED`, error “Simulation task was cancelled,” and was excluded. Invalid-path, `MISSING`, and three resource-URI errors recovered. All seven resource families succeeded; report coverage was one page, and output resources supplied metadata. Cleanup removed nothing; final status succeeded.

```json
{
  "city": "utrecht",
  "target_conduit_id": "c_906791",
  "event_day": "2018-08-25",
  "event_day_mm": 20.575,
  "forcing_total_mm": 23.025,
  "source_nodes": 311,
  "baseline_listed_flooding_nodes": 0,
  "scenario_listed_flooding_nodes": 0,
  "baseline_nodes_at_or_above_10m3": 0,
  "scenario_nodes_at_or_above_10m3": 0,
  "newly_at_or_above_10m3": 0,
  "newly_crossing_node_ids": [],
  "baseline_sum_reported_node_flood_volume_m3": 0.0,
  "scenario_sum_reported_node_flood_volume_m3": 0.0,
  "delta_sum_reported_node_flood_volume_m3": 0.0,
  "baseline_system_flooding_loss_m3": 0.0,
  "scenario_system_flooding_loss_m3": 0.0,
  "routing_continuity_error_percent": [-0.134, -0.134],
  "runoff_continuity_error_percent": [-0.098, -0.098],
  "warning_counts": [16, 16],
  "comparison_sha256": "7db4337410fbb06d878d6ee6dd20d68321b7c89e57601ee0834355f3fcc767af",
  "controls_physically_actuated": false,
  "calibration_revalidated": false,
  "forecast_admitted": false,
  "product_qualified": false
}
```