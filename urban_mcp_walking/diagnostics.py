"""Evidence annotations only: no routing, geographic inference or agent dependency."""
from collections import Counter
from itertools import combinations
import math


def normalize_links(links):
    """Closure pairs remove both directions and every parallel key."""
    if not isinstance(links, list) or len(links) > 10:
        raise ValueError("closed_links must be a list of at most ten node pairs")
    pairs = set()
    for link in links:
        if not isinstance(link, dict) or set(link) != {"u", "v"} or any(type(link[k]) is not int for k in ["u", "v"]):
            raise ValueError("Each closed link needs integer u and v node IDs")
        pairs.add(tuple(sorted((link["u"], link["v"]))))
    return [{"u": u, "v": v} for u, v in sorted(pairs)]


def link_membership(edges, closed_links):
    pairs = {(link["u"], link["v"]) for link in normalize_links(closed_links)}
    used = [dict(edge) for edge in edges if tuple(sorted((edge["u"], edge["v"]))) in pairs]
    return {"uses_closed_link": bool(used), "closed_edges_used": used,
            "avoids_all_declared_closed_links": not used}


def annotate_paths(paths, closed_links):
    links = normalize_links(closed_links)
    annotated = [{**path, "rank": rank, **link_membership(path["edges"], links)} for rank, path in enumerate(paths, 1)]
    overlap = []
    for a, b in combinations(annotated, 2):
        directed = lambda path: {(e["u"], e["v"], e["key"]) for e in path["edges"]}
        physical = lambda path: {tuple(sorted((e["u"], e["v"]))) for e in path["edges"]}
        shared_edges = sorted(directed(a) & directed(b))
        shared_links = sorted(physical(a) & physical(b))
        overlap.append({"path_ranks": [a["rank"], b["rank"]], "shared_directed_keyed_edge_count": len(shared_edges),
                        "shared_physical_link_count": len(shared_links), "directed_keyed_edge_disjoint": not shared_edges,
                        "physical_link_disjoint": not shared_links})
    return {"paths": annotated, "closed_links": links, "closure_links_checked": bool(links), "path_overlap": overlap,
            "path_ranks_avoiding_declared_closed_links": [p["rank"] for p in annotated if not p["uses_closed_link"]],
            "interpretation": "These are paths on the original graph, annotated against declared bidirectional/all-parallel link closures. k-shortest paths may overlap. An avoiding path is not a verified itinerary. Use the separately solved closure scenario for actual modeled rerouting."}


def _index_rows(rows, threshold_m):
    indexed = {}
    for raw in rows:
        row = dict(raw)
        key = row["origin_id"]
        if key in indexed:
            raise ValueError("Duplicate origin_id in accessibility rows")
        if row["status"] not in {"routed", "unreachable", "snap_rejected"}:
            raise ValueError("Unknown accessibility status")
        within = row["within_threshold"]
        if within not in {True, False, "True", "False"}:
            raise ValueError("within_threshold must be an explicit boolean")
        row["within_threshold"] = within is True or within == "True"
        total = row["total_m"]
        row["total_m"] = float(total) if total not in {None, ""} else None
        if row["status"] == "routed":
            if row["total_m"] is None or not math.isfinite(row["total_m"]) or row["total_m"] < 0:
                raise ValueError("Routed row needs a finite nonnegative total_m")
            if row["within_threshold"] != (row["total_m"] <= threshold_m):
                raise ValueError("Threshold flag disagrees with route distance")
            if not row["destination_id"]:
                raise ValueError("Routed row needs a destination_id")
        elif row["total_m"] is not None or row["within_threshold"]:
            raise ValueError("Unrouted row cannot claim distance or threshold coverage")
        indexed[key] = row
    return indexed


def _index_routes(routes, rows):
    indexed = {}
    for route in routes:
        properties = route["properties"]
        key = properties["origin_id"]
        if key in indexed:
            raise ValueError("Duplicate origin_id in route export")
        if key not in rows or rows[key]["status"] != "routed" or properties["destination_id"] != rows[key]["destination_id"]:
            raise ValueError("Route export and accessibility rows disagree")
        indexed[key] = properties
    if set(indexed) != {key for key, row in rows.items() if row["status"] == "routed"}:
        raise ValueError("Route export must contain exactly the routed origins")
    return indexed


def compare_records(before_rows, after_rows, before_routes, after_routes, closed_links, threshold_m):
    """Join every origin explicitly, including unchanged and unrouted records."""
    before, after = _index_rows(before_rows, threshold_m), _index_rows(after_rows, threshold_m)
    if not before or set(before) != set(after):
        raise ValueError("Baseline and scenario must contain the same nonempty origin set")
    routes_before = _index_routes(before_routes, before)
    routes_after = _index_routes(after_routes, after)
    links = normalize_links(closed_links)
    schools = []
    for key in sorted(before):
        a, b = before[key], after[key]
        if a["origin_name"] != b["origin_name"] or (a["status"] == "snap_rejected") != (b["status"] == "snap_rejected"):
            raise ValueError("Origin identity and snap eligibility must not change under closure")
        if a["status"] == "unreachable" and b["status"] == "routed":
            raise ValueError("Removing links cannot create reachability")
        difference = b["total_m"] - a["total_m"] if a["status"] == b["status"] == "routed" else None
        if difference is not None and difference < -1e-6:
            raise ValueError("Removing links unexpectedly shortened a shortest route")
        state = lambda row: ("within" if row["within_threshold"] else "outside") if row["status"] == "routed" else row["status"]
        state_before, state_after = state(a), state(b)
        used_before = link_membership(routes_before.get(key, {}).get("edges", []), links)
        used_after = link_membership(routes_after.get(key, {}).get("edges", []), links)
        if used_after["uses_closed_link"]:
            raise ValueError("Scenario route uses a removed link")
        lost = a["status"] == "routed" and b["status"] == "unreachable"
        changed_destination = a["destination_id"] != b["destination_id"]
        schools.append({"origin_id": key, "origin_name": a["origin_name"], "status_before": a["status"], "status_after": b["status"],
                        "destination_id_before": a["destination_id"] or None, "destination_id_after": b["destination_id"] or None,
                        "total_m_before": a["total_m"], "total_m_after": b["total_m"],
                        "within_before": a["within_threshold"], "within_after": b["within_threshold"],
                        "threshold_transition": state_before + "_to_" + state_after,
                        "crossed_threshold": a["status"] == b["status"] == "routed" and a["within_threshold"] != b["within_threshold"],
                        "left_threshold_coverage": a["within_threshold"] and not b["within_threshold"],
                        "gained_threshold_coverage": not a["within_threshold"] and b["within_threshold"],
                        "extra_distance_m": difference, "lost_reachability": lost, "destination_changed": changed_destination,
                        "affected": lost or (difference is not None and difference > 1e-6) or changed_destination,
                        "baseline_route_uses_closed_link": used_before["uses_closed_link"], "baseline_closed_edges_used": used_before["closed_edges_used"],
                        "scenario_route_uses_closed_link": used_after["uses_closed_link"]})
    affected = [row for row in schools if row["affected"]]
    return {"diagnostics_version": "2.0", "threshold_m": threshold_m, "closed_links": links,
            "origin_count": len(schools), "affected_count": len(affected),
            "crossed_threshold_origin_ids": [row["origin_id"] for row in schools if row["crossed_threshold"]],
            "affected_still_within_origin_ids": [row["origin_id"] for row in affected if row["within_before"] and row["within_after"]],
            "left_threshold_coverage_origin_ids": [row["origin_id"] for row in schools if row["left_threshold_coverage"]],
            "newly_unreachable_origin_ids": [row["origin_id"] for row in schools if row["lost_reachability"]],
            "transition_counts": dict(Counter(row["threshold_transition"] for row in schools)),
            "baseline_routes_using_closed_link_origin_ids": [row["origin_id"] for row in schools if row["baseline_route_uses_closed_link"]],
            "scenario_routes_using_closed_link_origin_ids": [row["origin_id"] for row in schools if row["scenario_route_uses_closed_link"]],
            "threshold_crossings": [row for row in schools if row["crossed_threshold"]],
            "affected_origins": affected, "schools": schools}
