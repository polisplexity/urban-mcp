"""Regression examples separate from native municipal path evidence."""
import copy
import unittest

from urban_mcp_walking import diagnostics


def row(name, distance, destination="library/a", status="routed"):
    return {"origin_id": name, "origin_name": name, "status": status, "total_m": distance,
            "destination_id": destination if status == "routed" else "", "within_threshold": distance is not None and distance <= 1200}


def routes(rows, edges=None):
    return [{"properties": {"origin_id": r["origin_id"], "destination_id": r["destination_id"], "edges": edges or []}}
            for r in rows if r["status"] == "routed"]


class WalkingDiagnostics(unittest.TestCase):
    def compare(self, before, after, before_edges=None):
        return diagnostics.compare_records(before, after, routes(before, before_edges), routes(after), [{"u": 1, "v": 2}], 1200)

    def test_large_detour_is_not_a_threshold_crossing(self):
        result = self.compare([row("large", 100), row("crossing", 1190)], [row("large", 900), row("crossing", 1210)])
        self.assertEqual(result["crossed_threshold_origin_ids"], ["crossing"])
        large = next(r for r in result["schools"] if r["origin_id"] == "large")
        self.assertEqual(large["extra_distance_m"], 800)
        self.assertEqual(large["threshold_transition"], "within_to_within")
        self.assertFalse(large["crossed_threshold"])

    def test_exact_boundary_rerouting_and_unreachable_rows(self):
        before = [row("boundary", 1200), row("rerouted", 100, "library/a"), row("isolated", None, status="unreachable")]
        after = [row("boundary", 1200.01), row("rerouted", 100, "library/b"), row("isolated", None, status="unreachable")]
        result = self.compare(before, after)
        self.assertEqual(result["crossed_threshold_origin_ids"], ["boundary"])
        changed = next(r for r in result["schools"] if r["origin_id"] == "rerouted")
        self.assertEqual((changed["destination_id_before"], changed["destination_id_after"]), ("library/a", "library/b"))
        self.assertTrue(changed["destination_changed"])
        self.assertEqual(result["transition_counts"]["unreachable_to_unreachable"], 1)

    def test_lost_reachability_is_explicit_not_a_finite_distance_crossing(self):
        result = self.compare([row("lost", 500)], [row("lost", None, status="unreachable")])
        self.assertEqual(result["left_threshold_coverage_origin_ids"], ["lost"])
        self.assertEqual(result["newly_unreachable_origin_ids"], ["lost"])
        self.assertEqual(result["crossed_threshold_origin_ids"], [])
        self.assertEqual(result["schools"][0]["threshold_transition"], "within_to_unreachable")
        self.assertIsNone(result["schools"][0]["extra_distance_m"])

    def test_reverse_direction_and_all_parallel_keys_are_closed(self):
        edges = [{"u": 2, "v": 1, "key": 7, "length_m": 10}, {"u": 1, "v": 2, "key": 3, "length_m": 20}]
        actual = diagnostics.link_membership(edges, [{"u": 1, "v": 2}])
        self.assertTrue(actual["uses_closed_link"])
        self.assertEqual(actual["closed_edges_used"], edges)

    def test_two_alternatives_can_both_be_blocked(self):
        paths = [{"edges": [{"u": 1, "v": 2, "key": 0}], "total_m": 100},
                 {"edges": [{"u": 1, "v": 2, "key": 7}, {"u": 2, "v": 3, "key": 0}], "total_m": 120}]
        original = copy.deepcopy(paths)
        result = diagnostics.annotate_paths(paths, [{"u": 2, "v": 1}])
        self.assertEqual(paths, original)
        self.assertEqual(result["path_ranks_avoiding_declared_closed_links"], [])
        self.assertTrue(all(p["uses_closed_link"] for p in result["paths"]))
        self.assertTrue(result["path_overlap"][0]["directed_keyed_edge_disjoint"])
        self.assertFalse(result["path_overlap"][0]["physical_link_disjoint"])

    def test_an_avoiding_alternative_is_distinguished(self):
        paths = [{"edges": [{"u": 1, "v": 2, "key": 0}]}, {"edges": [{"u": 1, "v": 3, "key": 0}]}]
        result = diagnostics.annotate_paths(paths, [{"u": 1, "v": 2}])
        self.assertEqual(result["path_ranks_avoiding_declared_closed_links"], [2])

    def test_mismatched_origins_duplicate_rows_and_false_flags_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "same nonempty origin"):
            self.compare([row("a", 100)], [row("b", 200)])
        with self.assertRaisesRegex(ValueError, "Duplicate origin"):
            self.compare([row("a", 100)] * 2, [row("a", 200)])
        wrong = row("a", 1250)
        wrong["within_threshold"] = True
        with self.assertRaisesRegex(ValueError, "flag disagrees"):
            self.compare([row("a", 100)], [wrong])

    def test_shortened_and_closed_scenario_paths_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "shortened"):
            self.compare([row("a", 100)], [row("a", 90)])
        records = [row("a", 100)]
        with self.assertRaisesRegex(ValueError, "Scenario route uses a removed link"):
            diagnostics.compare_records(records, records, routes(records), routes(records, [{"u": 2, "v": 1, "key": 5}]), [{"u": 1, "v": 2}], 1200)

    def test_invalid_and_duplicate_closure_pairs(self):
        self.assertEqual(diagnostics.normalize_links([{"u": 2, "v": 1}, {"u": 1, "v": 2}]), [{"u": 1, "v": 2}])
        with self.assertRaisesRegex(ValueError, "integer"):
            diagnostics.normalize_links([{"u": True, "v": 2}])
        with self.assertRaisesRegex(ValueError, "at most ten"):
            diagnostics.normalize_links([{"u": 1, "v": 2}] * 11)
