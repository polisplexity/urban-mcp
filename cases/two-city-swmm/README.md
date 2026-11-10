# Two-city historical drainage-capacity experiment

Municipal question: which model nodes reach at least **10 m³ of reported
overflow**, and which newly cross that threshold, when one original circular
conduit's effective diameter is reduced to 75% under observed regional rain?
The conduit is selected from original catchment areas, before examining results.
This is a reproducible computational experiment on historical neighborhood
models. It does not establish a current blockage or a calibrated flood forecast.

This capability is under development on `feat/two-city-swmm`; it has not been
merged into `main`. See the [recipe](recipe.json), [source snapshot lock](snapshot.lock.json)
and [blind agent task](agent-task.md). Evidence and host verdicts are recorded
separately in the [master](../../MASTER_TEST_RECORD.md). Independent-person,
third-city acceptance remains required before final-product qualification.

## Real models and observations

| Municipality / bounded model | Network source | Rain source |
| --- | --- | --- |
| Odense, Denmark / Bellinge | [DTU model v2](https://doi.org/10.11583/DTU.12513428.v2), CC BY 4.0; original `BellingeSWMM_v021_nopervious.inp` | DMI climateData station 06120, hourly `acc_precip`, CC BY 4.0; validity and quality metadata retained |
| Utrecht, Netherlands / Tuindorp development division | [4TU v1](https://doi.org/10.4121/fec1e3de-9586-4a61-b3a1-02382592e52c.v1), CC BY 4.0; original development network | KNMI De Bilt station 260, hourly RH from the 2011–2020 archive, CC0 with source/no-endorsement notice |

The data prerelease [data-swmm-20261110](https://github.com/polisplexity/urban-mcp/releases/tag/data-swmm-20261110)
contains original model bytes, weather, publisher terms, attribution and
request/hash manifests. Tuindorp's 2.7 GB archive is accessed through
version-consistent HTTP ZIP ranges; only the selected network is extracted.
Learned GNN weights are not hydraulic models. Original Bellinge rain-gauge
collection data have a separate noncommercial license and are excluded.

Choose the largest **complete local-calendar wet day in August 2018**, using
the rainfall lower bound for KNMI traces; ties choose the earliest. Require
the preceding and following full day: 72 hourly intervals, 24 h warm-up and
24 h cooldown. DMI supplies interval start/end explicitly. KNMI HH is interval
end UTC, including HH=24; subtract one hour before conversion to the local
model clock. No DST transition occurs in these August windows. Trace `-1`
uses an explicitly declared midpoint of 0.025 mm and ±0.025 mm uncertainty
per trace interval. Missing, invalid and duplicate rain is rejected.

All original pipe/node geometry, controls, roughness, catchment parameters,
DWF and ponding settings are preserved except the declared scenario diameter.
Tuindorp has 13 `NaN` impervious percentages on **zero-area** subcatchments;
these become zero with every original row/ID retained and each edit recorded.
The unmodified publisher file remains in the snapshot. A non-finite parameter
on a positive-area catchment is refused. Original timeseries remain present;
the observed series is added and bound to each source gauge. The time window,
hourly volume forcing and one-thread setting are explicit transformations.

## Docker reproduction

Use Linux Docker Engine/Compose or Docker Desktop with a Linux environment.
The pinned runtime targets linux/amd64. No model account or provider key is
needed for source, native, protocol or deterministic contract checks.

```sh
git clone --branch feat/two-city-swmm https://github.com/polisplexity/urban-mcp.git
cd urban-mcp
git rev-parse HEAD
export URBAN_MCP_UID="$(id -u)" URBAN_MCP_GID="$(id -g)"
export URBAN_MCP_SWMM_WORKDIR="$PWD/.urban-mcp/my-swmm-reproduction"
mkdir -p "$URBAN_MCP_SWMM_WORKDIR"
docker compose --profile swmm build swmm
docker compose --profile swmm run --rm swmm-harvest harvest --city odense --mode snapshot
docker compose --profile swmm run --rm swmm-harvest harvest --city utrecht --mode snapshot
docker compose --profile swmm run --rm --entrypoint python swmm -m unittest urban_mcp_swmm.test_contracts -v
docker compose --profile swmm run --rm --entrypoint python -e PYSWMM_MCP_TEST_MODEL=/opt/fixture/model_full_features.inp swmm -m unittest discover -s /opt/pyswmm-mcp/tests -v
docker compose --profile swmm run --rm swmm test --city odense
docker compose --profile swmm run --rm swmm test --city utrecht
```

Each full city test runs baseline/scenario with the separately compiled
original EPA C CLI, then again through the original PySWMM MCP's isolated
workers over actual stdio. It compares every node/outfall row, native report
metrics and binary time-series/snapshot values. It exercises all 27 tools,
all eight resource families, the prompt, controls/hotstart, cancellation,
invalid inputs and recovery. Logs, original reports/binary outputs and
versioned receipts remain in the data mount. `evidence/<city>/latest.json`
points to the latest test without erasing failed attempts. Odense can take
several minutes; each native batch has a 300 s budget and MCP calls 360 s.

For individual native runs use new immutable run IDs:

```sh
docker compose --profile swmm run --rm swmm prepare --city odense
docker compose --profile swmm run --rm swmm run --city odense --run-id my-baseline --scenario baseline
docker compose --profile swmm run --rm swmm run --city odense --run-id my-capacity75 --scenario capacity75
```

Native services have no network. Harvest/MCP have a bridge for public source
requests and publish no ports. Containers use a read-only root, non-root UID,
2 CPU/3 GiB RAM limits, an init process and ephemeral `/tmp`/`/.config` caches.
EPA CLI uses its own library RPATH; it must not replace the PySWMM wheel's
different toolkit library via global `LD_LIBRARY_PATH`.

The original [PySWMM MCP](https://github.com/foundanotusedname/pyswmm-mcp)
is pinned at `a4db37b45d3b30dcfbd80fc0162a8238e727a80f`, Apache-2.0.
We reuse its 18 function families and seven resource families using the
**official Python MCP SDK 2.3.0 `MCPServer`**. Two metadata responses replace
unbounded ID arrays with counts/samples; full IDs remain queryable. Nine
additions provide sources, binding, comparison and paging. A reviewed Linux
parent-death patch supplements the original Windows watchdog; the pristine
checkout remains `/opt/pyswmm-mcp`, the marked runtime copy is separate.
The original EPA solver source is compiled without mathematical changes.
Runtime pins are in [the lock](../../adapters/swmm/runtime.lock.txt) and
[Dockerfile](../../adapters/swmm/Dockerfile). This is not a new SWMM solver,
an LLM framework requirement or a promise to expose every SWMM GUI feature.

## Reharvest from publishers

Use a **fresh** mount, then run the same preparation and validation:

```sh
export URBAN_MCP_SWMM_WORKDIR="$PWD/.urban-mcp/my-swmm-live-harvest"
mkdir -p "$URBAN_MCP_SWMM_WORKDIR"
docker compose --profile swmm run --rm swmm-harvest harvest --city odense --mode live
docker compose --profile swmm run --rm swmm-harvest harvest --city utrecht --mode live
docker compose --profile swmm run --rm swmm prepare --city odense
docker compose --profile swmm run --rm swmm prepare --city utrecht
```

Acquisition verifies original member hashes, archive/range consistency and
weather content. Raw DMI responses retain retrieval/envelope timestamps;
the separately recorded observation-content fingerprint excludes only the
changing envelope and sorts records by ID. Updated quality-controlled records
therefore fail the pinned experiment rather than silently rewriting it.
Use a reviewed new recipe/snapshot for new observations. Failed acquisitions
remain available for investigation. Packaging: [package_swmm_data.py](../../tools/package_swmm_data.py).

## Connect Codex, Hermes or another MCP host

```sh
python tools/client_config.py --capability swmm --format mcp-json --data-dir .urban-mcp/my-swmm-client
python tools/client_config.py --capability swmm --format codex --data-dir .urban-mcp/my-swmm-codex
python tools/client_config.py --capability swmm --format hermes --data-dir .urban-mcp/my-swmm-hermes
```

On Windows add `--wsl-distro Ubuntu-22.04` when that is the installed Docker
environment. Inspect configuration and register it in your own host. Hermes
0.18.2 requires GNU `env -C` for its stdio working directory; generated Linux
configuration includes it. The tool timeout is 420 s. Use existing host
authentication, an isolated Hermes profile and initially empty mounts for
each host/city. No credentials or messaging connectors belong in evidence.

```sh
python tools/run_agent_check.py codex --capability swmm --city odense --label swmm-odense-v1
python tools/run_agent_check.py hermes --capability swmm --city odense --label swmm-odense-v1 --hermes-home /your/isolated/profile --hermes-executable /your/hermes
# Repeat with utrecht, a distinct label/profile and a fresh mount.
```

Use only the [public blind task](agent-task.md). Read complete source/comparison
CSV pages; each page is ≤12,000 characters and identifies original byte hashes.
Review successful operations, exact numeric claims and prose separately.
An exit code, a corrected answer or a different model operated by the original
team does not supply independent third-person qualification.

## What another municipality must supply

An openly licensed, coherent hydraulic drainage model is essential: original
asset IDs, node inverts, pipe sections/roughness, catchment drainage assignment,
controls, boundary/DWF/inflow assumptions, source units and time conventions.
Open streets or a global DEM do not supply those measurements. Add permitted
rainfall with stated spatial/temporal resolution and full interval coverage,
then document all conversions and independent validation needs. Preserve
native warnings and original publisher provenance. A zero-change or no-flood
result is valid evidence; do not increase rainfall or change assets merely
to make a demonstration more dramatic.

Overflow statistics are not a 2D flood extent, property damage, population
exposure, observed blockage or safety decision. Both models remain historical;
their original calibration is not inherited. Final-product admission requires
an independent person reproducing a third city and an accepted public review.
