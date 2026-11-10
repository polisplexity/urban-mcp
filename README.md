# Urban MCP

Open infrastructure that lets any MCP-capable agent operate urban open-source tools with the data, installation recipes and evidence needed for useful municipal work.

**Start with the [master test record](MASTER_TEST_RECORD.md): what we tested, why, the evidence and the limits.** Catalog entries remain research until a scoped municipal case passes data, native engine, MCP and independent-host checks.

**Final-product qualification is pending.** Promotion requires a [person outside the original implementation/test team to harvest and reproduce a third city](docs/product-qualification.md), after the first two, with reviewed native/MCP and two-host evidence. Integration into `main` preserves development work; the [qualification register](registry/product-qualification.json) records final-product eligibility separately.

## Executable cases on main

- [Helsinki service inventory](cases/helsinki-service-inventory/README.md): registered public-library and health-station locations against 2025 district population; original GDAL MCP plus municipal preparation/inventory operations, with Codex/Hermes evidence.
- [Helsinki and Amsterdam walking access](cases/two-city-walking/README.md): mapped school-to-library routes, snap/disconnection accounting and a declared link-closure scenario. Includes an OSMnx MCP source audit, a separately implemented adapter, harvested ODbL snapshots and Docker/native/MCP checks in two cities.
- [Current walking diagnostics](cases/two-city-walking/issue-39.md): exact per-school threshold transitions and per-path closed-edge membership, with a versioned blind task and four reviewed Codex/Hermes observations. Numerical artifacts, answer JSON and broader prose have separate verdicts.
- [Helsinki and Amsterdam historical vegetation](cases/two-city-vegetation/README.md): WorldCover 2021 categorical zone shares with 2025 aggregate population, source harvesting/snapshots, audited original GDAL MCP, complete paged results and four reviewed host observations.

The ordered integration is [RFC #1](https://github.com/polisplexity/urban-mcp/pull/1) → [inventory #37](https://github.com/polisplexity/urban-mcp/pull/37) → [walking #38](https://github.com/polisplexity/urban-mcp/pull/38) → [diagnostics #40](https://github.com/polisplexity/urban-mcp/pull/40) → [vegetation #42](https://github.com/polisplexity/urban-mcp/pull/42). Use `main` for current reproduction. Historical branches and versioned failed observations remain available for audit.

## Reproduce and contribute

The [two-city historical vegetation case merged in PR #42](https://github.com/polisplexity/urban-mcp/pull/42) is available on `main`. Its [guide](cases/two-city-vegetation/README.md) reuses the audited original GDAL MCP and adds eight municipal operations. Native/stdio suites pass 110/131 checks across 21 tools, 12 synthetic regressions and 69 original-server tests. All four recorded Codex/Hermes observations reproduce artifacts, full CSV pages and answer JSON. Codex Helsinki's brief passes; Codex Amsterdam exceeds the length limit; both broader Hermes briefs fail factual review. [Findings](cases/two-city-vegetation/findings.md), [verdicts](cases/two-city-vegetation/evidence/narrative-review.json), [integration receipt](docs/integration/2026-11-10-vegetation-main.json).

Vegetation is modeled **2021** data with aggregate **2025** population, not current canopy, park access or heat exposure. The [data prerelease](https://github.com/polisplexity/urban-mcp/releases/tag/data-vegetation-20261110) preserves rights/hashes. Independent-person third-city qualification is pending; issue #41 remains the separate walking task.

```sh
git clone --branch main https://github.com/polisplexity/urban-mcp.git
cd urban-mcp
git rev-parse HEAD
python -m pip install -r requirements-dev.txt
python tools/validate.py
python -m unittest discover -s tests
```

Then follow the selected case's Docker guide above. Metadata CI is a separate stage; each executable case has real native/MCP checks. Deterministic reproduction needs no LLM account. Host tests use an existing privately authenticated agent and an independent data mount. [Client configuration](tools/client_config.py), [blind host runner](tools/run_agent_check.py), [agent runbook](docs/agents/day-zero.md).

The current walking suite passes 84 checks in Helsinki and 83 in Amsterdam across all 15 tools, resource families and prompt, plus seven Docker integrity/cache regressions. All four final Codex/Hermes observations reproduce native artifacts and pass checked threshold/membership JSON fields. Codex briefs pass review; broader Hermes commentary remains qualified. See the master for exact versions, CI and useful failures. These results cover bounded study disks and mapped objects, not entire cities, pupils, wheelchair access, verified entrances, public admission or observed travel times.

A contribution joins original software/API, a justified interface delta, exact sources and rights, preparation, a municipal question, reproducible startup, native/MCP comparison and reviewed host evidence. A portal link or successful container startup is insufficient. [Contribution guide](CONTRIBUTING.md), [roadmap](docs/roadmap.md), [public tasks](docs/tasks.md), [research registry](registry/tools.json), [data matrix](docs/data/tool-data-matrix.md).

New documentation, tasks, code comments and reports are in English. Historical research and observed evidence retain their original language and bytes. Original code is MIT licensed; upstream tools and datasets retain their terms. OSM-derived snapshots and databases are ODbL-1.0, © OpenStreetMap contributors. Keep credentials, private product code, operator data and bulk caches outside Git. Public recipes, provenance, reviewed evidence and useful failures let anyone repeat and improve the work.
