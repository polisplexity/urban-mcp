# Urban MCP

Open infrastructure that lets any MCP-capable agent operate urban open-source tools with admitted data, installation/startup recipes and reproducible municipal evidence.

**Start with the [master test record: what we tested and why](https://github.com/polisplexity/urban-mcp/blob/feat/two-city-walking-accessibility/MASTER_TEST_RECORD.md).** It distinguishes source harvesting, native computation, MCP compatibility, agent artifacts and factual narrative review.

## Review the executable work

- **[Helsinki and Amsterdam walking access · PR #38](https://github.com/polisplexity/urban-mcp/pull/38):** central school-to-library experiments, original OSMnx MCP source audit, separately implemented 15-tool adapter, harvested ODbL snapshots and Docker/native/MCP checks in two cities. [Reproduction guide](https://github.com/polisplexity/urban-mcp/blob/feat/two-city-walking-accessibility/cases/two-city-walking/README.md), [findings and maps](https://github.com/polisplexity/urban-mcp/blob/feat/two-city-walking-accessibility/cases/two-city-walking/findings.md), [data release](https://github.com/polisplexity/urban-mcp/releases/tag/data-walking-20261110).
- **[Helsinki service inventory · PR #37](https://github.com/polisplexity/urban-mcp/pull/37):** library/health-station registry locations against district population, original GDAL MCP plus municipal operations, with independent Codex/Hermes evidence. [Case guide](https://github.com/polisplexity/urban-mcp/blob/feat/two-city-walking-accessibility/cases/helsinki-service-inventory/README.md).
- **[Public proposal · RFC PR #1](https://github.com/polisplexity/urban-mcp/pull/1):** capability/data contracts and wider research catalog. A catalog listing is not proof of operational readiness.

The implementation remains in review branches: PR #38 is stacked on the inventory branch, which is based on the RFC. This main branch is the public entry point; these links do not imply that the implementation is merged.

## What the walking tests establish

Both city cases pass 62 native/stdio-MCP checks across 15 tools; six separate synthetic regressions test snapshot integrity. Four independent final runs in Codex CLI and fresh Hermes profiles reproduce native numerical artifacts. **Narrative review is separate:** Codex's observed briefs pass the declared review; Hermes prose fails specific per-object threshold/overlapping-route claims. [Read the exact failures and corrections](https://github.com/polisplexity/urban-mcp/blob/feat/two-city-walking-accessibility/cases/two-city-walking/evidence/narrative-review.md).

These are bounded study disks and mapped facility objects. Public library admission, verified entrances, complete municipal coverage, population, wheelchair access and measured travel times remain unproven. The master record preserves what worked, what failed and why.

## Reproduce and contribute

```sh
git clone --branch feat/two-city-walking-accessibility https://github.com/polisplexity/urban-mcp.git
cd urban-mcp
# Follow cases/two-city-walking/README.md for Docker, data and MCP commands.
```

Deterministic checks need no LLM account. Agent testing uses your existing host and private authentication, with an agent-neutral stdio MCP. No proprietary agent or global language/framework is required.

[Contribution guide](https://github.com/polisplexity/urban-mcp/blob/feat/two-city-walking-accessibility/CONTRIBUTING.md), [roadmap](https://github.com/polisplexity/urban-mcp/blob/feat/two-city-walking-accessibility/docs/roadmap.md), [open tasks](https://github.com/polisplexity/urban-mcp/issues), [next evidence-interface contribution #39](https://github.com/polisplexity/urban-mcp/issues/39).

New project documentation, tasks, code comments and reports are in English. Historical research and observed transcripts may retain their original language. Repository code is MIT; each upstream tool and dataset retains its own license. Walking data and derived databases remain ODbL-1.0, © OpenStreetMap contributors. Public recipes, provenance, reviewed evidence and useful failures make the work repeatable and open to contribution.
