"""Reuse the pinned original GDAL MCP; add only municipal vegetation operations."""
from __future__ import annotations

import json
import math
from typing import Literal

import anyio
from fastmcp.exceptions import ToolError
from fastmcp.server.middleware import Middleware
import pyogrio
import rasterio
from pyproj import CRS
from shapely.geometry import shape

from src.server import mcp
from src.config import resolve_path
from src.middleware.paths import validate_path
from . import data, engine
from .interface import public_summary

mcp._mcp_server.instructions = (
    "Urban MCP two-city vegetation case. Start vegetation_status, harvest_vegetation_data(snapshot), "
    "prepare_vegetation_data, vegetation_class_catalog, analyze_vegetation; inspect full CSV/JSON with "
    "read_vegetation_artifact paging. vegetation_compare is threshold sensitivity, never temporal change. "
    "Land cover is WorldCover 2021, population is aggregate 2025 with its own date/rounding. "
    "Report land-share and all-surface denominators, water, NoData, all zone IDs and population reconciliation. "
    "Never infer current canopy, park access, heat/air temperature, NDVI, resident pixel locations or causality. "
    "Original raster_stats means describe numeric class codes, not physical vegetation. raster_query is a "
    "bounding-window extractor, not a polygon-masked zonal count. Use the new operation for exact zone accounting. "
    "Categorical reprojection and overviews require nearest/mode; explicit raster bounds/width/height are not "
    "admitted by the pinned upstream implementation. Raster query extents must stay entirely inside source "
    "bounds; partially outside windows have an upstream transform defect. Primary analysis is compact; "
    "complete zone records are in artifacts with pages of at most 12000 characters. A source water_zone flag "
    "does not establish zero mapped land; use actual valid_land_pixels. Consult schemas and justification prompts."
)


class VegetationPolicy(Middleware):
    async def on_call_tool(self, context, call_next):
        name, args = context.message.name, context.message.arguments or {}
        if name == "raster_reproject":
            params = args.get("params") or args
            if any(params.get(key) is not None for key in ["bounds", "width", "height"]):
                raise ToolError("Explicit bounds/width/height are not admitted: pinned upstream ignores bounds and does not rescale its transform for explicit dimensions. Use resolution instead.")
            if params.get("resampling") not in {"nearest", "mode"}:
                raise ToolError("Categorical land-cover classes require nearest or mode; continuous interpolation invents class values")
        if name == "raster_convert":
            options = args.get("options") or {}
            if options.get("overviews") and options.get("overview_resampling", "average") not in {"nearest", "mode"}:
                raise ToolError("Categorical overviews require explicit nearest or mode resampling")
        if name == "vector_simplify" and args.get("method", "douglas-peucker") != "douglas-peucker":
            raise ToolError("Visvalingam is not admitted: pinned upstream delegates that label to Douglas-Peucker. Use explicit douglas-peucker.")
        if name == "raster_query" and args.get("uri"):
            geometry = args.get("geometry")
            try:
                bounds = list(shape(geometry).bounds) if isinstance(geometry,dict) else geometry
                if isinstance(bounds,list) and len(bounds)==4 and all(isinstance(v,(int,float)) and math.isfinite(v) for v in bounds):
                    path = validate_path(str(resolve_path(args["uri"])))
                    with rasterio.open(path) as source:
                        if bounds[0] < source.bounds.left-1e-9 or bounds[1] < source.bounds.bottom-1e-9 or bounds[2] > source.bounds.right+1e-9 or bounds[3] > source.bounds.top+1e-9:
                            raise ToolError("Raster query extent must stay fully within source bounds: pinned upstream clips partial windows but retains the unclipped transform. Choose an inside-source extent.")
            except (ValueError, TypeError) as exc:
                raise ToolError("Invalid raster query geometry") from exc
        if name in {"vector_buffer", "vector_simplify"} and args.get("uri"):
            path = validate_path(str(resolve_path(args["uri"])))
            info = pyogrio.read_info(path)
            crs = CRS.from_user_input(info["crs"]) if info.get("crs") else None
            if crs is None or not crs.is_projected or not crs.axis_info or any(axis.unit_name not in {"metre", "meter"} for axis in crs.axis_info[:2]):
                raise ToolError("This municipal profile requires a projected CRS in metres; degrees are not metres")
        return await call_next(context)


# FastMCP 2.12.3 exposes the ordered list; add_middleware only appends.
# Reject unsupported profile choices before asking for upstream justification.
# Admitted operations still pass through original path/reflection middleware.
mcp.middleware.insert(0, VegetationPolicy())


async def call(function, *args):
    try:
        return await anyio.to_thread.run_sync(function, *args)
    except (ValueError, OSError, RuntimeError, KeyError) as exc:
        raise ToolError(str(exc)) from exc


@mcp.tool()
async def vegetation_status() -> dict:
    """Discover both cities, exact data/method recipe, input integrity, scientific limits and pending product qualification. Start here."""
    return await call(data.status)


@mcp.tool()
async def harvest_vegetation_data(city: str, mode: Literal["snapshot", "live"] = "snapshot") -> dict:
    """Restore the public city-specific hash-locked snapshot, or acquire a new live WorldCover/municipal observation in a fresh workspace. Does not analyze. Live needs network and preserves original source/failed receipts."""
    return await call(data.harvest, city, mode)


@mcp.tool()
async def prepare_vegetation_data(city: str) -> dict:
    """Verify inputs; nearest-warp categorical source crops into the declared 10 m local metric grid, rasterize zone indices by centre and reject overlaps. Return original-tool input paths and receipts. Population is not rasterized."""
    return await call(engine.prepare, city)


@mcp.tool()
async def vegetation_class_catalog() -> dict:
    """Explain the 11 WorldCover codes, vegetation inclusion (including cropland), water/NoData denominators and limits. Class-code means are not vegetation or canopy measures."""
    return engine.class_catalog()


@mcp.tool()
async def analyze_vegetation(city: str, run_id: str, threshold: float = 0.2) -> dict:
    """Run exact per-zone accounting; return compact complete low-share ID sets, pooled class/denominator metrics, ranking, population reconciliation and artifact references. Full zone records/class counts remain in paged summary/CSV artifacts, avoiding host truncation. Low means land-share strictly below threshold (0..1), an exploratory scenario. Aggregate population in flagged zones is not population lacking access or exposed to heat. Preserves missing population as null; a water_zone source label does not replace observed valid-land eligibility."""
    return public_summary(await call(engine.analyze, city, run_id, threshold))


@mcp.tool()
async def vegetation_compare(city: str, baseline_id: str, scenario_id: str) -> dict:
    """Compare threshold classifications on identical source observations and method. Explicitly list newly/no-longer-below zone IDs and attached population totals. This is sensitivity, not vegetation change over time or causal population impact."""
    return await call(engine.compare, city, baseline_id, scenario_id)


@mcp.tool()
async def read_vegetation_artifact(city: str, run_id: str, name: str = "summary.json", offset: int = 0, limit: int = 8000) -> dict:
    """Read allowlisted summary/zone/class CSV/GeoJSON/report text in pages of at most 12000 characters, with SHA-256. Follow next_offset until null for complete evidence; bounded pages prevent host truncation. PNG returns hash/size, not bytes; no arbitrary paths."""
    return await call(engine.read_artifact, city, run_id, name, offset, limit)


@mcp.tool()
async def render_vegetation_map(city: str, run_id: str) -> dict:
    """Render actual 2021 class pixels, metric zone outlines and lowest valid-land shares with attribution and limits. Returns a PNG receipt in the mounted workspace; not an access, canopy or temperature map."""
    return await call(engine.render, city, run_id)


@mcp.resource("vegetation://case")
def case_recipe() -> dict:
    return data.recipe()


@mcp.resource("vegetation://{city}/manifest")
def manifest(city: str) -> dict:
    return data.verify(city)[1]


@mcp.resource("vegetation://{city}/quality")
def quality(city: str) -> dict:
    return engine.prepared(city)[1]


@mcp.prompt()
def municipal_vegetation_review(city: str) -> str:
    data.city_config(city)
    return f"Review {city}: discover source/classes/limits; restore snapshot and prepare; analyze threshold 0.20 and sensitivity 0.40 on the same raster; read every CSV row and full summaries; compare explicit zone flags, water/NoData, denominator and population reconciliation; render a map; exercise original GDAL tools with justified CRS/resampling and categorical nearest/mode. Report 2021 modeled vegetation and 2025 aggregate population with temporal mismatch, missing/rounded counts and zone boundaries. Never infer park access, current canopy, air temperature, NDVI, individual exposure or causality. State field validation needed before a municipal intervention."
