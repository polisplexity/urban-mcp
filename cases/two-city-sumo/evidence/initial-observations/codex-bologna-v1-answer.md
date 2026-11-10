The hypothetical works limit increased mean scheduled-to-arrival time by **126.99 seconds** among **1,289 eligible completed pairs**. This comprises **101.62 seconds inside the network** and **25.37 seconds of additional insertion delay**. Exactly **991 pairs exceeded a strict 30-second increase**. These are historical computational results, not approval of an intervention.

The restored, hash-verified source is `DLR-TS/sumo-scenarios`, commit `79d2e1837a9683617393c69aaf754c6bc812e3f8`, under EPL-2.0, attributed to DLR Institute of Transportation Systems, Comune di Bologna and iTETRIS authors. I read the entire manifest, publisher LICENSE and original `bologna/acosta/run.sumocfg`. Native SUMO was **1.28.0**. The model represents the historical 08:00–09:00 peak using November 2008 observations; published demand derives from supplied VISSIM scenarios and detector observations.

The Andrea Costa study network contains 178 edges, 112 nodes and seven signals; it does not represent the whole municipality. Original routes, vehicle types, detectors, bus stops and mandatory `acosta_tls.add.xml` signal programs were preserved. Both runs used seed 37, one-second steps and simulation seconds 0–4500, with departures through 3600, a declared 900-second warm-up and evaluation departures at 900–2700. Initialization was empty; earlier traffic was absent.

Selection maximized distinct scheduled evaluation vehicles among published-route edges at least 100 metres long with passenger lanes above 30 km/h, breaking ties by source edge ID. This selected `204a[0]`, length 190.3 metres, with 1,348 scheduled cohort vehicles. Its three eligible lanes changed from 13.89 to 8.333333333333334 m/s starting at second 900. Route membership establishes a planned corridor cohort, not proven traversal.

Across all 8,772 scheduled vehicles, baseline recorded 8,414 arrivals, 126 unfinished and 232 undeparted; works recorded 8,352, 131 and 289 respectively. Within the corridor cohort, 18 baseline and 59 works trips remained unfinished. The comparison excludes 59 censored pairs and zero teleport-identified completed pairs. Separate completed-cohort means have different denominators—1,330 and 1,289—and should not be subtracted.

Both complete summaries, comparison JSON and all eight CSV pages were read through `next_offset: null`: 92,396 characters and 1,348 unique vehicle rows. Every completion/teleport state and threshold flag was retained; censored thresholds remain blank. Row checks reproduced the reported means and flags, including false flags at exactly 30 seconds. The works map receipt records a 133,238-byte PNG; **I did not view the image**.

The reused inspection connected with bounds 0–60 and stepped to absolute second 30. Simulation returned loaded/departed/arrived counters of 485/77/0; these are per-step counters, not cumulative journey outcomes. Active vehicle `Audinot_12_1` returned speed 12.92846 m/s, position (1500.38096, 208.10683) source-network metres, acceleration 0.16151 m/s², lane `131_0` and its planned route. After disconnecting, original FCD analysis returned 101 samples averaging 12.809109 m/s at the configured ten-second output period: a sample-weighted speed, not unique vehicles or mean journey time.

Both runs reported zero native teleports, collisions and incompatible-signal warnings. Nevertheless, long insertion delays, incomplete trips, uncertain warm-up adequacy, limited route choice and potentially unrealistic multilane-roundabout queues remain model-quality concerns.

Codex observed all four required rejections, with successful status recovery after each and no unexpected host/tool failure. No fresh field validation, calibration or new random demand generation occurred. Credible local application requires licensed current network, demand, vehicle/transit and signal inputs, actual works staging/compliance assumptions, independent counts, queues and journey observations, calibration and uncertainty testing. No current forecast, observed causal effect, safety/emissions result, city ranking or independent third-person replication is established.

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