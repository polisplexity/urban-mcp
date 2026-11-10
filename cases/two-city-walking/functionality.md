# Function coverage and ownership

The admitted interface has **15 tools**, one static resource, two resource templates and one prompt. All tools run over a real stdio MCP subprocess and are compared with native artifacts/calculations. See each city's `evidence/<city>/mcp.json` for exact executed checks and failures. Host traces are separate evidence: an LLM need not exercise every parameter to establish the deterministic contract.

| MCP tool | Original engine/API reused | Project-specific behavior | Acceptance evidence |
| --- | --- | --- | --- |
| `walking_status` | Input manifest/recipe | Both cities, readiness and limits | Verified input state, explicit missing-data state in fresh agent workspaces |
| `harvest_walking_data` | OSMnx polygon/bbox acquisition and GraphML | Source receipts, snapshot locks, integrity checks and city isolation | Live CLI receipts; snapshot restoration through MCP in independent empty host workspaces. Live mode is not claimed tested through MCP. |
| `walking_graph_info` | NetworkX components, OSMnx GraphML | Dataset identity and unsimplified semantics | Exact native/MCP equality |
| `walking_feature_catalog` | GeoPandas, projected Shapely representative points | OSM IDs, core membership, access tags | Exact native/MCP equality and nonempty denominator |
| `walking_snap` | OSMnx nearest nodes | Geographic bounds and 150 m rule | Brute-force great-circle distance comparison, invalid remote coordinate rejection |
| `walking_accessibility` | NetworkX reverse Dijkstra | Destination connectors in selection, all-origin accounting, keyed routes, constant-speed scenario, CSV/report export | Every row compared with independent forward per-origin Dijkstra and enumeration of every accepted library; native/MCP exact CSV equality |
| `walking_compare` | NetworkX edge deletion / same route solver | Bidirectional/all-parallel link removal, compatible-run checks and affected objects | Real detours, monotonic shortest-distance/threshold checks, exact native/MCP affected lists |
| `walking_route` | NetworkX shortest path, OSMnx k-shortest paths | Explicit feature endpoints, actual parallel keys and connector totals | Two ordered alternatives, route totals vs municipal CSV, synthetic keyed-edge regression |
| `walking_isochrone` | NetworkX cutoff Dijkstra | Origin connector deducted, bounded sample | Exact reachable-node count/sample vs native cutoff; explicitly not a population/polygon estimate |
| `walking_network_stats` | NetworkX components, OSMnx bearings/entropy | Honest unsimplified/directed-length semantics | Native equality, positive finite entropy |
| `walking_node` | NetworkX node lookup | Explicit city, bounded adjacent-node inspection | Exact attributes, invalid ID rejection |
| `walking_edge` | NetworkX keyed-edge lookup | Explicit edge key and city | Exact original length/tags, invalid ID rejection |
| `walking_export_graph` | OSMnx GraphML | Unique mounted output with receipt | Round trip preserves node IDs, all keyed edges and all lengths |
| `walking_render_map` | GeoPandas/PyProj, Matplotlib | Metric map of exact routes/core/facilities with attribution | Nonempty PNG/receipt plus visual inspection of both city maps |
| `walking_read_artifact` | Standard file I/O/hash | Allowlisted names, bounded pages, no arbitrary paths | Exact CSV hashes, route pagination and path/size rejection |

Resources: `walking://case`, `walking://{city}/manifest`, `walking://{city}/graph`. The suite reads each family. Prompt: `municipal_walking_review(city)`; discovery and content are checked. Some hosts expose prompt/resource helpers and others expose only tools; host-specific gaps must be reported, not disguised as protocol failure.

Missing input, unknown city/feature/node/edge, remote coordinates, invalid budgets/speeds, nonexistent closure links, duplicate run IDs, arbitrary artifact paths, incompatible comparisons and excessive output limits are rejection cases. Each check asserts the reason, not only an error flag.

Agent review exposed a specific interpretation hazard: k-shortest paths can overlap. `walking_route` alternatives are not edge-disjoint and do not establish availability after a link closure. Use the actual closure analysis and CSV for that question. The [narrative review](evidence/narrative-review.md) records a concrete Amsterdam counterexample and the Helsinki per-object classification errors; all four hosts' artifacts match even though Hermes prose fails review.

Not admitted: all of OSMnx, all original MCP tools, every driver/parameter, motor-speed imputation, DEM/elevation/grade, metric intersection consolidation, calibrated pedestrian simulation, barriers/turn restrictions, continuous-edge isochrone polygons, wheelchair routing, population coverage, authoritative school/library completeness, or whole-city/global reachability. Add a new operation only with its data contract, municipal need and native comparison.
