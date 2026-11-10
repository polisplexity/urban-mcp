"""Reuse GDAL-MCP at the pinned revision and add municipal data/table operations."""
from __future__ import annotations

import json
from typing import Literal

import anyio
from fastmcp.exceptions import ToolError
from fastmcp.server.middleware import Middleware
import pyogrio
from pyproj import CRS

from src.server import mcp
from src.config import resolve_path
from src.middleware.paths import validate_path
from urban_mcp_case import analysis, sources

# FastMCP 2.12.3 exposes a read-only instructions property. The underlying
# pinned MCP Server stores the initialization field used by every host.
mcp._mcp_server.instructions = (
    "Urban MCP Helsinki municipal case. Start with municipal_status, then "
    "harvest_municipal_sources(mode='snapshot') if inputs are missing, "
    "prepare_municipal_data, service_catalog(search='public librar'), and "
    "inventory_by_district. Inspect returned dataset paths and artifacts. "
    "Data acquisition is separate from scientific verification. Counts do not "
    "prove service quality or walking accessibility. Use EPSG:3067 for metres. "
    "The categorical district-ID raster is not population data. "
    + (mcp.instructions or "")
)


class MetricOperationPolicy(Middleware):
    """The admitted municipal profile interprets distance/tolerance as metres."""
    async def on_call_tool(self, context, call_next):
        if context.message.name in {"vector_buffer", "vector_simplify"}:
            args = context.message.arguments or {}
            uri = args.get("uri")
            if uri:
                path = validate_path(str(resolve_path(uri)))
                info = pyogrio.read_info(path)
                crs = CRS.from_user_input(info["crs"]) if info.get("crs") else None
                if crs is None or not crs.is_projected or not crs.axis_info or any(axis.unit_name not in {"metre", "meter"} for axis in crs.axis_info[:2]):
                    raise ToolError("This municipal profile requires a projected CRS in metres for buffer/simplify. Inspect metadata and reproject to EPSG:3067; degrees are not metres.")
        return await call_next(context)


mcp.add_middleware(MetricOperationPolicy())


async def call(function, *args):
    try:
        return await anyio.to_thread.run_sync(function, *args)
    except (ValueError, OSError, RuntimeError, KeyError) as exc:
        raise ToolError(str(exc)) from exc


@mcp.tool()
async def municipal_status() -> dict:
    """Inspect the Helsinki case, input integrity, preparation state and scientific limits. Start here."""
    return await call(analysis.status)


@mcp.tool()
async def harvest_municipal_sources(mode: Literal["snapshot", "live"] = "snapshot") -> dict:
    """Acquire Helsinki inputs: pinned public snapshot for reproduction, or bounded live API harvest into a new version. Live needs network; never overwrites the previous snapshot. This does not execute analysis."""
    return await call(sources.harvest_snapshot if mode == "snapshot" else sources.harvest_live)


@mcp.tool()
async def prepare_municipal_data() -> dict:
    """Validate raw hashes, reconcile district/population IDs, georeference services and record unmatched/null points. Produce GeoJSON, metric GeoPackage and a categorical district-ID raster; no population interpolation."""
    return await call(analysis.prepare)


@mcp.tool()
async def service_catalog(search: str = "", limit: int = 20) -> dict:
    """Find actual service IDs and names before filtering the municipal inventory. Search is a substring in supplied languages (e.g. 'librar' matches library/libraries). IDs use exact membership, without inferred hierarchy. No matches returns an empty result."""
    return await call(analysis.service_catalog, search, limit)


@mcp.tool()
async def inventory_by_district(service_ids: list[int] | None = None, run_id: str = "agent") -> dict:
    """Count distinct geolocated registry units by exact district polygon and service IDs; attach 2025 population and counts per 10000 residents. Empty IDs selects all units. Save CSV, GeoJSON, offline HTML and evidence. Counts do not establish accessibility or adequacy."""
    return await call(analysis.inventory, service_ids, run_id)


@mcp.tool()
async def read_case_artifact(run_id: str, name: Literal["summary.json", "district_inventory.csv"] = "summary.json") -> dict:
    """Read a result or district table produced by inventory_by_district, with checksum. The run ID is confined to the case workspace. Large maps/GeoJSON remain file artifacts."""
    return await call(analysis.read_artifact, run_id, name)


@mcp.resource("urban://helsinki/recipe")
def municipal_recipe() -> str:
    return json.dumps(sources.recipe(), ensure_ascii=False)


@mcp.resource("urban://helsinki/quality")
def municipal_quality() -> str:
    _, quality = analysis.prepared()
    return json.dumps(quality, ensure_ascii=False)


@mcp.prompt()
def municipal_inventory_task(service_query: str = "public librar") -> str:
    return (
        "Operate through this MCP. Inspect municipal_status, acquire the pinned snapshot if needed, "
        "prepare_municipal_data, and service_catalog for " + repr(service_query) + ". Select actual IDs, "
        "run inventory_by_district, inspect the CSV and report counts, unmatched data, temporal differences "
        "and limitations. Use metric EPSG:3067 for distance operations; district_ids.tif is categorical. "
        "Test missing/invalid inputs without inventing parameters. Do not infer service capacity, "
        "walking accessibility or municipal endorsement. Inspect upstream tool schemas before use."
    )
