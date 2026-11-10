The hypothetical 30 km/h limit increased scheduled-to-arrival time by **126.99 seconds on average across 1,289 eligible completed pairs**. Of these, 991 increased strictly more than 30 seconds. These results describe a historical computational scenario, not approval of a traffic intervention.

Using only the SUMO MCP on host **codex**, I discovered native SUMO **1.28.0**, restored the snapshot and prepared Bologna. I read the entire manifest, publisher LICENSE and original configuration. The publisher is `DLR-TS/sumo-scenarios`, commit `79d2e1837a9683617393c69aaf754c6bc812e3f8`, under **EPL-2.0**, attributed to DLR, Comune di Bologna and the iTETRIS authors. Demand represents the historical 08:00–09:00 peak using November 2008 observations and supplied VISSIM scenarios; simulated IDs do not identify observed people.

The Andrea Costa network contains 178 edges, 112 nodes and seven traffic lights. Selection maximized distinct evaluation-window vehicles whose published routes contain an eligible edge at least 100 metres long with passenger-lane speed above 30 km/h, breaking ties by source edge ID. This selected `204a[0]`, length 190.3 metres, and its three exact lanes listed below. Membership establishes planned routing, not observed traversal or exposure.

Both runs preserved demand, vehicle types, connectivity and mandatory `acosta_tls.add.xml` signal programs, using seed 37 and one-second steps. Simulation covered seconds 0–4500, departures through 3600, and evaluation departures during 900–2700. Initialization was empty, with 900 seconds of warm-up. Works capped the three lanes from second 900, reducing 13.89 m/s to 8.3333 m/s.

Among all 8,772 scheduled vehicles, baseline had 8,414 arrivals, 126 unfinished and 232 undeparted; works had 8,352 arrivals, 131 unfinished and 289 undeparted. Corridor completions fell from 1,330 to 1,289. Paired means exclude 59 censored pairs; none were excluded for identified teleporting. The **126.99-second** increase comprises **101.62 seconds in-network duration plus 25.37 seconds insertion delay**. Separate completed-only run averages have different denominators and should not replace this paired comparison.

I read both complete summaries, complete comparison JSON and every comparison CSV character: eight pages, 92,396 characters, 1,348 vehicle rows, ending at null offset. Completion states, teleport flags and strict threshold flags were retained; censored threshold fields remain blank. The CSV SHA-256 appears below. The works map was rendered and its 133,238-byte PNG receipt read; **I did not view the image**.

Inspection `agent-inspection` returned absolute bounds 0–60 seconds and advanced to 30. Simulation counters—485 loaded, 77 departed, zero arrived—are per-step, not cumulative journey outcomes. Actual vehicle `Audinot_12_1` returned speed 12.92846 m/s, position (1500.38096, 208.10683) in source-network metres, acceleration 0.16151 m/s², lane `131_0` and its planned route. After disconnecting, original FCD analysis returned 101 samples averaging 12.809109 m/s at the configured ten-second sampling period: a sample-weighted speed, not mean journey time.

Invalid city, invalid scenario, artifact traversal and disconnected vehicle queries were rejected. Each was followed by successful status recovery; no unexpected host/tool failure occurred.

Both scenarios reported zero teleports, collisions and incompatible-signal warnings. Nevertheless, source warnings identify limited route choice, warm-up uncertainty and potentially unrealistic multilane-roundabout queues. No fresh field validation/calibration or new random demand generation occurred. Another municipality must supply licensed, dated geometry with CRS, lane restrictions, signal timing, demand, independent observations and validated initialization/calibration. No current forecast, observed causal effect, safety/emissions result, city ranking or independent third-person replication is established; product qualification remains pending.

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