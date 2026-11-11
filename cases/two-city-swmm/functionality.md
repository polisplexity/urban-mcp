# Declared operation coverage

The profile advertises **27 tools: 18 reused function families and nine additions**.
All native/stdio tools, eight resource families and the prompt are exercised in
both city suites. Host operation, page/query/JSON and prose verdicts remain
separate in [the evidence index](evidence/agents.json). This table is a bounded
tested contract, not admission of every SWMM feature or every parameter choice.

The full Hermes runs cover every tool family but omit live subcatchment
`runoff`. Separate narrowly scoped runs validate live rainfall/runoff values
against direct PySWMM in both cities; see [the supplement](evidence/live-observations.json).
This does not turn the original full-task verdicts into passes.

| Tool(s) | Original or added | Tested meaning |
| --- | --- | --- |
| model_inspect | Reused | Native version, original units, counts and time window; outside-root rejection |
| model_list_objects | Reused | Node, link, subcatchment, raingage and LID IDs; empty LID catalog stays empty |
| simulation_run, run_summary | Reused with marked native balance-lifetime fix | Separate five-minute inspection, generated artifacts and completed status; errors captured before engine close |
| output_inspect | Reused, bounded response | Binary identity, counts and sample IDs; complete IDs remain queryable |
| simulation_create | Reused, bounded response | Isolated live process, original source IDs, exact status URI, stored-state load |
| simulation_start, simulation_observe, simulation_step | Reused | Native live state; node/link/subcatchment/raingage/system observations, 30 s advancement, all four approved control lists |
| simulation_save_hotstart, simulation_stop, simulation_close | Reused | Save/load state, stop and release owned workers; loaded state does not advance the model clock automatically |
| output_query_series, output_query_snapshot | Reused with explicit typed vocabulary | Node depth, link flow, subcatchment rainfall and system outfall flow against independent native binary values; inclusive range/snapshot semantics, original bounds/units |
| simulation_run_start, simulation_task_status, simulation_task_cancel | Reused | Asynchronous batch state and cancellation; cancelled results excluded from municipal comparisons |
| run_cleanup | Reused | Retention disabled; removes zero runs and preserves evidence |
| swmm_status | Added | Exact cities/method/limits, false admission flags, original output vocabulary, two-worker budget and static resource URIs |
| harvest_swmm_data | Added | Locked public snapshot or real publisher acquisition in a fresh mount, rights and byte/content fingerprints |
| read_swmm_source | Added | Complete manifest, requests, rights, recipe and admitted textual source pages; no arbitrary paths or ZIP-as-text |
| prepare_swmm_case | Added | Observed hourly forcing, explicit dates/threads/zero-area normalization, source-based target, baseline/capacity75/separate inspection inputs |
| inspect_swmm_case | Added | Scope, original IDs/units, transformations, exact paths and quality URI |
| run_swmm_scenario | Added binding around original batch | Full 72-hour run, native warnings/continuity, every node/outfall row, immutable original run ID and exact resource URIs |
| compare_swmm_runs | Added | Complete same-source node denominator, report volumes and ≥10 m³ transitions; explicit city/scenario/source checks |
| read_swmm_artifact | Added | Full node/outfall/comparison CSV/JSON paging with original byte hashes; ≤12,000 characters per page |
| read_swmm_resource | Added bridge | Seven original resource families plus municipal quality, bounded pages, exact URI/expected-error guidance |

Original resource families are `pyswmm://models`, `pyswmm://runtime/status`,
run summary/report/output metadata, session status and task status. The added
resource is `swmm://cities/{city}/quality`. The actual MCP prompt is
`municipal_drainage_review`. Deterministic tests use SDK discovery/read/get;
hosts can use the resource bridge when their UI lacks native resource reads.
Host-provided discovery helpers are not counted as additional server tools.

Only one page of the original short report is required in the blind host task;
complete source/comparison/node/outfall pages are mandatory. Original binary
output resources are metadata, not binary file expansion. Native checks compare
full report-derived CSVs and selected binary observations; they do not claim
bitwise equality of every internal solver state or whole OS image.

Live API controls are isolated software tests with declared values and source
IDs. They neither actuate municipal infrastructure nor alter either bound
scenario's inputs/results. An empty LID catalog or zero groundwater variable
does not validate LID design, groundwater physics or pollutant transport.
