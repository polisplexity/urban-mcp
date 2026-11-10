# Urban MCP

Open infrastructure that lets any MCP-capable agent operate urban open-source tools with the data, installation recipes and evidence needed to do useful municipal work.

**Start with the [master test record](MASTER_TEST_RECORD.md): what we tested, why, the evidence and the limits.** Catalog entries remain research until a scoped municipal case passes data, native engine, MCP and independent-host checks.

## Executable cases

- [Helsinki service inventory](cases/helsinki-service-inventory/README.md): public library and health-station registry locations against 2025 district population; original GDAL MCP plus municipal preparation/inventory operations, with Codex and Hermes evidence. [PR #37](https://github.com/polisplexity/urban-mcp/pull/37).
- [Helsinki and Amsterdam walking access](cases/two-city-walking/README.md): mapped school-to-library routes, snap/disconnection accounting and an explicit link-closure scenario. Includes an OSMnx MCP source audit, separately implemented adapter, harvested ODbL snapshots, Docker recipes, native/protocol checks and blind host tasks. Consult the master record for completed stages.

Use `feat/two-city-walking-accessibility` for the combined implementation. The inventory PR is based on `rfc/data-ready-capabilities`; these branches remain reviewable, not a claim that all work is merged into the default branch. [RFC #1](https://github.com/polisplexity/urban-mcp/pull/1) tracks the wider proposal.

## What a contribution contains

A capability package joins the original software/API, the missing interface delta, exact data sources and rights, preparation/binding, a municipal question, reproducible installation/startup, native/MCP comparisons, reviewed host evidence and clear limitations. A portal link, container startup or tool listing alone is insufficient.

The [research registry](registry/tools.json), [data matrix](docs/data/tool-data-matrix.md) and [public tasks](docs/tasks.md) help locate candidate work; their generic requirements are not proof that those tools run. Historical research notes and original earlier agent transcripts may retain their original language. Current project entry points, new capability code/documentation, test tasks and reports are maintained in English; preserve observed evidence verbatim and add an English interpretation when needed.

## Reproduce and contribute

Follow the case's Docker instructions for a deterministic run without an LLM account. For an agent test, configure the same stdio MCP in your existing host; no proprietary agent, model provider or mandatory SOUL framework is required. [Configuration generator](tools/client_config.py), [blind host runner](tools/run_agent_check.py), [contribution guide](CONTRIBUTING.md), [roadmap](docs/roadmap.md).

```sh
python -m pip install -r requirements-dev.txt
python tools/validate.py
python -m unittest discover -s tests
```

Each executable case additionally has native/MCP Docker checks. Metadata CI is a separate stage. New families do not inherit another tool's readiness, language or framework choice.

This repository's original code is MIT licensed. Each upstream program and dataset retains its own terms. Walking snapshots and derived databases are ODbL-1.0, with © OpenStreetMap contributors attribution. Keep private product code, credentials, operator data and bulk caches outside Git. Public recipes, source receipts, reviewed evidence and useful failures make it possible for anyone to repeat, inspect and improve the work.
