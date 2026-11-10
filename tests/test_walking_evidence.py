"""Public artifact receipts must survive Git/platform newline handling exactly."""
import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / "cases/two-city-walking"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class WalkingEvidence(unittest.TestCase):
    def test_committed_city_artifacts_match_declared_byte_hashes(self):
        reproduction = json.loads((CASE / "evidence/reproduction.json").read_text(encoding="utf-8"))
        for city in reproduction["cities"]:
            folder = CASE / "evidence" / city["city"]
            for file, key in [("baseline.csv", "baseline_csv_sha256"), ("closure.csv", "closure_csv_sha256"), ("map.png", "map_sha256")]:
                with self.subTest(city=city["city"], file=file):
                    self.assertEqual(sha(folder / file), city[key])

    def test_observed_answers_match_hash_bound_narrative_reviews(self):
        reviews = json.loads((CASE / "evidence/narrative-review.json").read_text(encoding="utf-8"))["reviews"]
        agents = json.loads((CASE / "evidence/agents.json").read_text(encoding="utf-8"))
        self.assertEqual(len(agents["hosts"]), 4)
        self.assertEqual(agents["task_template_sha256"], sha(CASE / "agent-task.md"))
        for host in agents["hosts"]:
            key = host["city"] + ":" + host["host"]
            observed = CASE / "evidence" / host["city"] / (host["host"] + "-answer.md")
            with self.subTest(host=key):
                self.assertEqual(sha(observed), host["answer_sha256"])
                self.assertEqual(sha(observed), reviews[key]["answer_sha256"])
                self.assertEqual(host["narrative_review"], reviews[key])
                self.assertTrue(host["artifacts_match_native"])

    def test_artifact_success_does_not_hide_failed_hermes_interpretations(self):
        reviews = json.loads((CASE / "evidence/narrative-review.json").read_text(encoding="utf-8"))["reviews"]
        for city in ["helsinki", "amsterdam"]:
            self.assertEqual(reviews[city + ":hermes"]["status"], "failed_factual_narrative_review")
            self.assertEqual(reviews[city + ":codex"]["status"], "passed_for_declared_brief")

    def test_issue39_artifact_hashes_and_prior_csvs_remain_exact(self):
        folder=CASE/"evidence/issue-39"
        reproduction=json.loads((folder/"reproduction.json").read_text(encoding="utf-8"))
        for city in reproduction["cities"]:
            for name,key in [("baseline.csv","baseline_csv_sha256"),("closure.csv","closure_csv_sha256"),("map.png","map_sha256")]:
                self.assertEqual(sha(folder/city["city"]/name),city[key])
            for name in ["baseline.csv","closure.csv"]:
                self.assertEqual(sha(folder/city["city"]/name),sha(CASE/"evidence"/city["city"]/name))

    def test_issue39_four_host_claims_and_hash_bound_reviews(self):
        folder=CASE/"evidence/issue-39"
        agents=json.loads((folder/"agents.json").read_text(encoding="utf-8"))
        reviews=json.loads((folder/"narrative-review.json").read_text(encoding="utf-8"))["reviews"]
        self.assertEqual(agents["task_template_sha256"],sha(CASE/"agent-task-issue-39.md"))
        self.assertEqual(len(agents["hosts"]),4)
        for host in agents["hosts"]:
            key=host["city"]+":"+host["host"]
            self.assertEqual(host["answer_sha256"],sha(folder/host["city"]/(host["host"]+"-answer.md")))
            self.assertEqual(host["narrative_review"],reviews[key])
            self.assertEqual(host["machine_claims"]["status"],"passed")
            self.assertEqual(host["machine_claims"]["mismatched_fields"],[])
            self.assertTrue(host["diagnostic_tool_results_match_native"])
