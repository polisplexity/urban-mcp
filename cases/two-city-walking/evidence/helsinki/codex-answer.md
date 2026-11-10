Helsinki’s baseline places **45 of 48 mapped school objects within a modeled 1,200 m library route**. The hypothetical link removal reduces this to **40 of 48**. These are facility-object counts, never pupils or residents.

| Result | `agent-baseline` | `agent-closure` |
|---|---:|---:|
| Denominator: core school objects | 48 | 48 |
| Routed | 46 | 46 |
| Within 1,200 m | 45 | 40 |
| Routed outside threshold | 1 | 6 |
| Unreachable | 2 | 2 |
| Snap-rejected origins | 0 | 0 |

Both runs use an assumed **4.8 km/h**. Distances include network length and two straight snap connectors; estimated minutes are scenario calculations, not actual travel times.

The baseline’s outside-threshold object is Etelä-Hesperiankadun väistötilat (`way/536980461`), at 1,467.502 m. Etu-Töölön lukio (`way/445933783`) and Helsingin eurooppalainen koulu (`way/725256831`) are unreachable in this snapshot. Their real-world causes remain unknown.

The baseline suggested pair **(501610897, 5912225309)** was removed in both directions, including every parallel edge. The receipts record two removed directed edges, both key `0`. This reproducible stress test affects 11 school objects; **none loses reachability**.

| Affected object | Additional metres, rounded | Newly outside 1,200 m |
|---|---:|:---:|
| Kallion lukio — `node/1017984829` | 556.338 | No |
| Suomen Diakoniaopisto — `node/8862204483` | 279.498 | Yes |
| SKY-Opisto — `node/8862204485` | 279.498 | Yes |
| Vallilan ala-asteen koulu, väistötila — `way/1038696462` | 493.909 | Yes |
| HEO: Portsi — `way/128161235` | 431.673 | No |
| Helsingin kuvataidelukio — `way/139225450` | 87.008 | No |
| Kallion ala-aste — `way/34069317` | 530.160 | No |
| Kallion lukio — `way/37295003` | 649.035 | No |
| Aleksis Kiven peruskoulu — `way/37296704` | 376.058 | No |
| Suomen Diakoniaopisto Alppikadun kampus — `way/38192458` | 284.883 | Yes |
| Åshöjdens grundskola — `way/592362656` | 233.890 | Yes |

The inspected baseline route connects Kallion lukio (`node/1017984829`) to Kallion kirjasto (`way/20010806`). Its network distance is 202.848 m, with origin/destination connectors of 9.799/13.210 m, totaling 225.856 m. Two additional length-shortest paths total 229.654 and 231.397 m. These alternatives measure graph-path length, without establishing safe or permitted passage.

Snap/node inspection identified origin node `8852622700` and destination node `501610897`. The origin node carries `access=private` and `wheelchair=no`; the inspected first edge is tagged `steps`. The test link is also tagged `steps`, with length 4.266 m in each direction. These tags require verification.

Network statistics report 111,650 nodes, 247,056 directed edges, 1,264 weak components, largest-component size 96,886 nodes, orientation entropy 3.544280 nats, and directed length sum 2,749,732.527 m. Reciprocal edges contribute separately; unsimplified nodes include shape points. These are neither unique street lengths nor intersection counts, and component counts cannot explain disconnection causes. The 1,200 m origin query returns **10,480 reachable nodes**, accounting for its origin connector; this is neither a coverage polygon nor a population estimate.

The restored, verified pinned snapshot was acquired **2026-11-10T13:26:57.775732+00:00**. Scope is a **2,000 m central disk around longitude 24.9414, latitude 60.1719**, with an additional 2,000 m network buffer. The bidirectional, unsimplified OSMnx 2.1.1 walking graph uses EPSG:4326; metric analysis uses EPSG:3067. Longer routes can be boundary-censored.

The catalog contains 90 school and 31 library objects. All 31 libraries pass the model’s filters; school/library snap rejections are zero under the 150 m rule. Polygon locations are **representative points, not centroids or verified entrances**. `representative_points_outside_buffer=1` flags a feature representative point outside the buffered acquisition area; it does not count core schools, routed origins or rejected snaps. Thirty libraries have unknown access. Rajatiedon kirjasto’s `access=yes` tag does not independently verify public admission.

Coordinate `(latitude=0, longitude=0)` was rejected because it lies outside the buffered study area. The codex host exposes no prompt-retrieval interface, so I did **not** retrieve the municipal review prompt.

A practical next investigation is to verify entrances, library admission and alternative connections around Kallion kirjasto, then review the five threshold-crossing objects against authoritative facility records. Real intervention requires field evidence on crossings, barriers, hours, stairs, slope and winter conditions, plus measured travel times. This test establishes neither wheelchair access, citywide coverage nor an observed disruption.

Both CSVs, a keyed baseline route-export page, and map/GraphML receipts were read. SHA-256 identifiers:

| Input or artifact | SHA-256 |
|---|---|
| Input manifest | `6a71ce0b324b31b95c0baadffc19cb1d711aa34a44db60d699987796981fe673` |
| Implementation | `e6ae49345b1f87315163ef06855ec92528ae435c44bd5bd63726268bdbd61be0` |
| `agent-baseline/accessibility.csv` | `0091c35f0e99e41afc05fbe362248dd901e7a08b94519a841ae4413fe9950a1f` |
| `agent-closure/accessibility.csv` | `04ec8cec8305ad8cc144b06ae9131d22ac8d30a4d2d5c5611ac34c0718834b9d` |
| `agent-baseline/routes.geojson` | `dc6dad4faf67829f6ba52b7b9b144251b5a08fee400582f70b63db328b599e7c` |
| `agent-baseline/map.png` — 665,545 bytes | `e81a86642bd1500f0f712608e736d96f90a99b58d451621cb880e13338f16ad5` |
| Input/export `network.graphml` — 95,455,038 bytes | `2ea8f1570dfea012a77bd7a7ab0f1042e73660c06e6454cadd8df5f63de495d5` |

Source: **© [OpenStreetMap contributors](https://www.openstreetmap.org/copyright)**, licensed under [ODbL-1.0](https://opendatacommons.org/licenses/odbl/1-0/).