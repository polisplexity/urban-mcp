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

Clone `main` and record `git rev-parse HEAD`. Follow the complete data/Docker/MCP instructions in the [Helsinki inventory guide](../../cases/helsinki-service-inventory/README.md) or [Helsinki/Amsterdam walking guide](../../cases/two-city-walking/README.md). For current walking host tests use the [issue-39 task and procedure](../../cases/two-city-walking/issue-39.md), not the earlier v1 task. Deterministic suites require no model account.

Generate configuration with `tools/client_config.py --capability inventory|walking --format mcp-json|codex|hermes --data-dir <fresh-workspace>`. The alternatives separated by `|` describe choices, not a literal shell command. The generator supplies only the case server. Preserve production host settings and use an independent data mount for each city/host. On Linux, its Hermes output establishes the repository working directory with GNU `env -C` before starting Docker.

For example, after building the walking image and configuring an isolated Hermes profile:

```sh
python tools/run_agent_check.py codex --capability walking --city helsinki --label walking-helsinki-my-review --task cases/two-city-walking/agent-task-issue-39.md
# From Windows with Docker in WSL, add --wsl-distro Ubuntu-22.04.
python tools/run_agent_check.py hermes --capability walking --city helsinki --label walking-helsinki-my-review --task cases/two-city-walking/agent-task-issue-39.md --hermes-home /absolute/path/to/fresh-profile
```

The Hermes profile must already contain the generated MCP configuration pointing to `.urban-mcp/hermes-walking-helsinki-my-review` and your privately configured model/provider authentication. The runner does not rewrite its data mount. Use another fresh profile/label for Amsterdam. The full walking guide includes export and review commands; do not publish raw host logs.

## Review evidence and failures

Give the host the public blind task without expected answers. Check complete municipal execution, missing required data, incompatible units and native-tool failure. The host must produce a verifiable artifact/receipt or identify the precise blocker. A plausible answer, tools/list response or successful process exit is insufficient.

Record exact source commit, input hashes/rights, host/model/version, task hash, transport, tool coverage, artifacts, errors and recovery. Compare native and MCP results independently, then review the final factual claims. Keep numerical artifacts, structured answer claims and narrative verdicts separate. The current walking evidence admits issue-39 facts from both hosts while preserving broader Hermes prose qualifications and all historical failed answers.

Agent tests use the selected host's existing authentication. Do not create messaging connectors, reuse a production gateway/profile, publish credentials or export system prompts, reasoning or private configuration. The Codex benchmark authorizes only this case's MCP within the requested test and uses a read-only shell policy; the public task forbids unrelated tools and the exporter checks the trace.

Publish reviewed, scoped evidence and update the master record. Host/model/version and skill/transport support belong to the result; no experiment promises identical behavior from every client or model. Historical public tasks and observed transcripts retain their original bytes and language.
