# Master test record

This is the project entry point for evidence: what we tested, why it matters to a municipality, and how far the evidence supports a claim. A catalog entry, a successful container startup and a tool listing do not establish a working capability.

## Final-product qualification: pending independent reproduction

The [required qualification rule](docs/product-qualification.md) separates development integration from final-product promotion. A person outside the original implementation and initial test team must harvest and reproduce the same capability in a third, distinct city after the first two, with full native/MCP coverage, two-host evidence and an accepted public review. Another model, agent instance or CI runner operated by the original team does not meet that condition.

| Capability | Initial developer-operated cities | Independent third-city review | Final-product promotion |
| --- | --- | --- | --- |
| Walking access | Helsinki, Amsterdam | Pending; no independent operator/city/evidence accepted | Blocked |
| Service inventory | Helsinki; second initial city pending | Pending | Blocked |
| Historical vegetation | Helsinki, Amsterdam, original team | Pending; no independent person/city/evidence accepted | Blocked |

The [qualification register](registry/product-qualification.json) records `product_qualified=false` for all three capabilities. [Issue #41](https://github.com/polisplexity/urban-mcp/issues/41) is the public independent walking reproduction task. Existing case admission, numerical results, observed host verdicts and merged PRs remain valid for their stated development scopes. No third-party reproduction is claimed. The destination final repository/release must be named in a later reviewed promotion change.

## Reproduce the current integrated source

PR [#42](https://github.com/polisplexity/urban-mcp/pull/42) is merged into `main` at [6f929fc](https://github.com/polisplexity/urban-mcp/commit/6f929fc3f1c0b2ccd8166496f8fd641c5efa73f5), following #1 → #37 → #38 → #40. There were no merge conflicts. Clone/update `main`, record `git rev-parse HEAD` and follow the English [vegetation Docker/live/snapshot/host guide](cases/two-city-vegetation/README.md), [inventory guide](cases/helsinki-service-inventory/README.md) or [walking diagnostics guide](cases/two-city-walking/issue-39.md). Preserve old workspaces, observations and answer hashes.

The [vegetation integration receipt](docs/integration/2026-11-10-vegetation-main.json) records the reviewed PR head, merge/source equality, CI heads/results and source/evidence fingerprints. Documentation changes after the merge do not create new Codex/Hermes observations. The earlier integration receipt below remains historical evidence for #1–#40. Final-product qualification is still pending independent-person reproduction in a third city.

### PR #42 integration verified, 2026-11-10

All four workflows passed on the integrated `6f929fc` main commit. Public log checks confirm the counts below. Documentation commit `ea3ad85` also passed metadata/reference CI and both vegetation jobs, with executable source, input locks and all observed case evidence unchanged. No host experiment was rerun or relabeled during integration. Issue #35 was closed by the merge; issue #41 remains open and the qualification register remains pending.

| CI on integrated main | Observed result |
| --- | --- |
| [Planning contracts and reference data](https://github.com/polisplexity/urban-mcp/actions/runs/42882308988) | Passed; 36 repository tests, metadata contracts, pinned reference assets and Docker preflight |
| [Vegetation, Helsinki and Amsterdam](https://github.com/polisplexity/urban-mcp/actions/runs/42882308943) | Passed; 110/131 native/stdio checks, all 21 tools/resources/prompts, 12 synthetic regressions and 69 original-server tests in each job |
| [Existing Helsinki inventory](https://github.com/polisplexity/urban-mcp/actions/runs/42882309048) | Passed; 72 native/MCP checks and 69 original-server regressions |
| [Existing two-city walking](https://github.com/polisplexity/urban-mcp/actions/runs/42882309050) | Passed; Helsinki 84 / Amsterdam 83 native/MCP checks |

The English [contribution checks](CONTRIBUTING.md), [agent runbook](docs/agents/day-zero.md), [roadmap](docs/roadmap.md) and [public task index](docs/tasks.md) now include the implemented vegetation workflow. Current entry-point verification covers 133 local Markdown targets and eight Bash blocks. Source/evidence hashes and exact CI job URLs are retained in the integration receipt.

## Historical vegetation: two-city evidence, issue #35 / PR #42

Municipal purpose: identify statistical zones with low **mapped 2021 vegetation share**, and report attached **2025 aggregate population**, to select a bounded local data-validation exercise. [Reproduction guide](cases/two-city-vegetation/README.md), [exact findings and maps](cases/two-city-vegetation/findings.md), [21-operation coverage](cases/two-city-vegetation/functionality.md), [source audit](cases/two-city-vegetation/upstream-audit.md). Source inputs were harvested in both cities and published as [hash-locked data snapshots](https://github.com/polisplexity/urban-mcp/releases/tag/data-vegetation-20261110). WorldCover/Helsinki attribution and CBS CC0 terms remain separate from MIT code licensing.

The numerical backend uses Rasterio 1.4.3, GeoPandas 1.1.1 and NumPy 2.3.3 with pinned GDAL/PROJ libraries. It reuses original GDAL MCP commit `418f401c7987e388eaaee6ad13289798a1ff69b6` and FastMCP 2.12.3; eight new municipal tools join the original 13. Python keeps the existing scientific and MCP runtime together; no agent framework/provider is required by the server. [Exact runtime receipt](cases/two-city-vegetation/evidence/runtime.json).

| Verified stage | Helsinki | Amsterdam | Why |
| --- | --- | --- | --- |
| Observed statistical zones / eligible mapped-land zones | 34 / 34 | 111 / 111 | Explicit boundary and water/NoData denominators, no water-label shortcut |
| Native/stdio-MCP, all 21 tools and resource/prompt families | 110 checks | 131 checks | Independent polygon-window class oracle, complete paged summaries and actual GIS operations |
| Strict share < 0.20: low zones / known attached population | 2 / 51,906 | 26 / 217,945 | Explicit source IDs, strict flags, no resident-pixel inference |
| Same-raster sensitivity < 0.40 | 6 / 144,068 | 65 / 557,965 known, one unknown | Threshold sensitivity, not vegetation loss |
| Codex actual MCP responses, all required CSV pages, CSV/map artifacts and answer JSON | Passed, 56 calls | Passed, 57 calls | Fresh empty city/host mount; no expected numeric answers |
| Hermes same transport/artifact/JSON checks | Passed, 88 calls | Passed, 93 calls | Fresh isolated profiles using Claude Sonnet 4.6; same agent-neutral MCP |
| Observed broader prose | Codex factual/length pass; Hermes factual fail | Codex factual pass but length fail; Hermes factual fail | Numerical success does not admit an inaccurate or noncompliant brief |

Twelve Docker categorical/integrity regressions and 69 original-server regressions pass separately. Four repository evidence regressions preserve numerical/answer bytes, complete returned page chains, explicit failed prose and strict claim types. [Native receipts](cases/two-city-vegetation/evidence/reproduction.json), [four host receipts](cases/two-city-vegetation/evidence/agents.json), [answer-hash-bound review and corrections](cases/two-city-vegetation/evidence/narrative-review.json). Host runs launched from `1f3a7b9f4fcb2b3ead1b22b5d4a96823dd430f34`; source fingerprints distinguish executing code from later documentation/evidence commits. Codex CLI 0.167.0-alpha.3.2 and Hermes 0.18.2 were used with existing private authentication.

Useful failures are retained. Original explicit raster dimensions shrink the footprint, explicit bounds are ignored, partial query windows mislocate clipped pixels, and a Visvalingam label runs Douglas–Peucker. This profile rejects these options instead of silently accepting them. Initial middleware ordering/test expectations failed, then were corrected and fully rerun. V1 Hermes Amsterdam analysis payloads were truncated; compact responses and ≤12,000-character artifact pages pass four fresh V2 runs with unchanged numeric CSV/map bytes. Hermes can also mistake consecutive tool-validation errors for server unavailability, requiring documented recovery. [Failure history](cases/two-city-vegetation/evidence/development-failures.json), [superseded observations](cases/two-city-vegetation/evidence/initial-observations/v1/status.json).

Helsinki's population difference of 13,682 remains unresolved. Amsterdam's known zone sum differs by 11, district counts are randomly rounded to five, and Groot water population is unknown; it has actual mapped land and becomes low at 0.40. NoData coverage is not classification confidence. Tree-class area is not fractional canopy; global accuracy is not local validation. These tests do not establish current vegetation, access, heat exposure, causality, every upstream function or independent-person final-product qualification. Issue #41 remains the separate independent walking task.

## Earlier integration, retained for audit

The earlier combined implementation was RFC #1 → Helsinki inventory #37 → two-city walking #38 → diagnostic revision #40. Vegetation #42 is now included as described above. Record `git rev-parse HEAD` for every independent reproduction. The English [two-city walking Docker guide](cases/two-city-walking/README.md), [walking task/export/review procedure](cases/two-city-walking/issue-39.md) and [agent runbook](docs/agents/day-zero.md) remain applicable. Use fresh workspaces and new host labels; preserve published observations and failed answers unchanged.

Integration checks repeat the deterministic suites. Existing Codex/Hermes observations remain bound to their original task, source and answer hashes; a merge or documentation translation is not a fresh LLM experiment. Historical research, tasks and observed transcripts retain their original language and bytes.

### Main integration verified, 2026-11-10

PRs [#1](https://github.com/polisplexity/urban-mcp/pull/1), [#37](https://github.com/polisplexity/urban-mcp/pull/37), [#38](https://github.com/polisplexity/urban-mcp/pull/38) and [#40](https://github.com/polisplexity/urban-mcp/pull/40) were reviewed and merged into `main` in that order. README conflicts were resolved during normal merges. The integrated source is [3802103](https://github.com/polisplexity/urban-mcp/commit/3802103e7c50fdf78dbacad8efbb03986a3487e5). Runtime modules, adapters, Compose, data recipes/locks and all published observations are byte-identical to the reviewed diagnostic head `65c011b`; English entry points now reproduce from `main`.

| CI on the integrated main commit | Observed result |
| --- | --- |
| [Planning contracts and reference data](https://github.com/polisplexity/urban-mcp/actions/runs/42849297144) | Passed; 32 repository tests, metadata contracts, six pinned reference assets and Docker metadata preflight |
| [Helsinki municipal native/MCP](https://github.com/polisplexity/urban-mcp/actions/runs/42849297104) | Passed; 19 tools / 72 checks plus 69 original GDAL-server regressions |
| [Two-city walking native/MCP](https://github.com/polisplexity/urban-mcp/actions/runs/42849297131) | Passed; Helsinki 84 checks, Amsterdam 83, all 15 tools/resources/prompt and seven synthetic integrity/cache regressions |

The [machine-readable integration receipt](docs/integration/2026-11-10-main.json) records merge times/commits, exact CI heads and jobs, count checks against public logs, source hashes and review scope. Local validation also passed; eight English entry points had 63 valid local targets and 16 Bash blocks checked before adding this receipt link. This documentation receipt follows the checked integration commit; the runtime and observed host evidence are unchanged.

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

The repository suite has 32 tests, including nine diagnostic regressions and versioned artifact/answer integrity. Seven Docker regressions separately cover snapshot integrity and a three-thread cold-cache load. The real MCP suite also performs three concurrent cold inspections under the existing 3 GB cap. An initial concurrent Codex attempt reached that cap; duplicate graph loads were inferred from plain `lru_cache` semantics. Reentrant synchronization prevents duplicate cold misses in the threaded regression, and the repeated real MCP/host checks complete under the same cap. See [the failure record](cases/two-city-walking/evidence/issue-39/runtime-failure.json). [The corrected pre-integration two-city CI run passed](https://github.com/polisplexity/urban-mcp/actions/runs/42834941975); integrated-main CI is listed above.

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
