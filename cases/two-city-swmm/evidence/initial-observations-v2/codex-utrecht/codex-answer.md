Tuindorp is a historical neighborhood model (Garzón Díaz, 2024; CC-BY-4.0), driven here by regional hourly KNMI 260 De Bilt observations (CC0-1.0; no KNMI endorsement). The diameter loss in c_906791 is hypothetical.

All 311 nodes remain below 10 m³ in both complete runs. Each retains 16 minimum-elevation-drop warnings; report-derived routing/runoff continuity errors are −0.134%/−0.098%. JSON preserves report precision. Node-overflow sums and system flooding loss remain distinct quantities.

Limits include historical assets, uniform hourly rainfall, trace uncertainty, 13 zero-area NaN normalizations, unverified warm-up equilibrium and changed SWMM versions. This is computational reproduction without field validation.

Inspection controls, observations, hotstart, cancellation and all seven resource families were exercised. Hotstart loading preserved the initial clock. Only one short-report page was reviewed; output resources contained metadata. URI/parsing errors recovered before successful resource reads. Boundary/MISSING requests failed, followed by successful status checks. The asynchronous task ended `CANCELLED`: “Simulation task was cancelled”; it supplied no municipal evidence. Cleanup removed nothing; final status succeeded.

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