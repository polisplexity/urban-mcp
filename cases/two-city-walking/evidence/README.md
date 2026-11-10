# Evidence guide

Read the [master test record](../../../MASTER_TEST_RECORD.md) and [municipal findings](../findings.md) before treating a successful call as a planning conclusion.

## Deterministic evidence

- `reproduction.json`: fresh public-snapshot restoration, canonical committed engine hash, runtime lock identity and artifact receipts for both cities.
- `<city>/harvest.json`: exact admitted input files, hashes, geometry/graph counts, acquisition time and source attribution. Original requests/responses and failed HTTP bodies are in the public [data release](https://github.com/polisplexity/urban-mcp/releases/tag/data-walking-20261110), not duplicated in Git.
- `<city>/native.json`: municipal baseline and quality/interpretation contract.
- `<city>/native-comparison.json`: affected objects under the declared bidirectional link closure.
- `<city>/mcp.json`, `mcp-tools.json`: every exposed operation over a real stdio subprocess, native comparisons, meaningful rejection reasons and full schemas. Each city has 62 passing checks; the source integrity suite has six additional explicitly synthetic regressions.
- `<city>/baseline.csv`, `closure.csv`, reports and `map.png`: compact public results. Large GraphML/route files remain reproducible workspace artifacts; input graphs are offered in the release.
- `upstream-audit.json`: inspected source revision, 33-tool inventory, 28 distinct original tools evaluated offline, the separate synthetic parallel-edge regression and five unexecuted live acquisition tools. Returned results are observations, not automatic correctness passes.

## Independent host evidence

`agents.json` records mechanical artifact/tool checks; it does not independently certify every narrative sentence. Each city's `codex-*` and `hermes-*` files contain a reviewed final answer, the public-case tool trace and process receipt. See `narrative-review.md` for the primary-agent review and the distinction between host workflow success, artifact equality and factual interpretation.

Codex uses a fresh ephemeral CLI context, read-only shell sandbox, no web search, unrelated MCP registrations disabled for that process, and app/plugin features disabled. Only the case MCP is approved for the authorized benchmark. Hermes uses a fresh profile per admitted city run, no inherited skills/memory, the selected existing provider's private authentication and one MCP. No messaging gateway is started. Its Linux launcher uses GNU `env -C <repo>` because this Hermes revision does not forward a configured stdio working directory.

The blind task includes no expected numerical answers. Each host starts with an empty input/output workspace, restores its own release snapshot, runs baseline/closure, reads CSV/keyed routes, exercises the 15 tools, tests an invalid remote snap and inspects map/GraphML receipts. Hermes exposes resource/prompt helpers; Codex exposes resources but did not expose prompt retrieval in the tested CLI. Protocol prompt correctness is tested separately.

## Preserved unsuccessful observations

`initial-observations/` contains the original blind task and **unaccepted** initial Hermes answers/tool traces. Their CSV artifacts matched the native engine, but narrative review found unsupported explanations of disconnected components, an inconsistent school geometry subtotal, confusion between representative points and centroids, incorrect interpretation of the outside-buffer flag, and overstatement of tag-based library admission. These are not accepted municipal findings. The task was tightened to require a concise evidence-only brief without expected answers, and fresh runs were reviewed separately.

A subsequent Hermes repeat could not initialize MCP because Docker Compose inherited an unusable working directory (`getwd: no such file or directory`). The process returned exit code 0 despite no completed municipal workflow. The launcher fix establishes a stable directory before Docker starts. This is why process exit codes alone never admit a host.

The first Codex invocation inherited startup of unrelated registered servers, although its trace contained only case calls. The runner was corrected to disable static MCP registrations and app/plugin features for the test process. Two intermediate configuration-only starts failed before a workflow because dynamic app entries from `mcp list` are not static server configurations; the final runner reads only static registration names. Private host logs/configuration are not published.

No chain of thought, system prompts, credentials, provider configuration, unrelated connector responses or complete private host sessions are included. The export tools retain only the selected public task's calls, bounded response excerpts and observed answer. Retain [data attribution](LICENSE.md) and review notes when redistributing evidence.
