import copy
import hashlib
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from validate import load_all, validate_data
from reference_case import check_asset


class AdmissionTests(unittest.TestCase):
    def setUp(self):
        self.tools, self.sources, self.profiles, self.cases = copy.deepcopy(load_all())

    def errors(self):
        return validate_data(self.tools, self.sources, self.profiles, self.cases)

    def test_current_proposal_is_consistent(self):
        self.assertEqual(self.errors(), [])

    def test_unknown_source_is_rejected(self):
        self.profiles[0]["requirements"][0]["candidate_sources"] = ["missing-provider"]
        self.assertTrue(any("Unknown source" in e for e in self.errors()))

    def test_unverified_tool_cannot_be_promoted(self):
        self.tools[0]["ready_to_run"] = True
        self.assertTrue(any("Unverified runtime" in e for e in self.errors()))

    def test_case_with_pending_license_and_runtime_cannot_be_ready(self):
        self.cases[0]["ready_to_run"] = True
        self.assertTrue(any("admission blockers" in e for e in self.errors()))

    def test_source_url_cannot_embed_credentials(self):
        self.sources[0]["url"] = "https://example-user:example-value@example.org/data"
        self.assertTrue(any("without credentials" in e for e in self.errors()))

    def test_asset_path_cannot_escape_case(self):
        self.cases[0]["assets"][0]["file"] = "../outside.xml"
        self.assertTrue(any("does not match" in e for e in self.errors()))

    def test_integrity_check_detects_changed_data(self):
        asset = {"file": "sample.xml", "bytes": 3, "sha256": hashlib.sha256(b"abc").hexdigest()}
        check_asset(b"abc", asset)
        with self.assertRaisesRegex(ValueError, "integrity mismatch"):
            check_asset(b"abd", asset)


if __name__ == "__main__":
    unittest.main()
