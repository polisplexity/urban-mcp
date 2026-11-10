# Upstream OSMnx MCP audit and implementation decision

Inspected repository: [msradam/osmnx-mcp](https://github.com/msradam/osmnx-mcp), revision `be547a94038b7b3fa353615381a330b94e2b0b7c`. This audit reads and runs source, not just the README. The machine-readable observations are in `evidence/upstream-audit.json`; the public audit driver is `tools/audit_osmnx_upstream.py`.

## Reuse decision

The checkout exposes **33 tools**, multi-graph lifecycle operations and seven graph resources. Its Python server uses **FastMCP**, calling **OSMnx** and **NetworkX**. It already supplies graph acquisition/persistence, nearest nodes/edges, routing/alternatives, statistics, feature downloads, enrichment, truncation and plotting. Rebuilding those numerical engines would add no value.

At this revision there is no license file or license declaration, and GitHub reports `license: null`. That does not establish an open-source redistribution permission. We keep the independently obtained checkout outside Git, mount it read-only for evaluation, and do not copy it into our source, public image or data releases. No upstream endorsement is implied. If the maintainer supplies an appropriate license, re-evaluate reuse through the same acceptance tests.

Our **separately implemented MIT adapter** uses public OSMnx/NetworkX APIs and FastMCP. This is a scoped municipal interface, not a fork or a replacement for all 33 tools. The numerical work remains upstream: OSMnx downloads, graph I/O, nearest-node search, bearings and alternatives; NetworkX solves paths and components; GeoPandas/PyProj/Shapely handle geometry/CRS; Matplotlib renders evidence. FastMCP provides MCP schemas, stdio, resources and prompts. Python avoids serializing large native Python graphs into a second language/runtime. This does not select a global language or framework for every Urban MCP capability.

## What the code and execution show

| Finding | Evidence and implication | Our response |
| --- | --- | --- |
| Walking loader still defaults to `add_speeds=True` and `add_travel_times=True` | `tools/graph_loading.py` invokes OSMnx's motor-vehicle maxspeed imputation for any network type. Static source finding; not a measured walking speed. | Route by length. Only report minutes from an explicit user-visible constant-speed scenario. |
| Route total always reads parallel key `0` | `tools/routing.py`; synthetic regression: native minimum is 10 m on key 7, MCP reports 90 m from key 0. Synthetic result is separate from city evidence. | Preserve and sum actual minimum-length parallel keys, and compare every city's totals with a separate forward solver. |
| Bounding boxes are passed in `(north,south,east,west)` order | `features.py`, `graph_loading.py`, `spatial.py`; current OSMnx expects `(west,south,east,north)`. Truncation can return plausible nonempty data for a different area. | Explicit city-bound geometry/CRS and public polygon/bbox API ordering; test output identities and bounds. |
| Intersection tolerance can operate on degrees | `consolidate_intersections` does not project or enforce projected metre coordinates. In the audit it returned 305 nodes and zero edges from the geographic graph. | Not exposed in this admitted case. Any future consolidation operation needs its own metric CRS/parameter and topology tests. |
| Plotting assumes a writable `~/Downloads` | Four plotting paths fail in the non-root read-only sandbox because `/Downloads` does not exist. Orientation plotting separately fails on unsupported `show` keyword. | Write allowlisted artifacts to the explicit mounted case workspace, preserving attribution and receipts. |
| Grade and travel-time enrichment have required input preconditions | Without elevation/speed attributes, the corresponding upstream calls reject. These are expected missing-data rejections, not evidence that those solvers are defective. | No slope/wheelchair or observed-time claims without admitted inputs. |
| Original feature calls hit live Overpass; graph state is process-global | Agent retries can change data or active graph and produce non-reproducible results. | Hash-locked acquisition, immutable inputs, explicit city on every operation, bounded outputs and unique run IDs. |

The runtime audit exercises 28 distinct non-acquisition tools plus the parallel-edge regression. Five live acquisition tools are inventoried but not executed through this original MCP; native acquisition is tested separately by the municipal harvester. The original resources and every possible parameter/driver are not admitted by this audit. Read each observation's status; a tool returning a result is not a correctness pass.

## What we add

The missing product capability is an auditable municipal experiment: provenance/rights/receipts, snapshot recovery, city-bound input validation, OSM object/entrance caveats, snap exclusions, nearest-library selection including endpoint costs, disconnected-origin accounting, a consistent school-object denominator, link-closure comparison, portable artifacts, a bounded MCP surface, and blind tests in two different hosts and cities. The original MCP does not supply this complete municipal/data/verification contract.

## Re-run the audit

Acquire the referenced checkout yourself; inspect its terms before redistribution. With the walking image built, mount the checkout at `/audited-upstream`, its `src` on `PYTHONPATH`, the audit driver at `/audit.py`, the Urban MCP code on `PYTHONPATH`, and the admitted Amsterdam inputs at `/data/inputs/amsterdam`. Run `python /audit.py` with networking disabled. The driver evaluates supplied source without installing its agent SDK or contacting an LLM. Preserve the runtime lock and exact checkout revision with the observations.

Primary API reference: [OSMnx user reference](https://osmnx.readthedocs.io/en/stable/user-reference.html). Data terms: [OpenStreetMap copyright](https://www.openstreetmap.org/copyright) and [ODbL-1.0](https://opendatacommons.org/licenses/odbl/1-0/). These references support API/rights context; code and executable evidence support the findings above.
