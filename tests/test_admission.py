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

    def admit_technical_fixture(self):
        case = self.cases[0]
        case.update(ready_to_run=True, status="admitted", blockers=[], engine_status="verified", mcp_binding_status="verified", expected_result_status="verified")
        for asset in case["assets"]:
            asset["license_status"] = "reviewed_for_declared_use"
        tool = next(t for t in self.tools if t["id"] == case["tool_id"])
        tool.update(ready_to_run=True, execution_role="candidate", input_binding_status="verified", engine_runtime_status="verified", reference_case_status="verified", real_city_status="verified_for_declared_scope")
        return case, tool

    def test_technical_fixture_cannot_promote_municipal_tool(self):
        self.admit_technical_fixture()
        self.assertTrue(any("public reproducible municipal case" in e for e in self.errors()))

    def test_municipal_case_requires_evidence_files(self):
        case, _ = self.admit_technical_fixture()
        case["data_class"] = "project_observations"
        case["municipal_case"] = {
            "municipality": {"country_code": "MX", "geographic_id": "test-only", "name": "Test fixture"},
            "question": "Test only: is the evidence present?",
            "data_access": "public_reproducible",
            "harvest_manifest": "missing-harvest.json",
            "native_evidence": "missing-native.json",
            "mcp_evidence": "missing-mcp.json",
            "reproduction_evidence": "missing-reproduction.md",
        }
        self.assertEqual(sum("Municipal evidence" in e for e in self.errors()), 4)

    def test_synthetic_fixture_cannot_claim_municipal_identity(self):
        self.cases[0]["municipal_case"] = {"data_access": "public_reproducible"}
        self.assertTrue(any("Synthetic upstream fixture" in e for e in self.errors()))

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
