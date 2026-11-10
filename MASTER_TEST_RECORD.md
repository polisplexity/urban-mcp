# Master test record

This is the project entry point for evidence: what we tested, why it matters to a municipality, and how far the evidence supports a claim. A catalog entry, a successful container startup and a tool listing do not establish a working capability.

| Capability | Municipal scope and purpose | Native | MCP | Codex | Hermes | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| GDAL/GeoPandas service inventory | Helsinki: count registered library and health-station locations by district against 2025 district population | Passed, declared parameters | 19 tools, 72 checks | Passed, separate workspace | Passed, separate workspace | [Case](cases/helsinki-service-inventory/README.md), [agent checks](cases/helsinki-service-inventory/evidence/agents.json), [PR #37](https://github.com/polisplexity/urban-mcp/pull/37) |
| OSMnx/NetworkX walking access | Helsinki central study disk: mapped school-to-library access and hypothetical link closure | Pending | Pending | Pending | Pending | [Recipe](cases/two-city-walking/recipe.json) |
| OSMnx/NetworkX walking access | Amsterdam central study disk: transfer of the same method to a canal/bridge network | Pending | Pending | Pending | Pending | [Recipe](cases/two-city-walking/recipe.json) |

## Why these tests

The first case establishes harvesting, provenance, coordinate handling and descriptive inventory. The walking case must establish network distances rather than Euclidean buffers, an explicit denominator, snap quality, disconnected paths, reproducible exports and a controlled disruption scenario. Two independent agent hosts must discover and operate the same MCP without access to expected answers. Two cities test transfer; they do not establish universal city coverage.

## What remains unproven

The research catalog is not a coverage claim. Walking access is not wheelchair accessibility, observed travel time, population coverage, school enrollment, service capacity or an authoritative municipal finding. Every result must retain its study boundary, acquisition date, data license, assumptions and known omissions.

## Updating this record

Each new row needs a municipal question, exact input assets and rights, pinned engine/interface versions, native comparison, real MCP transport checks, tool-by-tool coverage, host traces with reviewed artifacts, reproduction commands and documented failures. Mark a stage passed only after its evidence exists. Preserve unsuccessful observations when they explain a correction. New project documentation and test tasks are in English; historical agent transcripts remain verbatim evidence.
