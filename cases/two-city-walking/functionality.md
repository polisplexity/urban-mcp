# Function coverage and ownership

The admitted interface has **15 tools**, one static resource, two resource templates and one prompt. All tools run over a real stdio MCP subprocess and are compared with native artifacts/calculations. Current diagnostic checks are in `evidence/issue-39/<city>/mcp.json`; `evidence/<city>/mcp.json` preserves version 1. Host traces are separate evidence: an LLM need not exercise every parameter to establish the deterministic contract.

| MCP tool | Original engine/API reused | Project-specific behavior | Acceptance evidence |
| --- | --- | --- | --- |
| `walking_status` | Input manifest/recipe | Both cities, readiness and limits | Verified input state, explicit missing-data state in fresh agent workspaces |
| `harvest_walking_data` | OSMnx polygon/bbox acquisition and GraphML | Source receipts, snapshot locks, integrity checks and city isolation | Live CLI receipts; snapshot restoration through MCP in independent empty host workspaces. Live mode is not claimed tested through MCP. |
| `walking_graph_info` | NetworkX components, OSMnx GraphML | Dataset identity and unsimplified semantics | Exact native/MCP equality |
| `walking_feature_catalog` | GeoPandas, projected Shapely representative points | OSM IDs, core membership, access tags | Exact native/MCP equality and nonempty denominator |
| `walking_snap` | OSMnx nearest nodes | Geographic bounds and 150 m rule | Brute-force great-circle distance comparison, invalid remote coordinate rejection |
| `walking_accessibility` | NetworkX reverse Dijkstra | Destination connectors in selection, all-origin accounting, keyed routes, constant-speed scenario, CSV/report export | Every row compared with independent forward per-origin Dijkstra and enumeration of every accepted library; native/MCP exact CSV equality |
| `walking_compare` | Existing baseline/closure solver outputs | Compatible-run checks; all schools' before/after states, exact threshold crossings, lost reachability and closed keyed-edge membership | Independent complete CSV/route joins, unchanged numerical CSVs, monotonicity, exact native/MCP diagnostics and two-host JSON claims |
| `walking_route` | NetworkX shortest path, OSMnx k-shortest paths | Feature endpoints, actual parallel keys/connectors; optional closed-link membership and pairwise keyed/physical overlap | Ordered alternatives and totals vs CSV; both regression paths explicitly blocked in each city; reverse/parallel/avoiding synthetic cases; native/MCP equality and two-host JSON claims |
| `walking_isochrone` | NetworkX cutoff Dijkstra | Origin connector deducted, bounded sample | Exact reachable-node count/sample vs native cutoff; explicitly not a population/polygon estimate |
| `walking_network_stats` | NetworkX components, OSMnx bearings/entropy | Honest unsimplified/directed-length semantics | Native equality, positive finite entropy |
| `walking_node` | NetworkX node lookup | Explicit city, bounded adjacent-node inspection | Exact attributes, invalid ID rejection |
| `walking_edge` | NetworkX keyed-edge lookup | Explicit edge key and city | Exact original length/tags, invalid ID rejection |
| `walking_export_graph` | OSMnx GraphML | Unique mounted output with hash/size receipt | The native/MCP suite separately reloads the export and checks node IDs, keyed edges and lengths; the export tool itself does not perform a topology check |
| `walking_render_map` | GeoPandas/PyProj, Matplotlib | Metric map of exact routes/core/facilities with attribution | Nonempty PNG/receipt plus visual inspection of both city maps |
| `walking_read_artifact` | Standard file I/O/hash | Allowlisted names, bounded pages, no arbitrary paths | Exact CSV hashes, route pagination and path/size rejection |

Resources: `walking://case`, `walking://{city}/manifest`, `walking://{city}/graph`. The suite reads each family. Prompt: `municipal_walking_review(city)`; discovery and content are checked. Some hosts expose prompt/resource helpers and others expose only tools; host-specific gaps must be reported, not disguised as protocol failure.

Missing input, unknown city/feature/node/edge, remote coordinates, invalid budgets/speeds, nonexistent closure links, duplicate run IDs, arbitrary artifact paths, incompatible comparisons and excessive output limits are rejection cases. Each check asserts the reason, not only an error flag.

Agent review exposed a specific interpretation hazard: k-shortest paths can overlap. `walking_route` alternatives do not establish availability after a link closure; inspect the new per-rank flags and overlap, then use the separately solved closure analysis for modeled rerouting. The [version-1 narrative review](evidence/narrative-review.md) preserves the original Amsterdam/Helsinki errors. The [current dossier](evidence/issue-39/README.md) records all four hosts' matching diagnostic results and passing targeted JSON claims while retaining broader Hermes prose qualifications.

Not admitted: all of OSMnx, all original MCP tools, every driver/parameter, motor-speed imputation, DEM/elevation/grade, metric intersection consolidation, calibrated pedestrian simulation, barriers/turn restrictions, continuous-edge isochrone polygons, wheelchair routing, population coverage, authoritative school/library completeness, or whole-city/global reachability. Add a new operation only with its data contract, municipal need and native comparison.
