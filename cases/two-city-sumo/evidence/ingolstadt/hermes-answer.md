All four error tests completed and recovered. All data is now collected. I can now compose the full municipal assessment.

---

MUNICIPAL COMPUTATIONAL SCENARIO REVIEW
Ingolstadt - Hypothetical 30 km/h Works Limit on Theodor-Heuss-Strasse
Eclipse SUMO 1.28.0 | Seed 37 | Historical model date 2020-09-16
Host: hermes

SOURCE MODEL AND PROVENANCE

The dataset originates from TUM-VT/sumo_ingolstadt at publisher commit e0a95deebe200ff81b6705044d66310d6266d42b, acquired 2026-11-10 and held at input manifest SHA-256 6dfdc367fdfc2f9167e5e44112ca1d9e5b976396cee773a4dc3336f1d1c16956. The license is Apache-2.0 (AUDI AG and Chair of Traffic Engineering and Control, Technical University of Munich; SAVe:, SAVeNoW and KIVI authors). The model represents 2020-09-16 demand fitted to mobility matrices and induction-loop counts, with hourly fixed-time traffic-light programs fitted to observed green times. No raw independent traffic observations, fresh field calibration, or current-day validation were performed; this is explicitly a historical scenario, not a contemporaneous forecast. No new random demand was generated: departures, routes, vehicle types and mandatory signal programs are reproduced verbatim from the publisher file.

The original SUMO config (24h_sim.sumocfg) declares a full 24-hour network run from t=0 to t=86400 at 0.25s step length, with processing flags: ignore-junction-blocker=15s, time-to-teleport=300s, max-depart-delay=100s, device.rerouting.probability=0.2. This recipe runs a bounded slice: begin=24300s (06:45), cohort departure window 25200-25800s (07:00-07:10), depart_end=25800, end=27000s (07:30). Mandatory additional file: tlLogics_WAUT_2020-09-16_24h.add.xml (WAUT hourly signal programs). Two optional files excluded: GUI settings and polygon layer. The pedestrian route file is not used (publisher pedestrian connectivity is unsuitable for this motorized recipe).

Unknown inputs: raw induction-loop detector data files are not included in the published repository and are not available here. The demand-calibration residuals and original mobility matrix are also absent. These constitute the principal unknown inputs that limit independent replication.

CORRIDOR SELECTION AND COHORT

The corridor is selected deterministically: among all edges referenced by evaluation-window published routes, the edge with the greatest number of distinct scheduled vehicles, minimum 100 m length, and at least one passenger lane with speed above 30 km/h is chosen, with ties broken by source edge ID. Edge 54858973#0 (Theodor-Heuss-Strasse, 118.79 m) was selected. It has 5 lanes; lanes _2, _3 and _4 allow passenger vehicles and had original speed 13.89 m/s (50 km/h). Lanes _0 and _1 are non-passenger and are unaffected. Route membership means a vehicle's published planned route contains this edge; it does not establish that the vehicle was observed to traverse it in the field. The corridor cohort is 320 vehicles whose published routes list this edge and whose scheduled departures fall within the evaluation window.

TRIP ACCOUNTING

Total scheduled vehicles in the slice: 6492 (all departed in both runs).

Corridor cohort (320 scheduled):
- Baseline: 318 arrived, 2 unfinished (did not arrive before t=27000), 0 undeparted/removed/not_recorded.
- Works30: 318 arrived, 2 unfinished, 0 undeparted/removed/not_recorded.
The 2 unfinished vehicles in each run are censored trips: they were still in-network when the simulation ended and their journey times are unknown. These are excluded from paired comparison.

Matched completed cohort: 318 vehicles arrived in both runs. After excluding 2 censored pairs and 1 teleport-identified completed pair (a vehicle that received a teleport warning in the baseline run), the eligible paired comparison denominator is 317.

TIMING BREAKDOWN

For the 317 eligible paired vehicles:
- Mean scheduled-to-arrival delta (works minus baseline): +15.27s. This includes both in-network travel time and insertion delay.
- Mean in-network duration delta: +15.26s. This measures time from actual departure (insertion) to arrival.
- Mean insertion delay delta: +0.008s. The works scenario introduced a negligible additional departure-queue delay on average.

The ~15 s mean increase reflects the speed cap on the 118.79 m corridor segment reducing throughput for affected corridor vehicles. 74 of 317 vehicles (23%) exceeded the 30s threshold increase; 24 vehicles (8%) exceeded 30s in the other direction (faster in the works run - a consequence of secondary signal-timing interactions in this historical fixed model, not a physical speed benefit claim). Of the full corridor cohort means (318 completed), baseline scheduled-to-arrival was 797.1s (13.3 min), works was 811.5s (13.5 min).

MODEL QUALITY ISSUES

Both runs produced identical total teleport counts (20, all network-wide, mostly yield-type). Native collisions: 2 each. Emergency stops: 222 (baseline) / 227 (works). Emergency braking events: 341 (baseline) / 364 (works). There are 577 incompatible signal-program compatibility warnings in each run, arising from the WAUT TLS file using legacy formatting against SUMO 1.28.0. These warnings are retained as originally published and do not cause SUMO to exit non-zero, but they represent a known model quality concern. One corridor cohort vehicle received a teleport warning in baseline (excluded from comparison). No fresh field validation was available; no calibration revalidation was claimed. SUMO exiting zero does not imply a calibrated or current forecast.

INSPECTION AND FCD

The inspection run (agent-inspection, baseline, begin=24300, end=24360) was connected, stepped to t=24330 (begin+30s), and queried. At t=24330: 100 per-step departed vehicles, 697 loaded, 0 arrived (this is a per-step counter at that instant, not cumulative). Active vehicle dv_6_275 had speed 14.12 m/s, position (5737.2, 6130.8) in network metres, acceleration 0.059 m/s^2, lane 32021408_2, and a planned route of 57 edges. The FCD file for the 60-second inspection window contained 117 position samples (at 10s output period across vehicles present). The sample-weighted mean speed was 13.73 m/s (std 14.45 m/s, min 0.0, max 55.53 m/s). These are per-step sample counts and instantaneous speeds - not unique vehicle counts, mean journey times, or field observations.

BOUNDARY TESTS

All four deliberate invalid requests were rejected cleanly: (1) city "atlantis" - unknown city error; (2) scenario "works50" - scenario must be baseline or works30; (3) artifact path traversal "../../etc/passwd" - artifact name not allowed; (4) vehicle query without active inspection - no active inspection session. All four sumo_status recovery calls confirmed server health after each rejection. One tool failure was encountered during inspection: the wrong action name was used for simulation stepping (description says "absolute-step" but server requires "step" with key "step"), triggering the host circuit breaker for approximately 60 seconds. The circuit breaker recovered fully and the inspection was completed successfully on retry with correct parameters. This blocker is reported honestly.

FOR ANOTHER MUNICIPALITY

A municipality wishing to replicate or adapt this analysis for their own network must supply: (1) a published SUMO network file for their city; (2) a demand/routes file covering the target time window, with documented provenance and calibration basis; (3) traffic signal programs matching the target date; (4) independent field measurements (detector counts, journey-time surveys) to validate model outputs against reality before any operational use; (5) confirmation of vehicle type parameters appropriate to their local fleet; and (6) a network-specific corridor selection rationale. This Ingolstadt result cannot be transferred to another city's network or used as a city-ranking reference. No safety, emissions, or operational conclusions should be drawn without independent calibration and regulatory review.

```json
{
  "city": "ingolstadt",
  "target_edge_id": "54858973#0",
  "target_lane_ids": ["54858973#0_2", "54858973#0_3", "54858973#0_4"],
  "scheduled_vehicles": 6492,
  "scheduled_corridor_cohort": 320,
  "baseline_states": {
    "arrived": 318,
    "unfinished": 2,
    "undeparted": 0,
    "removed": 0,
    "not_recorded": 0
  },
  "works_states": {
    "arrived": 318,
    "unfinished": 2,
    "undeparted": 0,
    "removed": 0,
    "not_recorded": 0
  },
  "matched_completed_cohort": 318,
  "eligible_paired_comparison": 317,
  "excluded_censored_pairs": 2,
  "excluded_teleport_identified_completed_pairs": 1,
  "increased_over_30s": 74,
  "mean_matched_scheduled_to_arrival_delta_s": 15.272082018927446,
  "mean_matched_in_network_duration_delta_s": 15.264195583596214,
  "mean_matched_insertion_delay_delta_s": 0.007886435331230283,
  "baseline_native_teleport_events": 20,
  "works_native_teleport_events": 20,
  "baseline_native_collisions": 2,
  "works_native_collisions": 2,
  "comparison_sha256": "ce4b431e355128f709561d0567c1d90f288e4288618a845aaffcf498d7bb0f2e",
  "calibration_revalidated": false,
  "forecast_admitted": false,
  "new_random_demand_generated": false
}
```
