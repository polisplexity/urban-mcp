**Amsterdam: the modeled closure causes no 1,200 m threshold crossings.** Five origins have longer routes, all remaining within threshold. This review used only `urban_mcp_walking`, on host `codex`.

The locked snapshot was restored through MCP. The study covers a **2,000 m core centered at 52.3731° N, 4.8936° E**, with a further 2,000 m network buffer—not Amsterdam’s municipal territory. The denominator is **40 mapped OSM school objects** whose representative points fall inside the core, not campuses, pupils or people.

The snapshot contains 204 school and 21 library objects. Twenty library objects were accepted, all with unknown access tags; one private library was rejected. Duplicate objects may represent one institution. Polygon locations are representative points, not centroids or verified entrances. Neither unknown access nor `access=yes` independently establishes public admission.

Both runs assumed **1,200 m and 4.8 km/h**, including unverified straight snap connectors:

| Run | Origins | Routed | Within | Outside | Unreachable | Snap-rejected |
|---|---:|---:|---:|---:|---:|---:|
| `agent-baseline` | 40 | 38 | 22 | 16 | 2 | 0 |
| `agent-closure` | 40 | 38 | 22 | 16 | 2 | 0 |

The selected baseline suggestion was `{46386552,12534903767}`. Closure removed both directed key-0 edges. Both complete accessibility CSVs and a keyed baseline route-export page were read.

`walking_compare.threshold_crossings` is empty. Its `schools` fields identify these five affected origins, all classified `within_to_within`:

| Origin ID | Total before, m | Total after, m | Within before | Within after |
|---|---:|---:|---|---|
| `node/2725797085` | 290.6402977159591 | 402.78398300623644 | true | true |
| `node/2741066971` | 185.53112451970844 | 513.6787294131672 | true | true |
| `node/4446826076` | 1041.5386862625548 | 1132.9656562271632 | true | true |
| `way/904127355` | 296.87068522146865 | 409.014370511746 | true | true |
| `way/904127931` | 225.33296871506528 | 553.4805736085241 | true | true |

`node/4446826076` changes destination to `node/2742996051`. Separately, `way/427679639` and `way/670993791` remain `unreachable_to_unreachable`, with null distances and false/false threshold booleans. There are no newly unreachable or snap-rejected origins; no disconnection cause was established.

Explicit annotations show that **all five affected baseline routes use the closed link; no scenario route does**. Detour magnitude establishes no crossing.

For regression origin `node/2741066971`, the baseline destination is `node/13196135282`. `walking_route(k=2)` returned:

| Rank | Total m | `uses_closed_link` | `avoids_all_declared_closed_links` | Matched directed `(u,v,key)` |
|---|---:|---|---|---|
| 1 | 185.53112451970844 | true | false | `(46386552,12534903767,0)` |
| 2 | 284.3288317743368 | true | false | `(46386552,12534903767,0)` |

The paths share **11 directed keyed edges and 11 physical links**. Neither avoids closure; these original-graph alternatives are neither closure reruns nor disjoint routes. The actual closure run yields **513.6787294131672 m** for this origin.

Inspection confirmed a 15.423149493909495 m accepted snap to node `46382990`; node/edge inspection identified the selected 19.202529624657387 m Oudeschans edge. Network statistics report 79,384 nodes, 176,632 directed edges and 468 weak components. Nodes include shape points. The 1,200 m reachable-node query returned **5,948 nodes**, not population coverage. Coordinate `(0,0)` was rejected outside the buffered area.

Baseline map rendering and GraphML export succeeded; both receipts were read. **GraphML reload was not demonstrated.** The `codex` bridge exposes no municipal-prompt retrieval operation.

Snapshot acquisition: `2026-11-10T13:18:41.849586+00:00`. Stored CRS: EPSG:4326; analysis CRS: EPSG:28992. Runtime: Python 3.12.14, OSMnx 2.1.1, NetworkX 3.7, FastMCP 3.4.2; diagnostics version 2.0.

| Identity/artifact | SHA-256 |
|---|---|
| Recipe | `f5c2d45958c56483f121433c02fb65642a844057234930514bfab106ae4350e7` |
| Snapshot manifest | `3c2c8dce71deeac129471de1e1a0ce3d8fb17de772b5316288a53f4ac3538e34` |
| Input/ exported GraphML, 75,464,517 bytes | `c76f0abd5b41962ce4722ad0e969d9fb78bb49b3f05374ab4c760d363837f44e` |
| Implementation | `a2d4ddf61f6f1ca6ae547b33e6962386281a5412c9d308c831b964d81969153d` |
| Diagnostics | `ad3a3a462c2a69852c422c0dd44213a897d7dcb04402aa6f31d1c8d73d4e59cf` |
| Baseline summary | `7c808fab74a9242e34ab49e92205aae1fd0695f22b7674b11eb41e4f23ff9b3b` |
| Closure summary | `3f360b0806b6a9b78223472bf68be1d747e79bc861ecf5bece83b672925d6ff2` |
| Baseline CSV | `f246dca57b503e73746e272152a63933fcafdc12500b8aa7d14f4cf86c8fe575` |
| Closure CSV | `83272b7213f3c4d3716981d780d5272a996aea08e891ff2167cd0bc1dde6dcf0` |
| Baseline routes | `595665cf37f72c248435726a67db02a7c8825d5f165d9360899b082c9515769a` |
| Closure routes | `3cae06f487ceab4b1ab467dacfaeb4135e65fab2c1b1ce0b1b9ac3ba272382ee` |
| Baseline PNG, 784,880 bytes | `5d154ef0b4f47c0260b27b18f079510ffbbb5e8b22a535ccff9efcac4564796d` |

The bidirectional walking model incompletely represents access, barriers, direction, crossings, hours, stairs, slope and seasonal conditions. Longer routes can be boundary-censored. No wheelchair, measured-time, authoritative service-adequacy or observed-disruption conclusion follows. Next, verify entrances, library admission and pedestrian passage along the affected routes.

© [OpenStreetMap contributors](https://www.openstreetmap.org/copyright), [ODbL-1.0](https://opendatacommons.org/licenses/odbl/1-0/). Artifact equality, machine-readable claims and prose review remain separate acceptance stages.

```json
{
  "city": "amsterdam",
  "crossed_threshold_origin_ids": [],
  "affected_still_within_origin_ids": ["node/2725797085", "node/2741066971", "node/4446826076", "way/904127355", "way/904127931"],
  "newly_unreachable_origin_ids": [],
  "baseline_routes_using_closed_link_origin_ids": ["node/2725797085", "node/2741066971", "node/4446826076", "way/904127355", "way/904127931"],
  "scenario_routes_using_closed_link_origin_ids": [],
  "route_origin_id": "node/2741066971",
  "path_membership": [
    {"rank": 1, "uses_closed_link": true, "avoids_all_declared_closed_links": false},
    {"rank": 2, "uses_closed_link": true, "avoids_all_declared_closed_links": false}
  ],
  "path_ranks_avoiding_declared_closed_links": []
}
```