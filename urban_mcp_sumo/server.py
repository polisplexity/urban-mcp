"""Municipal profile: reused original MCP operations plus explicit missing bindings."""
from contextlib import asynccontextmanager
import math
from pathlib import Path
from threading import RLock

import anyio
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.exceptions import ToolError
import traci

# The MIT original checkout is installed unmodified at /opt/sumo-mcp/src.
import server as upstream
from . import data, engine
from .compat import install_traci_stderr

install_traci_stderr()

_SERIAL = RLock()
_owner = None
_process = None


def cleanup():
    global _owner, _process
    try:
        upstream.connection_manager.disconnect(timeout_s=5)
    finally:
        if _process is not None and _process.poll() is None:
            _process.terminate()
            try:
                _process.wait(timeout=5)
            except Exception:
                _process.kill()
                _process.wait(timeout=5)
        _owner, _process = None, None


@asynccontextmanager
async def lifespan(server):
    try:
        yield {}
    finally:
        with anyio.CancelScope(shield=True):
            await anyio.to_thread.run_sync(engine.stop_owned_batches)
            await anyio.to_thread.run_sync(cleanup)


mcp = FastMCP("urban_mcp_sumo", instructions="Discover sumo_status and the exact recipe. Restore snapshot, prepare, inspect source network/target lane IDs. Run baseline and works30 with new immutable run IDs; compare the same scheduled corridor cohort, fixed seed and horizon. Follow complete comparison CSV pages of at most 12000 characters. Distinguish scheduled, arrived, unfinished, undeparted and not-recorded vehicles; completed-only means need their denominator. These are historical published models, not current observed traffic, freshly revalidated calibration, safety/emissions evidence or city rankings. Original control_simulation is restricted to new baseline inspection runs: connect params={city,run_id}, step params={step:absolute_simulation_time}, disconnect. Inspect the returned begin/end; do not infer step duration from call count. query_simulation_state reuses original vehicle_list, simulation and five vehicle-variable queries. run_analysis describes sample-weighted FCD points, not unique vehicles or mean journey time. Numeric artifacts, answer claims and prose require separate review. Interleave successful status calls between deliberate validation failures if the host uses a failure circuit breaker.", lifespan=lifespan)


async def execute(function, *args):
    def serialized():
        with _SERIAL:
            return function(*args)
    try:
        return await anyio.to_thread.run_sync(serialized)
    except (OSError, ValueError, RuntimeError, KeyError) as exc:
        raise ToolError(str(exc)) from exc


def original_result(value):
    if value.startswith(("Error", "Unknown", "Simulation error")):
        raise ValueError(value)
    return value


def control(action, params):
    global _owner, _process
    params = params or {}
    if action == "connect":
        if _owner is not None:
            raise ValueError("An inspection session is already active; disconnect before another run")
        if set(params) != {"city", "run_id"}:
            raise ValueError("Inspection connect requires only city and a new run_id; external hosts/configuration/executables are not admitted")
        output, spec = engine.make_run(params["city"], params["run_id"], inspection=True)
        try:
            text = original_result(upstream.control_simulation("connect", {"config_file": spec["config"], "gui": False, "port": 8813, "timeout_s": 45}))
            _owner = spec
            _process = traci.getConnection("default")._process
            return {"original_result": text, "inspection": spec, "absolute_simulation_time": traci.simulation.getTime()}
        except Exception:
            cleanup()
            raise
    if action == "disconnect":
        active = _owner is not None
        text = original_result(upstream.control_simulation("disconnect", {}))
        cleanup()
        return {"original_result": text, "active_before": active, "active_after": False}
    if action != "step":
        raise ValueError("action must be connect, step or disconnect")
    if _owner is None:
        raise ValueError("No active inspection session")
    if set(params)-{"step"}:
        raise ValueError("Only the absolute step target is admitted")
    target = params.get("step", 0)
    current = traci.simulation.getTime()
    if type(target) not in {int, float} or not math.isfinite(target) or target < 0 or (target > 0 and (target <= current or target > _owner["end"])) or (target == 0 and current >= _owner["end"]):
        raise ValueError("Step must advance within the returned absolute inspection horizon")
    text = original_result(upstream.control_simulation("step", {"step": target, "timeout_s": 45}))
    return {"original_result": text, "city": _owner["city"], "absolute_simulation_time": traci.simulation.getTime(), "inspection_end": _owner["end"]}


@mcp.tool()
async def get_sumo_info() -> str:
    """Reused original MCP function: report installed native SUMO version and paths."""
    return await execute(lambda: original_result(upstream.get_sumo_info()))


@mcp.tool()
async def control_simulation(action: str, params: dict | None = None) -> dict:
    """Reused original connect/absolute-step/disconnect operations with bounded model ownership. Connect params: city, new run_id. Inspection lasts 60 simulated seconds from the city's declared begin, with seed and mandatory signals preserved. External hosts, arbitrary config paths, GUI and unbounded timeouts are refused. Repeated connect cannot silently select another model."""
    return await execute(control, action, params)


def query(target, params):
    if _owner is None:
        raise ValueError("No active inspection session; disconnected is not an empty city")
    params = params or {}
    if target not in {"vehicle_list", "simulation", "vehicle_variable"}:
        raise ValueError("Unknown inspection target")
    if target == "vehicle_variable":
        if set(params) != {"vehicle_id", "variable"} or params["variable"] not in {"speed", "position", "acceleration", "lane", "route"}:
            raise ValueError("Supply vehicle_id and one of speed/position/acceleration/lane/route")
    elif params:
        raise ValueError("This inspection target has no parameters")
    if target == "vehicle_list" and traci.vehicle.getIDCount() > 1000:
        raise ValueError("Inspection vehicle list exceeds the 1000-object bound")
    return original_result(upstream.query_simulation_state(target, params))


@mcp.tool()
async def query_simulation_state(target: str, params: dict | None = None) -> str:
    """Reused original vehicle_list, simulation and vehicle-variable speed/position/acceleration/lane/route. Requires this profile's active inspection. Speeds m/s, acceleration m/s², positions source-network metres; route is current planned route, not proven past traversal. Original departed/arrived/loaded counts are per-step, not cumulative."""
    return await execute(query, target, params)


def analyze_original(path):
    resolved = Path(path).resolve()
    base = (data.root()/"results").resolve()
    if not resolved.is_relative_to(base) or resolved.name != "fcd.xml.gz" or len(resolved.relative_to(base).parts) != 3:
        raise ValueError("Only a case run's fcd.xml.gz is admitted")
    city, run_id, _ = resolved.relative_to(base).parts
    data.config(city); data.token(run_id)
    if not resolved.is_file():
        raise ValueError("FCD artifact does not exist")
    return original_result(upstream.run_analysis(str(resolved)))


@mcp.tool()
async def run_analysis(fcd_file: str) -> str:
    """Reused original FCD analysis for a case run's fcd.xml.gz. Counts samples and their speed distribution at the configured 10 s output period; not unique vehicles, journey-time mean, field traffic measurements or exposure."""
    return await execute(analyze_original, fcd_file)


@mcp.tool()
async def sumo_status() -> dict:
    """Discover exact supported cities, sources/rights/time windows, fixed-seed method, missing inputs and pending qualification."""
    return await execute(lambda: {**data.status(), "recipe":data.public_recipe(), "active_inspection": _owner})


@mcp.tool()
async def harvest_sumo_data(city: str, mode: str = "snapshot") -> dict:
    """Restore the locked public snapshot, or reacquire exact pinned original publisher assets in live mode. No random demand or hidden calibration. Fresh workspace required for live acquisition; source failures are preserved."""
    def acquire():
        data.harvest(city,mode)
        folder,manifest=data.verify(city)
        return {"city":city,"mode":mode,"publisher_repository":manifest["publisher_repository"],"publisher_commit":manifest["publisher_commit"],"asset_count":len(manifest["files"]),"license":manifest["license"],"input_manifest_sha256":data.sha(folder/"manifest.json"),"source_details":"Read the full manifest.json and publisher license through read_sumo_source pages."}
    return await execute(acquire)


@mcp.tool()
async def read_sumo_source(city: str, name: str = "manifest.json", offset: int = 0, limit: int = 8000) -> dict:
    """Read complete source manifest/requests, exact recipe, original config or publisher LICENSE in ≤12000-character pages. Follow next_offset until null. Sources stay hash-verified/read-only; arbitrary files and raw bulk demand are refused."""
    return await execute(data.read_source,city,name,offset,limit)


@mcp.tool()
async def prepare_sumo_case(city: str) -> dict:
    """Verify source hashes, preserve vehicle types/routes/signals and the declared departure slice, select the most-used eligible published corridor and identify its scheduled evaluation cohort. Preserve source step length and processing settings. Planned route membership is not observed traversal."""
    return await execute(engine.prepare, city)


@mcp.tool()
async def sumo_network_info(city: str, edge_id: str | None = None) -> dict:
    """Inspect published network counts, signal count, source XY bounds, target edge/lanes and time/seed. Optional exact source edge lookup gives geometry and lane speeds; no geographic-distance or municipal-boundary inference."""
    return await execute(engine.network_info, city, edge_id)


@mcp.tool()
async def run_sumo_scenario(city: str, run_id: str, scenario: str = "baseline") -> dict:
    """Run baseline or works30 directly with original SUMO, preserved historical inputs/settings and seed 37. New immutable run ID. Works30 limits only the declared target's eligible passenger lanes to 30 km/h from cohort_begin; connectivity and other speeds remain unchanged. Explicitly report non-completed/undeparted/missing trips and completed-only means, not current traffic, fresh calibration, causal or safety/emission conclusions."""
    # Each native batch owns a separate process/config/output directory. It does
    # not use the original global TraCI connection; independent batches may run
    # concurrently within the container's CPU/RAM budget.
    try:
        return await anyio.to_thread.run_sync(engine.run, city, run_id, scenario, abandon_on_cancel=True)
    except (OSError, ValueError, RuntimeError, KeyError) as exc:
        raise ToolError(str(exc)) from exc


@mcp.tool()
async def compare_sumo_runs(city: str, baseline_id: str, scenario_id: str) -> dict:
    """Compare baseline/works30 with identical data/method/seed/horizon and scheduled corridor cohort. Report completion states, paired-completed denominator and excluded censored trips. Every per-vehicle state and strict 30 s flag remains in paged comparison.csv; not a between-city ranking or observed causal effect."""
    return await execute(engine.compare, city, baseline_id, scenario_id)


@mcp.tool()
async def read_sumo_artifact(city: str, run_id: str, name: str = "summary.json", offset: int = 0, limit: int = 8000) -> dict:
    """Read allowlisted public result text and SHA/bytes in ≤12000-character pages. Follow next_offset until null for the entire comparison/cohort CSV. Map returns a receipt, not image bytes; arbitrary paths are refused."""
    return await execute(engine.read_artifact, city, run_id, name, offset, limit)


@mcp.tool()
async def render_sumo_map(city: str, run_id: str) -> dict:
    """Render original network geometry, declared works corridor and explicit scheduled-cohort completion states with attribution. No visual field validation or trajectory-exposure claim. Returns a PNG receipt."""
    return await execute(engine.render, city, run_id)


@mcp.resource("sumo://case")
def case_recipe() -> dict:
    return data.public_recipe()


@mcp.resource("sumo://{city}/manifest")
def source_manifest(city: str) -> dict:
    folder,manifest=data.verify(city)
    return {**{k:v for k,v in manifest.items() if k!="requests"},"full_manifest_sha256":data.sha(folder/"manifest.json"),"raw_requests":"Read manifest.json through read_sumo_source paging for complete original request receipts."}


@mcp.resource("sumo://{city}/quality")
def preparation_quality(city: str) -> dict:
    return engine.prepared(city)[1]


@mcp.prompt()
def municipal_sumo_review(city: str) -> str:
    data.config(city)
    return f"Review {city}: discover sources/rights, source period and unknown validation inputs; restore snapshot; prepare and inspect exact target edge/lanes and scheduled corridor cohort; run fixed-seed baseline and works30; compare completion states and full paged CSV; render map; exercise original version, live inspection/vehicle variables and FCD sample analysis; preserve semantic errors and host gaps. Distinguish historical modeled demand from raw observations, in-network duration from insertion delay, completed-only differences from censored outcomes and per-step counters from totals. Do not infer current congestion, calibrated forecast, city ranking, causality, safety or measured emissions. Interleave successful status calls between expected failures if necessary for host recovery."


async def serve():
    async def wakeup():
        while True:
            await anyio.sleep(.1)
    # Preserve the original server's stdio event-loop wakeup workaround.
    async with anyio.create_task_group() as group:
        group.start_soon(wakeup)
        try:
            await mcp.run_stdio_async()
        finally:
            group.cancel_scope.cancel()
