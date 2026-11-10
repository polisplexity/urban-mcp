The historical works30 experiment produced a **15.272 s mean scheduled-to-arrival increase across 317 eligible completed pairs**. This computational scenario review does not approve a real intervention.

Native Eclipse SUMO **1.28.0** replayed the restored `TUM-VT/sumo_ingolstadt` snapshot at commit `e0a95deebe200ff81b6705044d66310d6266d42b`. The publisher license is Apache-2.0, with attribution to AUDI AG, TUM and the SAVe:, SAVeNoW and KIVI authors. I read the complete manifest, publisher license, original configuration and recipe, each through `next_offset: null`. Demand and hourly signal programs represent **16 September 2020**. Publisher demand was fitted to mobility matrices and induction-loop counts; signal programs to observed green times. Mandatory `tlLogics_WAUT_2020-09-16_24h.add.xml` was preserved. Raw independent observations are absent.

The inspected network has 27,754 edges, 12,138 nodes and 124 traffic lights. Selection maximized distinct evaluation-window vehicles whose published routes reference an eligible edge: length at least 100 m, passenger-lane speed above 30 km/h, ties resolved by source edge ID. This selected **Theodor-Heuss-Straße, `54858973#0`**, length 118.79 m, and 320 vehicles. Works30 capped its three eligible passenger lanes from 13.89 to 8.3333 m/s at 07:00. Two non-passenger lanes were outside the cap. Route membership establishes planned use, not observed traversal or exposure.

Runs `agent-baseline` and `agent-works` preserved demand, vehicle types, signals, processing settings, seed **37** and **0.25 s** steps. Departures covered **06:45–07:10**, evaluated departures **07:00–07:10**, with simulation ending **07:30**. Initialization was empty; the 15-minute warm-up excludes earlier traffic. All 6,492 scheduled vehicles were inserted. Baseline had 6,480 arrivals and 12 unfinished trips; works had 6,481 arrivals and 11 unfinished trips.

Each corridor cohort had 318 arrivals and two unfinished trips, with no undeparted, removed or unrecorded vehicles. Of 318 completed pairs, one teleport-identified pair was excluded, leaving **317 eligible pairs**. Mean works-minus-baseline changes were **+15.264 s in-network duration** and **+0.007886 s insertion delay**, together forming scheduled-to-arrival time. **74/317 strictly exceeded +30 s**; 24 decreased by more than 30 s. Censored vehicles were `pv_7_15063` and `pv_7_15068_1`; teleport-excluded `pv_7_3298_0` completed both runs. Their comparison flags remain blank, not false. Both complete summaries, complete comparison JSON and all **20,631 CSV characters across two pages** were read, preserving all 320 rows and flags. Its SHA-256 appears below.

Both native runs recorded **20 teleports, two collisions and 577 incompatible-signal-program warnings**. Emergency stops were 222/227 and emergency braking events 341/364, baseline/works. Original pedestrian connectivity is unsuitable. Successful execution therefore does not establish model quality.

Original inspection `agent-inspection` returned begin/end **24300/24360 s** and stepped to **24330 s**. Simulation and vehicle-list queries succeeded; actual vehicle `dv_6_275` returned speed, position, acceleration, lane and route. After disconnect, original FCD analysis returned **117 samples averaging 13.73 m/s** at 10-second output spacing. These sample-weighted speeds differ from journey outcomes; loaded/departed/arrived query counters are per-step.

All four deliberate invalid requests were rejected, each followed by successful status recovery. Three additional source-name requests hit the allowlist; recovery succeeded without a host circuit failure. The works-map receipt was read; **the PNG was not viewed**.

Another municipality needs licensed, dated network/demand/signal inputs, explicit works geometry, representative observations, initialization evidence and independent calibration/validation. No fresh field validation, calibration revalidation or new random demand occurred. No current forecast, observed causal effect, safety/emissions benefit, city ranking or independent third-person replication is established.

```json
{
  "city": "ingolstadt",
  "target_edge_id": "54858973#0",
  "target_lane_ids": [
    "54858973#0_2",
    "54858973#0_3",
    "54858973#0_4"
  ],
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