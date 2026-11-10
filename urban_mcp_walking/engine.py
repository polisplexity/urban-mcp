"""Municipal recipes on OSMnx/NetworkX, with explicit distance accounting."""
from __future__ import annotations

from collections import Counter
from functools import lru_cache
import csv
import hashlib
import importlib.metadata
import io
import json
import math
from pathlib import Path
import re

import geopandas as gpd
import networkx as nx
import osmnx as ox
from shapely.geometry import LineString, Point, mapping

from . import data


def token(value, label="run_id"):
    if not re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9_-]{0,63}", value):
        raise ValueError(f"{label} must be a simple alphanumeric identifier (max 64 characters)")
    return value


def positive(value, label, maximum):
    if not math.isfinite(value) or value <= 0 or value > maximum:
        raise ValueError(f"{label} must be finite, positive and at most {maximum}")


@lru_cache(maxsize=2)
def load(city):
    base, manifest = data.verify(city)
    graph = ox.load_graphml(base / "network.graphml")
    if len(graph) != manifest["nodes"] or graph.number_of_edges() != manifest["edges"]:
        raise ValueError("Graph count mismatch")
    if str(graph.graph["crs"]).lower() != "epsg:4326" or graph.graph["city"] != city:
        raise ValueError("Graph CRS/city mismatch")
    if any(not math.isfinite(d.get("length", -1)) or d.get("length", -1) <= 0 for _, _, d in graph.edges(data=True)):
        raise ValueError("Every admitted edge needs a finite positive length")
    return graph, base, manifest


def graph_info(city):
    graph, _, manifest = load(city)
    return {"city": city, "nodes": len(graph), "edges": graph.number_of_edges(), "crs": str(graph.graph["crs"]),
            "weak_components": nx.number_weakly_connected_components(graph),
            "edge_attributes": sorted({k for _, _, d in graph.edges(data=True) for k in d}),
            "snapshot_manifest_sha256": data.sha(data.root() / "inputs" / city / "manifest.json"),
            "acquired_at": manifest["retrieved_at"], "model": graph.graph["snapshot_model"]}


def catalog(city, amenity="all", core_only=False):
    if amenity not in {"all", "school", "library"}:
        raise ValueError("amenity must be all, school or library")
    _, base, _ = load(city)
    cfg = data.city_config(city)
    features = gpd.read_file(base / "features.geojson").to_crs(cfg["analysis_crs"])
    core = gpd.GeoSeries([data.study_polygon(city)], crs=4326).to_crs(cfg["analysis_crs"]).iloc[0]
    records = []
    for _, row in features.iterrows():
        geometry = row.geometry
        if geometry is None or geometry.is_empty or not geometry.is_valid:
            # Retain rejected records for an explicit quality denominator.
            point = None
        else:
            point = geometry.representative_point()
        inside = bool(point is not None and core.covers(point))
        kind = str(row.get("amenity", "unknown"))
        if (amenity != "all" and kind != amenity) or (core_only and not inside):
            continue
        location = gpd.GeoSeries([point], crs=cfg["analysis_crs"]).to_crs(4326).iloc[0] if point is not None else None
        def text(key, default=""):
            value = row.get(key)
            return str(value) if value is not None and not (isinstance(value, float) and math.isnan(value)) else default
        records.append({"feature_id": text("element") + "/" + text("id"), "name": text("name", "Unnamed mapped object"),
                        "amenity": kind, "access": text("access", "unknown"), "in_core": inside,
                        "geometry_type": geometry.geom_type if geometry is not None else None,
                        "longitude": location.x if location is not None else None, "latitude": location.y if location is not None else None})
    return {"city": city, "count": len(records), "features": sorted(records, key=lambda f: f["feature_id"]),
            "point_method": "Representative point in local projected CRS, then EPSG:4326; not a verified entrance"}


def snap(city, longitude, latitude):
    if not math.isfinite(longitude) or not math.isfinite(latitude) or not -180 <= longitude <= 180 or not -90 <= latitude <= 90:
        raise ValueError("longitude/latitude must be finite WGS84 coordinates")
    graph, _, _ = load(city)
    # Refuse remote locations instead of snapping arbitrary coordinates across the planet.
    if not data.study_polygon(city, buffered=True).covers(Point(longitude, latitude)):
        raise ValueError("coordinate is outside the buffered study area")
    node, distance = ox.distance.nearest_nodes(graph, X=longitude, Y=latitude, return_dist=True)
    limit = data.recipe()["max_snap_m"]
    return {"node": int(node), "distance_m": float(distance), "accepted": bool(distance <= limit), "max_snap_m": limit,
            "longitude": float(graph.nodes[node]["x"]), "latitude": float(graph.nodes[node]["y"])}


@lru_cache(maxsize=2)
def prepare(city):
    features = catalog(city)["features"]
    counts = Counter(f["amenity"] for f in features)
    buffered = data.study_polygon(city, buffered=True)
    eligible = [f for f in features if f["longitude"] is not None and buffered.covers(Point(f["longitude"], f["latitude"]))]
    graph, _, _ = load(city)
    nodes, distances = ox.distance.nearest_nodes(graph, X=[f["longitude"] for f in eligible], Y=[f["latitude"] for f in eligible], return_dist=True)
    for feature in features:
        feature["snap"] = None
    for feature, node, distance in zip(eligible, nodes, distances):
        feature["snap"] = {"node": int(node), "distance_m": float(distance), "accepted": bool(distance <= data.recipe()["max_snap_m"]),
                           "max_snap_m": data.recipe()["max_snap_m"], "longitude": float(graph.nodes[node]["x"]), "latitude": float(graph.nodes[node]["y"])}
    origins = [f for f in features if f["amenity"] == "school" and f["in_core"]]
    destinations = [f for f in features if f["amenity"] == "library" and f["access"] not in {"no", "private"}]
    accepted_destinations = [f for f in destinations if f["snap"] and f["snap"]["accepted"]]
    if not origins or not accepted_destinations:
        raise ValueError("The case needs nonempty core school objects and accepted library destinations")
    return origins, accepted_destinations, {"mapped_features_by_amenity": dict(counts), "core_school_objects": len(origins),
            "buffer_library_objects": len(destinations), "accepted_library_objects": len(accepted_destinations),
            "library_objects_rejected_for_access": sum(f["amenity"] == "library" and f["access"] in {"no", "private"} for f in features),
            "school_objects_rejected_for_snap": sum(not f["snap"] or not f["snap"]["accepted"] for f in origins),
            "library_objects_rejected_for_snap": len(destinations) - len(accepted_destinations),
            "invalid_geometries": sum(f["longitude"] is None for f in features),
            "representative_points_outside_buffer": sum(f["longitude"] is not None and not buffered.covers(Point(f["longitude"], f["latitude"])) for f in features),
            "unknown_library_access": sum(f["access"] == "unknown" for f in accepted_destinations)}


def close_links(graph, closures):
    if len(closures) > 10:
        raise ValueError("At most ten link closures per scenario")
    result = graph.copy() if closures else graph
    removed = []
    for link in closures:
        if set(link) != {"u", "v"} or not isinstance(link["u"], int) or not isinstance(link["v"], int):
            raise ValueError("Each closure needs integer u and v node IDs")
        u, v = link["u"], link["v"]
        edges = [(a, b, k) for a, b in {(u, v), (v, u)} if graph.has_edge(a, b) for k in graph[a][b]]
        if not edges:
            raise ValueError("closure link does not exist in the input graph")
        for edge in edges:
            if result.has_edge(*edge):
                result.remove_edge(*edge)
                removed.append(list(edge))
    return result, removed


def keyed_route(graph, nodes):
    edges = []
    for u, v in zip(nodes[:-1], nodes[1:]):
        key = min(graph[u][v], key=lambda k: (graph[u][v][k]["length"], k))
        edge = graph[u][v][key]
        edges.append({"u": int(u), "v": int(v), "key": int(key), "length_m": float(edge["length"])})
    return edges


def solve(city, graph, origins, destinations, threshold_m, speed_kph):
    # Add destination connector costs to a virtual sink. This includes both
    # endpoint offsets in nearest-library selection instead of choosing by
    # network distance and adding offsets only after selection.
    sink = "urban-mcp-library-sink"
    augmented = graph.copy()
    by_node = {}
    for destination in destinations:
        node = destination["snap"]["node"]
        if node not in by_node or (destination["snap"]["distance_m"], destination["feature_id"]) < (by_node[node]["snap"]["distance_m"], by_node[node]["feature_id"]):
            by_node[node] = destination
    for node, destination in by_node.items():
        augmented.add_edge(node, sink, length=destination["snap"]["distance_m"])
    distances, paths = nx.single_source_dijkstra(augmented.reverse(copy=False), sink, weight="length")
    rows, routes = [], []
    for origin in origins:
        row = {"origin_id": origin["feature_id"], "origin_name": origin["name"], "status": "snap_rejected",
               "destination_id": None, "destination_name": None, "network_m": None, "origin_snap_m": origin["snap"]["distance_m"] if origin["snap"] else None,
               "destination_snap_m": None, "total_m": None, "estimated_minutes": None, "within_threshold": False}
        origin_snap = origin["snap"]
        if origin_snap and origin_snap["accepted"]:
            node = origin_snap["node"]
            row["status"] = "unreachable"
            if node in distances:
                nodes = list(reversed(paths[node]))[:-1]
                destination = by_node[nodes[-1]]
                edges = keyed_route(graph, nodes)
                length = sum(e["length_m"] for e in edges)
                total = length + origin_snap["distance_m"] + destination["snap"]["distance_m"]
                if not math.isclose(total, distances[node] + origin_snap["distance_m"], abs_tol=1e-6, rel_tol=0):
                    raise ValueError("Route edge accounting disagrees with the shortest-path solver")
                row.update(status="routed", destination_id=destination["feature_id"], destination_name=destination["name"],
                           network_m=length, destination_snap_m=destination["snap"]["distance_m"], total_m=total,
                           estimated_minutes=total / (speed_kph * 1000 / 60), within_threshold=total <= threshold_m)
                coordinates = [[graph.nodes[n]["x"], graph.nodes[n]["y"]] for n in nodes]
                # Zero-edge routes remain explicit point geometries.
                geometry = LineString(coordinates) if len(coordinates) > 1 else Point(coordinates[0])
                routes.append({"type": "Feature", "geometry": mapping(geometry), "properties": {"origin_id": origin["feature_id"],
                               "destination_id": destination["feature_id"], "network_m": length, "nodes": [int(n) for n in nodes], "edges": edges}})
        rows.append(row)
    return rows, routes


def analyze(city, run_id, threshold_m=1200.0, speed_kph=4.8, closures=None):
    token(run_id)
    positive(threshold_m, "threshold_m", data.recipe()["network_buffer_m"] - data.recipe()["max_snap_m"])
    positive(speed_kph, "speed_kph", 10)
    closures = closures or []
    graph, _, manifest = load(city)
    origins, destinations, quality = prepare(city)
    scenario_graph, removed = close_links(graph, closures)
    rows, routes = solve(city, scenario_graph, origins, destinations, threshold_m, speed_kph)
    within = sum(r["within_threshold"] for r in rows)
    counts = Counter(r["status"] for r in rows)
    edges_used = Counter((min(e["u"], e["v"]), max(e["u"], e["v"])) for route in routes for e in route["properties"]["edges"])
    candidate = sorted(edges_used, key=lambda pair: (-edges_used[pair], pair))[0] if edges_used else None
    summary = {"city": city, "run_id": run_id, "question": "Mapped school objects in the central study disk with a modeled library route within an explicit distance threshold",
               "threshold_m": threshold_m, "walking_speed_kph": speed_kph, "core_radius_m": data.recipe()["core_radius_m"],
               "network_buffer_m": data.recipe()["network_buffer_m"], "denominator": "mapped OSM school objects whose representative point is in the study core",
               "origin_count": len(rows), "routed_count": counts["routed"], "within_threshold": within,
               "outside_threshold": counts["routed"] - within, "unreachable": counts["unreachable"], "snap_rejected": counts["snap_rejected"],
               "within_share_of_all_origins": within / len(rows), "quality": quality, "graph": graph_info(city),
               "closures": closures, "removed_directed_edges": removed,
               "suggested_closure": {"u": candidate[0], "v": candidate[1], "baseline_routes_using_link": edges_used[candidate]} if candidate else None,
               "source": {"attribution": manifest["attribution"], "license": manifest["license"], "license_url": manifest["license_url"],
                          "manifest_sha256": data.sha(data.root() / "inputs" / city / "manifest.json")},
               "implementation_sha256": data.sha(Path(__file__)),
               "runtime": {name: importlib.metadata.version(name) for name in ["osmnx", "networkx", "fastmcp", "geopandas", "shapely", "pyproj"]},
               "limits": data.recipe()["limits"],
               "artifacts": ["summary.json", "accessibility.csv", "routes.geojson", "report.md"]}
    out = data.root() / "results" / city / run_id
    if out.exists():
        raise ValueError("run_id already exists; choose a new identifier to preserve evidence")
    out.mkdir(parents=True)
    data.dump(out / "summary.json", summary)
    with (out / "accessibility.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    data.dump(out / "routes.geojson", {"type": "FeatureCollection", "attribution": manifest["attribution"], "license": manifest["license_url"], "features": routes})
    report = f"# {data.city_config(city)['name']}: school-to-library walking experiment\n\n{within} of {len(rows)} mapped school objects in the central study disk have an accepted modeled library route within {threshold_m:g} m. {counts['unreachable']} are unreachable on this snapshot and {counts['snap_rejected']} fail the snap rule. This denominator is not residents or pupils.\n\n" + "\n".join("- " + limit for limit in summary["limits"]) + "\n\n" + manifest["attribution"] + ". Data: ODbL-1.0.\n"
    (out / "report.md").write_text(report, encoding="utf-8", newline="\n")
    return summary


def artifact(city, run_id, name="summary.json", offset=0, limit=20000):
    data.city_config(city)
    token(run_id)
    if name not in {"summary.json", "accessibility.csv", "routes.geojson", "report.md", "map.png", "network.graphml"}:
        raise ValueError("artifact name is not allowed")
    if not isinstance(offset, int) or not isinstance(limit, int) or offset < 0 or not 1 <= limit <= 50000:
        raise ValueError("offset must be nonnegative and limit must be 1..50000")
    path = data.root() / "results" / city / run_id / name
    if name in {"map.png", "network.graphml"}:
        return {"name": name, "bytes": path.stat().st_size, "sha256": data.sha(path), "note": "Binary/bulk artifact remains in the mounted workspace"}
    content = path.read_text(encoding="utf-8")
    return {"name": name, "text": content[offset:offset+limit], "characters": len(content), "next_offset": offset + limit if len(content) > offset + limit else None,
            "sha256": data.sha(path)}


def compare(city, baseline_id, scenario_id):
    baseline = json.loads(artifact(city, baseline_id)["text"])
    scenario = json.loads(artifact(city, scenario_id)["text"])
    if baseline["closures"] or not scenario["closures"]:
        raise ValueError("Compare an unmodified baseline with a declared closure scenario")
    if any(baseline[key] != scenario[key] for key in ["threshold_m", "walking_speed_kph", "source", "implementation_sha256"]):
        raise ValueError("Scenario inputs, method, speed and threshold must match baseline")
    def read(run):
        return {row["origin_id"]: row for row in csv.DictReader(io.StringIO(artifact(city, run, "accessibility.csv", limit=50000)["text"]))}
    before, after = read(baseline_id), read(scenario_id)
    affected = []
    for key, row in before.items():
        nxt = after[key]
        if row["status"] == "routed":
            if nxt["status"] == "routed":
                difference = float(nxt["total_m"]) - float(row["total_m"])
                if difference < -1e-6:
                    raise ValueError("Removing links unexpectedly shortened a shortest route")
                if difference > 1e-6:
                    affected.append({"origin_id": key, "extra_distance_m": difference, "lost_reachability": False})
            else:
                affected.append({"origin_id": key, "extra_distance_m": None, "lost_reachability": True})
    return {"city": city, "baseline_id": baseline_id, "scenario_id": scenario_id,
            "within_before": baseline["within_threshold"], "within_after": scenario["within_threshold"],
            "affected_origins": affected, "affected_count": len(affected), "removed_directed_edges": scenario["removed_directed_edges"],
            "interpretation": "Hypothetical removal of both directions and every parallel edge for each node pair; not an observed closure"}


def route(city, origin_id, destination_id, k=1):
    if not 1 <= k <= 3:
        raise ValueError("k must be 1..3")
    graph, _, _ = load(city)
    features = {f["feature_id"]: f for f in catalog(city)["features"]}
    if origin_id not in features or destination_id not in features:
        raise ValueError("Unknown feature_id; inspect the feature catalog")
    a, b = features[origin_id], features[destination_id]
    start, end = snap(city, a["longitude"], a["latitude"]), snap(city, b["longitude"], b["latitude"])
    if not start["accepted"] or not end["accepted"]:
        raise ValueError("Route endpoint exceeds max_snap_m")
    try:
        paths = list(ox.routing.k_shortest_paths(graph, start["node"], end["node"], k, weight="length")) if k > 1 else [nx.shortest_path(graph, start["node"], end["node"], weight="length")]
    except nx.NetworkXNoPath:
        return {"city": city, "paths": [], "status": "unreachable"}
    results = []
    for nodes in paths:
        edges = keyed_route(graph, nodes)
        network = sum(e["length_m"] for e in edges)
        results.append({"nodes": [int(n) for n in nodes], "edges": edges, "network_m": network,
                        "origin_snap_m": start["distance_m"], "destination_snap_m": end["distance_m"], "total_m": network + start["distance_m"] + end["distance_m"]})
    return {"city": city, "status": "routed", "paths": results}


def network_stats(city):
    graph, _, _ = load(city)
    bearing = ox.bearing.add_edge_bearings(graph.copy())
    return {"city": city, "nodes": len(graph), "directed_edges": graph.number_of_edges(),
            "weak_components": nx.number_weakly_connected_components(graph),
            "largest_weak_component_nodes": len(max(nx.weakly_connected_components(graph), key=len)),
            "orientation_entropy_nats": float(ox.bearing.orientation_entropy(bearing)),
            "directed_length_sum_m": sum(d["length"] for _, _, d in graph.edges(data=True)),
            "caution": "Unsimplified graph; nodes include shape points. Directed length counts reciprocal walking edges. These are not unique street lengths or intersection counts."}


def isochrone(city, longitude, latitude, budget_m=1200.0, sample_limit=20):
    positive(budget_m, "budget_m", 1800)
    if not 1 <= sample_limit <= 100:
        raise ValueError("sample_limit must be 1..100")
    graph, _, _ = load(city)
    nearest = snap(city, longitude, latitude)
    if not nearest["accepted"]:
        raise ValueError("Origin exceeds max_snap_m")
    remaining = budget_m - nearest["distance_m"]
    distances = nx.single_source_dijkstra_path_length(graph, nearest["node"], cutoff=remaining, weight="length") if remaining >= 0 else {}
    return {"city": city, "budget_m": budget_m, "origin_snap_m": nearest["distance_m"], "reachable_nodes": len(distances),
            "max_total_m": max(distances.values()) + nearest["distance_m"] if distances else None,
            "sample_node_ids": sorted(int(n) for n in distances)[:sample_limit],
            "interpretation": "Reachable graph nodes after subtracting the origin connector. Not a coverage polygon, resident estimate or continuous-edge isochrone."}


def export_graph(city, run_id):
    token(run_id)
    graph, _, _ = load(city)
    out = data.root() / "results" / city / run_id
    out.mkdir(parents=True, exist_ok=True)
    path = out / "network.graphml"
    if path.exists():
        raise ValueError("Graph export already exists")
    ox.save_graphml(graph, path)
    return artifact(city, run_id, "network.graphml")


def render(city, run_id):
    token(run_id)
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.collections import LineCollection
    from matplotlib.lines import Line2D
    graph, _, _ = load(city)
    route_features = json.loads((data.root() / "results" / city / run_id / "routes.geojson").read_text(encoding="utf-8"))["features"]
    cfg = data.city_config(city)
    nodes = gpd.GeoDataFrame({"node": list(graph.nodes)}, geometry=[Point(d["x"], d["y"]) for _, d in graph.nodes(data=True)], crs=4326).to_crs(cfg["analysis_crs"])
    xy = {int(row.node): (row.geometry.x, row.geometry.y) for row in nodes.itertuples()}
    fig, ax = plt.subplots(figsize=(9, 9))
    ax.add_collection(LineCollection([[xy[u], xy[v]] for u, v in graph.edges()], colors="#d3d9de", linewidths=0.35))
    for feature in route_features:
        points = [xy[n] for n in feature["properties"]["nodes"]]
        if len(points) > 1:
            ax.plot(*zip(*points), color="#166c67", linewidth=1.2, alpha=0.75)
    core = gpd.GeoSeries([data.study_polygon(city)], crs=4326).to_crs(cfg["analysis_crs"])
    core.boundary.plot(ax=ax, color="#be6a25", linewidth=1.5)
    origins, destinations, _ = prepare(city)
    for features, color, marker, size in [(origins, "#823741", "o", 13), (destinations, "#253f72", "^", 35)]:
        points = gpd.GeoSeries([Point(f["longitude"], f["latitude"]) for f in features if f["longitude"] is not None], crs=4326).to_crs(cfg["analysis_crs"])
        ax.scatter(points.x, points.y, color=color, marker=marker, s=size, zorder=4)
    ax.legend(handles=[Line2D([], [], color="#be6a25", label="Study core"), Line2D([], [], color="#166c67", label="Modeled route"),
                       Line2D([], [], color="#823741", marker="o", linestyle="", label="Mapped school object"),
                       Line2D([], [], color="#253f72", marker="^", linestyle="", label="Accepted library object")], loc="lower right", fontsize=8)
    ax.autoscale()
    ax.set_aspect("equal")
    ax.set_title(cfg["name"] + " · mapped school-to-library routes\nCentral 2 km study core with buffered walking graph")
    ax.set_xlabel("Easting (m) · " + cfg["analysis_crs"])
    ax.set_ylabel("Northing (m)")
    fig.text(0.1, 0.02, "© OpenStreetMap contributors · ODbL-1.0 · openstreetmap.org/copyright\nGeneral walking model; not verified entrances or wheelchair accessibility", fontsize=8)
    path = data.root() / "results" / city / run_id / "map.png"
    if path.exists():
        raise ValueError("Map already exists")
    fig.savefig(path, dpi=140, bbox_inches="tight")
    plt.close(fig)
    return artifact(city, run_id, "map.png")
