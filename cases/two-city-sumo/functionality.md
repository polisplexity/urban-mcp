# Operation coverage and justified additions

The profile advertises **13 tools**. The independent SDK suite exercises
every tool, static resource, both resource templates and the prompt. The
blind host task exercises all tool families and complete paged comparison
data; it does not claim either host viewed returned PNG receipts.

| Advertised operation | Original behavior retained / missing binding supplied | Verification |
| --- | --- | --- |
| `get_sumo_info` | Reused original version/path diagnostics | Actual installed native version over stdio |
| `control_simulation` | Reused connect/absolute step/disconnect; new city/run ownership, 60 s horizon, immutable IDs, no external config/hosts, EOF cleanup | Independent native TraCI equality, backwards/out-of-horizon/double-connect rejection, live process reaped at EOF |
| `query_simulation_state` | Reused vehicle list, simulation counters, speed/position/acceleration/lane/route; disconnected state becomes an explicit error | Same IDs, five values and counters as direct native connection at identical time/seed |
| `run_analysis` | Reused original FCD sample analysis; path restricted to a case FCD artifact | Independent streaming gzip/XML sample count and two-decimal mean |
| `sumo_status` | Added compact supported sources, rights, missing data, method and lifecycle discovery | Actual payload and recovery after expected failures |
| `harvest_sumo_data` | Added exact publisher acquisition and locked snapshot restore | Both actual source harvests; restored byte/hash/identity/rights checks; synthetic corruption/traversal/duplicate/symlink failures |
| `read_sumo_source` | Added complete bounded manifest/license/config/recipe pages | Every returned page reconstructed and compared with source bytes/text |
| `prepare_sumo_case` | Added deterministic demand-window binding, source definitions/routes/signals and explicit corridor cohort | Every selected original vehicle subtree compared; counts/IDs/units retained |
| `sumo_network_info` | Added network/target edge/lane/XY inspection | Original network loader, exact edge geometry and lane speed/permission checks |
| `run_sumo_scenario` | Added fixed-seed preserved-input baseline and VSS works limit; independent owned native processes | Full native/MCP summaries and all-vehicle/cohort CSVs match; XML/state oracle includes censored/teleport cases |
| `compare_sumo_runs` | Added keyed completed-pair analysis with insertion delay, censoring, teleport exclusions and strict >30 s flags | Independent arrival-difference join for every cohort row; incompatible scenario comparison rejected |
| `read_sumo_artifact` | Added bounded full CSV/JSON/report paging and PNG receipts | Complete comparison page chains, exact hashes, unsafe paths refused |
| `render_sumo_map` | Added source network/corridor and completion-state PNG | Native/MCP/host byte identity; separate human image review |

`sumo://case`, `sumo://{city}/manifest`, `sumo://{city}/quality` and
`municipal_sumo_review(city)` are separately exercised through the SDK.
Complete raw request receipts remain available through paged source reads;
the manifest resource is compact and points to them.

## Every original tool has a disposition

The unmodified original MCP checkout registers eleven tools. Re-registration
does not mean all upstream methods are admitted for municipal use.

| Original registered tool | Disposition |
| --- | --- |
| `get_sumo_info` | Reused |
| `control_simulation` | Reused with ownership/time/model guards |
| `query_simulation_state` | Reused; bounded live list and five original vehicle variables |
| `run_analysis` | Reused FCD sample analysis with canonical artifact path |
| `manage_network` | Excluded; generated/converted networks need a separate input-validation case |
| `convert_ezdesignx_network` | Excluded; no reviewed municipal ezdesignX asset |
| `manage_demand` | Excluded; random/synthesized demand is not the harvested historical model |
| `optimize_traffic_signals` | Excluded; needs calibrated constraints, objectives and independent validation |
| `run_workflow` | Excluded; generated grid/signal/RL pipelines change this experiment |
| `manage_rl_task` | Excluded; no training/field-validation contract |
| `run_simple_simulation_tool` | Excluded; original implementation adds `--random` |

The new code uses Python because it directly calls the selected original
Python MCP functions, sumolib and TraCI while the original C++ SUMO binary
performs the numerical simulation. The framework is the original project's
**official MCP Python SDK FastMCP (`mcp==1.25.0`)**, separate from the
third-party `fastmcp` package used by the GDAL case. Neither a universal
language choice nor an agent/provider dependency is introduced.

Counters returned after `simulationStep(absolute_time)` describe that TraCI
advance. An advance can span multiple native numerical steps. They are not
whole-run cumulative totals; use native statistics and explicit CSV rows for
run totals. FCD's sample-weighted mean speed/count is not the number of
unique vehicles, a journey mean, field measurement or exposure metric.
