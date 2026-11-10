Use only the `urban_mcp_swmm` MCP for a municipal drainage review in **{{city}}**.
Work from this empty workspace. Do not use shell, scripts, web, other MCPs,
messaging, previous answers or expected-result files. All work and your answer
must be in English. Use only original IDs, paths, timestamps and units returned
by this server. This is a blind computational test, not field validation.

1. Discover status, restore the public snapshot and prepare/inspect the city.
   Read **all pages** of `manifest.json`, `requests.json`, `rights.json` and
   `recipe.json` through `read_swmm_source`. Retain original licenses, exact
   model/observation identities, data dates and declared transformations.
2. Exercise original `model_inspect` and `model_list_objects` for node, link,
   subcatchment, raingage and lid_control. An empty LID list is valid. Run the
   returned **inspection.inp** once using original `simulation_run`; call
   `run_summary` and `output_inspect` for that short run. It is separate from
   the municipal comparison.
3. Run full `baseline` and `capacity75` with `run_swmm_scenario`; allow each
   call to finish. Compare their returned run IDs with `compare_swmm_runs`.
   Read **every page** of the scenario run's `comparison.csv`,
   `comparison.json`, `nodes.csv` and `outfalls.csv` until `next_offset=null`.
   Use `limit=12000`. Keep all nodes in the denominator, including displayed
   zeros and nodes that were never listed as overflowing. Identify every node
   newly reaching **at least 10 m³ of native reported overflow volume**.
   A listed flooding row can round to zero; system loss and node overflow
   sum have different meanings when water ponds/re-enters. Do not equate them.
4. Query original `output_query_series` (max_points=5) and
   `output_query_snapshot` for **each** of node/depth, link/flow,
   subcatchment/rainfall and system/outfall_flow, using a full baseline output.
   System object ID is `system`; use IDs from `inspect_swmm_case` otherwise.
   Choose snapshot at 01:00:00 on the returned start-local date. These
   sampled rates/depths do not replace the native cumulative overflow report.
5. With **inspection.inp only**, exercise original `simulation_create`,
   `simulation_start`, `simulation_observe`, `simulation_step` (30 seconds),
   `simulation_save_hotstart`, `simulation_stop` and `simulation_close`.
   Observe node depth/flooding, link flow, subcatchment rainfall/runoff,
   raingage rainfall/total_precip and system runoff_stats/routing_stats.
   On the step, exercise the four approved control lists using the returned
   IDs: link_target_settings value=1, node_generated_inflows value=0,
   outfall_stages value=0 and raingage_total_precipitation value=0.
   These are isolated model API tests, never physical municipal actuation
   or either scenario's outputs. Save and then load the returned hotstart
   into a new inspection session; verify `hotstart_loaded`, then close it.
   Loading stored hydraulic state does not automatically advance the clock.
6. Start an asynchronous **baseline.inp** using `simulation_run_start`, read
   its status, then immediately cancel with `simulation_task_cancel`; read
   status until terminal. Preserve actual `state` and any error text. Do not
   use a cancelled/incomplete run as municipal evidence.
7. Exercise `read_swmm_resource` for all seven original resource families:
   models, runtime/status, runs/{run_id}/summary, runs/{run_id}/report,
   runs/{run_id}/output, sessions/{session_id}/status and tasks/{task_id}/status.
   Use the short run for report/output. Read the session status **before**
   closing its session. For the report, one page with its complete length/hash
   suffices for this interface check; do not claim a full report review.
   Read the other resource pages to completion.
   Output resources contain metadata, not binary output bytes.
8. Deliberately request `model_inspect` outside the model root, and request
   a series for node `MISSING`. They should fail. Call `swmm_status` after
   **each** failure to verify recovery and avoid a host failure circuit.
   Call original `run_cleanup` at the end; retention is disabled and all
   municipal evidence must survive. Finish with `swmm_status`.

Your final answer must contain **at most 180 words of prose**, followed by
exactly one JSON code block with the keys below and no additional keys.
Numbers and IDs must come from actual returned results and full CSV pages:

```text
city (string)
target_conduit_id (string)
event_day (YYYY-MM-DD string)
event_day_mm (number)
forcing_total_mm (number, the whole 72-hour window)
source_nodes (integer)
baseline_listed_flooding_nodes (integer)
scenario_listed_flooding_nodes (integer)
baseline_nodes_at_or_above_10m3 (integer)
scenario_nodes_at_or_above_10m3 (integer)
newly_at_or_above_10m3 (integer)
newly_crossing_node_ids (array of source ID strings, sorted)
baseline_sum_reported_node_flood_volume_m3 (number)
scenario_sum_reported_node_flood_volume_m3 (number)
delta_sum_reported_node_flood_volume_m3 (number)
baseline_system_flooding_loss_m3 (number)
scenario_system_flooding_loss_m3 (number)
routing_continuity_error_percent (array: baseline, scenario)
runoff_continuity_error_percent (array: baseline, scenario)
warning_counts (array of integers: baseline, scenario)
comparison_sha256 (string)
controls_physically_actuated (false)
calibration_revalidated (false)
forecast_admitted (false)
product_qualified (false)
```

In the prose distinguish historical neighborhood models, regional hourly
observations and the hypothetical diameter loss. Explain the actual results,
warnings/continuity and decisive input limits. Do not claim a current blockage,
2D inundation, damage, safety, calibration, current forecast or city ranking.
Report any incomplete operation or recovered error honestly. Numerical claims,
complete operation coverage and prose are reviewed separately.
