# Blind municipal SUMO task: {{city}}

Use only the `urban_mcp_sumo` MCP. Do not use shell, files, browser, web,
other MCP servers, skills, messaging, memory or a previous city's answer.
Your empty workspace and this public task are the starting point. Discover
the tool schemas before choosing arguments. Do not invent missing inputs.

A municipal transport team wants to examine a hypothetical 30 km/h works
limit on a reproducibly selected corridor. Use the published historical
model for **{{city}}**. This is a computational scenario review, not approval
of a real traffic intervention.

1. Discover status and the native version. Restore the snapshot; prepare the
   case. Read the **entire** source `manifest.json`, publisher LICENSE and
   original SUMO configuration via `read_sumo_source` (follow `next_offset`
   to null; `limit` may be 12000). Identify publisher commit, rights, model
   date, demand provenance, mandatory signals, time window and unknown inputs.
   Inspect network summary and the selected exact edge/lanes. Explain how the
   scheduled corridor cohort was chosen and what route membership establishes.
2. With new run IDs `agent-baseline` and `agent-works`, run `baseline` and
   `works30`. The native process can take several minutes; await the result.
   Compare those runs; render the works map. Read both complete `summary.json`
   files and the complete `comparison.json`. Read **every character of
   `comparison.csv`**, following offsets to null; preserve every vehicle's
   completion/teleport status and strict threshold flag. Read the map receipt.
   Do not substitute a preview, summary or hash for the full comparison CSV.
   List its SHA-256 in the answer. A PNG receipt does not mean you viewed it.
3. Exercise the reused original MCP operations separately: connect an
   inspection with `params={city:"{{city}}",run_id:"agent-inspection"}`;
   inspect the returned absolute begin/end, step to **begin + 30** seconds,
   query `simulation` and `vehicle_list`, and query one actual returned
   vehicle's `speed`, `position`, `acceleration`, `lane` and `route` using
   `vehicle_variable`. Disconnect. Run original FCD analysis on
   `/data/results/{{city}}/agent-inspection/fcd.xml.gz`. Distinguish per-step
   counters, sample-weighted FCD speeds and journey outcomes.
4. Deliberately test one invalid city, one invalid scenario, an artifact
   traversal name, and a disconnected vehicle query. These must be rejected.
   **After each expected error, make a successful `sumo_status` call before
   trying the next one** so that a host failure circuit does not mask recovery.
   Recover and finish; report any host/tool failure honestly.

Write an English municipal assessment of at most 600 words (excluding the
JSON below). Distinguish scheduled-to-arrival time (including insertion
delay), in-network duration, incomplete/undeparted trips, teleport exclusions,
source-model warnings and completed-pair denominators. Explain what another
municipality must supply for a credible local application. Do not infer a
current calibrated forecast, observed causal effect, safety/emissions result,
city ranking, or an independent third-person replication. Mention whether
fresh field validation/calibration was performed and whether new random
demand was generated. Report model quality problems even if SUMO exits zero.

End with one fenced `json` object with these exact fields. Use integers for
counts, numbers or null for means, actual booleans, and the complete state
objects reported by the backend. Do not guess expected values:

```json
{
  "city": "{{city}}",
  "target_edge_id": "from network/comparison",
  "target_lane_ids": ["from network"],
  "scheduled_vehicles": 0,
  "scheduled_corridor_cohort": 0,
  "baseline_states": {},
  "works_states": {},
  "matched_completed_cohort": 0,
  "eligible_paired_comparison": 0,
  "excluded_censored_pairs": 0,
  "excluded_teleport_identified_completed_pairs": 0,
  "increased_over_30s": 0,
  "mean_matched_scheduled_to_arrival_delta_s": null,
  "mean_matched_in_network_duration_delta_s": null,
  "mean_matched_insertion_delay_delta_s": null,
  "baseline_native_teleport_events": 0,
  "works_native_teleport_events": 0,
  "baseline_native_collisions": 0,
  "works_native_collisions": 0,
  "comparison_sha256": "from full comparison artifact",
  "calibration_revalidated": false,
  "forecast_admitted": false,
  "new_random_demand_generated": false
}
```
