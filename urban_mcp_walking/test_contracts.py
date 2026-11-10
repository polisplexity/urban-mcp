"""Synthetic acquisition-integrity regressions, separate from municipal evidence."""
from contextlib import contextmanager
import hashlib
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile

from . import data


class SnapshotContracts(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)
        self.case = self.base / "case"
        self.case.mkdir()
        self.recipe_bytes = (data.CASE / "recipe.json").read_bytes()
        (self.case / "recipe.json").write_bytes(self.recipe_bytes)
        self.root = self.base / "workspace"
        self.env = patch.dict(os.environ, {"URBAN_MCP_DATA": str(self.root)})
        self.env.start()
        self.case_patch = patch.object(data, "CASE", self.case)
        self.case_patch.start()

    def tearDown(self):
        self.case_patch.stop()
        self.env.stop()
        self.tmp.cleanup()

    def archive(self, extra=None, city="helsinki", recipe_hash=None):
        content = b"synthetic integrity fixture, not a municipal graph"
        manifest = {"case": "two-city-walking", "city": city,
                    "recipe_sha256": recipe_hash or hashlib.sha256(self.recipe_bytes).hexdigest(),
                    "files": {"network.graphml": {"sha256": hashlib.sha256(content).hexdigest(), "bytes": len(content)}}}
        stream = io.BytesIO()
        with zipfile.ZipFile(stream, "w") as zipped:
            zipped.writestr("network.graphml", content)
            zipped.writestr("manifest.json", json.dumps(manifest))
            for name, value in (extra or {}).items():
                zipped.writestr(name, value)
        payload = stream.getvalue()
        lock = {"helsinki": {"url": "https://github.com/polisplexity/urban-mcp/releases/download/test/synthetic.zip", "sha256": hashlib.sha256(payload).hexdigest(), "bytes": len(payload),
                              "manifest_sha256": hashlib.sha256(json.dumps(manifest).encode()).hexdigest()}}
        (self.case / "snapshot.lock.json").write_text(json.dumps(lock))
        return payload

    @contextmanager
    def download(self, payload):
        with patch.object(data.urllib.request, "urlopen", return_value=io.BytesIO(payload)):
            yield

    def test_round_trip_then_tampered_input_is_rejected(self):
        payload = self.archive()
        with self.download(payload):
            data.restore("helsinki")
        (self.root / "inputs/helsinki/network.graphml").write_bytes(b"tampered")
        with self.assertRaisesRegex(ValueError, "integrity failure"):
            data.restore("helsinki")

    def test_wrong_archive_hash_never_activates_inputs(self):
        payload = self.archive()
        with self.download(payload[:-1] + b"x"), self.assertRaisesRegex(ValueError, "SHA-256 mismatch"):
            data.restore("helsinki")
        self.assertFalse((self.root / "inputs/helsinki").exists())

    def test_path_traversal_is_rejected_before_extraction(self):
        payload = self.archive({"../../escape": b"no"})
        with self.download(payload), self.assertRaisesRegex(ValueError, "Unsafe snapshot member"):
            data.restore("helsinki")
        self.assertFalse((self.root / "inputs/helsinki").exists())
        self.assertFalse((self.root / "escape").exists())

    def test_city_mismatch_is_rejected_before_activation(self):
        payload = self.archive(city="amsterdam")
        with self.download(payload), self.assertRaisesRegex(ValueError, "case/recipe mismatch"):
            data.restore("helsinki")

    def test_recipe_mismatch_is_rejected_before_activation(self):
        payload = self.archive(recipe_hash="0" * 64)
        with self.download(payload), self.assertRaisesRegex(ValueError, "case/recipe mismatch"):
            data.restore("helsinki")

    def test_existing_other_snapshot_cannot_silently_satisfy_lock(self):
        payload = self.archive()
        with self.download(payload):
            data.restore("helsinki")
        path = self.root / "inputs/helsinki/manifest.json"
        manifest = json.loads(path.read_text())
        manifest["different_observation"] = True
        path.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, "differ from the locked snapshot"):
            data.restore("helsinki")
