All tools exercised. Now I compile the full structured report.

---

AMSTERDAM INDEPENDENT MUNICIPAL WALKING REVIEW v2
host: hermes
date: 2026-11-10

====================================================================
SECTION 1: DISCOVERY, IDENTITY AND BOUNDARY
====================================================================

RECIPE (locked snapshot restored 2026-11-10T13:18:41Z)
  Recipe SHA-256:        f5c2d45958c56483f121433c02fb65642a844057234930514bfab106ae4350e7
  Snapshot manifest SHA: 3c2c8dce71deeac129471de1e1a0ce3d8fb17de772b5316288a53f4ac3538e34
  network.graphml SHA:   c76f0abd5b41962ce4722ad0e969d9fb78bb49b3f05374ab4c760d363837f44e
  Source:                OpenStreetMap contributors, ODbL-1.0
  OSMnx:                 2.1.1 / Python 3.12.14
  Analysis CRS:          EPSG:28992 (Rijksdriehoek)
  Geographic ID:         GM0363 (Amsterdam)
  Center:                lon 4.8936, lat 52.3731

STUDY BOUNDARY
  Core disk radius:      2000 m from center (the analysis denominator)
  Graph buffer:          additional 2000 m outward (reduces boundary edge effects)
  This is NOT the full municipal territory of Amsterdam. Routes longer than
  ~1200 m toward libraries near the buffer edge may be censored.

GRAPH IDENTITY
  Nodes:                 79,384
  Directed edges:        176,632
  Weak components:       468  (largest: 62,165 nodes)
  Model:                 bidirectional unsimplified OSMnx walk (EPSG:4326 storage)
  Orientation entropy:   3.557 nats (high, consistent with Amsterdam's canal grid)
  Directed length sum:   2,757,580 m (counts reciprocal edges; not unique street length)

FEATURE CATALOG
  Total OSM features harvested: 225 (across both cities)
  Amsterdam mapped:  schools 204 objects, libraries 21 objects
  Core school objects (denominator): 40
  Buffer libraries accepted: 20 (1 rejected: LLC node/432855895, access=private)
  Unknown access on accepted libraries: 20 (all others tagged unknown, NOT confirmed public)
  Snap-rejected schools/libraries: 0
  Representative points outside buffer: 3 (excluded from analysis)
  Geometry types: Points and Polygons (polygon centroids are representative points,
    not verified entrances; this is a methodological limitation)

SOURCE LIMITATIONS (verbatim from recipe)
1. Central 2 km disks, not complete municipal territories.
2. OSM mapped amenity=school/library objects, not an authoritative register.
   Multiple OSM objects may represent one campus; no deduplication.
3. Representative points and snap nodes are proxies, not verified entrances.
   Snap connectors are straight distances, not verified paths. Max snap 150 m.
4. Bidirectional walk model; directional foot rules, barriers, opening hours,
   crossings, stairs, slope, winter conditions, wheelchair access not fully modeled.
5. 1200 m and 4.8 km/h are explicit scenario assumptions, not measured values.
6. Denominator = mapped school objects in core, never population/pupils/capacity.
7. Closure scenario is hypothetical robustness test, not observed disruption.

====================================================================
SECTION 2: BASELINE RUN agent-baseline
====================================================================

Parameters: threshold_m=1200, speed_kph=4.8, closures=none
Implementation SHA: a2d4ddf61f6f1ca6ae547b33e6962386281a5412c9d308c831b964d81969153d

BASELINE COUNTS (40 origin school objects in core)
  Routed:            38
  Unreachable:        2  (way/427679639 Marcanti College,
                          way/670993791 Westerparkschool)
  Snap-rejected:      0
  Within threshold:  22  (55.0% of all 40 origins)
  Outside threshold: 16

ROUTES.GEOJSON (first feature sampled)
  Feature 1 origin:      node/13430642513 (De Burght)
  Destination:           node/2722023232 (NIOD)
  Network distance:      1230.0 m, total (inc. snaps): 1318.0 m
  First 5 directed edges from routes.geojson:
    (12842570837 -> 12842570838, key 0, 200.9 m)
    (12842570838 -> 46411497, key 0, 28.4 m)
    (46411497 -> 12842570839, key 0, 69.2 m)
    (12842570839 -> 12842570840, key 0, 75.2 m)
    (12842570840 -> 12842570841, key 0, 85.7 m)
  routes.geojson SHA:    595665cf37f72c248435726a67db02a7c8825d5f165d9360899b082c9515769a

SUGGESTED CLOSURE (from baseline): u=46386552, v=12534903767
  Used by 5 baseline routes

====================================================================
SECTION 3: CLOSURE SCENARIO agent-closure
====================================================================

Closure declared: {u:46386552, v:12534903767}
Removed directed edges: (12534903767,46386552,0) and (46386552,12534903767,0)
  [bidirectional removal of all parallel edges]

CLOSURE COUNTS
  Origin count:          40
  Routed:                38
  Within threshold:      22  (55.0% -- identical to baseline)
  Outside threshold:     16
  Unreachable:            2  (same two as baseline)
  Snap-rejected:          0

The aggregate within_threshold count did NOT change. The closure edge is on
the residential street Oudeschans (OSMid 7370719, 19.2 m long, paving_stones,
sidewalk left). Its removal forced detours but no school crossed the 1200 m
threshold boundary.

====================================================================
SECTION 4: walking_compare RESULTS
====================================================================

Using explicit threshold_crossings and schools fields (diagnostics v2.0):

THRESHOLD CROSSINGS: none
  threshold_crossings list is empty.
  crossed_threshold_origin_ids: []  (zero objects)

AFFECTED ORIGINS (5 objects whose route used the closed link):
All 5 show threshold_transition="within_to_within" and crossed_threshold=false.

Detailed per-affected-school data:

1. node/2725797085  Voorschool De Kleine Sint Antonius
   Destination before/after: node/13196135282 (Internet Archive Europe) / same
   total_m before: 290.6 m   within_before: True
   total_m after:  402.8 m   within_after:  True
   extra_distance: +112.1 m
   crossed_threshold: False   transition: within_to_within
   baseline_route_uses_closed_link: True  (edge 46386552->12534903767, key 0, 19.2 m)
   scenario_route_uses_closed_link: False

2. node/2741066971  De Witte Olifant (node)
   Destination before/after: node/13196135282 / same
   total_m before: 185.5 m   within_before: True
   total_m after:  513.7 m   within_after:  True
   extra_distance: +328.1 m
   crossed_threshold: False   transition: within_to_within
   baseline_route_uses_closed_link: True
   scenario_route_uses_closed_link: False

3. node/4446826076  Reinwardt Academie
   Destination before: node/13196135282 (Internet Archive Europe)
   Destination after:  node/2742996051  (Artis Bibliotheek) -- CHANGED
   total_m before: 1041.5 m  within_before: True
   total_m after:  1133.0 m  within_after:  True
   extra_distance: +91.4 m
   crossed_threshold: False   transition: within_to_within
   baseline_route_uses_closed_link: True
   scenario_route_uses_closed_link: False

4. way/904127355  De Witte Olifant (polygon A)
   Destination before/after: node/13196135282 / same
   total_m before: 296.9 m   within_before: True
   total_m after:  409.0 m   within_after:  True
   extra_distance: +112.1 m
   crossed_threshold: False   transition: within_to_within
   baseline_route_uses_closed_link: True
   scenario_route_uses_closed_link: False

5. way/904127931  De Witte Olifant (polygon B)
   Destination before/after: node/13196135282 / same
   total_m before: 225.3 m   within_before: True
   total_m after:  553.5 m   within_after:  True
   extra_distance: +328.1 m
   crossed_threshold: False   transition: within_to_within
   baseline_route_uses_closed_link: True
   scenario_route_uses_closed_link: False

TRANSITION COUNTS
  outside_to_outside:        16
  within_to_within:          22
  unreachable_to_unreachable: 2

NEWLY UNREACHABLE: none
LEFT THRESHOLD COVERAGE: none

BASELINE ROUTES USING CLOSED LINK (5):
  node/2725797085, node/2741066971, node/4446826076, way/904127355, way/904127931

SCENARIO ROUTES USING CLOSED LINK: none (0)
  Correct -- the closed link is removed from the scenario graph.

AFFECTED STILL WITHIN THRESHOLD (5):
  node/2725797085, node/2741066971, node/4446826076, way/904127355, way/904127931
  All five incurred detours but remained within 1200 m.

NOTE: The three "De Witte Olifant" entries (node/2741066971, way/904127355,
way/904127931) are distinct OSM objects mapped for what may be one campus.
These are separate mapped school objects, not the same physical school
triplicated. No deduplication is performed by the tool.

====================================================================
SECTION 5: ROUTE INSPECTION (Step 4)
====================================================================

walking_route(origin=node/2741066971, destination=node/13196135282, k=2,
              closed_links=[{u:46386552, v:12534903767}])

RANK 1
  Network distance: 160.3 m, total: 185.5 m
  Nodes: 46382990 -> 9117186306 -> 5657441661 -> 9117186305 -> 46384703 ->
         46385947 -> 452388610 -> 8241207445 -> 8241207444 -> 452388611 ->
         46386552 -> 12534903767 -> 46387306
  Key edges (12 total):
    (46382990,9117186306,0)  7.8 m
    (9117186306,5657441661,0) 23.5 m
    (5657441661,9117186305,0) 20.1 m
    (9117186305,46384703,0)  7.2 m
    (46384703,46385947,0)   51.7 m
    (46385947,452388610,0)   1.8 m
    (452388610,8241207445,0) 3.5 m
    (8241207445,8241207444,0) 6.1 m
    (8241207444,452388611,0)  1.3 m
    (452388611,46386552,0)   4.7 m
    (46386552,12534903767,0) 19.2 m  <-- CLOSED LINK
    (12534903767,46387306,0) 13.5 m
  uses_closed_link: True
  avoids_all_declared_closed_links: False

RANK 2
  Network distance: 259.1 m, total: 284.3 m
  Takes a longer loop through 836274952, 46386052, 8044660055, 836275193,
  46387305, 836275210 before rejoining at 46385947 and again using
  46386552->12534903767 (closed link).
  Key edges (18 total): adds 6 extra edges vs rank 1 through the loop,
    then rejoins and uses the same final 7 edges including the closed link.
  uses_closed_link: True
  avoids_all_declared_closed_links: False

PATH OVERLAP (ranks 1 & 2)
  shared_directed_keyed_edge_count: 11
  shared_physical_link_count: 11
  directed_keyed_edge_disjoint: False
  physical_link_disjoint: False

path_ranks_avoiding_declared_closed_links: []  (neither rank avoids the closed link)

INTERPRETATION: Both k-shortest paths on the original graph converge onto the
Oudeschans segment and use the closed link. This is an annotation on the
original graph -- it does NOT simulate closure. The agent-closure run already
models the actual rerouted result (total_m=513.7 m). The k=2 result confirms
the closed link lies on the dominant corridor; both original-graph alternatives
pass through it. Neither original-graph path can be called closure-safe.

====================================================================
SECTION 5: INFRASTRUCTURE INSPECTION EXERCISES
====================================================================

SNAP TEST (valid coordinate: lon 4.905, lat 52.371)
  Nearest node: 46382990 at 51.8 m, accepted (< 150 m limit)
  Node 46382990 at (4.9042669, 52.3708693)

REMOTE COORDINATE REJECTION (lon 25.0, lat 60.0 -- Helsinki area)
  Error: "coordinate is outside the buffered study area"
  Correctly rejected.

NODE INSPECTION (closure node 46386552)
  Location: lon 4.9045935, lat 52.3716588
  Street count: 3 (junction node)
  Outgoing neighbors: 46389402, 452388611, 12534903767

EDGE INSPECTION (u=46386552, v=12534903767, key=0)
  OSM ID:    7370719
  Highway:   residential
  Name:      Oudeschans
  Max speed: 30 km/h
  Oneway:    false
  Sidewalk:  left
  Surface:   paving_stones
  Length:    19.202 m (directed)
  Reversed:  false

ISOCHRONE (from node 46382990, budget 1200 m)
  Reachable graph nodes: 6,216
  Max total distance:    1199.97 m
  Sample nodes (20):     16568167, 25596477, 25752666, 26586270, 26586651...
  Caution: This is a graph-node count, not a population count or polygon.

MAP RENDER (agent-baseline)
  map.png: 784,880 bytes
  SHA-256: 5d154ef0b4f47c0260b27b18f079510ffbbb5e8b22a535ccff9efcac4564796d
  File remains in mounted workspace (no attachment channel in CLI mode).

GRAPHML EXPORT (agent-baseline)
  network.graphml: 75,464,517 bytes
  SHA-256: c76f0abd5b41962ce4722ad0e969d9fb78bb49b3f05374ab4c760d363837f44e
  Note: SHA matches the input snapshot. The GraphML was exported to the
  workspace; this report does NOT claim it was reloaded or its topology
  verified beyond the tool's own topology check on export.

MUNICIPAL REVIEW PROMPT
  The prompt "municipal_walking_review" is exposed and was retrieved.
  Content (abbreviated): Review amsterdam -- discover recipe, restore snapshot,
  inspect graph/schools/libraries, run baseline, read CSV, inspect closures,
  compare, render/export. Use threshold_crossings and school flags, not detour
  size. Report mapped school objects, not population.
  (Full prompt confirmed accessible on this host.)

REPORT.MD SHA: 9629cf17409352956e4f68c469d253a9431e646ee548f9edf111461d03d9cea5
ACCESSIBILITY.CSV SHA (baseline): f246dca57b503e73746e272152a63933fcafdc12500b8aa7d14f4cf86c8fe575
ACCESSIBILITY.CSV SHA (closure):  83272b7213f3c4d3716981d780d5272a996aea08e891ff2167cd0bc1dde6dcf0

====================================================================
SECTION 6: CONCISE MUNICIPAL BRIEF
====================================================================

AMSTERDAM WALKING ACCESSIBILITY -- SCHOOL TO NEAREST LIBRARY
Municipal Review v2 | Host: hermes | Date: 2026-11-10

STUDY IDENTITY
Run baseline:  agent-baseline (threshold 1200 m, 4.8 km/h assumed)
Run closure:   agent-closure  (same, +closure u=46386552 v=12534903767)
Input manifest SHA: 3c2c8dce71deeac129471de1e1a0ce3d8fb17de772b5316288a53f4ac3538e34
Implementation SHA: a2d4ddf61f6f1ca6ae547b33e6962386281a5412c9d308c831b964d81969153d
© OpenStreetMap contributors; https://www.openstreetmap.org/copyright (ODbL-1.0)

SCOPE AND DENOMINATOR
The study covers a 2 km radius disk centered on Amsterdam (GM0363, EPSG:28992).
The denominator is 40 mapped OSM amenity=school objects whose representative
point falls in that disk -- not residents, not enrolled pupils, not campuses.
20 OSM library objects are accepted as destinations (1 rejected: access=private).
All access tags are "unknown" on accepted libraries; OSM tagging is not verified
admission evidence.

BASELINE (agent-baseline)
  Origins: 40 | Routed: 38 | Unreachable: 2 | Snap-rejected: 0
  Within 1200 m: 22 (55.0%) | Outside: 16
  Unreachable objects: way/427679639 (Marcanti College) and
                       way/670993791 (Westerparkschool) -- both isolated
                       on sub-components in the 468-component graph.

CLOSURE SCENARIO (agent-closure)
  Closed link: Oudeschans residential segment (OSM 7370719), 19.2 m,
               nodes 46386552 -- 12534903767. Bidirectional, paving_stones.
  Removed directed edges: (12534903767,46386552,0) and (46386552,12534903767,0)
  Result: Within 1200 m: 22 (unchanged). No threshold crossings.

THRESHOLD CROSSING ANALYSIS
  crossed_threshold_origin_ids: NONE
  No mapped school object crossed the 1200 m threshold in either direction.
  5 objects were affected (detoured) but all remained well within 1200 m.

AFFECTED STILL WITHIN THRESHOLD (5):
  node/2725797085 Voorschool De Kleine Sint Antonius (+112 m detour, 290->403 m)
  node/2741066971 De Witte Olifant (node)           (+328 m detour, 186->514 m)
  node/4446826076 Reinwardt Academie                (+91 m detour, 1042->1133 m;
                                                     dest. changed: Internet
                                                     Archive -> Artis Bibliotheek)
  way/904127355   De Witte Olifant (polygon)        (+112 m detour, 297->409 m)
  way/904127931   De Witte Olifant (polygon)        (+328 m detour, 225->553 m)

Note: node/2741066971, way/904127355, and way/904127931 are three distinct OSM
objects labeled "De Witte Olifant" and may represent the same campus. The tool
does not deduplicate.

BASELINE/SCENARIO ROUTE MEMBERSHIP
  Baseline routes using closed link: 5
    node/2725797085, node/2741066971, node/4446826076, way/904127355, way/904127931
  Scenario routes using closed link: 0 (correctly absent -- link removed)

ROUTE INSPECTION (node/2741066971 -> node/13196135282)
  Baseline destination: node/13196135282 (Internet Archive Europe)
  Rank 1: total 185.5 m; uses_closed_link=True; avoids=False;
    closed edge used: (46386552,12534903767,0) 19.2 m
  Rank 2: total 284.3 m; uses_closed_link=True; avoids=False;
    same closed edge used via longer loop
  Shared keyed edges (ranks 1&2): 11 of 12/18 edges
  path_ranks_avoiding_declared_closed_links: [] (zero ranks avoid it)
  Conclusion: Both original-graph alternatives pass through the closed link.
  Actual closure rerouting is modeled in agent-closure (total_m=513.7 m,
  still within threshold). Do not interpret k=2 paths as closure-safe routes.

ARTIFACTS
  map.png SHA:         5d154ef0b4f47c0260b27b18f079510ffbbb5e8b22a535ccff9efcac4564796d
  network.graphml SHA: c76f0abd5b41962ce4722ad0e969d9fb78bb49b3f05374ab4c760d363837f44e
  report.md SHA:       9629cf17409352956e4f68c469d253a9431e646ee548f9edf111461d03d9cea5
  accessibility.csv (baseline) SHA: f246dca57b503e73746e272152a63933fcafdc12500b8aa7d14f4cf86c8fe575
  accessibility.csv (closure)  SHA: 83272b7213f3c4d3716981d780d5272a996aea08e891ff2167cd0bc1dde6dcf0

PRACTICAL NEXT INVESTIGATION
The 2 persistently unreachable school objects (Marcanti College and
Westerparkschool) lie in isolated graph sub-components. Field validation
should check whether these buildings have pedestrian connections omitted
from OSM or are genuinely pedestrian-inaccessible (e.g., gated campuses,
construction sites). The 16 objects outside the threshold but routed suggest
a spatial cluster worth mapping: the Westpoort/buffer-edge schools reach
libraries only at >1200 m under the assumed speed; reducing the speed
assumption or adding a closer library mapping would shift that share.
Access tagging on the 20 "unknown" libraries should be ground-truthed before
any service-adequacy conclusion is drawn.

---

MACHINE-READABLE EVIDENCE JSON:

```json
{
  "city": "amsterdam",
  "crossed_threshold_origin_ids": [],
  "affected_still_within_origin_ids": [
    "node/2725797085",
    "node/2741066971",
    "node/4446826076",
    "way/904127355",
    "way/904127931"
  ],
  "newly_unreachable_origin_ids": [],
  "baseline_routes_using_closed_link_origin_ids": [
    "node/2725797085",
    "node/2741066971",
    "node/4446826076",
    "way/904127355",
    "way/904127931"
  ],
  "scenario_routes_using_closed_link_origin_ids": [],
  "route_origin_id": "node/2741066971",
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

====================================================================
END OF REVIEW
====================================================================
