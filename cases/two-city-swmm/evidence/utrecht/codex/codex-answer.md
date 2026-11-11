The historical Tuindorp development neighborhood model (Garzón Díaz, 2024; DOI 10.4121/fec1e3de-9586-4a61-b3a1-02382592e52c.v1; CC-BY-4.0) used regional hourly De Bilt station 260 observations (CC0-1.0; bron: KNMI; no endorsement). The hypothetical 0.75 diameter multiplier on `c_906791` produced no reported overflow or ≥10 m³ crossings among all 311 nodes in either 72-hour run.

Each run retained 16 minimum-elevation-drop warnings. Report-derived routing/runoff continuity errors were −0.134%/−0.098%; higher-precision native metadata round accordingly. Node volumes have 1 m³ report resolution; node overflow sums and system losses remain distinct.

Decisive limits include uniform hourly rainfall, trace imputation, unverified empty-start warm-up, 13 declared zero-area NaN normalizations, and historical physics transferred from SWMM 5.1.015 to 5.2.4. This is computational reproduction without field validation.

Requested API/resource checks completed, with inspection controls isolated; only one short-report page was reviewed. Hotstart loaded without clock advancement. The asynchronous run ended `CANCELLED`: “Simulation task was cancelled”; excluded from municipal evidence. Outside-root and `MISSING` errors recovered. Cleanup removed zero runs; final status succeeded.

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