# Master test record

This is the project entry point for evidence: what we tested, why it matters to a municipality, and how far the evidence supports a claim. A catalog entry, a successful container startup and a tool listing do not establish a working capability.

## Current walking revision: explicit diagnostic evidence, issue #39

The [v2 interface and reproduction guide](cases/two-city-walking/issue-39.md) documents the implemented correction. `walking_compare` now explicitly identifies every school's before/after distance, destination, threshold booleans, transition and closed-link membership. `walking_route(closed_links=...)` marks every original-graph path's exact closed keyed edges, avoiding flag and overlap. The solver, pinned OSM inputs, distance rules and all original baseline/closure CSV bytes remain unchanged.

| Current test | Helsinki | Amsterdam | Why |
| --- | --- | --- | --- |
| Native/stdio-MCP suite, all 15 tools/resources/prompt | 84 passed | 83 passed | Independent CSV/keyed-route joins, every new field and full native/MCP equality |
| Exact crossing IDs | 5 | 0 | Prevent interpreting detour magnitude as a threshold crossing |
| Affected objects that remain within threshold | 6 | 5 | Preserve large non-crossing detours as a separate result |
| Baseline routes using the closed link / scenario routes | 11 / 0 | 5 / 0 | Evidence of actual directed/keyed link membership |
| Selected original-graph alternatives using the closed pair | 2 of 2 | 2 of 2 | k-shortest alternatives can both be blocked; neither is substituted for the closure rerun |
| Codex full diagnostic responses and answer JSON | Passed | Passed | Exact origin sets and per-path booleans checked independently |
| Fresh Hermes full diagnostic responses and answer JSON | Passed | Passed | Same checks through a second host/provider without expected numerical answers |

All four final workspaces restore their own public snapshots and reproduce native CSV/map/GraphML artifacts. The [v2 evidence dossier](cases/two-city-walking/evidence/issue-39/README.md) preserves full selected MCP responses, observed answers, process/task receipts and an answer-hash-bound prose review. Codex's observed briefs pass review. Hermes's targeted issue-39 facts pass, while additional prose remains qualified; this does not admit autonomous municipal recommendations. The earlier failed v1 answers and verdicts remain unchanged.

The repository suite has 32 tests, including nine diagnostic regressions and versioned artifact/answer integrity. Seven Docker regressions separately cover snapshot integrity and a three-thread cold-cache load. The real MCP suite also performs three concurrent cold inspections under the existing 3 GB cap. An initial Codex attempt reached that cap because plain `lru_cache` allowed duplicate cold graph deserializations; reentrant synchronization fixes the observed failure. See [the failure record](cases/two-city-walking/evidence/issue-39/runtime-failure.json). [The corrected two-city CI run passed](https://github.com/polisplexity/urban-mcp/actions/runs/42834941975).

## Earlier baseline experiments, retained

| Capability | Municipal scope and purpose | Native | MCP | Codex | Hermes | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| GDAL/GeoPandas service inventory | Helsinki: count registered library and health-station locations by district against 2025 district population | Passed, declared parameters | 19 tools, 72 checks | Passed, separate workspace | Passed, separate workspace | [Case](cases/helsinki-service-inventory/README.md), [agent checks](cases/helsinki-service-inventory/evidence/agents.json), [PR #37](https://github.com/polisplexity/urban-mcp/pull/37) |
| OSMnx/NetworkX walking access | Helsinki central study disk: mapped school-to-library access and hypothetical link closure | Passed, every school row vs separate forward solver | Passed, 15 tools / 62 checks | Artifacts and observed brief passed review | Artifacts passed; prose failed factual review | [Case](cases/two-city-walking/README.md), [city evidence](cases/two-city-walking/evidence/helsinki/) |
| OSMnx/NetworkX walking access | Amsterdam central study disk: transfer of the same method to a canal/bridge network | Passed, every school row vs separate forward solver | Passed, 15 tools / 62 checks | Artifacts and observed brief passed review | Artifacts passed; prose failed factual review | [Case](cases/two-city-walking/README.md), [city evidence](cases/two-city-walking/evidence/amsterdam/) |

## Why these tests

The first case establishes harvesting, provenance, coordinate handling and descriptive inventory. The walking case must establish network distances rather than Euclidean buffers, an explicit denominator, snap quality, disconnected paths, reproducible exports and a controlled disruption scenario. Two independent agent hosts must discover and operate the same MCP without access to expected answers. Two cities test transfer; they do not establish universal city coverage.

## Walking experiment, 2026-11-10

The runtime pins OSMnx 2.1.1, NetworkX 3.7 and FastMCP 3.4.2 with the full dependency lock and base-image digest. The [source audit](cases/two-city-walking/upstream-audit.md) found no license declaration for the third-party OSMnx MCP revision and reproduced incorrect keyed-route totals and wrong-area truncation. The new MIT adapter uses original OSMnx/NetworkX APIs; the unlicensed checkout is not redistributed. This is a capability-specific runtime decision.

| Measured result | Helsinki | Amsterdam | Why this check matters |
| --- | ---: | ---: | --- |
| Core mapped school objects | 48 | 40 | Explicit complete denominator for this snapshot/core; not pupils or residents |
| Within 1,200 m, baseline | 45 | 22 | Network distance plus both unverified endpoint connectors |
| Unreachable / snap-rejected | 2 / 0 | 2 / 0 | Missing modeled routes remain visible instead of disappearing from the denominator |
| Within 1,200 m after declared closure | 40 | 22 | A real detour can occur with zero threshold change |
| Objects with a detour | 11 | 5 | Separates route effects from threshold classifications |
| Accepted library objects with unknown access | 30 of 31 | 20 of 20 | The experiment cannot establish public-library service adequacy |

Data snapshots, source requests/responses, failed HTTP receipts and attribution are [publicly released](https://github.com/polisplexity/urban-mcp/releases/tag/data-walking-20261110). Both cases restore in fresh Docker workspaces. Every exposed tool, resource family and prompt is tested; six additional synthetic regressions check archive/input integrity. [GitHub's independent two-city runner passed](https://github.com/polisplexity/urban-mcp/actions/runs/42826900452). These checks require no model credential.

Host acceptance compares complete baseline/closure CSVs, graph/map receipts, tool coverage and a reviewed brief. [Preserved initial observations](cases/two-city-walking/evidence/initial-observations/) show why process exit or matching tables is insufficient: initial Hermes prose added unsupported explanations, and a later launcher failure still returned exit code 0. The [evidence guide](cases/two-city-walking/evidence/README.md) describes those failures and corrections. Codex prompt retrieval was not exposed by the tested host; protocol tests and Hermes check the prompt separately.

**Version 1 host result:** all four city/host runs operate the 15 tools and reproduce the native artifacts. Codex's two observed briefs pass the declared factual review. Hermes's prose is not admitted: it mislabels individual Helsinki threshold crossings and describes an overlapping Amsterdam route as available after closure. The [answer-hash-bound narrative review](cases/two-city-walking/evidence/narrative-review.md) gives exact corrections. Computational readiness does not establish unsupervised municipal recommendation readiness.

[Issue #39](https://github.com/polisplexity/urban-mcp/issues/39) is implemented by the current diagnostic revision above. Its new evidence establishes the observed classification/membership improvement while retaining the original failures and broader prose qualifications.

## What remains unproven

The research catalog is not a coverage claim. Walking access is not wheelchair accessibility, observed travel time, population coverage, school enrollment, service capacity or an authoritative municipal finding. Every result must retain its study boundary, acquisition date, data license, assumptions and known omissions.

## Updating this record

Each new row needs a municipal question, exact input assets and rights, pinned engine/interface versions, native comparison, real MCP transport checks, tool-by-tool coverage, host traces with reviewed artifacts, reproduction commands and documented failures. Mark a stage passed only after its evidence exists. Preserve unsuccessful observations when they explain a correction. New project documentation and test tasks are in English; historical agent transcripts remain verbatim evidence.
