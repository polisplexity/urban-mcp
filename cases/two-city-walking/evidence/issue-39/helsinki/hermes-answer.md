All evidence gathered. Now writing the full municipal brief.

---

## Step 6: Municipal Brief

### HELSINKI WALKING ACCESSIBILITY REVIEW
#### Independent Municipal Review v2 — Host: hermes

---

### 1. Study Identity, Boundary and Source Limitations

Recipe ID: two-city-walking
Snapshot acquired: 2026-11-10T13:26:57.775732+00:00
Snapshot manifest SHA-256: 6a71ce0b324b31b95c0baadffc19cb1d711aa34a44db60d699987796981fe673
Recipe SHA-256: f5c2d45958c56483f121433c02fb65642a844057234930514bfab106ae4350e7
Implementation SHA-256: a2d4ddf61f6f1ca6ae547b33e6962386281a5412c9d308c831b964d81969153d
OSMnx: 2.1.1 / Python 3.12.14

Study boundary: Central 2 km disk centered at lon 24.9414, lat 60.1719 (Helsinki geographic ID 091). Graph extends to a 2 km network buffer (4 km total radius from center) to reduce boundary effects. This is NOT the full municipal territory of Helsinki.

Denominator: 48 OSM-mapped amenity=school objects whose representative point falls inside the 2 km study core. This counts mapped objects, not educational facilities, campuses, school-age population or pupils served. Multiple objects may represent a single physical campus; no silent deduplication was performed.

Feature catalog: 121 OSM features total (90 school objects, 31 library objects). 48 school objects are in-core. All 31 library objects are accepted; none snap-rejected; 1 library point falls outside the network buffer (Suomenlinnan kirjasto, an island location). 30 of 31 libraries have access=unknown — this is not confirmed public admission; only Rajatiedon kirjasto has access=yes (OSM-tagged, unverified).

Graph: 111,650 nodes; 247,056 directed edges; 1,264 weak components; largest component 96,886 nodes. CRS: EPSG:4326 (analysis in EPSG:3067). Model: bidirectional unsimplified OSMnx walk. Orientation entropy: 3.544 nats.

Source limitations (verbatim from recipe):
- Central 2 km disk only, not complete municipal territory
- OSM amenity=school/library objects, not authoritative facility registers
- Polygon representative points and graph snap nodes, not verified entrances; snaps over 150 m rejected
- Bidirectional walk model; directional foot rules, barriers, stairs, slope, winter, wheelchair not fully modeled
- 1200 m and 4.8 km/h are explicit scenario assumptions, not measured
- Denominator is mapped objects, never population or pupils
- Closures are hypothetical robustness tests, not observed works or forecasts

The municipal_walking_review prompt is exposed and was retrieved. It instructs: use walking_compare threshold_crossings and per-school flags, not detour size; inspect walking_route closed_links annotations before claiming any alternative is closure-safe; preserve ODbL attribution and all limitations.

---

### 2. Baseline Counts (run: agent-baseline, threshold 1200 m, 4.8 km/h)

Origins (core school objects): 48
Snap-rejected: 0
Unreachable: 2 (way/445933783 Etu-Töölön lukio; way/725256831 Helsingin eurooppalainen koulu — both disconnected from the graph's main component, reason not independently determined)
Routed: 46
Within threshold (<=1200 m): 45
Outside threshold: 1 (way/536980461 Etelä-Hesperiankadun väistötilat, 1467.5 m to Töölön kirjasto)
Within-threshold share of all 48 origins: 93.75%

Suggested closure from baseline: u=501610897, v=5912225309 (11 baseline routes use this link)
Closed link OSM edge: highway=steps, surface=concrete, osmid=626242711, length=4.27 m. Node 501610897 has street_count=1 and only one outgoing neighbor (5912225309), marking it as a dead-end shape point on the stair segment.

Baseline CSV artifact SHA-256: 0091c35f0e99e41afc05fbe362248dd901e7a08b94519a841ae4413fe9950a1f
Routes GeoJSON artifact SHA-256: dc6dad4faf67829f6ba52b7b9b144251b5a08fee400582f70b63db328b599e7c
Map PNG SHA-256: e81a86642bd1500f0f712608e736d96f90a99b58d451621cb880e13338f16ad5
GraphML SHA-256: 2ea8f1570dfea012a77bd7a7ab0f1042e73660c06e6454cadd8df5f63de495d5 (95,455,038 bytes; not reloaded, receipt only)

---

### 3. Closure Scenario (run: agent-closure)

Closure declared: {u:501610897, v:5912225309} — both directions and all parallel edges removed. The removed directed edges were [501610897,5912225309,0] and [5912225309,501610897,0].

Within threshold after closure: 40 (down from 45)
Outside threshold after closure: 6 (up from 1)
Unreachable: 2 (unchanged)

Closure CSV artifact SHA-256: 04ec8cec8305ad8cc144b06ae9131d22ac8d30a4d2d5c5611ac34c0718834b9d

---

### 3. Compare Results: Threshold Crossings and Affected Schools

Walking_compare diagnostics_version: 2.0

THRESHOLD CROSSINGS (crossed_threshold=true, within_to_outside):

5 origin IDs explicitly flagged:

1. node/8862204483 — Suomen Diakoniaopisto
   Before: way/20010806 (Kallion kirjasto), 961.73 m, within=true
   After:  node/7784183480 (Kotimaisten kielten keskuksen arkisto), 1241.22 m, within=false
   Extra: +279.50 m | Destination changed: yes | Baseline route uses closed link: YES (edge 5912225309->501610897, key 0, 4.27 m) | Scenario route uses closed link: no

2. node/8862204485 — SKY-Opisto
   Before: way/20010806 (Kallion kirjasto), 958.82 m, within=true
   After:  node/7784183480 (Kotimaisten kielten keskuksen arkisto), 1238.32 m, within=false
   Extra: +279.50 m | Destination changed: yes | Baseline route uses closed link: YES | Scenario route uses closed link: no

3. way/1038696462 — Vallilan ala-asteen koulu, väistötila
   Before: way/20010806 (Kallion kirjasto), 977.96 m, within=true
   After:  node/7784183480 (Kotimaisten kielten keskuksen arkisto), 1471.87 m, within=false
   Extra: +493.91 m | Destination changed: yes | Baseline route uses closed link: YES | Scenario route uses closed link: no

4. way/38192458 — Suomen Diakoniaopisto Alppikadun kampus
   Before: way/20010806 (Kallion kirjasto), 1055.25 m, within=true
   After:  node/7784183480 (Kotimaisten kielten keskuksen arkisto), 1340.13 m, within=false
   Extra: +284.88 m | Destination changed: yes | Baseline route uses closed link: YES | Scenario route uses closed link: no

5. way/592362656 — Åshöjdens grundskola
   Before: way/20010806 (Kallion kirjasto), 1058.54 m, within=true
   After:  way/128611004 (Vallilan kirjasto), 1292.43 m, within=false
   Extra: +233.89 m | Destination changed: yes | Baseline route uses closed link: YES | Scenario route uses closed link: no

AFFECTED STILL WITHIN THRESHOLD (affected=true, within_to_within, crossed_threshold=false):

6 origin IDs — detour increased but threshold not crossed:

- node/1017984829 — Kallion lukio: 225.86 m -> 782.19 m (+556.34 m); dest changed (Kallion kirjasto -> Kavi kansallinen audiovisuaalinen instituutti kirjasto); baseline uses closed link; still within
- way/128161235 — HEO: Portsi: 237.85 m -> 669.53 m (+431.67 m); dest changed; baseline uses closed link; still within
- way/139225450 — Helsingin kuvataidelukio (Polygon): 440.90 m -> 527.91 m (+87.01 m); dest changed; baseline uses closed link; still within
- way/34069317 — Kallion ala-aste: 300.40 m -> 830.56 m (+530.16 m); dest changed; baseline uses closed link; still within
- way/37295003 — Kallion lukio (Polygon): 153.97 m -> 803.00 m (+649.04 m); dest changed; baseline uses closed link; still within
- way/37296704 — Aleksis Kiven peruskoulu: 632.16 m -> 1008.21 m (+376.06 m); dest changed; baseline uses closed link; still within

NEWLY UNREACHABLE: None.

TRANSITION COUNTS:
- within_to_within: 40
- within_to_outside: 5
- unreachable_to_unreachable: 2
- outside_to_outside: 1

Baseline routes using closed link: 11 origin IDs:
node/1017984829, node/8862204483, node/8862204485, way/1038696462, way/128161235, way/139225450, way/34069317, way/37295003, way/37296704, way/38192458, way/592362656

Scenario routes using closed link: 0 (empty list — the closed link is absent from the closure graph so no scenario route traverses it).

The annotated closed edge in all baseline_closed_edges_used is the REVERSE direction: (5912225309 -> 501610897, key 0, 4.27 m). This is the direction traversed on the way from these schools toward Kallion kirjasto. Bidirectional closure removes both (501610897->5912225309) and (5912225309->501610897).

---

### 4. Original-Graph Route Test: node/1017984829 -> way/20010806

Origin: node/1017984829 (Kallion lukio, point object)
Destination from baseline CSV: way/20010806 (Kallion kirjasto)
Closed links declared to walking_route: [{u:501610897, v:5912225309}]

Rank 1 path:
  network_m: 202.85 m; total_m: 225.86 m
  uses_closed_link: TRUE
  avoids_all_declared_closed_links: false
  closed_edges_used: [{u:5912225309, v:501610897, key:0, length:4.27 m}]
  (Enters the closed link in the reverse direction 5912225309->501610897)

Rank 2 path:
  network_m: 206.65 m; total_m: 229.65 m
  uses_closed_link: TRUE
  avoids_all_declared_closed_links: false
  closed_edges_used: [{u:5912225309, v:501610897, key:0, length:4.27 m}]

Path overlap (ranks 1 and 2):
  shared_directed_keyed_edge_count: 23 out of 25-26 total edges; shared_physical_link_count: 23
  directed_keyed_edge_disjoint: false; physical_link_disjoint: false

path_ranks_avoiding_declared_closed_links: [] (EMPTY — neither rank avoids the closed link)

Interpretation: Both k=2 original-graph alternatives use the closed stair link. Neither constitutes a closure-safe route. These are annotations on the original graph, not a re-solve. The actual modeled rerouting (longer, to Kavi kirjasto, 782.19 m) is properly represented only in the agent-closure run, as confirmed by the compare output for node/1017984829 (within_to_within, destination changed).

No claim is made that either ranked route survives closure — both explicitly use the removed pair.

---

### 5. Inspection Exercises

Snap test (node/1017984829 coordinates): snapped to node 8852622700 at 9.80 m — accepted (well within 150 m limit).

Remote coordinate rejection test: coordinates (lat=51.5, lon=0.0) — correctly rejected with "coordinate is outside the buffered study area". Remote rejection confirmed.

Node 501610897: lon=24.9534885, lat=60.1835149, street_count=1, sole outgoing neighbor=5912225309. This is a dead-end graph node attached to a stair segment.

Edge (501610897->5912225309, key 0): highway=steps, surface=concrete, oneway=false (OSMnx reversed=true), osmid=626242711, length=4.266 m. This short stair segment is the closed link; closure of a 4.27 m stairway triggers significant rerouting for 11 schools, illustrating how the centrally-located Kallion kirjasto is accessed by many nearby schools via a narrow pedestrian stair shortcut that has no close parallel.

Network stats: 111,650 nodes; 247,056 directed edges; 1,264 weak components; largest component 96,886 nodes; orientation entropy 3.544 nats (note: unsimplified graph, nodes include shape points, directed length 2,749,732.5 m counts reciprocal pairs).

Isochrone from node/1017984829 coordinates (budget 1200 m, snap deducted): 10,480 reachable graph nodes, max total 1199.995 m. This is a node count, not a coverage polygon or population estimate.

Baseline map rendered: map.png, 665,545 bytes, SHA-256 e81a86642bd1500f0f712608e736d96f90a99b58d451621cb880e13338f16ad5. Binary stays in workspace; not reprinted here.

GraphML exported: network.graphml, 95,455,038 bytes, SHA-256 2ea8f1570dfea012a77bd7a7ab0f1042e73660c06e6454cadd8df5f63de495d5. Receipt obtained; file not reloaded or parsed — only the export receipt is confirmed.

Municipal review prompt: exposed as "municipal_walking_review" and successfully retrieved. Prompt text instructs: use threshold_crossings and per-school flags (not detour size), inspect closed_links annotations in walking_route before claiming closure-safety, preserve ODbL attribution and limits, make exploratory recommendation with field validation needs stated.

---

### 6. Concise Municipal Brief (<=900 words)

HELSINKI WALKING ACCESSIBILITY — CENTRAL STUDY ZONE
Hypothetical Stair Closure Scenario | OSM Snapshot 2026-11-10

BASELINE (agent-baseline, 1200 m, 4.8 km/h assumed):
48 mapped school objects in the 2 km central core. 46 routed, 2 unreachable (Etu-Töölön lukio and Helsingin eurooppalainen koulu — isolated in separate graph components). 45 of 48 (93.75%) modeled within 1200 m of a nearest mapped library. One school (Etelä-Hesperiankadun väistötilat) was already outside threshold at 1467.5 m.

CLOSURE SCENARIO (agent-closure):
Hypothetical removal of link {501610897, 5912225309} — a 4.27 m OSM stairway (highway=steps, surface=concrete, osmid=626242711) near Kallion kirjasto. This link appeared in 11 of 46 routed baseline paths, suggesting it is a critical pedestrian shortcut connecting the Kallio neighborhood schools to their nearest library.

Impact: within-threshold count falls from 45 to 40. Five additional schools lose the threshold:
- Suomen Diakoniaopisto (node/8862204483): 962 m -> 1241 m
- SKY-Opisto (node/8862204485): 959 m -> 1238 m
- Suomen Diakoniaopisto Alppikadun kampus (way/38192458): 1055 m -> 1340 m
- Åshöjdens grundskola (way/592362656): 1059 m -> 1292 m (reroutes to Vallilan kirjasto)
- Vallilan ala-asteen koulu, väistötila (way/1038696462): 978 m -> 1472 m (largest detour: +494 m)

Six additional schools are affected but remain within threshold (detour 87–649 m). No schools become unreachable.

The closed link is traversed in the reverse direction (5912225309->501610897) in all 11 baseline routes; the scenario correctly routes around it in every case (scenario_route_uses_closed_link=false for all origins).

Original-graph k=2 route test for node/1017984829 (Kallion lukio, baseline destination way/20010806 Kallion kirjasto): both rank 1 and rank 2 paths use the closed stair. Neither avoids_all_declared_closed_links. path_ranks_avoiding_declared_closed_links is empty. This confirms the stair has no close k-shortest alternative on the original graph for this origin-destination pair. The closure scenario's actual modeled rerouting (to Kavi kansallinen audiovisuaalinen instituutti kirjasto, 782 m) must be treated as the authoritative result, not these annotated original-graph paths.

METHODOLOGICAL NOTES:
All threshold crossings are taken directly from walking_compare's crossed_threshold and threshold_transition fields — not inferred from detour size. A large detour alone does not establish a crossing. The five crossings are the only objects with crossed_threshold=true; the six affected-within objects have crossed_threshold=false and are reported separately. Snap connectors are unverified straight-line estimates. All destinations have access=unknown except Rajatiedon kirjasto (access=yes, unverified admission). Library multiplicity in OSM is high (multiple nodes/polygons for the same institution); no deduplication was performed. The 2-km study disk excludes most of Helsinki's area; these findings do not generalise to the city.

NEXT INVESTIGATION:
The OSM stairway (osmid=626242711, highway=steps) near Kallion kirjasto is a single point of dependency for 11 modeled routes in this central zone. Field validation would include: (1) confirming the stair physically exists and is publicly accessible, (2) verifying that all five crossing schools' nearest alternative library is correctly identified by OSM (the model reroutes most to Kotimaisten kielten keskuksen arkisto, whose access=unknown), (3) checking whether any parallel informal paths exist that are absent from OSM, and (4) verifying the two persistently unreachable schools' graph disconnection cause (possible ferry/island-related isolation). A scenario with a secondary stair or bridge crossing added to the graph could test whether the threshold crossings are reversible by infrastructure addition.

ODbL Attribution: (C) OpenStreetMap contributors; https://www.openstreetmap.org/copyright | License: ODbL-1.0 | https://opendatacommons.org/licenses/odbl/1-0/

---

### Machine-Readable JSON Summary

```json
{
  "city": "helsinki",
  "crossed_threshold_origin_ids": [
    "node/8862204483",
    "node/8862204485",
    "way/1038696462",
    "way/38192458",
    "way/592362656"
  ],
  "affected_still_within_origin_ids": [
    "node/1017984829",
    "way/128161235",
    "way/139225450",
    "way/34069317",
    "way/37295003",
    "way/37296704"
  ],
  "newly_unreachable_origin_ids": [],
  "baseline_routes_using_closed_link_origin_ids": [
    "node/1017984829",
    "node/8862204483",
    "node/8862204485",
    "way/1038696462",
    "way/128161235",
    "way/139225450",
    "way/34069317",
    "way/37295003",
    "way/37296704",
    "way/38192458",
    "way/592362656"
  ],
  "scenario_routes_using_closed_link_origin_ids": [],
  "route_origin_id": "node/1017984829",
  "path_membership": [
    {
      "rank": 1,
      "uses_closed_link": true,
      "avoids_all_declared_closed_links": false
    },
    {
      "rank": 2,
      "uses_closed_link": true,
      "avoids_all_declared_closed_links": false
    }
  ],
  "path_ranks_avoiding_declared_closed_links": []
}
```

---

### Artifact Receipt Summary

| Artifact | Run | SHA-256 |
|---|---|---|
| accessibility.csv | agent-baseline | 0091c35f0e99e41afc05fbe362248dd901e7a08b94519a841ae4413fe9950a1f |
| routes.geojson | agent-baseline | dc6dad4faf67829f6ba52b7b9b144251b5a08fee400582f70b63db328b599e7c |
| accessibility.csv | agent-closure | 04ec8cec8305ad8cc144b06ae9131d22ac8d30a4d2d5c5611ac34c0718834b9d |
| map.png | agent-baseline | e81a86642bd1500f0f712608e736d96f90a99b58d451621cb880e13338f16ad5 |
| network.graphml | agent-baseline | 2ea8f1570dfea012a77bd7a7ab0f1042e73660c06e6454cadd8df5f63de495d5 |
| snapshot manifest | helsinki | 6a71ce0b324b31b95c0baadffc19cb1d711aa34a44db60d699987796981fe673 |
