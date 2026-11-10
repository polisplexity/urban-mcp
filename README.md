# Urban MCP

Open infrastructure that lets any MCP-capable agent operate urban open-source tools with admitted data, installation/startup recipes and reproducible municipal evidence.

**Start with the [master test record: what we tested and why](https://github.com/polisplexity/urban-mcp/blob/fix/walking-threshold-route-evidence/MASTER_TEST_RECORD.md).** It distinguishes source harvesting, native computation, MCP compatibility, agent artifacts and factual narrative review.

## Review the executable work

- **[Explicit threshold crossings and closed-link evidence · PR #40](https://github.com/polisplexity/urban-mcp/pull/40):** exact per-school transitions and per-path closed-edge membership, checked in both cities with Codex and fresh Hermes profiles. [Current interface/reproduction guide](https://github.com/polisplexity/urban-mcp/blob/fix/walking-threshold-route-evidence/cases/two-city-walking/issue-39.md), [versioned evidence and prose qualifications](https://github.com/polisplexity/urban-mcp/blob/fix/walking-threshold-route-evidence/cases/two-city-walking/evidence/issue-39/README.md).
- **[Helsinki and Amsterdam walking access · PR #38](https://github.com/polisplexity/urban-mcp/pull/38):** central school-to-library experiments, original OSMnx MCP source audit, separately implemented 15-tool adapter, harvested ODbL snapshots and Docker/native/MCP checks in two cities. [Reproduction guide](https://github.com/polisplexity/urban-mcp/blob/feat/two-city-walking-accessibility/cases/two-city-walking/README.md), [findings and maps](https://github.com/polisplexity/urban-mcp/blob/feat/two-city-walking-accessibility/cases/two-city-walking/findings.md), [data release](https://github.com/polisplexity/urban-mcp/releases/tag/data-walking-20261110).
- **[Helsinki service inventory · PR #37](https://github.com/polisplexity/urban-mcp/pull/37):** library/health-station registry locations against district population, original GDAL MCP plus municipal operations, with independent Codex/Hermes evidence. [Case guide](https://github.com/polisplexity/urban-mcp/blob/feat/two-city-walking-accessibility/cases/helsinki-service-inventory/README.md).
- **[Public proposal · RFC PR #1](https://github.com/polisplexity/urban-mcp/pull/1):** capability/data contracts and wider research catalog. A catalog listing is not proof of operational readiness.

The implementation remains in review branches: PR #40 is stacked on PR #38, which is stacked on the inventory branch, which is based on the RFC. This main branch is the public entry point; these links do not imply that the implementation is merged.

## What the walking tests establish

The current issue-39 revision passes 84 native/stdio-MCP checks in Helsinki and 83 in Amsterdam across all 15 tools, plus seven Docker integrity/cache regressions. All four final Codex/Hermes runs reproduce native artifacts and pass the independently checked threshold/membership JSON fields. Original baseline/closure CSV bytes are unchanged. Codex's observed briefs pass review; broader Hermes commentary remains qualified. The first experiment's failed narratives are preserved in the versioned record.

These are bounded study disks and mapped facility objects. Public library admission, verified entrances, complete municipal coverage, population, wheelchair access and measured travel times remain unproven. The master record preserves what worked, what failed and why.

## Reproduce and contribute

```sh
git clone --branch fix/walking-threshold-route-evidence https://github.com/polisplexity/urban-mcp.git
cd urban-mcp
# Follow cases/two-city-walking/issue-39.md for current Docker, data and MCP commands.
```

Deterministic checks need no LLM account. Agent testing uses your existing host and private authentication, with an agent-neutral stdio MCP. No proprietary agent or global language/framework is required.

[Contribution guide](https://github.com/polisplexity/urban-mcp/blob/feat/two-city-walking-accessibility/CONTRIBUTING.md), [roadmap](https://github.com/polisplexity/urban-mcp/blob/feat/two-city-walking-accessibility/docs/roadmap.md), [open tasks](https://github.com/polisplexity/urban-mcp/issues), [resolved evidence-interface issue #39](https://github.com/polisplexity/urban-mcp/issues/39).

New project documentation, tasks, code comments and reports are in English. Historical research and observed transcripts may retain their original language. Repository code is MIT; each upstream tool and dataset retains its own license. Walking data and derived databases remain ODbL-1.0, © OpenStreetMap contributors. Public recipes, provenance, reviewed evidence and useful failures make the work repeatable and open to contribution.
