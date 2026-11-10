**Amsterdam’s baseline places 22 of 40 mapped school objects within a modeled 1,200 m library route.** The hypothetical closure lengthens routes for five objects but produces **zero threshold crossings and zero losses of reachability**.

| Outcome, in school objects | `agent-baseline` | `agent-closure` |
|---|---:|---:|
| Denominator | 40 | 40 |
| Routed | 38 | 38 |
| Within 1,200 m | 22 | 22 |
| Routed outside 1,200 m | 16 | 16 |
| Unreachable | 2 | 2 |
| Snap-rejected | 0 | 0 |

The denominator is mapped OSM school objects whose representative points fall within the study core—never pupils or residents. Both complete accessibility CSVs and a page of the baseline’s keyed route export were read. Distances are meters; CSV time estimates are minutes under the assumed constant **4.8 km/h** speed, including connectors.

The catalog contains 204 school and 21 library objects. The model accepts 20 library objects, all with unknown access; one is rejected for access. Public admission is unverified. Neither a library’s name nor an OSM access tag independently verifies admission. There are zero school or library snap rejections. The quality flag `representative_points_outside_buffer=3` means three representative points fall outside the buffered acquisition area; it does not count core schools, routed origins or rejected snaps. Polygon locations use representative points, not centroids or verified entrances.

For the inspected route, **De Burght (`node/13430642513`) → NIOD (`node/2722023232`)**, network distance is 1,229.9700893928616 m. Accepted endpoint connectors are 59.17261701364222 m and 28.849664135603344 m, giving 1,317.992370542107 m total. Snapped nodes are `12842570837` and `4446887357`; both node records were inspected. The first keyed edge, `(12842570837,12842570838,0)`, is tagged Herengracht and measures 200.93444703928068 m. Two additional length-shortest alternatives total 1,369.1418844345496 m and 1,371.0845475281885 m. These are general walking proxies, not verified itineraries.

The 1,200 m reachable-node operation returns **5,017 nodes**, after allowing for the origin connector. It measures graph-node reachability, not a coverage polygon or population. Network statistics report 79,384 nodes, 176,632 directed edges, 468 weak components, directed length sum 2,757,579.6999721443 m and orientation entropy 3.5566437843819623 nats. Unsimplified nodes include shape points; reciprocal edges contribute to directed length. These are not intersection or unique-street-length counts. Component and unreachable-route causes remain unknown.

The reproducible stress test removes both directions and every parallel edge of baseline-suggested pair **`(46386552,12534903767)`**, tagged Oudeschans. The receipt confirms removal of both key-0 directed edges.

| Affected object | Added distance, m (rounded) |
|---|---:|
| Voorschool De Kleine Sint Antonius — `node/2725797085` | 112.144 |
| De Witte Olifant — `node/2741066971` | 328.148 |
| Reinwardt Academie — `node/4446826076` | 91.427 |
| De Witte Olifant — `way/904127355` | 112.144 |
| De Witte Olifant — `way/904127931` | 328.148 |

All five remain within threshold. Reinwardt Academie’s selected destination changes from Internet Archive Europe to Artis Bibliotheek. This is a hypothetical graph test, not an observed disruption.

The baseline map and GraphML were produced and their receipts reread: **784,880 bytes** and **75,464,517 bytes**, respectively. The exported graph hash matches the input graph. Snapping `(latitude=0, longitude=0)` returns “coordinate is outside the buffered study area”; no snap distance was returned. The codex host exposes no prompt retrieval operation, so the municipal review prompt was not retrieved.

The exact scope is case `two-city-walking`, Amsterdam `GM0363`: a **2,000 m core** centered at **52.3731° N, 4.8936° E**, with an additional **2,000 m graph buffer**. Analysis CRS is **EPSG:28992**; stored graph CRS is **EPSG:4326**. The restored pinned snapshot records acquisition **2026-11-10T13:18:41.849586+00:00**, using bidirectional, unsimplified OSMnx walk data, OSMnx 2.1.1 and Python 3.12.14. Coverage is limited to this study area; longer routes may be boundary-censored.

A practical next investigation is to verify De Burght–NIOD entrances and admission, plus the mapped connectivity around unreachable Marcanti College (`way/427679639`) and Westerparkschool (`way/670993791`). Before intervention, reconcile an authoritative facility register, duplicate campus objects, opening hours, crossings, barriers, directional foot rules, stairs and slope, and collect observed journey evidence. Straight snap connectors are unverified paths; estimated minutes are not actual travel times. Wheelchair suitability remains unassessed.

Data attribution: [© OpenStreetMap contributors](https://www.openstreetmap.org/copyright), licensed [ODbL-1.0](https://opendatacommons.org/licenses/odbl/1-0/).

SHA-256 receipts:

| Identity/artifact | SHA-256 |
|---|---|
| Input manifest | `3c2c8dce71deeac129471de1e1a0ce3d8fb17de772b5316288a53f4ac3538e34` |
| Input/exported `network.graphml` | `c76f0abd5b41962ce4722ad0e969d9fb78bb49b3f05374ab4c760d363837f44e` |
| Implementation | `e6ae49345b1f87315163ef06855ec92528ae435c44bd5bd63726268bdbd61be0` |
| `agent-baseline/summary.json` | `20ef51f35315d4b2c233b482a64f4c4a8d527363bffabbf9399e0f728e6303fc` |
| `agent-baseline/accessibility.csv` | `f246dca57b503e73746e272152a63933fcafdc12500b8aa7d14f4cf86c8fe575` |
| `agent-baseline/routes.geojson` | `595665cf37f72c248435726a67db02a7c8825d5f165d9360899b082c9515769a` |
| `agent-baseline/map.png` | `5d154ef0b4f47c0260b27b18f079510ffbbb5e8b22a535ccff9efcac4564796d` |
| `agent-closure/summary.json` | `07a1726d3a4117f06017c4084fbc641e25d3a55df1dfbf4c45e7354c06bfdc94` |
| `agent-closure/accessibility.csv` | `83272b7213f3c4d3716981d780d5272a996aea08e891ff2167cd0bc1dde6dcf0` |