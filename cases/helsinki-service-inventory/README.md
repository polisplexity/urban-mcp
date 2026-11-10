# Helsinki: municipal service inventory by district

This executable case follows public harvesting → preparation → original geospatial tools → MCP → independent agent hosts. The municipal question is how registered public-library and health-station locations are distributed against 2025 district population. A zero in the selected registry supports an inventory review; it does not by itself justify building a facility. Start with the [master test record](../../MASTER_TEST_RECORD.md).

## Reproduce from main in Docker

Requirements: Git, Docker Engine with Compose, and HTTPS access during image construction and snapshot restoration. Native analysis and protocol checks run offline after restoration, with no data key or LLM account. Linux amd64 through WSL2 was tested; other platforms need their own evidence. Use a new workspace for each independent reproduction.

```sh
git clone --branch main https://github.com/polisplexity/urban-mcp.git
cd urban-mcp
# Record the exact source revision alongside your evidence.
git rev-parse HEAD
export URBAN_MCP_UID="$(id -u)"
export URBAN_MCP_GID="$(id -g)"
export URBAN_MCP_WORKDIR="$PWD/.urban-mcp/inventory-main-reproduction"
mkdir -p "$URBAN_MCP_WORKDIR"

docker compose --profile municipal build inventory
docker compose --profile municipal run --rm harvest harvest --mode snapshot
docker compose --profile municipal run --rm inventory prepare
docker compose --profile municipal run --rm inventory inventory --service-id 813 --run-id native-library
docker compose --profile municipal run --rm inventory inventory --service-id 703 --run-id native-health
docker compose --profile municipal run --rm inventory test
# Match CI's original-server regression environment.
docker compose --profile municipal run --rm --entrypoint env inventory -u GDAL_MCP_WORKSPACES python -m pytest /opt/gdal-mcp/test -q -o cache_dir=/tmp/pytest-cache
```

Run this shell block inside WSL on Windows with Docker integration. For an existing clean checkout, use `git switch main` and `git pull --ff-only` instead of cloning. Results are in `$URBAN_MCP_WORKDIR/results/`: summary JSON, CSV, district/point GeoJSON and an offline `report.html` map/table. MCP paths beginning `/data/` refer to this mounted directory. Keep outputs outside Git.

The `inventory` service has no network, a read-only root filesystem, dropped capabilities and CPU/memory/process limits. `harvest` and `municipal-mcp` have network access for acquisition. Give concurrent clients separate `URBAN_MCP_WORKDIR` values; concurrent writers to one workspace are not admitted. Inventory writes reuse the selected run directory, so choose a fresh workspace or new run ID to preserve earlier evidence.

## Acquire a new observation

```sh
export URBAN_MCP_WORKDIR="$PWD/.urban-mcp/inventory-new-observation"
mkdir -p "$URBAN_MCP_WORKDIR"
docker compose --profile municipal run --rm harvest harvest --mode live
docker compose --profile municipal run --rm inventory prepare
```

A live harvest creates a new source version and changes the active pointer only after complete acquisition. Preparation must be repeated. Snapshot mode restores the version in [snapshot.lock.json](snapshot.lock.json); updating data and reproducing a historical result are distinct operations. Review each new observation independently.

The [recipe](recipe.json) records URLs, filters, CRS, period, rights and limitations. Receipts preserve original responses and the PxWeb query, pages, public URLs, sizes, SHA-256 hashes, counts, retries and pagination completion. Duplicate IDs, changing pagination totals and incomplete responses are rejected. Preparation verifies hashes, schemas, geometries, keys and year; prepared assets receive hashes too.

## Connect an MCP-capable host

```sh
docker compose --profile municipal run --rm -T municipal-mcp
```

This launches stdio MCP. Generate the configuration for the host and its data workspace:

```sh
python tools/client_config.py --capability inventory --format mcp-json --data-dir .urban-mcp/inventory-host
python tools/client_config.py --capability inventory --format codex --data-dir .urban-mcp/inventory-codex
python tools/client_config.py --capability inventory --format hermes --data-dir .urban-mcp/inventory-hermes
# Windows Python launching Docker through WSL:
python tools/client_config.py --capability inventory --format codex --data-dir .urban-mcp/inventory-codex --wsl-distro Ubuntu-22.04
```

Helpers need Python 3.11 or later; install `requirements-dev.txt` for YAML output. Generated configuration contains no provider credential. Add it to the existing host according to that host's policy. For Hermes, use a fresh profile without inherited skills or memories, configure your own provider privately, and add only this case's MCP block. Preserve production profiles and gateways. On Linux the Hermes generator uses GNU `env -C <repo>` to establish the working directory before Docker starts.

The workflow is `municipal_status` → `harvest_municipal_sources` → `prepare_municipal_data` → `service_catalog` → `inventory_by_district` → `read_case_artifact`. Returned datasets also feed the original GDAL tools. Category search uses substrings in source languages: `librar` matches library/libraries. Tested exact IDs are `813` for public libraries and `703` for health stations, without implicit category-hierarchy expansion.

## Repeat and review host tests

Use new labels and initially empty data mounts for each host. A Hermes profile must point at the matching `.urban-mcp/hermes-<label>` directory before launch; the runner does not rewrite that profile.

```sh
python tools/run_agent_check.py codex --capability inventory --label inventory-main-review
# Add --wsl-distro Ubuntu-22.04 when launching from Windows.
python tools/run_agent_check.py hermes --capability inventory --label inventory-main-review --hermes-home /absolute/path/to/fresh-profile
```

Use `--hermes-executable` if the installed launcher is outside PATH. The [original blind task](agent-task.md) and observed answers are retained verbatim as historical evidence. To run a new English task, place a versioned public Markdown task under `cases/`, pass `--task`, and review its new outputs; that is a new experiment, not the original task-hash observation.

Record source commit, host/model/version, task hash, transport, calls, artifacts, errors/retries and a factual review of the final answer. Compare both service CSVs with native results. Process exit alone is insufficient. Export only this public case's calls and reviewed answer; never commit private configuration, credentials, whole sessions or reasoning. The [committed evidence](evidence/README.md) records the original independent Codex/Hermes observations; this guide does not claim a fresh LLM rerun during integration.

## Original software and interface delta

The runtime reuses [JordanGunn/gdal-mcp](https://github.com/JordanGunn/gdal-mcp) at `418f401c7987e388eaaee6ad13289798a1ff69b6`, with the archive verified by SHA-256. It retains FastMCP 2.12.3, MCP SDK 1.14.0 and the original geospatial libraries; dependency constraints come from its `uv.lock`. Python fits that upstream API and GeoPandas; it does not select a language for other capability families.

Our additions are recipe connectors, admitted/versioned data, GeoPandas preparation/spatial joins, category lookup, district/population aggregation, reports, sandbox, protocol suite and host checks. Native projection, geometry and format drivers are reused. The [function matrix](functionality.md) separates original and added operations.

Four verified compatibility corrections address URI templates; catalog arguments/serialization/subdirectories; COG overviews before writer closure; and a typed justification schema. [apply_compat.py](../../adapters/municipal_inventory/apply_compat.py) checks exact pinned source blocks and fails on drift. It does not silently upgrade the original server or replace geometry algorithms. Historical [findings](findings.md) remain available.

## Inputs and limits

- Snapshot acquired on 2026-11-10: 12,455 Service Map entries, 34 districts and 1,113 categories. Preparation retains 12,423 valid points; 32 entries lack a usable point and 26 points have no unique district.
- Population at 2025-12-31: 694,392 municipal total versus 680,710 across the selected 34 district rows. The remaining 13,682 are a statistical aggregate difference; no resident coordinates were acquired and their location outside district polygons is not established.
- Category `813` has 46 geolocated records; `703` has 23. These are records, not unique buildings, capacity, opening hours or quality. Districts `302`, `402`, `405`, `601` have no selected library record; this does not establish lack of access.
- GeoJSON coordinates use WGS84; metric operations use EPSG:3067. A 500 m buffer is Euclidean and omits the walking network, barriers and demand calibration.
- `district_ids.tif` is a categorical 100 m raster for cartographic-chain checks. Pixels encode district IDs; their averages are not physical indicators and must never be added as population. This is not vegetation analysis or a population model.

Sources and rights: [Service Map / CC BY 4.0](https://www.hel.fi/palvelukarttaws/restpages/index_en.html), [Helsinki PxWeb](https://stat.hel.fi/Resources/Images/PxWebAPI_Help_Helsinki_en.pdf), [Statistics Finland / CC BY 4.0](https://stat.fi/en/about-us/get-to-know-statistics-finland/legislation/terms-of-use). Attribution: City of Helsinki Service Map; City of Helsinki Urban Research and Statistics / Statistics Finland. Provenance and transformations are identified. Photos and contact fields are not harvested. The MIT code license does not relicense source data or imply institutional endorsement.

## Contribute

The real MCP suite discovers and tests all 19 exposed tools, resource/prompt families and invalid inputs. It compares IDs, geometries, pixels, statistics and municipal outputs with native calls. CI restores the pinned snapshot; it does not run live city acquisition or model-host tests on every PR.

Useful contributions include independent reproduction, source/transformation review, an additional parameter/driver check, clearer errors, specialist indicator review or another municipal case. A new city needs its own recipe, source IDs, preparation and acceptance evidence. Update the [master record](../../MASTER_TEST_RECORD.md), preserve useful failures and follow [CONTRIBUTING.md](../../CONTRIBUTING.md).
