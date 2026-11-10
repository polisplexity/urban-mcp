# Historical vegetation and aggregate population in Helsinki and Amsterdam

Municipal question: **which statistical zones have low mapped 2021 vegetation share, and how much published 2025 population is attached to those zones?** This is exploratory screening for deciding where to validate data locally. It does not establish park access, heat exposure, current canopy or a planting intervention.

The implementation reuses [JordanGunn/gdal-mcp](https://github.com/JordanGunn/gdal-mcp/tree/418f401c7987e388eaaee6ad13289798a1ff69b6), its FastMCP 2.12.3 server, Rasterio/GDAL and GeoPandas. It adds harvesting, verified city bindings, categorical zonal counts, population reconciliation, threshold sensitivity, bounded artifact paging and maps. There is no agent SDK or LLM dependency in the server. [Source audit](upstream-audit.md), [tool coverage](functionality.md), [municipal findings](findings.md), [evidence index](evidence/README.md), [rights](LICENSE.md).

## Reproduce without an agent account

Use Linux or WSL with Docker Engine/Compose. Until PR #42 is merged, check out its feature branch and record the exact commit. Do not overwrite earlier workspaces or evidence.

```bash
git clone --branch feat/two-city-vegetation https://github.com/polisplexity/urban-mcp.git
cd urban-mcp
git rev-parse HEAD
export URBAN_MCP_UID="$(id -u)"
export URBAN_MCP_GID="$(id -g)"
export URBAN_MCP_VEGETATION_WORKDIR="$PWD/.urban-mcp/vegetation-my-reproduction"
mkdir "$URBAN_MCP_VEGETATION_WORKDIR"
docker compose --profile vegetation build vegetation
for city in helsinki amsterdam; do
  docker compose --profile vegetation run --rm vegetation-harvest harvest --mode snapshot --city "$city"
done
docker compose --profile vegetation run --rm --entrypoint python vegetation -m unittest urban_mcp_vegetation.test_contracts -v
docker compose --profile vegetation run --rm --entrypoint python vegetation /opt/urban-mcp/tools/audit_vegetation_upstream.py --output /data/evidence/upstream-audit.json
for city in helsinki amsterdam; do
  docker compose --profile vegetation run --rm vegetation test --city "$city"
done
docker compose --profile vegetation run --rm --entrypoint env vegetation -u GDAL_MCP_WORKSPACES python -m pytest /opt/gdal-mcp/test -q -o cache_dir=/tmp/pytest-cache
```

Expected deterministic result: **110 checks in Helsinki, 131 in Amsterdam**, all 21 exposed tools and every resource/prompt family, 12 synthetic categorical/integrity regressions and 69 original-server regressions. Page counts differ because Amsterdam has more zones. The independent native oracle counts class values separately within each polygon window; it does not call the production label/bincount aggregation. It checks every zone/class, strict threshold flags, population reconciliation, paged full summaries and exact original numerical CSV bytes.

The image pins the base digest, original archive SHA and [dependency lock](../../adapters/vegetation/runtime.lock.txt). Containers run without root, with a read-only root, two CPUs and 2 GB RAM. Native analysis has no network; acquisition and the stdio MCP service use bridge networking to fetch public inputs. There is no published TCP port. [Runtime observations](evidence/runtime.json) distinguish Rasterio's and Pyogrio's different bundled GDAL versions.

Outputs under the workspace: `inputs/<city>` has immutable raw responses, crops and manifest; `prepared/<city>` has the metric raster, zone grid and quality receipt; `results/<city>/<run_id>` has full JSON/zone CSV/class CSV/GeoJSON/report/map; `evidence/<city>` has deterministic check records. CLI `prepare`, `analyze --run-id <new-id> --threshold 0.2`, and `status` are also available. Run IDs are immutable.

## Acquire a new live observation

Use a **different empty workspace**. Live acquisition downloads original WorldCover tiles and official city responses, then records native-grid crop windows. Full tile caches stay outside Git. Existing inputs are preserved and verified rather than silently refreshed.

```bash
export URBAN_MCP_VEGETATION_WORKDIR="$PWD/.urban-mcp/vegetation-my-live-harvest"
mkdir "$URBAN_MCP_VEGETATION_WORKDIR"
for city in helsinki amsterdam; do
  docker compose --profile vegetation run --rm vegetation-harvest harvest --mode live --city "$city"
  docker compose --profile vegetation run --rm vegetation prepare --city "$city"
  docker compose --profile vegetation run --rm vegetation analyze --city "$city" --run-id native-baseline --threshold 0.2
done
```

Live boundary/population responses can change; they need a new reviewed observation and snapshot before admission. Do not expect byte equality with the 2026-11-10 observation. Snapshot mode downloads the small [public data prerelease](https://github.com/polisplexity/urban-mcp/releases/tag/data-vegetation-20261110) ZIPs, verifies [locked sizes/hashes](snapshot.lock.json), safely stages/extracts them and verifies every manifest asset and recipe hash. It needs neither the full tile cache nor source-service uptime.

## Connect any MCP host

Generate a configuration with a separate initially empty data directory for each host/city. Host-side maintenance scripts need Python 3.11+ (CI uses 3.12) and the pinned metadata dependencies below; the numerical runtime stays in Docker. Standard MCP stdio is the interface in every host.

```bash
python -m pip install -r requirements-dev.txt
python tools/client_config.py --capability vegetation --format mcp-json --data-dir .urban-mcp/my-vegetation-host
python tools/client_config.py --capability vegetation --format codex --data-dir .urban-mcp/my-codex-vegetation
python tools/client_config.py --capability vegetation --format hermes --data-dir .urban-mcp/my-hermes-vegetation
```

On Windows add `--wsl-distro Ubuntu-22.04` for a Docker engine in that distro. The Linux Hermes config uses GNU `env -C` because this observed Hermes version does not forward `cwd` to its MCP watchdog. Add only this server to an isolated, already authenticated host profile. Do not copy credentials into the repository or enable messaging connectors.

Start `vegetation_status`; restore `harvest_vegetation_data(city, mode="snapshot")`; prepare; inspect `vegetation_class_catalog`; analyze `agent-baseline` at 0.20 and `agent-sensitivity` at 0.40; compare; read complete CSVs; render. Primary replies contain full low-ID sets and pooled metrics; complete per-zone records remain in artifacts. `read_vegetation_artifact` defaults to 8,000 characters and caps a page at 12,000: follow `next_offset` until null. This addresses observed Hermes truncation; increasing model context alone does not fix a tool-result limit.

## Repeat the blind host experiments

Use the unchanged [v2 task](agent-task-v2.md), new labels and empty workspaces. It has no expected numerical answers. Existing privately configured authentication is sufficient; deterministic tests need no LLM account. Each host must operate only this MCP. Exit code alone is not success.

```bash
python tools/run_agent_check.py codex --capability vegetation --city helsinki --label vegetation-helsinki-mytrial --task cases/two-city-vegetation/agent-task-v2.md
python tools/run_agent_check.py hermes --capability vegetation --city helsinki --label vegetation-helsinki-mytrial --task cases/two-city-vegetation/agent-task-v2.md --hermes-home /absolute/path/to/isolated-profile --hermes-executable /absolute/path/to/hermes
```

Repeat for Amsterdam with its own label/profile/data mount. Windows Codex can add the WSL flag above. The runner uses the label for the Codex mount; configure the Hermes mount explicitly to match `.urban-mcp/hermes-<label>`. Export selected public observations:

```bash
python tools/export_codex_trace.py --server urban_mcp_vegetation --events .urban-mcp/agent-evidence/codex-vegetation-helsinki-mytrial/events.log --output .urban-mcp/agent-evidence/codex-vegetation-helsinki-mytrial/trace.json --results-dir .urban-mcp/agent-evidence/codex-vegetation-helsinki-mytrial
python tools/export_hermes_trace.py --state-db /absolute/path/to/isolated-profile/state.db --task cases/two-city-vegetation/agent-task-v2.md --city helsinki --output .urban-mcp/agent-evidence/hermes-vegetation-helsinki-mytrial/trace.json --answer-output .urban-mcp/agent-evidence/hermes-vegetation-helsinki-mytrial/answer.md --results-dir .urban-mcp/agent-evidence/hermes-vegetation-helsinki-mytrial
```

After both cities/hosts finish, `python tools/collect_vegetation_evidence.py --workspace <native-workspace>` verifies committed executing-code hashes before collection. `python tools/review_vegetation_agents.py --suffix mytrial` checks actual bounded MCP responses, every required CSV page, full summaries/CSV/map hashes and exact answer JSON against native evidence. Explicit prose reviews in `evidence/narrative-review.json` must bind each unchanged answer SHA. The script preserves failed JSON verdicts and exits nonzero; it never invents a prose pass. Do not use historical `--allow-incomplete-results` to admit truncation.

See [the dossier](evidence/README.md) for actual host verdicts and superseded v1 observations. Expected input/schema/justification failures and host circuit-breaker refusals must be distinguished. Deterministic negative contracts are checked outside the LLM host as well.

## Extend the case openly

Keep original API binding, exact data/rights, preparation, native oracle, MCP tests, blind task and evidence together. The recipe supports only two cities. A third city needs its geography/source mapping, new assets, justified CRS/classes/denominators, missing/all-water checks and its own observation. Do not edit the hash-bound recipe and pretend old snapshots still satisfy it.

Final-product qualification is **pending** under [the independent-person rule](../../docs/product-qualification.md). These original-team experiments do not replace issue #41 or the external third-city gate for this capability.
