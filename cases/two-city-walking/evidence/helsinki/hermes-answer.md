All tool calls complete. Now I will write the final municipal brief.

---

# HELSINKI SCHOOL-TO-LIBRARY WALKING ACCESSIBILITY
## Independent Municipal Review -- Hermes Agent, 2026-11-10

---

## TOOL-CALL TRACE (Steps 1-5 Summary)

### Step 1: Case Discovery, Snapshot, Graph Identity, Catalog

The municipal_walking_review prompt was successfully retrieved from the host.
Its text is: "Review helsinki: discover recipe; restore the snapshot; inspect graph, schools and libraries; run the 1200 m baseline at assumed 4.8 km/h; read the CSV and keyed routes; inspect snap exclusions and disconnected paths; run one declared bidirectional link closure and compare; render/export evidence. Report mapped school objects, never population or pupils. Preserve the core/buffer bounds, input identity, ODbL attribution and all limitations. Make an exploratory municipal recommendation and state what field validation would be needed."

Snapshot restored at 2026-11-10T13:26:57.775732+00:00.
Graph: 111,650 nodes, 247,056 directed edges, CRS epsg:4326, bidirectional unsimplified OSMnx walk, 1,264 weak components (largest: 96,886 nodes). Directed edge total length: 2,749,732.5 m (counts reciprocal pairs; not unique street length).
Snapshot manifest SHA-256: 6a71ce0b324b31b95c0baadffc19cb1d711aa34a44db60d699987796981fe673

Feature catalog: 121 total objects (90 school, 31 library). Coordinates are representative points computed in the local projected CRS (EPSG:3067) then converted to EPSG:4326 -- not verified entrances. Polygon and MultiPolygon objects use a representative point, not a centroid. 48 school objects have their representative point inside the 2 km study core (denominator). 31 library objects are in the 4 km buffered acquisition area. 1 library has access=yes in OSM (Rajatiedon kirjasto, node/12997901856); 30 have access=unknown. The access=yes OSM tag is not independently verified public admission.

One quality flag: representative_points_outside_buffer = 1. This means exactly one mapped object's representative point fell outside the buffered acquisition polygon. This is not a count of rejected snaps or core schools.

### Step 2: Baseline Run agent-baseline

Parameters: threshold 1200 m, speed 4.8 km/h (assumed constant, never measured).
Denominator: 48 mapped OSM school objects whose representative point is in the study core (not population, not pupils, not residents).

  origin_count:        48  (all school objects in core)
  routed_count:        46  (found a network path to some library)
  within_threshold:    45  (nearest routed library <= 1200 m total)
  outside_threshold:    1  (routed, but nearest library > 1200 m)
  unreachable:          2  (no network path found to any library)
  snap_rejected:        0  (no origin rejected for snap > 150 m)

within_share_of_all_origins: 0.9375 (45/48)

The CSV artifact SHA-256: 0091c35f0e99e41afc05fbe362248dd901e7a08b94519a841ae4413fe9950a1f
Routes GeoJSON SHA-256: dc6dad4faf67829f6ba52b7b9b144251b5a08fee400582f70b63db328b599e7c
Summary JSON SHA-256: 834ea2fbaafc2b920caff1c37d5afcdceb4b416a96c69bb1c3ddd7a93be706b7

The CSV first route entry: node/1017984720 (Helsingin kuvataidelukio) -> node/12997901856 (Rajatiedon kirjasto), network_m=403.71, origin_snap=10.31 m, dest_snap=7.15 m, total_m=421.16, within_threshold=True.

### Step 3: Route, Snap, Node, Edge, Isochrone Inspection

Origin node/1017984720 (Helsingin kuvataidelukio, OSM Point):
  Snap: nearest graph node 1012942235 at 10.33 m (accepted; max 150 m).
  Node 1012942235: lon=24.9520217, lat=60.1751435, street_count=2, outgoing neighbors=[409705353, 409705354].

Two shortest paths returned (k=2):
  Path 1: 27 nodes, all edges key=0, network_m=403.71 m, total_m=421.16 m
  Path 2: 27 nodes, diverges at one mid-segment pair (391448664->355153148 vs. 391448669->12106869679->391448665), network_m=404.04 m, total_m=421.49 m
  Both paths share the same start and end. The difference (0.33 m) reflects the unsimplified shape-point graph.

The route tool measures graph-shortest-path walking distance only. It does not measure actual travel time, signal delays, crossing safety, stairs accessibility, or service quality. Speed of 4.8 km/h is an assumed scenario constant applied uniformly.

Suggested closure edge (u=501610897, v=5912225309, key=0):
  highway=steps, surface=concrete, oneway=false, reversed=true, length=4.27 m
  Node 501610897: lon=24.9534885, lat=60.1835149, street_count=1 (a dead-end node with one outgoing neighbor: 5912225309).

Isochrone from same origin at 1200 m budget: 10,692 reachable graph nodes after subtracting the 10.33 m origin connector. This is a count of reachable graph nodes (including shape points), not a geographic coverage polygon, population estimate, or service area.

### Step 4: Closure Scenario agent-closure

Closed pair: u=501610897, v=5912225309 (bidirectional steps link, OSM way 626242711, 4.27 m).
Removed directed edges: [501610897, 5912225309, key=0] and [5912225309, 501610897, key=0].
This is a hypothetical robustness stress-test, not a report of actual or planned works.

Closure results:
  origin_count:        48
  routed_count:        46
  within_threshold:    40  (was 45 in baseline; change = -5)
  outside_threshold:    6  (was 1; change = +5)
  unreachable:          2  (unchanged)
  snap_rejected:        0  (unchanged)
  within_share:         0.8333 (was 0.9375)

Closure CSV SHA-256: 04ec8cec8305ad8cc144b06ae9131d22ac8d30a4d2d5c5611ac34c0718834b9d

Comparison (walking_compare):
  11 school objects affected (extra distance required to reach nearest library).
  0 origins lost reachability (all 11 still found some library route).
  5 of the 11 crossed the 1200 m threshold (within_threshold changed True->False).

Affected origins and detour distances (from compare artifact):
  node/1017984829  (Kallion lukio):         +556.3 m (threshold crossed: True->False)
  node/8862204483  (Suomen Diakoniaopisto): +279.5 m (threshold crossed: True->False)
  node/8862204485  (SKY-Opisto):            +279.5 m (threshold crossed: True->False)
  way/1038696462   (Vallilan ala-asteen koulu, väistötila): +493.9 m (threshold crossed: True->False)
  way/128161235    (HEO: Portsi):           +431.7 m (threshold crossed: True->False)
  way/139225450    (Helsingin kuvataidelukio polygon): +87.0 m (stayed within threshold)
  way/34069317     (Kallion ala-aste):      +530.2 m (stayed within threshold per closure CSV: total=830.6 m)
  way/37295003     (Kallion lukio polygon): +649.0 m (stayed within threshold)
  way/37296704     (Aleksis Kiven peruskoulu): +376.1 m (stayed within threshold)
  way/38192458     (Suomen Diakoniaopisto Alppikadun kampus): +284.9 m (stayed within threshold)
  way/592362656    (Åshöjdens grundskola):  +233.9 m (stayed within threshold)

### Step 5: Map, GraphML, Prompt, Invalid Snap

Map rendered (baseline): map.png, 665,545 bytes,
  SHA-256: e81a86642bd1500f0f712608e736d96f90a99b58d451621cb880e13338f16ad5

GraphML exported: network.graphml, 95,455,038 bytes,
  SHA-256: 2ea8f1570dfea012a77bd7a7ab0f1042e73660c06e6454cadd8df5f63de495d5
  (Matches snapshot input network.graphml SHA-256; topology verified by reload.)

Municipal review prompt: successfully retrieved (see Step 1 above).

Invalid snap test: coordinates (-33.868, 151.209) -- Sydney, Australia -- submitted to helsinki snap operation. Returned error: "coordinate is outside the buffered study area". The snap tool enforces a geographic boundary check and rejects coordinates that do not fall within the buffered acquisition area, before any nearest-node search. This prevents silently misleading results from off-target queries.

---

## FINAL MUNICIPAL BRIEF (~900 words)

### Helsinki School-to-Library Walking Access -- Exploratory Summary

STUDY SCOPE AND INPUT IDENTITY

Data source: OpenStreetMap contributors, license ODbL-1.0 (https://opendatacommons.org/licenses/odbl/1-0/).
Attribution: (c) OpenStreetMap contributors; https://www.openstreetmap.org/copyright
Snapshot acquired: 2026-11-10T13:26:57 UTC.
Manifest SHA-256: 6a71ce0b324b31b95c0baadffc19cb1d711aa34a44db60d699987796981fe673
Recipe SHA-256: f5c2d45958c56483f121433c02fb65642a844057234930514bfab106ae4350e7
Implementation SHA-256: e6ae49345b1f87315163ef06855ec92528ae435c44bd5bd63726268bdbd61be0

Study area: central 2 km disk around 60.1719 N, 24.9414 E (Helsinki), plus 2 km network buffer. This is not the complete municipal territory.

The analysis covers OSM-mapped amenity=school and amenity=library objects only. This is not an authoritative facility register. Multiple OSM objects may represent one campus and are not silently deduplicated. All coordinates for polygon and MultiPolygon objects are representative points computed in EPSG:3067 then converted to EPSG:4326 -- not verified entrances or main gates.

BASELINE FINDINGS (run_id: agent-baseline)

Denominator: 48 mapped OSM school objects whose representative point falls in the 2 km study core. This count refers to mapped objects, not pupils, students, residents or service capacity.

Of the 48:
- 46 were routed to some library on the pedestrian network.
- 45 had a nearest routed library within 1200 m (combined network path plus both snap connectors).
- 1 was routed but outside the 1200 m threshold.
- 2 were unreachable (no connected network path to any library was found).
- 0 were snap-rejected (no origin exceeded the 150 m maximum snap distance).

The 1200 m threshold and 4.8 km/h walking speed are explicit scenario assumptions, not measured values. Estimated minutes in the CSV use this assumed constant speed uniformly across all segments including snap connectors.

Snap connectors are straight-line distances from representative points to the nearest graph node; they are not verified walking paths. The unsimplified OSMnx graph has 111,650 nodes, including shape points; node count is not an intersection count.

30 of 31 library objects in the acquisition buffer have access=unknown in OSM. Only 1 (Rajatiedon kirjasto, node/12997901856) has access=yes. Even that tag has not been independently verified as public admission. The model routes to all 31 regardless; actual admission status is unknown.

HYPOTHETICAL CLOSURE SCENARIO (run_id: agent-closure)

Closed link: OSM node pair u=501610897, v=5912225309 (OSM way 626242711, highway=steps, surface=concrete, 4.27 m). Both directed edges and all parallel edges were removed. This is a reproducible stress-test on the graph, not a report of actual or planned infrastructure works.

After closure:
- within_threshold dropped from 45 to 40 (-5 objects).
- outside_threshold rose from 1 to 6 (+5 objects).
- unreachable remained at 2 (no change).
- 11 school objects required a longer detour to their nearest library.
- 0 of the 11 lost all reachability; all found alternative routes.
- The 5 objects newly outside the threshold had detours of +279.5 m to +556.3 m above their baseline nearest-library distance.

The compare operation confirmed: removing edges cannot shorten shortest paths; all detour distances are non-negative.

WHAT THE OUTPUTS MEASURE AND DO NOT MEASURE

The route lengths are graph shortest-path distances; they are not observed walking times, do not account for traffic signals, pedestrian crossings, staircase accessibility, locked gates, seasonal conditions or opening hours. The 1264 weak components are reported as a topology fact; causes are unknown from the graph alone. The isochrone result (10,692 reachable nodes from one origin at 1200 m) is a count of graph nodes, not a geographic coverage area, resident count or service catchment polygon.

ARTIFACTS AND RECEIPTS

Run agent-baseline:
  summary.json SHA-256:  834ea2fbaafc2b920caff1c37d5afcdceb4b416a96c69bb1c3ddd7a93be706b7
  accessibility.csv SHA: 0091c35f0e99e41afc05fbe362248dd901e7a08b94519a841ae4413fe9950a1f
  routes.geojson SHA:    dc6dad4faf67829f6ba52b7b9b144251b5a08fee400582f70b63db328b599e7c
  map.png SHA-256:       e81a86642bd1500f0f712608e736d96f90a99b58d451621cb880e13338f16ad5
  network.graphml SHA:   2ea8f1570dfea012a77bd7a7ab0f1042e73660c06e6454cadd8df5f63de495d5

Run agent-closure:
  accessibility.csv SHA: 04ec8cec8305ad8cc144b06ae9131d22ac8d30a4d2d5c5611ac34c0718834b9d

EXPLORATORY FINDING

The model found 2 of 48 core school objects unreachable on the pedestrian graph to any library in the acquisition buffer, and 1 within threshold but at distance greater than 1200 m. The cause of unreachability (component isolation, snap failure, or buffer edge) cannot be determined from artifact counts alone and requires field investigation.

The 4.27 m steps link (u=501610897, v=5912225309) used 11 baseline routes. Its hypothetical removal pushed 5 more school objects outside the 1200 m threshold. This concentration of routes on a short steps segment is a network-structure observation that could inform field prioritisation, but the steps' actual physical state, accessibility status and whether alternative routes are walkable in practice are unknown.

NEXT INVESTIGATION

Field verification of the 2 unreachable and 1 outside-threshold school objects: confirm whether the unreachability is a network-mapping gap or a genuine physical barrier. Survey the steps link (OSM 626242711) for physical condition and usability. Cross-check the 31 OSM library objects against the official Helsinki library register for completeness, admission status and operating hours. Verify representative points against actual entrance locations. None of these findings support a claim about wheelchair access, citywide coverage, actual travel times or observed service disruption.
