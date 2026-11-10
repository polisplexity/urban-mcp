"""Agent-neutral MCP surface. No agent SDK, credentials or global graph state."""
import json

from fastmcp import FastMCP
from mcp.types import ToolAnnotations

from . import data, engine

mcp = FastMCP("Urban MCP walking", instructions="Start with walking_status. Choose an explicit city; graph state never switches implicitly. Harvest the pinned snapshot, inspect graph and feature catalog, run a new baseline, then an explicit link closure and compare. Distances include two straight snap connectors which are not verified paths. Denominator is mapped school objects, not people. Read the limits and preserve provenance. Never use vehicle maxspeed as walking speed. Read resources for data receipts and the prompt for a municipal review checklist.")
READ = ToolAnnotations(readOnlyHint=True, destructiveHint=False, idempotentHint=True, openWorldHint=False)
WRITE = ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=False)


@mcp.tool(annotations=READ)
def walking_status() -> dict:
    """Discover both cities, exact recipe, data readiness, assumptions and limitations."""
    return data.status()


@mcp.tool(annotations=ToolAnnotations(readOnlyHint=False, destructiveHint=False, idempotentHint=False, openWorldHint=True))
def harvest_walking_data(city: str, mode: str = "snapshot") -> dict:
    """Restore hash-locked public data (snapshot), or explicitly harvest live OSM into a fresh workspace. Never silently refresh. The live route needs network access and may take minutes."""
    return data.harvest(city, mode)


@mcp.tool(annotations=READ)
def walking_graph_info(city: str) -> dict:
    """Graph topology, CRS, acquisition time, components and input identity."""
    return engine.graph_info(city)


@mcp.tool(annotations=READ)
def walking_feature_catalog(city: str, amenity: str = "all", core_only: bool = False) -> dict:
    """Inspect harvested school/library OSM IDs, representative points, access tags and study-core membership. No live API call."""
    return engine.catalog(city, amenity, core_only)


@mcp.tool(annotations=READ)
def walking_snap(city: str, longitude: float, latitude: float) -> dict:
    """Nearest node and snap distance in meters; reject remote coordinates, flag snaps over the fixed 150 m rule."""
    return engine.snap(city, longitude, latitude)


@mcp.tool(annotations=WRITE)
def walking_accessibility(city: str, run_id: str, threshold_m: float = 1200, speed_kph: float = 4.8, closures: list[dict[str, int]] | None = None) -> dict:
    """School-to-nearest-library network analysis. Export CSV, exact keyed routes, summary and report. Include snap connectors in destination choice and totals. New run_id required. A closure {u,v} removes both directions and all parallel edges; no closures means baseline. Threshold <=1850 m; speed is an explicit scenario assumption, never measured."""
    return engine.analyze(city, run_id, threshold_m, speed_kph, closures)


@mcp.tool(annotations=READ)
def walking_compare(city: str, baseline_id: str, scenario_id: str) -> dict:
    """Compare compatible baseline and link-closure runs; identify detours, loss of reachability and threshold changes. Removing edges cannot shorten shortest paths."""
    return engine.compare(city, baseline_id, scenario_id)


@mcp.tool(annotations=READ)
def walking_route(city: str, origin_id: str, destination_id: str, k: int = 1) -> dict:
    """One to three alternative length-shortest paths between harvested feature IDs, with actual parallel-edge keys and endpoint connector distances. Paths are general walking proxies."""
    return engine.route(city, origin_id, destination_id, k)


@mcp.tool(annotations=READ)
def walking_isochrone(city: str, longitude: float, latitude: float, budget_m: float = 1200, sample_limit: int = 20) -> dict:
    """Reachable graph-node count after subtracting the origin snap connector from the distance budget, with a bounded node sample. Not a coverage polygon or population calculation."""
    return engine.isochrone(city, longitude, latitude, budget_m, sample_limit)


@mcp.tool(annotations=READ)
def walking_network_stats(city: str) -> dict:
    """Components, directed total edge length and orientation entropy. Unsimplified nodes include shape points; do not call them intersections."""
    return engine.network_stats(city)


@mcp.tool(annotations=READ)
def walking_node(city: str, node_id: int) -> dict:
    """Inspect a harvested OSM node and its outgoing neighbors without downloading anything."""
    graph, _, _ = engine.load(city)
    if node_id not in graph:
        raise ValueError("node_id does not exist in the input graph")
    return {"node_id": node_id, "attributes": dict(graph.nodes[node_id]), "outgoing_neighbors": sorted(int(n) for n in graph.successors(node_id))}


@mcp.tool(annotations=READ)
def walking_edge(city: str, u: int, v: int, key: int = 0) -> dict:
    """Inspect a specific directed parallel edge and its length/OSM tags."""
    graph, _, _ = engine.load(city)
    if not graph.has_edge(u, v, key):
        raise ValueError("edge does not exist in the input graph")
    return {"u": u, "v": v, "key": key, "attributes": {k: v for k, v in graph[u][v][key].items() if k != "geometry"}}


@mcp.tool(annotations=WRITE)
def walking_export_graph(city: str, run_id: str) -> dict:
    """Export a fresh GraphML copy to the mounted results workspace; verify topology by reloading it. Does not rewrite the input snapshot."""
    return engine.export_graph(city, run_id)


@mcp.tool(annotations=WRITE)
def walking_render_map(city: str, run_id: str) -> dict:
    """Render a baseline/scenario's exact routes and study boundary in the city's metric CRS, with OSM attribution. Output map.png stays in the mounted results directory."""
    return engine.render(city, run_id)


@mcp.tool(annotations=READ)
def walking_read_artifact(city: str, run_id: str, name: str = "summary.json", offset: int = 0, limit: int = 20000) -> dict:
    """Read bounded pages from a run's allowlisted outputs. Inspect CSV/report/routes or obtain SHA-256 and size of PNG/GraphML; arbitrary paths are refused."""
    return engine.artifact(city, run_id, name, offset, limit)


@mcp.resource("walking://case")
def case_recipe() -> dict:
    """Exact two-city recipe and interpretation limits."""
    return data.recipe()


@mcp.resource("walking://{city}/manifest")
def input_manifest(city: str) -> dict:
    """Verified input hashes and source receipts for a city."""
    return data.verify(city)[1]


@mcp.resource("walking://{city}/graph")
def graph_metadata(city: str) -> dict:
    """Topology and identity of a city's immutable graph."""
    return engine.graph_info(city)


@mcp.prompt
def municipal_walking_review(city: str) -> str:
    """Municipal workflow with assumptions and evidence to inspect before interpreting results."""
    data.city_config(city)
    return f"Review {city}: discover recipe; restore the snapshot; inspect graph, schools and libraries; run the 1200 m baseline at assumed 4.8 km/h; read the CSV and keyed routes; inspect snap exclusions and disconnected paths; run one declared bidirectional link closure and compare; render/export evidence. Report mapped school objects, never population or pupils. Preserve the core/buffer bounds, input identity, ODbL attribution and all limitations. Make an exploratory municipal recommendation and state what field validation would be needed."
