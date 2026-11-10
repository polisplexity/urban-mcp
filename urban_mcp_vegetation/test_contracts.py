"""Synthetic diagnostic/integrity regressions; these are not municipal observations."""
import copy
import hashlib
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import warnings
import zipfile

from . import data, engine


class VegetationContracts(unittest.TestCase):
    def test_water_does_not_dilute_the_land_denominator(self):
        result = engine.counts_to_metrics({10: 2, 50: 2, 80: 6, 0: 2}, [10, 20, 30, 40, 90, 95, 100])
        self.assertEqual(result["vegetation_share_of_valid_land"], .5)
        self.assertEqual(result["vegetation_share_of_valid_all"], .2)
        self.assertEqual(result["valid_fraction_of_zone_pixels"], 10/12)

    def test_no_valid_land_is_unknown_not_zero_vegetation(self):
        for counts in [{80: 10}, {0: 10}, {}]:
            with self.subTest(counts=counts):
                result = engine.counts_to_metrics(counts, [10, 20, 30, 40, 90, 95, 100])
                self.assertIsNone(result["vegetation_share_of_valid_land"])
                self.assertIsNone(result["tree_class_share_of_valid_land"])

    def test_cropland_is_explicitly_included_and_tree_class_is_separate(self):
        result = engine.counts_to_metrics({10: 2, 40: 4, 50: 4}, data.recipe()["vegetation_classes"])
        self.assertEqual(result["vegetation_share_of_valid_land"], .6)
        self.assertEqual(result["tree_class_share_of_valid_land"], .2)

    def test_unknown_or_negative_class_counts_are_rejected(self):
        for counts in [{11: 1}, {50: -1}]:
            with self.assertRaisesRegex(ValueError, "Invalid class counts"):
                engine.counts_to_metrics(counts, data.recipe()["vegetation_classes"])

    def test_unknown_city_and_unsafe_run_identifiers_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "Unknown city"):
            data.city_config("../../../outside")
        for value in ["../outside", "", "a"*49]:
            with self.assertRaisesRegex(ValueError, "run_id"):
                engine.token(value)

    def test_manifest_requires_exact_recipe_and_required_files(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            manifest = {"city": "helsinki", "case": data.recipe()["id"], "recipe_sha256": data.sha(data.CASE/"recipe.json"), "source_tiles": [], "files": {}}
            data.dump(base/"manifest.json", manifest)
            with self.assertRaisesRegex(ValueError, "required files"):
                data.verify("helsinki", base)
            manifest["recipe_sha256"] = "0"*64
            data.dump(base/"manifest.json", manifest)
            with self.assertRaisesRegex(ValueError, "identity mismatch"):
                data.verify("helsinki", base)

    def test_input_content_tampering_is_detected(self):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            for name in ["zones.geojson", "requests.json", "source-test.tif"]:
                (base/name).write_bytes(b"original fixture")
            manifest = {"city": "helsinki", "case": data.recipe()["id"], "recipe_sha256": data.sha(data.CASE/"recipe.json"), "source_tiles": [{"file": "source-test.tif"}], "files": {name: {"bytes": (base/name).stat().st_size, "sha256": data.sha(base/name)} for name in ["zones.geojson", "requests.json", "source-test.tif"]}}
            data.dump(base/"manifest.json", manifest)
            data.verify("helsinki", base)
            (base/"source-test.tif").write_bytes(b"tampered fixture")
            with self.assertRaisesRegex(ValueError, "integrity failure"):
                data.verify("helsinki", base)

    def test_threshold_is_bounded_before_missing_data_is_read(self):
        for threshold in [float("nan"), float("inf"), -0.1, 1.1]:
            with self.assertRaisesRegex(ValueError, "threshold"):
                engine.analyze("helsinki", "fixture-only", threshold)

    def restore_fixture(self, entries, expected_error, corrupt_hash=False):
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            case = base/"case"
            case.mkdir()
            (case/"recipe.json").write_bytes((data.CASE/"recipe.json").read_bytes())
            stream = io.BytesIO()
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", UserWarning)
                with zipfile.ZipFile(stream, "w") as z:
                    for name, payload in entries:
                        z.writestr(name, payload)
            payload = stream.getvalue()
            lock = {"url": "https://example.invalid/synthetic-snapshot.zip", "bytes": len(payload), "sha256": "0"*64 if corrupt_hash else hashlib.sha256(payload).hexdigest(), "manifest_sha256": "0"*64}
            data.dump(case/"snapshot.lock.json", {"helsinki": lock})
            with patch.dict(os.environ, {"URBAN_MCP_DATA": str(base/"workspace")}), patch.object(data, "CASE", case), patch.object(data, "urlopen", return_value=io.BytesIO(payload)):
                with self.assertRaisesRegex(ValueError, expected_error):
                    data.restore("helsinki")

    def test_snapshot_traversal_is_rejected(self):
        self.restore_fixture([("../outside", b"synthetic")], "Unsafe snapshot member")

    def test_snapshot_duplicate_members_are_rejected(self):
        self.restore_fixture([("duplicate", b"a"), ("duplicate", b"b")], "member/count/expansion")

    def test_snapshot_symlink_is_rejected(self):
        info = zipfile.ZipInfo("link")
        info.external_attr = 0o120777 << 16
        self.restore_fixture([(info, b"../outside")], "Unsafe snapshot member")

    def test_snapshot_hash_is_checked_before_extraction(self):
        self.restore_fixture([("anything", b"synthetic")], "size/hash mismatch", corrupt_hash=True)


if __name__ == "__main__":
    unittest.main()
