All artifacts collected. Now compose the final municipal brief.

---

## MUNICIPAL BRIEF: AMSTERDAM SCHOOL-TO-LIBRARY WALKING ACCESS

### Study identity and data

Case: two-city-walking
City: Amsterdam, NL (geographic_id GM0363)
Study core: 2 km radius disk centered on 4.8936 E, 52.3731 N
Graph buffer: additional 2 km beyond core
Snapshot acquired: 2026-11-10T13:18:41 UTC
Snapshot manifest SHA-256: 3c2c8dce71deeac129471de1e1a0ce3d8fb17de772b5316288a53f4ac3538e34
Recipe SHA-256: f5c2d45958c56483f121433c02fb65642a844057234930514bfab106ae4350e7
Source: OpenStreetMap contributors, license ODbL-1.0 (https://opendatacommons.org/licenses/odbl/1-0/)
Attribution: (c) OpenStreetMap contributors; https://www.openstreetmap.org/copyright
Network model: bidirectional unsimplified OSMnx walk, CRS EPSG:28992 (analysis), EPSG:4326 (storage)
Graph: 79,384 nodes, 176,632 directed edges, 468 weak components (largest: 62,165 nodes)
Implementation SHA-256: e6ae49345b1f87315163ef06855ec92528ae435c44bd5bd63726268bdbd61be0
OSMnx 2.1.1 / NetworkX 3.7

---

### Feature catalog summary

Total OSM features harvested: 225 (204 amenity=school, 21 amenity=library)
Core school objects (denominator): 40
Buffer library objects: 21 total; 1 rejected for access=private (node/432855895, name "LLC"); 20 accepted as destinations; access for all 20 accepted libraries is tagged "unknown" in OSM -- public admission is not independently verified
Representative points outside the buffered acquisition area: 3 (quality flag; not a snap-rejection count)
Polygon features: coordinates are representative points in the local projected CRS reprojected to EPSG:4326; not verified entrances
Point features: OSM node coordinates; not verified entrances

---

### Baseline run: agent-baseline

Threshold: 1200 m total (network path + snap connectors)
Assumed speed: 4.8 km/h (constant; no measured speed, delays, or calibration)
Run artifacts SHA-256:
  accessibility.csv: f246dca57b503e73746e272152a63933fcafdc12500b8aa7d14f4cf86c8fe575
  routes.geojson: 595665cf37f72c248435726a67db02a7c8825d5f165d9360899b082c9515769a

DENOMINATOR: 40 mapped OSM school objects whose representative point is in the 2 km study core
(This is a count of OSM objects, not of pupils, campuses, enrollment, or residents.)

Counts:
  Origin objects (core school objects): 40
  Snap-rejected origins: 0
  Routed origins: 38
  Unreachable origins: 2 (Marcanti College way/427679639; Westerparkschool way/670993791 -- cause unknown from topology alone; both have small snap distances but no routable path was found to any accepted library)
  Within 1200 m (routed total incl. snap connectors): 22
  Outside 1200 m (routed but over threshold): 16
  Within-threshold share of all 40 origins: 0.55 (55%)

Speed note: 4.8 km/h is an explicit scenario assumption applied uniformly including snap connectors; it is not a measured pedestrian speed.

---

### Route and node inspection

Origin inspected: De Witte Olifant (node/2741066971), snapped to graph node 46382990 at 15.4 m (accepted; threshold 150 m).

Two alternative routes from De Witte Olifant to Internet Archive Europe (node/13196135282):
  Path 1: 13 nodes, network 160.3 m, total 185.5 m (within threshold)
    Uses edge (u=46386552, v=12534903767, key=0): OSM way "Oudeschans", highway=residential, 19.2 m, paving_stones surface, maxspeed 30
  Path 2 (alternative): 19 nodes, network 259.1 m, total 284.3 m (longer alternative if primary edge removed)

Isochrone from De Witte Olifant at 1200 m budget: 5,948 reachable graph nodes (not a coverage polygon, resident count, or continuous-edge isochrone; counts graph nodes reachable after subtracting the 15.4 m snap connector from the budget).

What these outputs measure: shortest-path distances on the harvested OSM pedestrian graph using graph nodes as waypoints. What they do not measure: actual foot-path geometry between nodes, crossing conditions, barriers, stair counts, slope, surface friction, intersection wait times, opening hours, or wheelchair accessibility.

---

### Closure scenario: agent-closure

Closed pair: u=46386552, v=12534903767 (both directions; OSM way "Oudeschans", 19.2 m residential segment)
This closure is a hypothetical network-robustness stress test, not a report of actual or planned works.
Removed directed edges: [12534903767, 46386552, 0] and [46386552, 12534903767, 0]
Scenario CSV SHA-256: 83272b7213f3c4d3716981d780d5272a996aea08e891ff2167cd0bc1dde6dcf0

Aggregate counts (unchanged):
  Within threshold before: 22 / within threshold after: 22
  No origin crossed the 1200 m threshold in either direction.
  No origin lost reachability.

Affected origins (detour without threshold crossing): 5

  node/2725797085 (Voorschool De Kleine Sint Antonius): +112.1 m detour; remained within threshold (total 402.8 m vs. baseline 290.6 m)
  node/2741066971 (De Witte Olifant): +328.1 m detour; remained within threshold (total 513.7 m vs. baseline 185.5 m)
  node/4446826076 (Reinwardt Academie): +91.4 m detour; remained within threshold; destination rerouted from Internet Archive Europe to Artis Bibliotheek (1,132.9 m total vs. 1,041.5 m baseline)
  way/904127355 (De Witte Olifant): +112.1 m detour; remained within threshold
  way/904127931 (De Witte Olifant): +328.1 m detour; remained within threshold

The model confirms the network has sufficient redundancy on Oudeschans that the 1200 m threshold is not breached for any of the 5 affected origins under this hypothetical closure.

---

### Evidence receipts

Baseline run ID: agent-baseline
Closure run ID: agent-closure
map.png SHA-256: 5d154ef0b4f47c0260b27b18f079510ffbbb5e8b22a535ccff9efcac4564796d (784,880 bytes; in mounted workspace)
network.graphml SHA-256: c76f0abd5b41962ce4722ad0e969d9fb78bb49b3f05374ab4c760d363837f44e (75,464,517 bytes; in mounted workspace)
Snapshot manifest SHA-256: 3c2c8dce71deeac129471de1e1a0ce3d8fb17de772b5316288a53f4ac3538e34

Invalid coordinate snap test: coordinate (lon=0.0, lat=0.0) was rejected with error "coordinate is outside the buffered study area". The snap operation refuses coordinates not within the acquisition buffer; it does not silently snap to a distant node.

Prompt retrieval: the municipal_walking_review prompt was successfully retrieved from the host. It instructs the reviewer to discover the recipe, restore the snapshot, inspect graph, schools and libraries, run the baseline, read CSV and routes, inspect snap exclusions and disconnected paths, run one bidirectional link closure and compare, render/export evidence, report mapped school objects (never population), preserve core/buffer bounds, input identity, ODbL attribution and all limitations.

---

### Assumptions and limitations

1. Study scope: central 2 km disk only. This is not a citywide analysis of Amsterdam. The 40 origin objects represent OSM-mapped school objects in that disk, not all Amsterdam schools.
2. OSM is not an authoritative facility register. No deduplication was performed; multiple OSM objects may represent the same campus.
3. Polygon representative points (not centroids) and node coordinates are proxies for feature locations; no field verification of entrances was performed.
4. Access=unknown for 20 of 20 accepted library destinations. Public admission is not established from OSM tags; "Internet Archive Europe", "NIOD", "CEDLA Library", "Artis Bibliotheek", "Fotografie Bibliotheek", and "Stichting L.A.K.A." appear in the destination pool but their public-access status is unverified. This is not equivalent to public library admission.
5. Speed 4.8 km/h is an explicit scenario assumption, not a measured pedestrian speed.
6. The network does not model barriers, gates, opening hours, crossings, stairs, slope, or wheelchair access.
7. 2 unreachable origins (Marcanti College, Westerparkschool): cause is unknown from artifact counts alone; no claim about why they are unreachable is made.
8. 3 representative points flagged as outside the buffered acquisition area: this is a data-quality flag, not a snap-rejection count and not a count of core schools excluded from routing.
9. Closure scenario is a hypothetical graph-robustness test; not an observed or planned road closure.

---

### Practical next investigation

The 16 school objects routed but outside 1200 m, and the 2 unreachable objects, warrant field-level follow-up before any planning action. Priority checks:
  (a) Verify which of the accepted library destinations are actually publicly accessible (opening hours, admission policy).
  (b) Field-verify representative points and walking path quality for the 5 origins most affected by the Oudeschans closure scenario (all rerouted without crossing threshold, but detours of up to 328 m were modeled).
  (c) Establish whether the 2 unreachable origins (Marcanti College, Westerparkschool) are genuinely disconnected from the main network component or whether OSM mapping gaps cause the disconnection -- the model cannot determine this from topology alone.
  (d) OSM audit: 3 objects whose representative points fall outside the 4 km buffered acquisition zone should be checked for coordinate accuracy.
  (e) Extend the study core or acquire a full-municipality network before making citywide claims.

This report is a reproducible exploratory analysis of OSM-mapped objects within a 2 km central disk. It does not constitute an accessibility audit, a service-level determination, or evidence of real network disruption.
