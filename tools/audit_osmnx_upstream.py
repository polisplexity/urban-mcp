"""Evaluate a separately obtained, pinned upstream checkout without redistributing it.

Run inside the walking image with the checkout mounted read-only and its src on
PYTHONPATH. Results are observations about that revision, not upstream admission.
No upstream code is copied into this repository or its Docker image.
"""
import ast
import asyncio
import json
from pathlib import Path
import warnings

from fastmcp import Client
import networkx as nx
import osmnx as ox
from osmnx_mcp import server

from urban_mcp_walking import data, engine


async def main():
    source = Path("/audited-upstream/src/osmnx_mcp")
    inventory = []
    for path in sorted(source.rglob("*.py")):
        for node in ast.walk(ast.parse(path.read_text())):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and any("mcp.tool" in ast.unparse(d) for d in node.decorator_list):
                inventory.append({"name": node.name, "source": str(path.relative_to(source)), "line": node.lineno})
    graph, _, _ = engine.load("amsterdam")
    records = []
    origins, destinations, _ = engine.prepare("amsterdam")
    a, b = origins[0], destinations[0]
    position = {"lng": a["longitude"], "lat": a["latitude"]}
    endpoints = {"orig_lng": a["longitude"], "orig_lat": a["latitude"], "dest_lng": b["longitude"], "dest_lat": b["latitude"]}
    mcp = server.mount(graph.copy(), name="audit")
    async with Client(mcp) as client:
        async def call(name, arguments=None):
            # Reset original global state before every destructive operation.
            server.set_graph(graph.copy(), "audit")
            try:
                with warnings.catch_warnings(record=True) as caught:
                    warnings.simplefilter("always")
                    result = await client.call_tool(name, arguments or {})
                value = result.data
                observation = {"tool": name, "status": "returned", "warnings": [str(w.message) for w in caught], "result_excerpt": str(value)[:400]}
                if name in {"truncate_graph_bbox", "subgraph_from_point"}:
                    current = server.get_graph()
                    bbox = arguments if name == "truncate_graph_bbox" else value["bbox"]
                    expected = ox.truncate.truncate_graph_bbox(graph, bbox=(bbox["west"], bbox["south"], bbox["east"], bbox["north"]))
                    observation.update(native_expected_nodes=len(expected), returned_nodes=len(current), same_node_set=set(current) == set(expected),
                                       actual_bounds={"west": min(d["x"] for _, d in current.nodes(data=True)), "south": min(d["y"] for _, d in current.nodes(data=True)),
                                                      "east": max(d["x"] for _, d in current.nodes(data=True)), "north": max(d["y"] for _, d in current.nodes(data=True))})
                if name == "consolidate_intersections":
                    observation["input_crs"] = str(graph.graph["crs"])
                    observation["metric_precondition_enforced"] = False
                records.append(observation)
            except Exception as error:
                records.append({"tool": name, "status": "error", "error": str(error)[:1200]})
        for name, args in [
            ("list_graphs", {}), ("graph_info", {}), ("set_active_graph", {"name": "audit"}),
            ("save_graph", {"path": "/tmp/audit.graphml"}), ("load_graph_from_file", {"path": "/tmp/audit.graphml", "name": "from-file"}),
            ("nearest_nodes", position), ("nearest_edges", position), ("shortest_path", endpoints), ("k_shortest_paths", {**endpoints, "k": 2}),
            ("basic_stats", {}), ("orientation_entropy", {}), ("streets_per_node_avg", {}), ("streets_per_node_proportions", {}),
            ("add_edge_speeds", {}), ("add_edge_travel_times", {}), ("add_edge_bearings", {}), ("add_edge_grades", {}),
            ("truncate_graph_bbox", {"north": 52.39, "south": 52.36, "east": 4.91, "west": 4.88}),
            ("subgraph_from_point", {"lat": 52.3731, "lng": 4.8936, "dist_m": 500, "source_name": "audit", "target_name": "subgraph"}),
            ("truncate_graph_dist", {**position, "dist_m": 500}), ("largest_component", {}), ("consolidate_intersections", {}),
            ("plot_graph", {}), ("plot_route", endpoints), ("plot_orientation", {}), ("plot_figure_ground", {}),
        ]:
            await call(name, args)
        path = nx.shortest_path(graph, a["snap"]["node"], b["snap"]["node"], weight="length")
        await call("plot_route_from_path", {"route": path})
        await call("drop_graph", {"name": "audit"})
        tiny = nx.MultiDiGraph(crs="EPSG:4326")
        tiny.add_node(1, x=4.89, y=52.37)
        tiny.add_node(2, x=4.891, y=52.371)
        tiny.add_edge(1, 2, key=0, length=90.0)
        tiny.add_edge(1, 2, key=7, length=10.0)
        server.set_graph(tiny, "parallel-regression")
        result = await client.call_tool("shortest_path", {"orig_lng": 4.89, "orig_lat": 52.37, "dest_lng": 4.891, "dest_lat": 52.371})
        records.append({"tool": "shortest_path", "fixture": "synthetic parallel edges", "reported_length_m": result.data["length_m"], "native_shortest_length_m": nx.shortest_path_length(tiny, 1, 2, weight="length"), "status": "returned"})
    tested = {r["tool"] for r in records}
    document = {"repository": "https://github.com/msradam/osmnx-mcp", "commit": "be547a94038b7b3fa353615381a330b94e2b0b7c", "license": "No license file or declaration at inspected revision; GitHub license metadata null",
                "runtime": "walking runtime.lock.txt, direct mounted source; not installed or redistributed as a package", "tool_inventory": inventory, "observations": records,
                "not_executed": [{**item, "reason": "Live acquisition not admitted; avoid redundant public API calls in this offline audit"} for item in inventory if item["name"] not in tested],
                "limits": "This is an audit of an independently obtained checkout, not a license determination or proof of all upstream functions. City evidence uses a separately implemented MIT adapter on public OSMnx/NetworkX APIs."}
    data.dump(data.root() / "evidence/upstream-audit.json", document)
    print(json.dumps({"tools": len(inventory), "observations": len(records), "errors": [r["tool"] for r in records if r["status"] == "error"]}))


if __name__ == "__main__":
    asyncio.run(main())
