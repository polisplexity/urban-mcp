# School-to-library walking access in Helsinki and Amsterdam

This case tests a real data-to-engine-to-MCP-to-agent workflow in **two central study areas**, with the same analysis recipe. It supports an exploratory municipal question: **which mapped school objects have a modeled route to a mapped library within 1,200 m, and what changes if one network link is removed?** It does not measure residents, pupils, service capacity, verified public admission or wheelchair accessibility.

Start with the project [master test record](../../MASTER_TEST_RECORD.md). See the [municipal findings and maps](findings.md), [upstream audit and implementation decisions](upstream-audit.md), [function coverage](functionality.md), [data recipe](recipe.json), [snapshot locks](snapshot.lock.json) and [blind agent task](agent-task.md). Results and host admission are recorded only after execution, in `evidence/`.

The [issue-39 revision](issue-39.md) adds explicit per-school threshold transitions and closed-link route membership, preserves the original numerical results, and repeats the two-city Codex/Hermes tests with a [versioned task](agent-task-issue-39.md). Its evidence is stored separately under `evidence/issue-39/`; the original v1 observations and verdicts remain historical evidence.

## Scope and inputs

| Item | Helsinki | Amsterdam |
| --- | --- | --- |
| Study center, longitude/latitude | 24.9414, 60.1719 | 4.8936, 52.3731 |
| Metric analysis CRS | EPSG:3067 | EPSG:28992 |
| Core / extra network buffer | 2,000 m / 2,000 m | 2,000 m / 2,000 m |
| Source | OpenStreetMap contributors | OpenStreetMap contributors |
| Walk graph | Unsimplified, all components retained | Unsimplified, all components retained |
| Origin / destination tags | `amenity=school` / `amenity=library` | Same |
| Acquisition date | 2026-11-10 UTC | 2026-11-10 UTC |

The core is a metric study disk, not the municipal boundary. Nodes include street-shape points. Destinations can lie in the extra buffer. School objects are included when their projected representative point is inside the core; libraries tagged `access=no/private` are excluded, while missing access tags remain **unknown**, not verified public. Each OSM object remains a separate record: campus nodes/buildings can duplicate one institution. The point is a geometry proxy, not a verified entrance.

Every route total includes origin snap + graph edge lengths + destination snap. Snaps above 150 m are refused. Straight connectors are unverified; a small connector can still cross a wall. The 1,200 m threshold and 4.8 km/h speed are declared scenarios. Longer paths in the truncated graph can be censored; the buffer is designed for the declared short-distance question, not global nearest-service claims. OSMnx walk mode is bidirectional and does not fully model directional foot rules, node barriers, opening hours, slope, crossings or winter conditions.

## Reproduce without an LLM account

Use Docker Engine with the Compose plugin on Linux, macOS or Windows through WSL2. Allow roughly 3 GB RAM per active case container and 1 GB free workspace storage. Concurrent host tests need additional memory/storage. These commands run from this repository checkout:

```sh
git switch feat/two-city-walking-accessibility
# Linux/WSL: map your UID/GID so the non-root container can write the mount.
export URBAN_MCP_UID="$(id -u)"
export URBAN_MCP_GID="$(id -g)"
export URBAN_MCP_WALKING_WORKDIR="$PWD/.urban-mcp/walking-reproduction"
mkdir -p "$URBAN_MCP_WALKING_WORKDIR"
docker compose --profile walking build walking
docker compose --profile walking run --rm walking-harvest harvest --mode snapshot --city helsinki
docker compose --profile walking run --rm walking-harvest harvest --mode snapshot --city amsterdam
docker compose --profile walking run --rm walking analyze --city helsinki
docker compose --profile walking run --rm walking analyze --city amsterdam
docker compose --profile walking run --rm walking test --city helsinki
docker compose --profile walking run --rm walking test --city amsterdam
```

The `walking` container runs with networking disabled, a read-only root filesystem, dropped capabilities and resource limits. `walking-harvest` and `walking-mcp` have outbound network access to restore snapshots or explicitly acquire live inputs. Stdio has no exposed TCP listener. Results stay in the mounted directory under `results/<city>/<run_id>/`; deterministic test receipts go under `evidence/<city>/`. Test run IDs are unique; `analyze` uses `native` and refuses to overwrite an existing result.

Snapshots are 8–12 MB compressed, containing GraphML, feature geometries, boundaries, request/response receipts, exact hashes and attribution. Restoration checks the release archive's size/SHA-256, member paths, expansion size, recipe identity and every input hash before activating a directory. Existing inputs must match the lock. Do not edit input files to make a test pass.

## Harvest new observations

Use a **new workspace** to preserve the pinned experiment. A live harvest is a new observation with potentially different answers:

```sh
export URBAN_MCP_WALKING_WORKDIR="$PWD/.urban-mcp/walking-new-observation"
mkdir -p "$URBAN_MCP_WALKING_WORKDIR"
docker compose --profile walking run --rm walking-harvest harvest --mode live --city helsinki --feature-endpoint private-coffee
docker compose --profile walking run --rm walking-harvest harvest --mode live --city amsterdam
```

The graph uses OSMnx's public polygon acquisition API. Features use the bounding-box API followed by exact polygon intersection filtering; `--feature-query polygon` exercises the original polygon request variant. Actual original requests and response bodies are retained, including failed responses. Our Helsinki network call succeeded on the primary Overpass service, while repeated feature requests failed; the successful feature call used the [documented Private.coffee instance](https://overpass.kumi.systems/). Amsterdam used the primary instance. These are separate queries with separate OSM timestamps, not a transactional snapshot. Public services do not promise permanent availability.

On failure, inspect `staging/<city>/raw/requests.json`. Stop retrying while a service is overloaded. After inspecting the failure and waiting, `--resume` reuses the source cache and appends receipts rather than overwriting them; `--feature-endpoint private-coffee` is an explicit alternate service choice. The primary's rate/slot handling remains enabled. Do not run live harvests in routine CI or separately for every agent. An upstream HTTP exception without a response may appear in the process log rather than as an HTTP receipt.

## Connect Codex, Hermes or another MCP client

The server uses stdio and requires neither a model SDK nor an agent framework. Generate configuration for your host:

```sh
python tools/client_config.py --capability walking --format mcp-json
python tools/client_config.py --capability walking --format codex
python tools/client_config.py --capability walking --format hermes
# Windows host launching Docker in WSL:
python tools/client_config.py --capability walking --format codex --wsl-distro Ubuntu-22.04
```

These emit the `urban_mcp_walking` server with an isolated writable data mount. A normal host must approve tool access according to its policy. The automated benchmark explicitly approves only this case server within the user's authorized test; its shell remains read-only and the task forbids other tools. No server configuration contains a provider credential.

For Codex, with its CLI installed and authenticated:

```sh
python tools/run_agent_check.py codex --capability walking --city helsinki --label walking-helsinki
python tools/run_agent_check.py codex --capability walking --city amsterdam --label walking-amsterdam
# Add --wsl-distro Ubuntu-22.04 when launching from Windows.
```

For Hermes, create a fresh profile with no inherited skills or memories. Configure only your selected model/provider and this one MCP; keep credentials in the host's private credential store. Give each city an initially empty workspace in the MCP config. Preserve any production Hermes profile/gateway. Then run:

```sh
python tools/run_agent_check.py hermes --capability walking --city helsinki --label walking-helsinki --hermes-home /absolute/path/to/isolated-profile
python tools/run_agent_check.py hermes --capability walking --city amsterdam --label walking-amsterdam --hermes-home /absolute/path/to/another-isolated-profile
```

`--hermes-executable` supports an installation outside PATH. A model account is optional for deterministic reproduction; model-host tests use each contributor's own configured authentication. Never commit host configuration, environment files, full private sessions or reasoning. Export only the public task's calls and reviewed answer with `tools/export_hermes_trace.py --task cases/two-city-walking/agent-task.md --city <city> ...`.

The tested Hermes 0.18.2 Linux launcher does not forward a configured `cwd` to its stdio watchdog. The Linux Hermes configuration generator therefore wraps Docker with `/usr/bin/env -C <absolute-repo> docker ...`. This sets a stable working directory before Compose loads its schema. If startup reports `getwd: no such file or directory`, inspect the host's MCP stderr, preserve the failure and use the generated launcher. Process exit code 0 can still accompany a failed MCP workflow.

## Interpret and contribute

Inspect CSV rows, exact keyed routes, rejected snaps, disconnected origins, map, closure comparison and input identities. A closure removes every parallel edge in both directions for a node pair. The suggested pair is a deterministic stress test, not a real works proposal or an optimal vulnerability ranking. Record a zero threshold change honestly even when routes become longer.

A useful next municipal action is to verify school/campus identities, library public admission and hours, entrances, barriers and the affected routes with local staff before selecting an intervention. Contributions can add an authoritative source adapter, verified entrances, a third city, independent reproduction, a bug fix or a well-scoped additional OSMnx operation. Every addition needs provenance, native/MCP comparison, failure cases and an updated [master record](../../MASTER_TEST_RECORD.md). Data derived from OSM remains ODbL-1.0 with **© OpenStreetMap contributors**; the repository's MIT code license does not replace it.
