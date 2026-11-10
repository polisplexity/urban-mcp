# Two-city historical SUMO works experiment

Municipal question: in two published historical city models, what changes for
vehicles scheduled through a selected corridor when eligible passenger lanes
are limited to **30 km/h** for works? We preserve the original C++ SUMO
solver, published demand, signals and behavior settings. We add acquisition,
explicit model binding, a same-seed comparison and reviewable full results.

This development is proposed in [PR #43](https://github.com/polisplexity/urban-mcp/pull/43).
It is separate from the cases already merged on `main`. See the
[master](../../MASTER_TEST_RECORD.md), [findings](findings.md),
[operation coverage](functionality.md), [code audit](upstream-audit.md),
[recipe](recipe.json), [licenses](LICENSE.md) and [snapshot lock](snapshot.lock.json).
All final-product qualification remains pending an independent person in a
third city; another agent/model operated by the original team does not count.

## Why these cities and data

| City / publisher | Actual model inputs | Declared experiment |
| --- | --- | --- |
| Bologna Acosta / DLR-TS, commit `79d2e1837a9683617393c69aaf754c6bc812e3f8` | Original network, historical routes, vehicle types, buses/stops, detectors and TLS; EPL-2.0 | Historical 08:00–09:00 demand informed by November 2008 observations. Begin 0, evaluation departures 900–2700 s, selected departures <3600, end 4500, step 1 s |
| Ingolstadt / TUM-VT, commit `e0a95deebe200ff81b6705044d66310d6266d42b` | Original full study network, motorized demand and mandatory WAUT programs for 2020-09-16; simulation Apache-2.0 | Begin 06:45, evaluation departures 07:00–07:10, selected departures <07:10, end 07:30, step 0.25 s |

These are harvested **real-city published models**, with modeled historical
demand. They are not fresh counts, raw observations of people or newly
validated forecasts. OSM streets alone cannot supply demand or signal timing.
The original studies' calibration is not inherited by this bounded experiment.
Ingolstadt produces native conflict, collision and teleport diagnostics;
successful replay preserves those problems rather than granting policy readiness.

Network XY coordinates use the original model's metre system. Do not assign
an EPSG code to Bologna's local Cartesian coordinates or infer municipal
boundary coverage. Network extents and exact source IDs are in the quality
resource/receipt. Optional GUI settings/polygons are explicitly omitted;
required traffic inputs remain present in original additional-file order.

## Docker reproduction without any model account

Use Linux Docker Engine/Compose or Docker Desktop with a Linux environment.
The pinned native wheel/profile targets **linux/amd64**. Deterministic native
and MCP checks require no LLM account, agent framework, cloud deployment or
API key. The selected runtime is SUMO/TraCI/sumolib 1.28.0 and the reused
original MCP's official Python SDK FastMCP 1.25.0, with Pydantic 2.12.5.
The [Dockerfile](../../adapters/sumo/Dockerfile) pins the Python base digest,
native wheel and original MCP archive hashes; the [lock](../../adapters/sumo/runtime.lock.txt)
pins Python dependencies. Apt packages come from the base distribution's
repositories; this is not a claim of a bit-for-bit reproducible whole OS image.

```sh
git clone --branch feat/two-city-sumo https://github.com/polisplexity/urban-mcp.git
cd urban-mcp
git rev-parse HEAD
export URBAN_MCP_UID="$(id -u)" URBAN_MCP_GID="$(id -g)"
# Choose a new directory. Preserve previous runs and failure observations.
export URBAN_MCP_SUMO_WORKDIR="$PWD/.urban-mcp/my-sumo-reproduction"
mkdir -p "$URBAN_MCP_SUMO_WORKDIR"
docker compose --profile sumo build sumo
docker compose --profile sumo run --rm sumo-harvest harvest --city bologna --mode snapshot
docker compose --profile sumo run --rm sumo-harvest harvest --city ingolstadt --mode snapshot
docker compose --profile sumo run --rm --entrypoint python sumo -m unittest urban_mcp_sumo.test_contracts -v
docker compose --profile sumo run --rm --entrypoint python sumo-mcp /opt/urban-mcp/tools/audit_sumo_upstream.py --output /data/evidence/upstream-audit.json
docker compose --profile sumo run --rm sumo test --city bologna
docker compose --profile sumo run --rm sumo test --city ingolstadt
```

Each full test executes baseline/works **twice**: direct native subprocess
and actual SDK/stdio MCP subprocess. It independently reads original vehicle
subtrees, native tripinfo, statistics, warnings and complete CSV rows; then
compares native/MCP summaries, CSVs and PNG bytes. It exercises all 13 tools,
all resource/prompt families, deliberate rejection boundaries and owned
process cleanup. Logs and immutable per-run artifacts remain under the data
mount; `evidence/<city>/latest.json` points to the latest suite. Full Ingolstadt
checks can take approximately 15 minutes. Each native batch has a 300 s
process budget; each MCP call a 420 s test budget. Slow hosts can fail honestly;
do not replace a timeout with success or remove problematic vehicles.

Native services have no network; the acquisition and MCP services have a
bridge for the exact public source fetches. No host port is published. The
profile uses a read-only container root, non-root UID, 2 CPU, 3 GiB RAM and
owned-process cleanup. Outputs go to `/data`, temporary files to `/tmp`.

For an isolated native run after restoring/preparing:

```sh
docker compose --profile sumo run --rm sumo prepare --city bologna
docker compose --profile sumo run --rm sumo run --city bologna --run-id my-baseline --scenario baseline
docker compose --profile sumo run --rm sumo run --city bologna --run-id my-works --scenario works30
```

The same operations are available through MCP, including comparison, map and
full artifact paging. Run IDs are immutable; a repeat must use a new ID.

## Reharvest original publishers

The data prerelease preserves exact original source bytes, rights and request
receipts. Restoring it is a reproducible observation of those historical inputs,
not a live municipal data feed. To reacquire the exact pinned original URLs,
use a **new** data mount:

```sh
export URBAN_MCP_SUMO_WORKDIR="$PWD/.urban-mcp/my-sumo-live-harvest"
mkdir -p "$URBAN_MCP_SUMO_WORKDIR"
docker compose --profile sumo run --rm sumo-harvest harvest --city bologna --mode live
docker compose --profile sumo run --rm sumo-harvest harvest --city ingolstadt --mode live
docker compose --profile sumo run --rm sumo prepare --city bologna
docker compose --profile sumo run --rm sumo prepare --city ingolstadt
```

Acquisition checks every recipe asset's size/hash, publisher commit, rights,
identity and URL receipt. Failed requests/staging are retained. A new live
manifest records its own retrieval timestamps, so its manifest hash can differ
from the frozen observation while original asset hashes remain identical.
Prepared data is bound to its source manifest and engine source bytes. A method
change requires a fresh workspace, not silently replacing cached results.
The packaging utility is [package_sumo_data.py](../../tools/package_sumo_data.py).

For the separately executed live acquisition/preparation **through MCP** review,
use another fresh mount (this intentionally makes live publisher calls and is
outside routine snapshot CI):

```sh
export URBAN_MCP_SUMO_WORKDIR="$PWD/.urban-mcp/my-sumo-live-mcp"
mkdir -p "$URBAN_MCP_SUMO_WORKDIR"
docker compose --profile sumo run --rm -v "$PWD/tools/check_sumo_live.py:/check-live.py:ro" --entrypoint python sumo-mcp /check-live.py
```

It records `evidence/live-mcp.json` and actual request manifests. It does not
run a simulation or agent; those remain separate milestones. The public
[live receipt](evidence/live-mcp.json) compares prepared route/schedule hashes
with the locked-input experiment while preserving new retrieval timestamps.

## Connect any MCP host

The server is agent/provider-independent. It does not load a model, SOUL,
memory store or agent framework. A host can discover sources/rights, restore,
prepare, inspect, simulate, compare and read complete results from day zero.
The public prompt and [blind task](agent-task.md) provide operation guidance
without expected numeric answers.

```sh
python tools/client_config.py --capability sumo --format mcp-json --data-dir .urban-mcp/my-client-sumo
python tools/client_config.py --capability sumo --format codex --data-dir .urban-mcp/my-codex-sumo
python tools/client_config.py --capability sumo --format hermes --data-dir .urban-mcp/my-hermes-sumo
```

On Windows add `--wsl-distro Ubuntu-22.04` if that is the installed Docker
environment. Inspect generated configuration before registering it. Hermes
0.18.2's stdio watchdog does not forward `cwd`; generated Linux configuration
uses GNU `env -C` before Docker. Host tool timeout is 420 s for this profile.

All text endpoints paginate at ≤12,000 characters. Follow `next_offset` until
null, including complete source licenses/manifests and `comparison.csv`.
Source text is decoded/normalized for paging; SHA-256 and byte counts identify
the original file bytes, including CSV CRLF. Do not compare the hash of
normalized page text to a raw-byte file hash. A map returns a receipt only.

Original inspection connect accepts **only** `{city,run_id}`. Use the returned
absolute begin/end; Ingolstadt begins at 24300, so advancing to 24330 means
30 s of model time. It is not `step=30`. Query a returned vehicle ID and one
`variable` per call. A `variables` array is rejected. Disconnect before the
FCD analysis. The FCD sample count/mean and live counters have the distinct
meanings described in [functionality.md](functionality.md).

## Fresh Codex and Hermes observations

Use existing private host authentication, a new empty data mount per city/host,
and new labels. Do not put credentials, private databases, reasoning or whole
host configuration in the repo. Configure Hermes through its own supported
profile setup with no copied memories, SOUL, skills, gateway or aliases;
register only this MCP and use your existing selected provider.

```sh
python tools/run_agent_check.py codex --capability sumo --city bologna --label my-sumo-bologna
python tools/run_agent_check.py codex --capability sumo --city ingolstadt --label my-sumo-ingolstadt
# Repeat for Hermes in separately authenticated, isolated profiles.
python tools/run_agent_check.py hermes --capability sumo --city bologna --label my-sumo-bologna --hermes-home /path/to/isolated-bologna-profile
python tools/run_agent_check.py hermes --capability sumo --city ingolstadt --label my-sumo-ingolstadt --hermes-home /path/to/isolated-ingolstadt-profile
```

Windows Codex runs also accept `--wsl-distro Ubuntu-22.04`; Linux Hermes
accepts `--hermes-executable /path/to/hermes`. Its profile must use the matching
`.urban-mcp/hermes-<label>` data mount. The benchmark grants only this case's
MCP toolset, disables other Codex MCP/apps/web, and forbids shell/file/web use
in the public task. Hermes receives a 100-turn limit; the host process budget
is 1800 s. The launch receipt binds commit, submitted task hash, timings and
exit status. Exit zero alone is not admission.

Export only selected public observations, then review actual complete payloads,
page chains, source/task bytes, every CSV/map hash and final strict JSON claims:

```sh
python tools/export_sumo_trace.py codex --city bologna --events .urban-mcp/agent-evidence/codex-my-sumo-bologna/events.log --output .urban-mcp/agent-evidence/codex-my-sumo-bologna/trace.json
python tools/export_sumo_trace.py hermes --city bologna --state-db /path/to/isolated-bologna-profile/state.db --output .urban-mcp/agent-evidence/hermes-my-sumo-bologna/trace.json --answer-output .urban-mcp/agent-evidence/hermes-my-sumo-bologna/answer.md
python tools/review_sumo_agents.py codex --city bologna --workspace .urban-mcp/codex-my-sumo-bologna --observations .urban-mcp/agent-evidence/codex-my-sumo-bologna
python tools/review_sumo_agents.py hermes --city bologna --workspace .urban-mcp/hermes-my-sumo-bologna --observations .urban-mcp/agent-evidence/hermes-my-sumo-bologna
```

Repeat exports/reviews with Ingolstadt and its matching paths. The review
compares against committed native evidence; a new method requires a separately
reviewed native dossier first, not editing expected outputs until a test passes.
`tools/collect_sumo_evidence.py` collects a full successful suite and checks its
engine bytes against `--source-commit`. Read answers yourself and write a
separate answer-hash-bound prose verdict. Preserve omissions, unexpected
argument errors, failed answers and length failures rather than rewriting
historical observations. Interleave a successful status call after deliberate
validation failures to avoid a host circuit breaker masking recovery.

## Contributions and qualification

A new city needs rights-reviewed network, time-specific demand, vehicle types,
lane restrictions, required signals/stops, coordinate system, validated warm-up
and independent field observations. Pin all assets and model assumptions;
compare the native original first. Then add a recipe/case, reproducible harvest,
negative tests, full MCP coverage, two independent host workspaces and critical
prose review. Distinguish historical modeled demand from actual measurement.

The intended municipal value is an auditable way to discover unsupported
assumptions and examine a proposed scenario before seeking proper calibration.
It does not authorize current traffic forecasts, causal/safety/emissions
conclusions or comparing the two cities' performance. Source conflicts and
teleports require qualified model repair and fresh independent validation.
Final-product promotion additionally requires the [independent third-city gate](../../docs/product-qualification.md).
Issue #41 remains the separate independent walking reproduction task.
