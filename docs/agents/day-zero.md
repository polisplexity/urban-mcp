# Agent operation from a fresh case workspace

The acceptance goal is that an independently configured agent can complete an admitted municipal case without knowing this conversation. It must discover the available inputs and operations, recognize missing data and report limits. The [master test record](../../MASTER_TEST_RECORD.md) separates native computation, MCP protocol checks, host artifacts and factual answer review.

| Component | Purpose | Limit |
| --- | --- | --- |
| MCP | Typed operations, resources and results | A protocol alone does not supply complete data or preparation knowledge |
| Registry/preflight | Case requirements and missing inputs | A candidate source is not an admitted asset |
| Agent Skill | Short procedure and case-specific checks | Host loading varies; a skill grants no permission or sandbox |
| Runbook/prompts/resources | Equivalent route for hosts without skills | Discovery and support must be tested per host |
| AGENTS.md | Repository contribution rules | Not a scientific execution contract |
| Optional SOUL.md | Host-specific identity/style | Not an MCP standard or substitute for data, permissions or validation |
| Agent runtime | User-selected orchestration/model | Not a mandatory dependency of the capability package |

Select a capability and read its requirements progressively rather than loading the entire 229-entry catalog into every session. The repository skill supports an existing host; it does not require a new proprietary agent, framework or provider.

## Reproduce the implemented cases

Clone `main` and record `git rev-parse HEAD`. Follow the complete data/Docker/MCP instructions in the [Helsinki inventory guide](../../cases/helsinki-service-inventory/README.md), [Helsinki/Amsterdam walking guide](../../cases/two-city-walking/README.md), [two-city historical vegetation guide](../../cases/two-city-vegetation/README.md) or [historical SUMO guide](../../cases/two-city-sumo/README.md). For walking use the [issue-39 task and procedure](../../cases/two-city-walking/issue-39.md); for vegetation use [agent-task-v2.md](../../cases/two-city-vegetation/agent-task-v2.md); for SUMO use [agent-task.md](../../cases/two-city-sumo/agent-task.md). Earlier tasks remain historical observations. Deterministic suites require no model account. Host maintenance scripts need Python 3.11+ and `requirements-dev.txt`; GIS engines run in Docker.

Generate configuration with `tools/client_config.py --capability inventory|walking|vegetation|sumo --format mcp-json|codex|hermes --data-dir <fresh-workspace>`. The alternatives separated by `|` describe choices, not a literal shell command. The generator supplies only the case server. Preserve production host settings and use an independent data mount for each city/host. On Linux, its Hermes output establishes the repository working directory with GNU `env -C` before starting Docker.

For example, after building the walking image and configuring an isolated Hermes profile:

```sh
python tools/run_agent_check.py codex --capability walking --city helsinki --label walking-helsinki-my-review --task cases/two-city-walking/agent-task-issue-39.md
# From Windows with Docker in WSL, add --wsl-distro Ubuntu-22.04.
python tools/run_agent_check.py hermes --capability walking --city helsinki --label walking-helsinki-my-review --task cases/two-city-walking/agent-task-issue-39.md --hermes-home /absolute/path/to/fresh-profile
```

The Hermes profile must already contain the generated MCP configuration pointing to `.urban-mcp/hermes-walking-helsinki-my-review` and your privately configured model/provider authentication. The runner does not rewrite its data mount. Use another fresh profile/label for Amsterdam. The full walking guide includes export and review commands; do not publish raw host logs.

For vegetation, build the `vegetation` Compose profile, generate a configuration with `--capability vegetation`, and use new `vegetation-<city>-<label>` mounts/profiles. Run the unchanged v2 blind task and follow the shared guide's strict export/review commands. Start with status → snapshot harvest → preparation → class catalog → baseline/sensitivity → comparison → complete paged CSVs → map receipt. Read pages of at most 12,000 characters until `next_offset` is null. Keep 2021 class coverage separate from 2025 population, explicit water/NoData denominators and unknown counts. The source water-zone label is not evidence of zero land.

## Review evidence and failures

Give the host the public blind task without expected answers. Check complete municipal execution, missing required data, incompatible units and native-tool failure. The host must produce a verifiable artifact/receipt or identify the precise blocker. A plausible answer, tools/list response or successful process exit is insufficient.

Record exact source commit, input hashes/rights, host/model/version, task hash, transport, tool coverage, artifacts, errors and recovery. Compare native and MCP results independently, then review the final factual claims. Keep numerical artifacts, structured answer claims and narrative verdicts separate. The current walking evidence admits issue-39 facts from both hosts while preserving broader Hermes prose qualifications and all historical failed answers.

The vegetation evidence verifies all four hosts' numerical artifacts, complete required CSV pages and answer JSON. Codex Helsinki's brief passes; Codex Amsterdam exceeds the length constraint; both Hermes briefs fail factual review. Preserve these verdicts, V1 truncation and observed Hermes circuit-breaker/recovery limitations; merging into `main` is not a new host run or independent-person third-city qualification.

Agent tests use the selected host's existing authentication. Do not create messaging connectors, reuse a production gateway/profile, publish credentials or export system prompts, reasoning or private configuration. The Codex benchmark authorizes only this case's MCP within the requested test and uses a read-only shell policy; the public task forbids unrelated tools and the exporter checks the trace.

Publish reviewed, scoped evidence and update the master record. Host/model/version and skill/transport support belong to the result; no experiment promises identical behavior from every client or model. Historical public tasks and observed transcripts retain their original bytes and language.
## Historical SUMO profile

The [two-city SUMO guide](../../cases/two-city-sumo/README.md) documents the
agent-neutral profile merged on `main` in PR #43. Generate a separate configuration
with `tools/client_config.py --capability sumo`; use a new mount for each city
and host. The official SDK FastMCP server reuses four original MCP families
and adds nine municipal bindings. No model/SOUL/agent framework is required
inside it. Use the [blind task](../../cases/two-city-sumo/agent-task.md), a
420-second tool timeout, the full comparison/source page chains and the
SUMO-specific export/review tools. Do not infer forecast readiness from native
exit zero, a numeric match or a successful model answer. Preserve source-model
warnings, censored trips, teleport exclusions, recovered argument failures and
explicit prose verdicts. The existing earlier capability guides below retain
their original scopes.
