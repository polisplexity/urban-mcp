# Reviewed vegetation evidence

Current deterministic and host evidence is **v2**, acquired/tested 2026-11-10. All four host tasks launched from source commit `1f3a7b9f4fcb2b3ead1b22b5d4a96823dd430f34` with [agent-task-v2.md](../agent-task-v2.md). No numerical answers were supplied in the task. The source commit and exact task SHA are recorded at process launch. Later documentation/export/review commits are not new LLM experiments.

## Dossier

- [reproduction.json](reproduction.json): executing engine/server/data/interface hashes, runtime lock, two public input snapshots, check counts and output hashes. Native checks are 110/131; both exercise the same 21 tools. Twelve synthetic tests and 69 original regressions are separate.
- [runtime.json](runtime.json): observed installed versions, including different GDAL libraries bundled with Rasterio and Pyogrio.
- [upstream-audit.json](upstream-audit.json): original numerical/API defects reproduced on explicitly synthetic fixtures and source hashes.
- [agents.json](agents.json): four host receipts, actual bounded MCP analysis/comparison equality, every returned required CSV page's text hash/continuation, complete artifact equality, exact structured answer claims and separate prose verdicts.
- [narrative-review.json](narrative-review.json): explicit review of unchanged answer bytes, supported statements, errors and constraint failures. A correct numerical artifact does not establish correct prose.
- [development-failures.json](development-failures.json): failed development expectations, middleware ordering, V1 truncation, corrections and full reverification requirements.

Each [Helsinki](helsinki/native.json) / [Amsterdam](amsterdam/native.json) directory contains `harvest.json`, full baseline/sensitivity native JSON and comparison, zone and class-count CSVs, reports/map, MCP schemas/catalogs and named native/stdio checks. `<host>-process.json`, `<host>-trace.json`, `<host>-answer.md`, `<host>-analysis-results.json` and `<host>-comparison-results.json` preserve public-case observations. Raw host events, databases, reasoning, system prompts, configuration and credentials are excluded. Returned CSV page receipts are checked against exact artifact text, not reconstructed and relabeled as a raw host response.

## Actual host verdicts

| Host/city | Calls | All 21 tools have a successful response | Actual bounded analyses/comparison, full CSV pages and artifacts | Answer JSON | Broader brief |
| --- | --- | --- | --- | --- | --- |
| Codex / Helsinki | 56 | Yes | Pass | Pass | Factual pass, 470 words |
| Codex / Amsterdam | 57 | Yes | Pass | Pass | Factual pass, 718 words exceeds 600 |
| Hermes / Helsinki | 88 | Yes | Pass | Pass | Factual fail, 886 words |
| Hermes / Amsterdam | 93 | Yes | Pass | Pass | Factual fail, 1,089 words |

Examples retained in failed Hermes prose: Helsinki's 3,794 vegetation pixels are misstated as 19, population rounding and acquisition dates are asserted inconsistently, and explanations for the unresolved population gap are speculative. Amsterdam's missing population is incorrectly equated to no registered residents. The native artifacts and structured JSON preserve correct counts and unknown values. See the hash-bound review for precise corrections; do not rewrite observed answers to hide failures.

Observed Codex lacks prompt retrieval; its answer reports that gap and uses original returned justification metadata. Hermes retrieves the municipal prompt. Deterministic tests fetch every original resource/prompt family regardless of host feature support. Hermes's heuristic treats consecutive application-level validation/justification errors as temporary server unavailability: 21 such host refusals in Helsinki and 23 in Amsterdam are preserved in traces. Recovery leads to successful operation and final semantic rejection checks; a host refusal alone is not proof that the server executed or semantically rejected an operation. These extra calls are part of the observed host counts.

## Historical observations

[initial-observations/v1](initial-observations/v1/status.json) preserves the unchanged task, all four answers/traces/process receipts and original native evidence. Amsterdam Hermes received 165,167/166,092-character primary analyses truncated to invalid JSON. Selected responses are explicitly null/incomplete and **not admitted as complete transport evidence**. The v2 primary projection avoids duplicating all zone rows, caps artifact pages at 12,000 characters, rejects the reproduced outside-window bug and repeats both cities/hosts from empty mounts. Exact baseline/sensitivity CSV and map bytes remain equal to v1.

Final-product qualification remains pending. These are original-team experiments, not the independent person reproducing a third city required by [policy](../../../docs/product-qualification.md). [Repeat/export/review instructions](../README.md).
