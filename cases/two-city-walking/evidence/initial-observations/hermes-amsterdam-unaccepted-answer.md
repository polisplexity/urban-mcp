All artifacts collected. Now I write the full report.

---

# AMSTERDAM WALKING ACCESS REVIEW
# Municipal brief produced by hermes agent, 2026-11-10
# All findings are from MCP server urban_mcp_walking only.

---

## STEP 1 — Case discovery, snapshot restoration, graph identity and catalog

CASE IDENTITY
  Recipe ID:          two-city-walking
  Source:             OpenStreetMap contributors
  License:            ODbL-1.0
  License URL:        https://opendatacommons.org/licenses/odbl/1-0/
  Attribution:        c OpenStreetMap contributors; https://www.openstreetmap.org/copyright
  Recipe SHA-256:     f5c2d45958c56483f121433c02fb65642a844057234930514bfab106ae4350e7

SNAPSHOT RESTORE
  City:               Amsterdam (NL, geographic_id GM0363)
  Acquired at:        2026-11-10T13:18:41.849586+00:00
  OSMnx version:      2.1.1 / Python 3.12.14
  Manifest SHA-256:   3c2c8dce71deeac129471de1e1a0ce3d8fb17de772b5316288a53f4ac3538e34
  network.graphml:    c76f0abd5b41962ce4722ad0e969d9fb78bb49b3f05374ab4c760d363837f44e (75.5 MB)
  features.geojson:   2795b1ade271b9e3a9954af26a3cc753a370c679762549b3abd3063f9f176b74
  areas.geojson:      e5aca3fd7d0f9101d30a3a925fcbb864a954f0aac4ccd0fb0cb1a2844391ac2e

GRAPH IDENTITY (walking_graph_info)
  Nodes:              79 384
  Directed edges:     176 632
  CRS:                EPSG:4326 (geographic storage; analysis in EPSG:28992)
  Weak components:    468   <-- 468 disconnected sub-graphs exist in the buffer; the
                             largest has 62 165 nodes. Isolated ways/courtyards account
                             for the small components.
  Model:              bidirectional unsimplified OSMnx walk
  Edge attributes present include: highway, length, name, sidewalk, surface, foot,
                             oneway, oneway:foot, wheelchair, bridge, tunnel (22 attrs)
  Orientation entropy: 3.557 nats (high variety, consistent with a canal-structured city)
  Directed edge sum:  2 757 580 m (counts reciprocal pairs; not unique street length)

FEATURE CATALOG
  Schools in core (amenity=school, in_core=true):  40 mapped objects
    -- Mix of Point (node) and Polygon (way) OSM geometries
    -- All 40 have access=unknown; no OSM access restriction recorded
    -- Example Point objects: De Burght, Alan Turing School, Altra College Centrum
    -- Example Polygon objects: Barlaeus Gymnasium, Cartesius Lyceum, IJpleinschool
    -- NOTE: OSM contains 204 total school objects in full download; 40 fall inside
       the 2 km core disk. Multiple OSM objects may represent one physical campus.

  Libraries total (amenity=library, all):  21 mapped objects
    -- 11 have in_core=true; 10 are in the buffer only
    -- 1 library (LLC, node/432855895) has access=private; rejected from routing pool
    -- 20 libraries have access=unknown (OSM tag absent; not verified as public)
    -- Accepted for routing:  20 (21 minus the 1 private-access object)
    -- Notable public branches: OBA Oosterdok, OBA Spaarndammerbuurt,
       OBA Staatsliedenbuurt, OBA De Hallen, OBA Van der Pek, OBA Javaplein
    -- Specialist/research institutions also tagged library: Internet Archive Europe,
       NIOD, CEDLA Library, Bibliotheek Universiteit van Amsterdam

SNAP QUALITY CHECK (two sampled schools)
  De Burght (node/13430642513):
    Nearest network node: 12842570837
    Snap distance:        59.17 m  (accepted; limit 150 m)
  Alan Turing School (node/2492759886):
    Nearest network node: 46383340
    Snap distance:        38.49 m  (accepted)
  Node 46383340 details:  lon 4.9212641, lat 52.3709606, street_count 3
    Outgoing neighbors: [46380963, 46381202, 7801983596]

INTERPRETATION LIMITS (verbatim from recipe)
  - Central 2 km study disks only; not complete municipal territory
  - OSM amenity tags only; not an authoritative facility register
  - Representative points and nearest nodes are proxies, not verified entrances
  - General pedestrian network; barriers, crossings, slope, wheelchair access
    not fully modeled
  - 1200 m is an explicit scenario assumption; minutes use assumed constant 4.8 km/h
  - Denominator = mapped school objects in core, never population or pupils
  - Closures are hypothetical robustness tests, not observed works

PROMPT STATUS
  The host exposes a prompt named "municipal_walking_review" (confirmed via list_prompts
  and successfully retrieved via get_prompt). The prompt text directs: review Amsterdam,
  restore snapshot, inspect graph, run 1200 m baseline at 4.8 km/h, read CSV and routes,
  inspect exclusions, run a bidirectional closure, compare, render/export evidence.
  It explicitly says to report mapped school objects, preserve ODbL attribution and limits,
  and state what field validation would be needed.

---

## STEP 2 — Baseline run agent-baseline: counts and CSV interpretation

RUN PARAMETERS
  run_id:         agent-baseline
  threshold_m:    1200.0
  speed_kph:      4.8 (assumed constant; not measured)
  closures:       none

EXACT COUNTS (units = mapped OSM school objects, never pupils or residents)
  Denominator (origin_count):       40  mapped school objects in the 2 km core disk
  Snap-rejected:                     0  (all 40 passed the 150 m snap check)
  Routed:                           38  (a nearest-library path was computed)
  Unreachable:                       2  (no graph path to any accepted library)
    -- way/427679639  Marcanti College  (snap distance 18.05 m; network issue)
    -- way/670993791  Westerparkschool  (snap distance  9.35 m; network issue)
  Within threshold (<=1200 m total):  22  of 40 (55.0% of all origins)
  Outside threshold (>1200 m total):  16  routed but nearest library >1200 m away

NOTE: within_share = 22/40 = 0.55. This is a share of mapped school objects, not of
the pupil population. No claim is made about citywide coverage.

QUALITY METADATA
  Total school objects in OSM download:  204 (only 40 in the 2 km core)
  Library objects rejected (access=private):  1
  Library objects with unknown access:  20  (OSM tag absent)
  Representative points outside buffer:  3  (3 school objects snapped but their
    centroid falls outside the 4 km buffered network; routes for these may be censored)
  Invalid geometries:  0

ROUTES GEOJSON PAGE (first feature examined)
  File SHA-256:  595665cf37f72c248435726a67db02a7c8825d5f165d9360899b082c9515769a
  Total file size: 528 722 characters (paged; next_offset=5000 needed for full file)
  First route: origin node/13430642513 (De Burght) -> node/2722023232
    (NIOD Instituut voor Oorlogs- Holocaust- en Genocidestudies)
    network_m = 1229.97 m; total_m = 1317.99 m (outside threshold: False line in CSV)
  Exact edge keys visible in route (first segment):
    u:12842570837 -> v:12842570838, key:0, length 200.93 m
  Routes export is a GeoJSON FeatureCollection with ODbL attribution embedded.

ACCESSIBILITY CSV
  File SHA-256:  f246dca57b503e73746e272152a63933fcafdc12500b8aa7d14f4cf86c8fe575
  All 40 rows present; no truncation (next_offset=null)
  Columns: origin_id, origin_name, status, destination_id, destination_name,
           network_m, origin_snap_m, destination_snap_m, total_m,
           estimated_minutes, within_threshold
  Shortest route found: De Witte Olifant (way/904127931) -> Internet Archive Europe
    network_m = 185.05 m, total_m = 225.33 m, estimated_minutes = 2.82
  Longest within-threshold: Obs De Waterkant -> OBA De Hallen
    total_m = 1187.88 m (just inside 1200 m)
  Two clear unreachable rows: status="unreachable", destination fields empty

---

## STEP 3 — Detailed inspection: route, nodes, edges, isochrone, network stats

CHOSEN SCHOOL: De Witte Olifant (node/2741066971)
  Coordinates: lon 4.904493, lat 52.370883
  Snap:  node 46382990 at 15.42 m from representative point (accepted; well under 150 m)
  Destination in baseline: Internet Archive Europe (node/13196135282)
    Snap: node 46387306 at 9.82 m (accepted)

TWO-PATH ROUTE (k=2) for De Witte Olifant -> Internet Archive Europe
  Path 1 (shortest):
    network_m = 160.29 m; total_m = 185.53 m; 12 directed edges; 13 nodes
    Key edge sequence includes: 46386552 -> 12534903767 (key:0, Oudeschans, 19.20 m)
    This is exactly the suggested closure link.
  Path 2 (alternative):
    network_m = 259.09 m; total_m = 284.33 m; 18 directed edges; 19 nodes
    Diverges via 836274952 -> 46386052 -> 8044660055 -> 836275193 -> 46387305 -> 836275210
    then rejoins the same tail toward the library
    Detour length: +98.80 m over path 1 on network distance alone

WHAT THESE ROUTES MEASURE AND DO NOT MEASURE
  MEASURE:
    - Length-shortest path in meters on the harvested OSMnx walk graph
    - Includes straight-line snap connectors at both endpoints
    - Each directed edge carries an exact OSM key (key:0 here = single edge, no parallel)
  DO NOT MEASURE:
    - Actual walking time (assumed 4.8 km/h flat-speed; no signals, delays, gradients)
    - Turn delay, crossing wait time, or gate access
    - Wheelchair or mobility-impaired accessibility
    - Actual entry/exit points of buildings (representative points used)
    - Whether the route is pleasant, safe, or lit

EDGE INSPECTION: 46386552 -> 12534903767 key:0
  osmid:    7370719
  highway:  residential
  name:     Oudeschans
  maxspeed: 30 (km/h; this is a road attribute, not relevant to walk speed model)
  oneway:   false (bidirectional for cars; OSMnx walk mode models both foot directions)
  sidewalk: left
  surface:  paving_stones
  length:   19.20 m
  reversed: false

NODE 46386552 (u-node of closure edge)
  lon 4.9045935, lat 52.3716588
  street_count: 3 (three outgoing edges in the directed graph)
  Outgoing neighbors: [46389402, 452388611, 12534903767]
  Removing the edge to 12534903767 leaves two other exit options.

ISOCHRONE from De Witte Olifant (node/2741066971) at 1200 m budget
  Origin snap deducted: 15.42 m from the 1200 m budget
  Reachable graph nodes: 5 948
  Max total_m reached:   1199.997 m (confirms budget correctly exhausted)
  Sample node IDs (first 20): 16568167, 25596477, 25752666, 26586270, 26586651,
    26586653, 26699425, 26865539, 30441801, 46345386, 46346612, 46346659, 46346719,
    46346752, 46349731, 46349864, 46349945, 46350963, 46351127, 46351186
  INTERPRETATION: 5 948 is the count of graph nodes reachable within the remaining budget.
  It is NOT a population estimate, NOT a coverage polygon, and NOT a count of unique
  streets. The unsimplified graph includes shape-points between junctions, so this
  number substantially overstates intersection count.

NETWORK STATISTICS (amsterdam full graph)
  Nodes:                      79 384 (shape-points included; not intersections)
  Directed edges:             176 632
  Weak components:            468
  Largest component nodes:    62 165
  Orientation entropy:        3.557 nats
    (For reference: a pure grid = 2 nats; a fully organic network approaches ~3.6 nats.
     Amsterdam's value reflects its radial canal-ring morphology with high variety.)
  Directed length sum:        2 757 580 m
  CAUTION: Directed length counts both directions of bidirectional edges.

---

## STEP 4 — Closure scenario: agent-closure and comparison

CLOSURE APPLIED
  Suggested pair from baseline summary: u=46386552, v=12534903767
  This is a 19.20 m segment of Oudeschans (highway=residential, paving_stones)
  Used by 5 baseline routes (as reported in baseline summary)
  Both directions removed: (46386552->12534903767, key:0) and (12534903767->46386552, key:0)
  Specification submitted as:
    closures = [{"u":46386552,"v":12534903767}, {"u":12534903767,"v":46386552}]
  Confirmed removed_directed_edges in run:
    [[12534903767,46386552,0],[46386552,12534903767,0]]

SCENARIO COUNTS (agent-closure)
  origin_count:          40  (unchanged)
  snap_rejected:          0  (unchanged)
  routed_count:          38  (unchanged)
  within_threshold:      22  (UNCHANGED -- no threshold crossings)
  outside_threshold:     16  (unchanged)
  unreachable:            2  (same two as baseline)
  within_share:         0.55  (unchanged)

COMPARISON RESULT (walking_compare)
  within_before:   22
  within_after:    22
  Zero change to threshold crossings. No school object gained or lost within-threshold
  status as a result of removing this link.

AFFECTED ORIGINS (detoured but still routed):  5
  1. node/2725797085  Voorschool De Kleine Sint Antonius
     extra_distance_m = +112.14 m   (baseline total 290.64 m; closure total 402.78 m)
     lost_reachability = false
     Still within threshold: True in both runs

  2. node/2741066971  De Witte Olifant
     extra_distance_m = +328.15 m   (baseline 185.53 m; closure 513.68 m)
     lost_reachability = false
     Still within threshold: True in both runs

  3. node/4446826076  Reinwardt Academie
     extra_distance_m = +91.43 m    (baseline 1041.54 m; closure 1132.97 m)
     lost_reachability = false
     Destination changed: baseline -> Internet Archive Europe (1041 m);
     closure -> Artis Bibliotheek (1133 m); still within 1200 m: True in both runs

  4. way/904127355  De Witte Olifant (polygon object)
     extra_distance_m = +112.14 m   (baseline 296.87 m; closure 409.01 m)
     lost_reachability = false
     Still within threshold: True in both runs

  5. way/904127931  De Witte Olifant (second polygon object)
     extra_distance_m = +328.15 m   (baseline 225.33 m; closure 553.48 m)
     lost_reachability = false
     Still within threshold: True in both runs

INTERPRETATION: Removing both directions of the Oudeschans segment forces 5 school
objects onto detour routes adding 91-328 m each. Because all five were comfortably
within the 1200 m budget in baseline, all five remain within threshold after the
closure. No school object becomes unreachable or crosses the 1200 m threshold.
The network demonstrates adequate local redundancy for this link at this threshold.
This is a hypothetical stress test only; it does not describe any planned work.

---

## STEP 5 — Map rendering, GraphML export, invalid snap rejection

MAP RENDER (agent-baseline)
  File:     map.png
  Bytes:    784 880 (approx 766 KB)
  SHA-256:  5d154ef0b4f47c0260b27b18f079510ffbbb5e8b22a535ccff9efcac4564796d
  Location: mounted results workspace (binary; not embeddable in terminal)
  Content:  Routes and study boundary in EPSG:28992 (Amersfoort RD New) with
            OSM base tiles and attribution

GRAPHML EXPORT (agent-baseline)
  File:     network.graphml
  Bytes:    75 464 517 (72 MB; full unsimplified graph)
  SHA-256:  c76f0abd5b41962ce4722ad0e969d9fb78bb49b3f05374ab4c760d363837f44e
  Location: mounted results workspace
  Topology verified on reload (export tool reloads and checks before confirming)
  Note: This SHA-256 matches the input snapshot hash, confirming the export is
  identical to the pinned input, not a rewritten file.

INVALID SNAP REJECTION TEST
  Coordinates submitted: lon 139.6917, lat 35.6895 (central Tokyo, Japan)
  Result: ERROR -- "coordinate is outside the buffered study area"
  Explanation: The snap tool enforces a geographic bounding check against the
  Amsterdam study buffer (center ~lon 4.8936, lat 52.3731; radius ~4 km including
  network buffer). Tokyo is roughly 9 000 km outside that bound. The tool rejects
  coordinates that cannot plausibly match any network node rather than returning a
  misleading nearest-node answer. This prevents silent misuse with out-of-area inputs.

PROMPT RETRIEVAL
  The host exposes the prompt "municipal_walking_review" (confirmed by list_prompts).
  It was successfully retrieved with city=amsterdam. The prompt instructs exactly the
  workflow followed here.
  No limitation to report: the prompt was available and retrieved.

---

## STEP 6 — MUNICIPAL BRIEF

FINDINGS SUPPORTED BY ARTIFACTS
---------------------------------------------------------------------------
1. DENOMINATOR: 40 mapped OSM school objects fall inside the 2 km central core
   of Amsterdam (centered on lon 4.8936, lat 52.3731). This is not a count of
   schools per se; multiple OSM objects may describe one campus (e.g. three
   De Witte Olifant objects appear). It is not a count of pupils or residents.

2. BASELINE ACCESS (agent-baseline, 1200 m threshold, 4.8 km/h assumed):
   - 22 of 40 school objects (55%) have a modeled total walk path of <=1200 m
     to their nearest accepted library.
   - 16 of 40 (40%) are routed but their nearest library exceeds 1200 m.
   - 2 of 40 (5%) are unreachable: Marcanti College (way/427679639) and
     Westerparkschool (way/670993791). Both snapped successfully (<20 m).
     Unreachability likely reflects graph component isolation for those specific
     nodes. This warrants field investigation.
   - 0 schools were snap-rejected (all within 150 m of a network node).
   - 20 of 21 libraries were accepted; 1 (LLC, access=private) was excluded.
   - 20 accepted libraries all carry access=unknown in OSM -- their actual
     public accessibility has not been verified in this dataset.

3. ROUTE CHARACTER: The shortest modeled path (De Witte Olifant to Internet Archive
   Europe, 185.53 m total) uses a 19.20 m Oudeschans residential segment (paving
   stones, sidewalk:left, 30 km/h zone). The longest within-threshold path is
   Obs De Waterkant to OBA De Hallen at 1187.88 m total. Routes are planar
   shortest-distance paths; they do not account for pedestrian comfort, safety,
   lighting, crossings or barriers.

4. NETWORK STRUCTURE: 468 weak components exist in the 4 km buffered graph.
   The largest holds 62 165 of 79 384 nodes. The 2 unreachable schools are almost
   certainly in smaller isolated components. High orientation entropy (3.56 nats)
   is consistent with Amsterdam's irregular canal-ring morphology.

5. CLOSURE ROBUSTNESS (agent-closure): Hypothetical removal of both directions of
   the Oudeschans segment (u=46386552, v=12534903767) detours 5 of 40 school
   objects by 91-328 m each. Zero school objects cross the 1200 m threshold.
   Zero school objects lose reachability. The local network is resilient to this
   single-link removal at this distance budget.

PRACTICAL NEXT INVESTIGATION
---------------------------------------------------------------------------
Priority: Investigate the 2 unreachable school objects.
  - Marcanti College (way/427679639, lon 4.8658, lat 52.3752) and
    Westerparkschool (way/670993791, lon 4.8773, lat 52.3849)
    both snap successfully (18 m and 9 m respectively) but have no routed path.
  - Action: Check whether these nodes lie in isolated graph components using
    walking_node and walking_edge. If so, examine the OSM ways around them for
    missing connections, ferry-only links, or access=private barriers.
  - If unreachability persists after OSM correction, the question becomes whether
    the nearest library is physically accessible by an alternative mode or is
    simply beyond the 4 km buffer.

Secondary: The 16 schools outside the 1200 m threshold.
  - Several cluster near the buffer edge (e.g. Alan Turing School 1829 m,
    Basisschool Oostelijke Eilanden 1829 m, Vinseschool objects >1500 m).
  - Testing a 1500 m or 1850 m threshold would indicate how sensitive the
    within-share is to the threshold assumption.
  - OBA Van der Pek (lon 4.9118, lat 52.3909) is out-of-core; it is used as a
    destination for Hyperion Lyceum and both IJpleinschool objects but its
    representative point falls outside the 2 km core. Its actual service zone
    warrants verification.

Third: Access tag audit.
  - 20 of 20 accepted libraries carry access=unknown. Several are specialist
    research institutions (NIOD, CEDLA, Internet Archive Europe, Bibliotheek UvA)
    that may not be freely open to school groups. If access tags are corrected in
    OSM, the accessible library count could change, potentially making more school
    objects fall outside threshold.

EXACT STUDY SCOPE AND INPUT IDENTITY
---------------------------------------------------------------------------
  Study area:    Central 2 km disk around lon 4.8936, lat 52.3731 (Amsterdam);
                 network graph extends to 4 km buffer
  Date:          Snapshot acquired 2026-11-10T13:18:41.849586+00:00
  Input network: network.graphml
                 SHA-256: c76f0abd5b41962ce4722ad0e969d9fb78bb49b3f05374ab4c760d363837f44e
  Manifest SHA:  3c2c8dce71deeac129471de1e1a0ce3d8fb17de772b5316288a53f4ac3538e34
  Features:      features.geojson
                 SHA-256: 2795b1ade271b9e3a9954af26a3cc753a370c679762549b3abd3063f9f176b74
  Recipe SHA:    f5c2d45958c56483f121433c02fb65642a844057234930514bfab106ae4350e7
  Impl. SHA:     e6ae49345b1f87315163ef06855ec92528ae435c44bd5bd63726268bdbd61be0
  CRS:           EPSG:28992 (analysis); EPSG:4326 (storage)
  OSMnx:         2.1.1 / NetworkX 3.7

SOURCE LICENSE / ATTRIBUTION
---------------------------------------------------------------------------
  c OpenStreetMap contributors; https://www.openstreetmap.org/copyright
  License: Open Database License (ODbL) 1.0
  https://opendatacommons.org/licenses/odbl/1-0/
  Any derived work must carry this attribution and comply with ODbL share-alike.

ASSUMPTIONS EMBEDDED IN ALL RESULTS
---------------------------------------------------------------------------
  - Walking speed: 4.8 km/h flat, constant, no measured calibration
  - Threshold: 1200 m is a planning assumption, not a standard or regulation
  - Snap connectors are straight-line Euclidean distances, not routed paths
  - Bidirectional network; foot-specific one-way restrictions, barriers and
    gates are not fully honored by the OSMnx walk mode
  - Representative points (polygon centroids in EPSG:28992) are proxies for
    building entrances; actual door locations not verified
  - Denominator is OSM-object count; campus deduplication not performed

MISSING EVIDENCE BEFORE A REAL INTERVENTION
---------------------------------------------------------------------------
  1. Authoritative school register: Amsterdam municipality register of active
     schools with verified addresses and entrance coordinates
  2. Library public-access confirmation: OBA branch list confirming which
     mapped library objects are freely accessible to school groups
  3. Actual pupil enrollment data: to weight school objects by population served
  4. Field verification of the 2 unreachable schools: on-the-ground check of
     connectivity around Marcanti College and Westerparkschool
  5. Barrier audit: canal crossings, locked gates, foot=no tags that the walk
     model may not capture
  6. Seasonal/temporal data: opening hours for libraries, temporary closures
  7. Measured walk speeds: GPS-tracked pedestrian speed data for Amsterdam rather
     than the assumed 4.8 km/h
  8. Wheelchair and mobility access tags: absent from OSM for most routes
  9. Comfort and safety attributes: lighting, surface quality, crossing type

RUN IDs AND ARTIFACT HASHES FOR INDEPENDENT VERIFICATION
---------------------------------------------------------------------------
  Run agent-baseline:
    summary.json SHA-256:     20ef51f35315d4b2c233b482a64f4c4a8d527363bffabbf9399e0f728e6303fc
    accessibility.csv SHA-256: f246dca57b503e73746e272152a63933fcafdc12500b8aa7d14f4cf86c8fe575
    routes.geojson SHA-256:   595665cf37f72c248435726a67db02a7c8825d5f165d9360899b082c9515769a
    map.png SHA-256:          5d154ef0b4f47c0260b27b18f079510ffbbb5e8b22a535ccff9efcac4564796d
    network.graphml SHA-256:  c76f0abd5b41962ce4722ad0e969d9fb78bb49b3f05374ab4c760d363837f44e

  Run agent-closure:
    accessibility.csv SHA-256: 83272b7213f3c4d3716981d780d5272a996aea08e891ff2167cd0bc1dde6dcf0
    Closure applied: (46386552,12534903767) both directions; OSM way 7370719,
      Oudeschans, residential, paving_stones, 19.20 m

  Snapshot manifest SHA-256:  3c2c8dce71deeac129471de1e1a0ce3d8fb17de772b5316288a53f4ac3538e34
  Network graphml SHA-256:    c76f0abd5b41962ce4722ad0e969d9fb78bb49b3f05374ab4c760d363837f44e

WHAT IS NOT CLAIMED
---------------------------------------------------------------------------
  - No claim of wheelchair accessibility on any route
  - No claim of actual travel time (all minutes are assumed-speed estimates)
  - No claim of citywide coverage (study covers only the 2 km central core)
  - No observed disruption reported (closure is a reproducible stress test only)
  - No claim that any school object equals a certain number of pupils or residents
