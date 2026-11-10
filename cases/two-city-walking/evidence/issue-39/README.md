# Issue #39 evidence: explicit transitions and closed-link membership

This is a new versioned experiment. The original [v1 evidence and failed narratives](../README.md) remain unchanged. Read the [interface/reproduction guide](../../issue-39.md) and [master record](../../../../MASTER_TEST_RECORD.md).

## Results

| City | Native/stdio-MCP checks | Codex final case calls | Hermes final case calls | Exact diagnostic JSON claims |
| --- | ---: | ---: | ---: | --- |
| Helsinki | 84 passed | 34 | 23 | Both hosts passed |
| Amsterdam | 83 passed | 27 | 23 | Both hosts passed |

Each host exercised all 15 advertised tools. Extra calls include host resource/prompt helpers. Four independent final workspaces restored their own locked snapshots. The complete comparison and selected route responses match native evidence; baseline/closure CSVs, maps and exported GraphML match the native artifacts. The original v1 CSV bytes are unchanged by this version.

`agents.json` checks the answer's fenced JSON against native evidence, field by field: every crossing ID, affected origin still within, newly unreachable origin, baseline/scenario membership set, diagnostic origin, both per-path booleans and avoiding-rank list. It separately retains a hash-bound [narrative review](narrative-review.json). Both Codex briefs pass this observed review. Hermes correctly reports the issue-39 facts, but broader prose still has unsupported or incorrect statements; see the qualifications below. No model-wide accuracy or unsupervised municipal-planning claim is established.

## Files

- `reproduction.json`: fresh snapshot restoration, canonical engine/diagnostic hashes, runtime/input identities and per-city artifact hashes.
- `<city>/native-comparison.json`: every school's statuses, distances, destination IDs, booleans, transition labels and keyed closed-link membership, including unchanged/unreachable objects.
- `<city>/native-route-diagnostics.json`: exact regression request and original-graph paths with ranks, matched closed edges, avoiding flags and overlap counts.
- `<city>/mcp.json`, `mcp-tools.json`: all exposed tools/resources/prompt, independent CSV/keyed-route joins, reversed-pair/invalid-input checks and concurrent cold graph inspections.
- `<city>/codex-*`, `hermes-*`: observed answers, selected public-case traces, process/task receipts, and **complete** comparison/closed-link route responses. The results files come from the recorded tool responses, not from an expected-answer file supplied to the model.
- Native CSV/report/map/harvest files: compact outputs with the same OSM license/attribution. Large input databases remain offered by the [locked release](https://github.com/polisplexity/urban-mcp/releases/tag/data-walking-20261110).
- `runtime-failure.json`: the earlier concurrent cold-cache failure and bounded correction. That attempt is not admitted as a successful workflow.

## Targeted facts now reported explicitly

Helsinki has five `within_to_outside` crossings: `node/8862204483`, `node/8862204485`, `way/1038696462`, `way/38192458`, `way/592362656`. Six other affected objects stay within. Amsterdam has no crossings; all five affected objects stay within. Neither city gains new unreachable origins under the chosen closure.

For the predeclared Helsinki regression origin `node/1017984829`, both returned original-graph paths use `(5912225309,501610897,0)` and share 23 keyed edges/physical links. For Amsterdam origin `node/2741066971`, both use `(46386552,12534903767,0)` and share 11. Both avoiding-rank lists are empty. The actual closure scenarios reroute to their own solutions; original-graph k-shortest alternatives are not substituted for them.

## Prose qualifications remain visible

The new structured evidence fixes the two targeted interpretation failures in all four observed claim objects. It does not eliminate free-form model errors. Helsinki Hermes misidentifies the all-feature outside-buffer flag as a library and adds unverified component/physical-shortcut explanations. Amsterdam Hermes incorrectly suggests a speed change affects a **distance** threshold share, speculates about a spatial cluster and attributes a topology check to graph export. The correct recipe uses speed only for estimated minutes; export only writes the graph and returns its receipt. The native suite tests the graph round trip separately. Both Hermes responses are longer than the requested compact format.

Treat the issue-39 fields/checked claims as accepted for this experiment, and the additional prose as requiring correction before municipal use. The old failed answers have not been edited into passes.

## Runtime and test recovery

The first issue-39 Codex Helsinki attempt issued three concurrent cold inspections and reached the 3 GB container memory cap. Plain `lru_cache` permits repeated execution of a cold miss. A reentrant cache lock now ensures one deserialization; the three-thread synthetic regression and real concurrent MCP cold-read test pass under the same resource cap. All final host runs use the corrected engine. A missing `asyncio` import in the first concurrency-test CI revision was corrected before final verification; the failed CI remains visible in repository history.

No private provider configuration, credentials, reasoning, system prompts or unrelated connector outputs are exported. Source/derived OSM data remains **ODbL-1.0**, © OpenStreetMap contributors; see the [data license notice](../LICENSE.md).
