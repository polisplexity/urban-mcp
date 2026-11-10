The hypothetical closure produces **five threshold crossings**, six other affected origins that remain within 1,200 m, and no newly unreachable origins.

The study boundary is a **2 km disk around 60.1719° N, 24.9414° E**, with an additional 2 km graph buffer—not Helsinki’s municipal territory. The denominator is **48 mapped school objects**, not campuses, pupils or people. The catalog contains 90 school and 31 library objects; multiple objects may represent one campus. Polygon locations are representative points, not centroids or verified entrances. Thirty library access values are unknown; the remaining `access=yes` tag does not independently verify public admission.

Both runs assume **1,200 m and 4.8 km/h**:

| Run | Origins | Routed | Within | Outside | Unreachable | Snap-rejected |
|---|---:|---:|---:|---:|---:|---:|
| `agent-baseline` | 48 | 46 | 45 | 1 | 2 | 0 |
| `agent-closure` | 48 | 46 | 40 | 6 | 2 | 0 |

The selected baseline suggestion was `{u:501610897,v:5912225309}`. The closure removed `(501610897,5912225309,0)` and `(5912225309,501610897,0)`.

From the explicit `threshold_crossings` results, total distances—including both snap connectors—are:

| Origin ID | Before, m | After, m | `within_before` | `within_after` | Classification |
|---|---:|---:|---|---|---|
| `node/8862204483` | 961.7262935293504 | 1241.2244744973766 | true | false | `within_to_outside` |
| `node/8862204485` | 958.8176598040282 | 1238.3158407720543 | true | false | `within_to_outside` |
| `way/1038696462` | 977.9637124317981 | 1471.8724185578415 | true | false | `within_to_outside` |
| `way/38192458` | 1055.2478913962748 | 1340.1308826211898 | true | false | `within_to_outside` |
| `way/592362656` | 1058.5409416389095 | 1292.4309009544202 | true | false | `within_to_outside` |

The `schools` fields separately identify six affected origins remaining within threshold: `node/1017984829`, `way/128161235`, `way/139225450`, `way/34069317`, `way/37295003`, `way/37296704`. All are `true → true`, classified `within_to_within`. A large detour does not establish a crossing.

`way/445933783` and `way/725256831` remain unreachable in both runs; their causes were not established. No objects fail snapping. Explicit annotations identify **11 baseline routes using the closed link and zero scenario routes**; their IDs appear below.

For regression origin `node/1017984829`, the baseline destination is `way/20010806`. The original-graph `walking_route(k=2,closed_links=[…])` returned:

| Rank | Total, m | `uses_closed_link` | `avoids_all_declared_closed_links` | Matched directed `(u,v,key)` |
|---|---:|---|---|---|
| 1 | 225.85597941138542 | true | false | `(5912225309,501610897,0)` |
| 2 | 229.6543587598288 | true | false | `(5912225309,501610897,0)` |

The paths share **23 directed keyed edges and 23 physical links**. Neither avoids the closure; they are neither a closure rerun nor disjoint alternatives. The actual `agent-closure` solution changes this origin’s destination to `node/7707562463`, totaling **782.1941328086926 m**, still within threshold.

Inspection accepted the origin’s **9.798528392739794 m** snap to node `8852622700`; inspected node `501610897` and the matched concrete-steps edge. Network statistics report **111,650 nodes, 247,056 directed edges and 1,264 weak components**; unsimplified nodes are not intersection counts. The 1,200 m reachable-node query returned **10,480 nodes**, not a coverage polygon. Remote coordinate `(0,0)` was rejected as outside the buffered area.

I read both complete CSVs and a keyed-route export page, rendered the baseline map, exported GraphML and retrieved artifact receipts. **GraphML was not reloaded.** Codex exposes no prompt-retrieval operation here; recipe, manifest and graph resources were read.

The restored snapshot records acquisition at `2026-11-10T13:26:57.775732+00:00`; graph CRS is EPSG:4326, analysis CRS EPSG:3067. Runtime includes OSMnx 2.1.1, NetworkX 3.7 and Python 3.12.14. SHA-256 identities and principal artifact receipts:

| Identity/artifact | SHA-256 |
|---|---|
| Input manifest | `6a71ce0b324b31b95c0baadffc19cb1d711aa34a44db60d699987796981fe673` |
| Recipe | `f5c2d45958c56483f121433c02fb65642a844057234930514bfab106ae4350e7` |
| Implementation | `a2d4ddf61f6f1ca6ae547b33e6962386281a5412c9d308c831b964d81969153d` |
| Diagnostics v2.0 | `ad3a3a462c2a69852c422c0dd44213a897d7dcb04402aa6f31d1c8d73d4e59cf` |
| Input/exported GraphML, 95,455,038 bytes | `2ea8f1570dfea012a77bd7a7ab0f1042e73660c06e6454cadd8df5f63de495d5` |
| Baseline CSV | `0091c35f0e99e41afc05fbe362248dd901e7a08b94519a841ae4413fe9950a1f` |
| Closure CSV | `04ec8cec8305ad8cc144b06ae9131d22ac8d30a4d2d5c5611ac34c0718834b9d` |
| Baseline routes | `dc6dad4faf67829f6ba52b7b9b144251b5a08fee400582f70b63db328b599e7c` |
| Closure routes | `ad8240a1e1c924323fd0f9669b0529d9c9e509a89edb91d2d70f4a93d8770fac` |
| Baseline PNG, 665,545 bytes | `e81a86642bd1500f0f712608e736d96f90a99b58d451621cb880e13338f16ad5` |

Source: **© [OpenStreetMap contributors](https://www.openstreetmap.org/copyright), ODbL-1.0**. These mapped amenities are not an authoritative facility register. Snap connectors are unverified; longer routes may be boundary-censored. The bidirectional model incompletely represents access, barriers, direction, hours, crossings, stairs, slope and seasonal conditions. It supports no wheelchair, measured-time, service-adequacy or observed-disruption conclusion.

Next, verify entrances, library admission and the modeled steps connection for the affected objects. Artifact equality, machine-readable claims and prose review remain separate acceptance stages.

```json
{
  "city": "helsinki",
  "crossed_threshold_origin_ids": ["node/8862204483", "node/8862204485", "way/1038696462", "way/38192458", "way/592362656"],
  "affected_still_within_origin_ids": ["node/1017984829", "way/128161235", "way/139225450", "way/34069317", "way/37295003", "way/37296704"],
  "newly_unreachable_origin_ids": [],
  "baseline_routes_using_closed_link_origin_ids": ["node/1017984829", "node/8862204483", "node/8862204485", "way/1038696462", "way/128161235", "way/139225450", "way/34069317", "way/37295003", "way/37296704", "way/38192458", "way/592362656"],
  "scenario_routes_using_closed_link_origin_ids": [],
  "route_origin_id": "node/1017984829",
  "path_membership": [
    {"rank": 1, "uses_closed_link": true, "avoids_all_declared_closed_links": false},
    {"rank": 2, "uses_closed_link": true, "avoids_all_declared_closed_links": false}
  ],
  "path_ranks_avoiding_declared_closed_links": []
}
```