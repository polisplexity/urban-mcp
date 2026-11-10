"""Native oracles plus every exposed operation over a real MCP subprocess."""
from __future__ import annotations

import csv
import json
import math
import os
from pathlib import Path
import sys
import time
from uuid import uuid4

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import networkx as nx
import numpy as np
import osmnx as ox
from pydantic import AnyUrl

from . import data, engine


def payload(result):
    value = result.structuredContent
    if value is None:
        value = json.loads(next(c.text for c in result.content if hasattr(c, "text")))
    return value["result"] if isinstance(value, dict) and set(value) == {"result"} else value


async def run(city):
    prefix = "check-" + uuid4().hex[:8]
    evidence = {"city": city, "transport": "MCP SDK stdio subprocess", "checks": [], "tools_exercised": [], "failures": []}
    out = data.root() / "evidence" / city
    out.mkdir(parents=True, exist_ok=True)

    def check(name, condition, detail=None):
        passed = bool(condition)
        evidence["checks"].append({"name": name, "passed": passed, "detail": detail})
        if not passed:
            evidence["failures"].append(name)
        print(json.dumps({"check": name, "passed": passed}), flush=True)

    graph, base, manifest = engine.load(city)
    info = engine.graph_info(city)
    check("nonempty graph with disconnected components retained", len(graph) > 100 and graph.number_of_edges() > 100 and info["weak_components"] > 0, info)
    native = engine.analyze(city, prefix + "-native")
    origins, destinations, quality = engine.prepare(city)
    rows = list(csv.DictReader((data.root() / "results" / city / native["run_id"] / "accessibility.csv").open(encoding="utf-8")))
    check("nonempty municipal denominator and exact row accounting", len(rows) == native["origin_count"] > 0 and native["origin_count"] == native["routed_count"] + native["unreachable"] + native["snap_rejected"])
    oracle_errors = []
    for origin, row in zip(origins, rows):
        if not origin["snap"] or not origin["snap"]["accepted"]:
            if row["status"] != "snap_rejected":
                oracle_errors.append(origin["feature_id"])
            continue
        # Independent direction and algorithm: forward per-origin Dijkstra,
        # enumerate every library connector, no virtual sink/reversed graph.
        distances = nx.single_source_dijkstra_path_length(graph, origin["snap"]["node"], weight="length")
        costs = [distances[d["snap"]["node"]] + d["snap"]["distance_m"] + origin["snap"]["distance_m"] for d in destinations if d["snap"]["node"] in distances]
        if not costs:
            correct = row["status"] == "unreachable"
        else:
            correct = row["status"] == "routed" and math.isclose(min(costs), float(row["total_m"]), abs_tol=1e-6, rel_tol=0) and (row["within_threshold"] == "True") == (min(costs) <= native["threshold_m"])
        if not correct:
            oracle_errors.append(origin["feature_id"])
    check("every municipal row matches independent forward-Dijkstra/library enumeration", not oracle_errors, {"origins_checked": len(rows), "mismatches": oracle_errors})
    closure = native["suggested_closure"]
    if closure is None:
        raise ValueError("No nonzero route available for the closure experiment")
    link = {key: closure[key] for key in ["u", "v"]}
    changed, removed = engine.close_links(graph, [link])
    check("closure removes every parallel edge in both directions and preserves input", len(removed) >= 1 and not changed.has_edge(link["u"], link["v"]) and not changed.has_edge(link["v"], link["u"]) and graph.has_edge(link["u"], link["v"]))
    native_scenario = engine.analyze(city, prefix + "-native-scenario", closures=[link])
    native_comparison = engine.compare(city, native["run_id"], native_scenario["run_id"])
    check("real-city closure produces a measurable detour or reachability loss", native_comparison["affected_count"] > 0, native_comparison)
    check("closure cannot increase threshold coverage", native_scenario["within_threshold"] <= native["within_threshold"])

    # A deliberately synthetic regression separates keyed-edge accounting from
    # the city evidence: key 0 is longer and key 7 is the shortest parallel edge.
    tiny = nx.MultiDiGraph()
    tiny.add_edge(1, 2, key=0, length=90.0)
    tiny.add_edge(1, 2, key=7, length=10.0)
    keyed = engine.keyed_route(tiny, [1, 2])
    check("synthetic regression: actual minimum parallel-edge key is used", keyed == [{"u": 1, "v": 2, "key": 7, "length_m": 10.0}])

    params = StdioServerParameters(command=sys.executable, args=["-m", "urban_mcp_walking", "serve"], env=dict(os.environ))
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as client:
            initialized = await client.initialize()
            evidence["protocol_version"] = initialized.protocolVersion
            tools = (await client.list_tools()).tools
            data.dump(out / "mcp-tools.json", [t.model_dump(mode="json") for t in tools])
            tool_names = {t.name for t in tools}

            async def invoke(name, arguments=None, error=None):
                started = time.monotonic()
                response = await client.call_tool(name, arguments or {})
                evidence["tools_exercised"].append(name)
                message = " ".join(getattr(c, "text", "") for c in response.content)
                check(name + (" / expected rejection" if error else " / success"), response.isError and error in message if error else not response.isError,
                      {"seconds": round(time.monotonic() - started, 3), "error": message if response.isError else None})
                if response.isError:
                    if not error:
                        raise RuntimeError(message)
                    return None
                return payload(response)

            await invoke("walking_status")
            await invoke("harvest_walking_data", {"city": city, "mode": "snapshot"})
            remote_info = await invoke("walking_graph_info", {"city": city})
            check("native/MCP graph identity", remote_info == info)
            catalog = await invoke("walking_feature_catalog", {"city": city, "amenity": "school", "core_only": True})
            check("native/MCP feature identity", catalog == engine.catalog(city, "school", True))
            selected = next(o for o in origins if o["snap"] and o["snap"]["accepted"])
            position = {"city": city, "longitude": selected["longitude"], "latitude": selected["latitude"]}
            snapped = await invoke("walking_snap", position)
            check("native/MCP snap distance and node identity", snapped == selected["snap"])
            ys = np.array([d["y"] for _, d in graph.nodes(data=True)])
            xs = np.array([d["x"] for _, d in graph.nodes(data=True)])
            brute = ox.distance.great_circle(selected["latitude"], selected["longitude"], ys, xs)
            check("nearest-node result agrees with brute-force great-circle distances", math.isclose(float(brute.min()), snapped["distance_m"], abs_tol=1e-6, rel_tol=0))
            node = await invoke("walking_node", {"city": city, "node_id": snapped["node"]})
            check("node lookup is original graph data", node["attributes"] == dict(graph.nodes[snapped["node"]]))
            edge = await invoke("walking_edge", {"city": city, "u": link["u"], "v": link["v"], "key": min(graph[link["u"]][link["v"]])})
            check("edge lookup retains original length", edge["attributes"]["length"] == graph[edge["u"]][edge["v"]][edge["key"]]["length"])
            baseline = await invoke("walking_accessibility", {"city": city, "run_id": prefix + "-mcp"})
            def semantic(result):
                return {k: v for k, v in result.items() if k != "run_id"}
            check("native/MCP baseline summaries identical", semantic(baseline) == semantic(native))
            csv_remote = await invoke("walking_read_artifact", {"city": city, "run_id": baseline["run_id"], "name": "accessibility.csv", "limit": 50000})
            check("native/MCP accessibility CSV exactly identical", csv_remote["sha256"] == data.sha(data.root() / "results" / city / native["run_id"] / "accessibility.csv") and csv_remote["next_offset"] is None)
            routes_remote = await invoke("walking_read_artifact", {"city": city, "run_id": baseline["run_id"], "name": "routes.geojson", "limit": 100})
            check("route export pagination is bounded and agrees with native bytes", len(routes_remote["text"]) == 100 and routes_remote["next_offset"] == 100 and routes_remote["sha256"] == data.sha(data.root() / "results" / city / native["run_id"] / "routes.geojson"))
            scenario = await invoke("walking_accessibility", {"city": city, "run_id": prefix + "-mcp-scenario", "closures": [link]})
            check("native/MCP closure summaries identical", semantic(scenario) == semantic(native_scenario))
            comparison = await invoke("walking_compare", {"city": city, "baseline_id": baseline["run_id"], "scenario_id": scenario["run_id"]})
            check("native/MCP detour lists identical", comparison["affected_origins"] == native_comparison["affected_origins"])
            routed_row = next(r for r in rows if r["status"] == "routed" and float(r["network_m"]) > 0)
            alternatives = await invoke("walking_route", {"city": city, "origin_id": routed_row["origin_id"], "destination_id": routed_row["destination_id"], "k": 2})
            check("alternative paths have nondecreasing correct keyed costs", len(alternatives["paths"]) == 2 and alternatives["paths"][0]["network_m"] <= alternatives["paths"][1]["network_m"] and all(math.isclose(p["network_m"], sum(e["length_m"] for e in p["edges"]), abs_tol=1e-6, rel_tol=0) for p in alternatives["paths"]))
            check("single-route total matches municipal CSV", math.isclose(alternatives["paths"][0]["total_m"], float(routed_row["total_m"]), abs_tol=1e-6, rel_tol=0))
            iso = await invoke("walking_isochrone", position)
            forward = nx.single_source_dijkstra_path_length(graph, snapped["node"], cutoff=1200 - snapped["distance_m"], weight="length")
            check("isochrone node count and sample match native cutoff including snap", iso["reachable_nodes"] == len(forward) > 0 and iso["sample_node_ids"] == sorted(forward)[:20] and iso["max_total_m"] <= 1200)
            stats = await invoke("walking_network_stats", {"city": city})
            check("network statistics match native with positive finite entropy", stats == engine.network_stats(city) and math.isfinite(stats["orientation_entropy_nats"]) and stats["orientation_entropy_nats"] > 0)
            exported = await invoke("walking_export_graph", {"city": city, "run_id": baseline["run_id"]})
            reloaded = ox.load_graphml(data.root() / "results" / city / baseline["run_id"] / "network.graphml")
            check("GraphML round trip preserves nodes, keyed edges and lengths", set(reloaded.nodes) == set(graph.nodes) and set(reloaded.edges) == set(graph.edges) and all(reloaded[u][v][k]["length"] == d["length"] for u, v, k, d in graph.edges(keys=True, data=True)))
            image = await invoke("walking_render_map", {"city": city, "run_id": baseline["run_id"]})
            path = data.root() / "results" / city / baseline["run_id"] / "map.png"
            check("map is a nonempty PNG with reproducible receipt", path.read_bytes().startswith(b"\x89PNG\r\n\x1a\n") and image["sha256"] == data.sha(path) and image["bytes"] > 10000)
            for uri in ["walking://case", f"walking://{city}/manifest", f"walking://{city}/graph"]:
                resource = await client.read_resource(AnyUrl(uri))
                check("resource " + uri, bool(resource.contents) and bool(json.loads(resource.contents[0].text)))
            prompts = (await client.list_prompts()).prompts
            prompt = await client.get_prompt("municipal_walking_review", {"city": city})
            check("municipal prompt is discoverable and explicit about denominator", len(prompts) == 1 and "never population or pupils" in prompt.messages[0].content.text)
            # Each negative check asserts the actual validation reason.
            await invoke("walking_graph_info", {"city": "unknown"}, error="city must be")
            await invoke("harvest_walking_data", {"city": city, "mode": "bad"}, error="mode must be")
            await invoke("walking_accessibility", {"city": city, "run_id": "../escape"}, error="run_id must be")
            await invoke("walking_accessibility", {"city": city, "run_id": prefix + "-invalid", "threshold_m": -1}, error="threshold_m must be")
            await invoke("walking_accessibility", {"city": city, "run_id": prefix + "-invalid", "speed_kph": 0}, error="speed_kph must be")
            await invoke("walking_accessibility", {"city": city, "run_id": prefix + "-invalid", "closures": [{"u": -1, "v": -2}]}, error="closure link does not exist")
            await invoke("walking_accessibility", {"city": city, "run_id": baseline["run_id"]}, error="run_id already exists")
            await invoke("walking_snap", {"city": city, "longitude": 0, "latitude": 0}, error="outside the buffered study area")
            await invoke("walking_feature_catalog", {"city": city, "amenity": "hospital"}, error="amenity must be")
            await invoke("walking_route", {"city": city, "origin_id": "missing", "destination_id": "missing"}, error="Unknown feature_id")
            await invoke("walking_route", {"city": city, "origin_id": "missing", "destination_id": "missing", "k": 20}, error="k must be")
            await invoke("walking_node", {"city": city, "node_id": -1}, error="node_id does not exist")
            await invoke("walking_edge", {"city": city, "u": -1, "v": -2}, error="edge does not exist")
            await invoke("walking_read_artifact", {"city": city, "run_id": baseline["run_id"], "name": "../../manifest.json"}, error="artifact name is not allowed")
            await invoke("walking_read_artifact", {"city": city, "run_id": baseline["run_id"], "limit": 100000}, error="limit must be")
            await invoke("walking_compare", {"city": city, "baseline_id": baseline["run_id"], "scenario_id": baseline["run_id"]}, error="declared closure scenario")
            check("all exposed tools exercised", set(evidence["tools_exercised"]) == tool_names, {"advertised": sorted(tool_names), "exercised": sorted(set(evidence["tools_exercised"]))})
    evidence.update(native_baseline=native["run_id"], native_scenario=native_scenario["run_id"], mcp_baseline=baseline["run_id"], mcp_scenario=scenario["run_id"], input_manifest_sha256=data.sha(base / "manifest.json"),
                    implementation_sha256=data.sha(Path(engine.__file__)), source_attribution=manifest["attribution"], checks_passed=sum(c["passed"] for c in evidence["checks"]))
    data.dump(out / "native.json", native)
    data.dump(out / "native-comparison.json", native_comparison)
    data.dump(out / "mcp.json", evidence)
    if evidence["failures"]:
        raise AssertionError(evidence["failures"])
    return {"city": city, "checks_passed": evidence["checks_passed"], "tools_exercised": len(set(evidence["tools_exercised"])), "evidence": str(out)}
