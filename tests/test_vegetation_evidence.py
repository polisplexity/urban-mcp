"""Guard evidence bytes, complete observed transport and separate factual verdicts."""
import hashlib
import json
from pathlib import Path
import unittest

from tools.review_vegetation_agents import check_claims

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / "cases/two-city-vegetation"
EVIDENCE = CASE / "evidence"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class VegetationEvidence(unittest.TestCase):
    def test_native_bytes_and_version_one_numeric_results_remain_exact(self):
        for city in load(EVIDENCE / "reproduction.json")["cities"]:
            folder = EVIDENCE / city["city"]
            for name, expected in city["artifacts"].items():
                with self.subTest(city=city["city"], artifact=name):
                    self.assertEqual(sha(folder / name), expected)
                    self.assertEqual(sha(folder / name), sha(EVIDENCE / "initial-observations/v1" / city["city"] / name))
            checks = load(folder / "mcp.json")
            self.assertEqual(checks["failures"], [])
            self.assertEqual(len(set(checks["tools_exercised"])), 21)
            self.assertEqual(checks["checks_passed"], len(checks["checks"]))

    def test_four_actual_observations_and_complete_csv_page_chains(self):
        agents = load(EVIDENCE / "agents.json")
        self.assertEqual(agents["task_template_sha256"], sha(CASE / "agent-task-v2.md"))
        self.assertEqual({(r["city"], r["host"]) for r in agents["hosts"]}, {(c, h) for c in ["helsinki", "amsterdam"] for h in ["codex", "hermes"]})
        for row in agents["hosts"]:
            self.assertTrue(row["actual_mcp_analysis_and_comparison_match_native"])
            self.assertTrue(row["artifacts_match_native"])
            self.assertEqual(row["machine_claims"]["status"], "passed")
            self.assertEqual(len(row["advertised_tools_with_successful_response"]), 21)
            self.assertEqual(len(row["observed_csv_pages"]), 3)
            for receipt in row["observed_csv_pages"]:
                prefix = "baseline" if receipt["run_id"] == "agent-baseline" else "sensitivity"
                path = EVIDENCE / row["city"] / (prefix + (".csv" if receipt["name"] == "zone_metrics.csv" else "-classes.csv"))
                self.assertEqual(receipt["sha256"], sha(path))
                text = path.read_text(encoding="utf-8")
                offset = 0
                for page in receipt["pages"]:
                    self.assertEqual(page["offset"], offset)
                    self.assertLessEqual(page["requested_limit"], 12000)
                    observed = text[offset:offset+page["requested_limit"]]
                    self.assertEqual(page["text_sha256"], hashlib.sha256(observed.encode()).hexdigest())
                    self.assertEqual(page["characters"], len(observed))
                    offset = page["next_offset"]
                self.assertIsNone(offset)

    def test_answer_reviews_are_hash_bound_and_do_not_hide_failed_prose(self):
        reviews = load(EVIDENCE / "narrative-review.json")["reviews"]
        for row in load(EVIDENCE / "agents.json")["hosts"]:
            key = row["city"] + ":" + row["host"]
            self.assertEqual(row["answer_sha256"], sha(EVIDENCE / row["city"] / (row["host"]+"-answer.md")))
            self.assertEqual(row["answer_sha256"], reviews[key]["answer_sha256"])
            self.assertEqual(row["narrative_review"], reviews[key])
        self.assertEqual(reviews["helsinki:codex"]["status"], "passed_for_declared_brief")
        self.assertEqual(reviews["amsterdam:codex"]["status"], "passed_facts_with_length_constraint_failure")
        for city in ["helsinki", "amsterdam"]:
            self.assertEqual(reviews[city+":hermes"]["status"], "failed_factual_narrative_review")
        historical = load(EVIDENCE / "initial-observations/v1/amsterdam/hermes-analysis-results.json")
        self.assertTrue(any(r.get("admitted_as_complete") is False and r["result"] is None for r in historical))
        qualification = load(ROOT / "registry/product-qualification.json")
        self.assertFalse(next(r for r in qualification["capabilities"] if r["id"] == "historical-vegetation")["product_qualified"])

    def test_claim_checks_reject_boolean_counts_and_duplicate_or_missing_ids(self):
        expected = {"city": "test-city", "count": 1, "ids": ["001", "002"]}
        def evaluate(claim):
            return check_claims("```json\n"+json.dumps(claim)+"\n```", expected)["status"]
        self.assertEqual(evaluate(expected), "passed")
        self.assertEqual(evaluate({**expected, "ids": ["002", "001"]}), "passed")
        self.assertEqual(evaluate({**expected, "count": True}), "failed")
        self.assertEqual(evaluate({**expected, "ids": ["001", "001", "002"]}), "failed")
        self.assertEqual(evaluate({**expected, "ids": ["001"]}), "failed")
        self.assertEqual(evaluate({**expected, "unrequested": 0}), "failed")
