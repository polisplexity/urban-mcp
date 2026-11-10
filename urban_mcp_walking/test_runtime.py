"""Synthetic cache-concurrency regression; real graph concurrency is checked via MCP."""
from concurrent.futures import ThreadPoolExecutor
import time
import unittest
from unittest.mock import patch

import networkx as nx

from . import engine


class RuntimeConcurrency(unittest.TestCase):
    def test_simultaneous_cold_graph_requests_deserialize_once(self):
        graph = nx.MultiDiGraph(crs="EPSG:4326", city="helsinki")
        graph.add_edge(1, 2, length=10.0)
        calls = []
        def deserialize(path):
            calls.append(str(path))
            time.sleep(0.1)
            return graph
        engine._load_cached.cache_clear()
        try:
            with patch.object(engine.data, "verify", return_value=(__import__("pathlib").Path("/synthetic"), {"nodes": 2, "edges": 1})), patch.object(engine.ox, "load_graphml", side_effect=deserialize):
                with ThreadPoolExecutor(max_workers=3) as pool:
                    results = list(pool.map(engine.load, ["helsinki"] * 3))
            self.assertEqual(len(calls), 1)
            self.assertTrue(all(result[0] is graph for result in results))
        finally:
            engine._load_cached.cache_clear()
