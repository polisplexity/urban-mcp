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

Use the same prerequisites as the [main case guide](README.md). Clone `main`, or update an existing clean checkout with `git switch main` and `git pull --ff-only`. Record the source commit and start with a new data directory:

```sh
git clone --branch main https://github.com/polisplexity/urban-mcp.git
cd urban-mcp
git rev-parse HEAD
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

Install `requirements-dev.txt` before the host-side repository tests and maintenance helpers. Keep raw workspaces/logs outside Git; a new reproduction must not overwrite either published evidence version. Run the commands sequentially unless sufficient additional memory is available for independent containers.

The native suite independently joins every CSV row with the exact keyed route export, compares the full diagnostics through MCP, checks the known threshold-identity and overlapping-path regressions, and verifies that baseline/closure CSV bytes remain identical to the original experiment. Synthetic regressions separately test exact-boundary crossings, rerouting, lost reachability, unchanged unreachable objects, reverse directions/parallel keys, avoiding alternatives and invalid evidence.

The suite also issues three simultaneous cold MCP graph/catalog inspections under the existing 3 GB memory cap. Reentrant cache synchronization prevents duplicate graph deserialization; a separate threaded regression requires exactly one load. The earlier saturated attempt and its correction are recorded in `evidence/issue-39/runtime-failure.json`.

## Repeat the blind host tests

The new [v2 task](agent-task-issue-39.md) supplies no expected numerical answers. It requests a compact JSON claim object in addition to a factual brief, so exact origin sets and per-path booleans can be checked mechanically. Use new host workspaces/profiles and the existing host's authentication; preserve private provider settings outside Git.

```sh
python tools/run_agent_check.py codex --capability walking --city helsinki --label walking-helsinki-my-review --task cases/two-city-walking/agent-task-issue-39.md
python tools/run_agent_check.py codex --capability walking --city amsterdam --label walking-amsterdam-my-review --task cases/two-city-walking/agent-task-issue-39.md
# On Windows add --wsl-distro Ubuntu-22.04.
# For Hermes use the same --task with fresh configured profiles and data mounts:
python tools/run_agent_check.py hermes --capability walking --city helsinki --label walking-helsinki-my-review --task cases/two-city-walking/agent-task-issue-39.md --hermes-home /absolute/path/to/fresh-helsinki-profile
python tools/run_agent_check.py hermes --capability walking --city amsterdam --label walking-amsterdam-my-review --task cases/two-city-walking/agent-task-issue-39.md --hermes-home /absolute/path/to/fresh-amsterdam-profile
```

For each fresh Hermes profile, generate configuration with `python tools/client_config.py --capability walking --format hermes --data-dir .urban-mcp/hermes-walking-<city>-my-review`, replacing `<city>` with the actual city. Add only that MCP block to the independently authenticated profile. The runner does not change its configured mount. The Linux generator uses GNU `env -C <repo>` before Docker to establish a stable working directory.

Use a new suffix if `my-review` already exists. Export only public-case traces and selected full tool results using the export tools' `--results-dir`, and the Hermes exporter's matching `--task`. Numerical artifacts, machine-readable claims and prose receive separate verdicts. A process exit or an answer corrected by the implementer is not a successful independent host result.

## Acceptance record

Both final city suites pass: **84 checks in Helsinki and 83 in Amsterdam**, exercising all 15 tools/resources/prompt, plus seven Docker integrity/concurrency regressions. The repository suite has 32 tests, including nine diagnostic regressions and versioned evidence-integrity checks. [The two-city CI run passed](https://github.com/polisplexity/urban-mcp/actions/runs/42834941975).

All four final Codex/Hermes city runs operate the 15 tools, reproduce native artifacts and full diagnostic responses, and pass the independently checked JSON claim fields. Helsinki reports the exact five crossings and six affected objects still within; Amsterdam reports zero crossings and five affected objects still within. Both selected two-path regression results explicitly use the closed pair in each city, with an empty avoiding-rank list.

Read the [new evidence and prose qualifications](evidence/issue-39/README.md). Codex's observed briefs pass review. Hermes's targeted classification/membership claims now pass, while additional commentary remains qualified and unsuitable for autonomous municipal recommendations. The original failed v1 narratives remain unchanged. Consult the [master record](../../MASTER_TEST_RECORD.md) for the combined test history.

After restoring and running both cities, collect into a new dossier. The following Bash example uses the labels above and keeps private host logs in their ignored locations:

```sh
export REVIEW_DOSSIER="cases/two-city-walking/evidence/my-review"
python tools/collect_walking_evidence.py --workspace "$URBAN_MCP_WALKING_WORKDIR" --output "$REVIEW_DOSSIER"
for city in helsinki amsterdam; do
  codex_evidence=".urban-mcp/agent-evidence/codex-walking-$city-my-review"
  python tools/export_codex_trace.py --events "$codex_evidence/events.log" --output "$codex_evidence/trace.json" --results-dir "$codex_evidence"
done
# Set these to the two actual fresh profiles used above.
export HELSINKI_HERMES_PROFILE="/absolute/path/to/fresh-helsinki-profile"
export AMSTERDAM_HERMES_PROFILE="/absolute/path/to/fresh-amsterdam-profile"
for city in helsinki amsterdam; do
  if [ "$city" = helsinki ]; then profile="$HELSINKI_HERMES_PROFILE"; else profile="$AMSTERDAM_HERMES_PROFILE"; fi
  hermes_evidence=".urban-mcp/agent-evidence/hermes-walking-$city-my-review"
  python tools/export_hermes_trace.py --state-db "$profile/state.db" --task cases/two-city-walking/agent-task-issue-39.md --city "$city" --output "$hermes_evidence/trace.json" --answer-output "$hermes_evidence/answer.md" --results-dir "$hermes_evidence"
done
python tools/review_walking_agents.py --codex-suffix my-review --hermes-suffix my-review --evidence-dir "$REVIEW_DOSSIER" --task cases/two-city-walking/agent-task-issue-39.md --diagnostics
```

The final published observations used the suffix `issue39-final`; these example commands use `my-review` to preserve them. A new dossier initially has no narrative review, so the reviewer reports prose as pending even when artifacts/JSON pass. Review the actual new answers, create an answer-hash-bound `narrative-review.json` following the published structure, and rerun the reviewer before admitting prose. Never copy an old review onto a new answer. On Windows/WSL, run exporters where both repository workspaces and the selected Hermes database are accessible; pass the exact corresponding paths.

The study remains limited to the same central disks and assumptions. Public admission, entrances, barriers, directional foot rules, winter conditions, wheelchair suitability, observed journey times and citywide service adequacy remain unverified. OSM-derived data remains ODbL-1.0, © OpenStreetMap contributors.
