All four error tests rejected correctly, host healthy after each. Now I have all the data needed to write the full assessment and JSON.

---

MUNICIPAL COMPUTATIONAL SCENARIO REVIEW: BOLOGNA ACOSTA CORRIDOR
Eclipse SUMO 1.28.0 | Seed 37 | EPL-2.0 | November 2026 Review

SOURCE MODEL AND PROVENANCE

The model is the DLR iTETRIS Andrea Costa (Acosta) scenario for Bologna, published by DLR-TS/sumo-scenarios at commit 79d2e1837a9683617393c69aaf754c6bc812e3f8 and licensed under EPL-2.0. Attribution is to DLR Institute of Transportation Systems, Comune di Bologna and iTETRIS scenario authors. The model date is a historical morning peak (08:00-09:00) derived from November 2008 detector observations and a supplied VISSIM scenario; it is not a current observation or a newly calibrated model. No fresh field validation was performed and no new random demand was generated. The simulation uses preserved departures, routes, vehicle types and mandatory signal programs from the publisher snapshot. Demand derives from VISSIM detector observations; simulated vehicle IDs are not observed people or license plates. The original authors warn of warm-up needs, small route-choice scope and potentially unrealistic multilane roundabout queues. The network covers the Andrea Costa study area (178 edges, 112 nodes, 7 traffic lights), not the whole municipality of Bologna.

UNKNOWN INPUTS: The raw VISSIM calibration data, detector count files and any proprietary signal timing used to build the original demand are not supplied. The warm-up duration is an experimental setting, not a newly validated one.

CORRIDOR SELECTION AND COHORT

Edge 204a[0] (190.3 m, three passenger lanes, original speed 13.89 m/s = 50 km/h) was selected deterministically: it is the edge with the most distinct scheduled evaluation-window vehicles among all edges at least 100 m long with passenger lane speed above 30 km/h, with ties broken by source edge ID. The scheduled corridor cohort of 1,348 vehicles comprises those whose published routes contain 204a[0] within the cohort window (s=900 to s=2700). Route membership is a plan declared in the source XML, not a proven in-simulation traversal.

TRIP ACCOUNTING

Total scheduled vehicles: 8,772. Baseline: 8,414 arrived network-wide, 232 undeparted (still waiting at simulation end), 126 unfinished (departed but not arrived). Works30: 8,352 arrived network-wide, 289 undeparted, 131 unfinished. For the corridor cohort of 1,348, baseline delivered 1,330 arrivals and 18 unfinished; works30 delivered 1,289 arrivals and 59 unfinished. No undeparted cohort vehicles in either run. The increase from 18 to 59 corridor unfinished trips under works30 is a model quality concern: those 59 vehicles are excluded from paired comparison as censored. No teleport events were recorded in either run; therefore no teleport-identified completed pairs were excluded.

PAIRED COMPARISON

The eligible paired comparison denominator is 1,289 vehicle pairs (both baseline and works arrived). Mean delta (works minus baseline) in scheduled-to-arrival time: +127.0 s. This includes insertion delay. Mean in-network duration delta: +101.6 s. Mean insertion delay delta: +25.4 s. Of the 1,289 eligible pairs, 991 (76.9%) exceeded the strict 30-second threshold, and 37 decreased by more than 30 seconds. These are differences between two same-seed deterministic replays of the same historical demand; they do not represent a currently calibrated forecast, an observed causal effect, a safety benefit or any safety/emissions finding.

FCD INSPECTION

The 60-second inspection run (agent-inspection, begin=0, end=60) produced 101 FCD samples at the 10-second output period (not unique vehicles). The sample-weighted mean speed was 12.81 m/s across all samples. Per-step simulator counters at step 30: loaded=485, departed=77 (this step), arrived=0, min_expected=501. These are per-step counters, not cumulative journey outcomes. Vehicle Pepoli_10_10 at step 30: speed=11.25 m/s, position=(1662.6, 226.1) network XY metres, acceleration=-0.206 m/s^2, lane=210_0, planned route includes 204a[0] as a future edge.

MODEL QUALITY

Both runs: 0 native teleport events, 0 collisions, 0 emergency stops, 0 emergency braking, 0 incompatible signal program warnings. No fresh field validation is available. No forecast readiness is inferred from successful replay.

WHAT ANOTHER MUNICIPALITY MUST SUPPLY

A credible local application requires: (1) a calibrated and recently validated SUMO network for the target area; (2) current observed OD demand data; (3) validated signal programs; (4) independent field detector data for GEH and flow validation; (5) a qualified warm-up period assessment; (6) current vehicle type distributions; and (7) any local legal or operational constraints on the corridor. The Bologna Acosta model cannot substitute for any of these.

ERROR BOUNDARY TESTS

Four deliberate invalid requests were all rejected: unknown city "atlantis" (rejected: unknown city), invalid scenario "speedlimit999" (rejected: must be baseline or works30), path traversal artifact name "../../etc/passwd" (rejected: not allowed), and vehicle query after disconnect (rejected: no active inspection session). Host status was confirmed healthy after each rejection. No host/tool failure occurred.

The map rendering returned a PNG receipt (SHA-256: 14379cb67bda891ea3b7408a2cf6e6398c2a799c0e853f4d43feba8a17b14b02, 133,238 bytes). A receipt is not a visual inspection of the image.

```json
{
  "city": "bologna",
  "target_edge_id": "204a[0]",
  "target_lane_ids": ["204a[0]_0", "204a[0]_1", "204a[0]_2"],
  "scheduled_vehicles": 8772,
  "scheduled_corridor_cohort": 1348,
  "baseline_states": {
    "arrived": 1330,
    "unfinished": 18,
    "undeparted": 0,
    "removed": 0,
    "not_recorded": 0
  },
  "works_states": {
    "arrived": 1289,
    "unfinished": 59,
    "undeparted": 0,
    "removed": 0,
    "not_recorded": 0
  },
  "matched_completed_cohort": 1289,
  "eligible_paired_comparison": 1289,
  "excluded_censored_pairs": 59,
  "excluded_teleport_identified_completed_pairs": 0,
  "increased_over_30s": 991,
  "mean_matched_scheduled_to_arrival_delta_s": 126.99456943366951,
  "mean_matched_in_network_duration_delta_s": 101.62141194724593,
  "mean_matched_insertion_delay_delta_s": 25.373157486423583,
  "baseline_native_teleport_events": 0,
  "works_native_teleport_events": 0,
  "baseline_native_collisions": 0,
  "works_native_collisions": 0,
  "comparison_sha256": "fbeaa87e64921df41953ab8bfd876119bcbfdb7ee310bbfe679d8e184e04bcc9",
  "calibration_revalidated": false,
  "forecast_admitted": false,
  "new_random_demand_generated": false
}
```
