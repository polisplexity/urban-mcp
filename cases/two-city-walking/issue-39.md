# Explicit threshold crossings and closed-link route evidence

Issue: [#39](https://github.com/polisplexity/urban-mcp/issues/39). This version addresses two observed interpretation failures while preserving the original OSM snapshots, shortest-path solver, distance/snap rules and mapped-school-object denominator. The original evidence and failed Hermes answers remain in `evidence/`; this run writes separately to `evidence/issue-39/`.

## Interface changes

`walking_compare(city, baseline_id, scenario_id)` now returns a versioned diagnostic object:

- `crossed_threshold_origin_ids` and `threshold_crossings`: explicit distance-threshold crossings for routed objects, with exact origin IDs/names, before/after totals, destination IDs, both within-threshold flags and a transition label.
- `affected_still_within_origin_ids`: detoured or rerouted objects that remain within the threshold. A large detour is not itself a crossing.
- `left_threshold_coverage_origin_ids` and `newly_unreachable_origin_ids`: distinguish a finite-distance crossing from losing route reachability.
- `schools`: every origin, including unchanged/unreachable/snap-rejected objects; `affected_origins` remains available with the expanded fields.
- `baseline_route_uses_closed_link`, `baseline_closed_edges_used`, `scenario_route_uses_closed_link`, and root origin-ID lists: membership checked against the actual keyed route exports. A scenario route containing a removed link is rejected.

`walking_route(city, origin_id, destination_id, k, closed_links=[{"u":...,"v":...}])` still computes original-graph k-shortest paths. Each path has a rank, `uses_closed_link`, exact `closed_edges_used` and `avoids_all_declared_closed_links`. `path_overlap` reports shared directed keyed edges and physical node-pair links. `path_ranks_avoiding_declared_closed_links` is explicit, including an empty list when all returned paths are blocked.

Declaring links here annotates the original paths; it does not remove links or reroute them. Use `walking_accessibility(..., closures=[...])` for the actual closure scenario. Closures match both directions and every parallel key. Even an avoiding path remains a general walking proxy, not a verified itinerary.

## Reproduce the computational checks

Use the same prerequisites as the [main case guide](README.md). Start with a new directory:

```sh
git switch fix/walking-threshold-route-evidence
export URBAN_MCP_UID="$(id -u)"
export URBAN_MCP_GID="$(id -g)"
export URBAN_MCP_WALKING_WORKDIR="$PWD/.urban-mcp/walking-issue39-reproduction"
mkdir -p "$URBAN_MCP_WALKING_WORKDIR"
docker compose --profile walking build walking
docker compose --profile walking run --rm walking-harvest harvest --mode snapshot --city helsinki
docker compose --profile walking run --rm walking-harvest harvest --mode snapshot --city amsterdam
docker compose --profile walking run --rm walking test --city helsinki
docker compose --profile walking run --rm walking test --city amsterdam
docker compose --profile walking run --rm --entrypoint python walking -m unittest urban_mcp_walking.test_contracts urban_mcp_walking.test_runtime -v
python -m unittest discover -s tests
```

The native suite independently joins every CSV row with the exact keyed route export, compares the full diagnostics through MCP, checks the known threshold-identity and overlapping-path regressions, and verifies that baseline/closure CSV bytes remain identical to the original experiment. Synthetic regressions separately test exact-boundary crossings, rerouting, lost reachability, unchanged unreachable objects, reverse directions/parallel keys, avoiding alternatives and invalid evidence.

The suite also issues three simultaneous cold MCP graph/catalog inspections under the existing 3 GB memory cap. Reentrant cache synchronization prevents duplicate graph deserialization; a separate threaded regression requires exactly one load. The earlier saturated attempt and its correction are recorded in `evidence/issue-39/runtime-failure.json`.

## Repeat the blind host tests

The new [v2 task](agent-task-issue-39.md) supplies no expected numerical answers. It requests a compact JSON claim object in addition to a factual brief, so exact origin sets and per-path booleans can be checked mechanically. Use new host workspaces/profiles and the existing host's authentication; preserve private provider settings outside Git.

```sh
python tools/run_agent_check.py codex --capability walking --city helsinki --label walking-helsinki-issue39 --task cases/two-city-walking/agent-task-issue-39.md
python tools/run_agent_check.py codex --capability walking --city amsterdam --label walking-amsterdam-issue39 --task cases/two-city-walking/agent-task-issue-39.md
# On Windows add --wsl-distro Ubuntu-22.04.
# For Hermes use the same --task with fresh configured profiles and data mounts:
python tools/run_agent_check.py hermes --capability walking --city helsinki --label walking-helsinki-issue39 --task cases/two-city-walking/agent-task-issue-39.md --hermes-home /absolute/path/to/fresh-helsinki-profile
python tools/run_agent_check.py hermes --capability walking --city amsterdam --label walking-amsterdam-issue39 --task cases/two-city-walking/agent-task-issue-39.md --hermes-home /absolute/path/to/fresh-amsterdam-profile
```

The Linux Hermes config generator uses GNU `env -C <repo>` before Docker to establish a stable working directory. Export only public-case traces and selected full tool results using the export tools' `--results-dir`, and the Hermes exporter's matching `--task`. Numerical artifacts, machine-readable claims and prose receive separate verdicts. A process exit or an answer corrected by the implementer is not a successful independent host result.

## Acceptance record

Both final city suites pass: **84 checks in Helsinki and 83 in Amsterdam**, exercising all 15 tools/resources/prompt, plus seven Docker integrity/concurrency regressions. The repository suite has 32 tests, including nine diagnostic regressions and versioned evidence-integrity checks. [The two-city CI run passed](https://github.com/polisplexity/urban-mcp/actions/runs/42834941975).

All four final Codex/Hermes city runs operate the 15 tools, reproduce native artifacts and full diagnostic responses, and pass the independently checked JSON claim fields. Helsinki reports the exact five crossings and six affected objects still within; Amsterdam reports zero crossings and five affected objects still within. Both selected two-path regression results explicitly use the closed pair in each city, with an empty avoiding-rank list.

Read the [new evidence and prose qualifications](evidence/issue-39/README.md). Codex's observed briefs pass review. Hermes's targeted classification/membership claims now pass, while additional commentary remains qualified and unsuitable for autonomous municipal recommendations. The original failed v1 narratives remain unchanged. Consult the [master record](../../MASTER_TEST_RECORD.md) for the combined test history.

After restoring and running both cities, collect/review without overwriting v1:

```sh
python tools/collect_walking_evidence.py --workspace "$URBAN_MCP_WALKING_WORKDIR" --output cases/two-city-walking/evidence/issue-39
# Export the public traces, answers and full selected tool responses to each
# private host evidence directory; use the exporters' --results-dir option.
python tools/review_walking_agents.py --codex-suffix issue39-final --hermes-suffix issue39-final --evidence-dir cases/two-city-walking/evidence/issue-39 --task cases/two-city-walking/agent-task-issue-39.md --diagnostics
```

The suffixes above refer to the final published run labels; use new labels and point each fresh Hermes profile at its corresponding new workspace when contributing a reproduction. Narrative reviews are bound to observed answer hashes and must be renewed for a new answer; do not copy an old review onto it.

The study remains limited to the same central disks and assumptions. Public admission, entrances, barriers, directional foot rules, winter conditions, wheelchair suitability, observed journey times and citywide service adequacy remain unverified. OSM-derived data remains ODbL-1.0, © OpenStreetMap contributors.
