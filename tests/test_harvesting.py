"""Admission failures that must never be reported as a complete municipal harvest."""
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from urban_mcp_case import sources


class HarvestTests(unittest.TestCase):
    def test_duplicate_between_pages_is_rejected(self):
        pages = [(b"one", {"count": 2, "next": "https://api.hel.fi/page2", "results": [{"id": 1}]}, []), (b"two", {"count": 2, "next": None, "results": [{"id": 1}]}, [])]
        with tempfile.TemporaryDirectory() as tmp, patch.object(sources, "get_json", side_effect=pages):
            with self.assertRaisesRegex(ValueError, "duplicate ID"):
                sources.collect_pages("units", "https://api.hel.fi/page1", Path(tmp))

    def test_count_change_during_pagination_is_rejected(self):
        pages = [(b"one", {"count": 2, "next": "https://api.hel.fi/page2", "results": [{"id": 1}]}, []), (b"two", {"count": 3, "next": None, "results": [{"id": 2}]}, [])]
        with tempfile.TemporaryDirectory() as tmp, patch.object(sources, "get_json", side_effect=pages):
            with self.assertRaisesRegex(ValueError, "count changed"):
                sources.collect_pages("units", "https://api.hel.fi/page1", Path(tmp))

    def test_truncated_pagination_is_not_complete(self):
        page = (b"one", {"count": 2, "next": None, "results": [{"id": 1}]}, [])
        with tempfile.TemporaryDirectory() as tmp, patch.object(sources, "get_json", return_value=page):
            with self.assertRaisesRegex(ValueError, "expected 2 rows"):
                sources.collect_pages("units", "https://api.hel.fi/page1", Path(tmp))

    def test_unadmitted_network_target_is_rejected(self):
        for url in ("http://api.hel.fi/units", "https://example.org/data", "https://user:secret@api.hel.fi/data"):
            with self.assertRaisesRegex(ValueError, "outside the admitted HTTPS recipe"):
                sources.get_json(url)

    def test_snapshot_tampering_is_detected(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {"URBAN_MCP_DATA": tmp}):
            root = Path(tmp)
            folder = root / "sources/test-snapshot"
            folder.mkdir(parents=True)
            (folder/"units.json").write_bytes(b"abc")
            receipt = {"complete": True, "failed": [], "sources": {"units": {"pages": [{"file": "units.json", "bytes": 3, "sha256": hashlib.sha256(b"abc").hexdigest()}]}}}
            sources.write_json(folder/"harvest.json", receipt)
            sources.write_json(root/"active.json", {"snapshot": "test-snapshot"})
            sources.active_folder()
            (folder/"units.json").write_bytes(b"abd")
            with self.assertRaisesRegex(ValueError, "integrity mismatch"):
                sources.active_folder()

    def test_snapshot_pointer_cannot_escape_workspace(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {"URBAN_MCP_DATA": tmp}):
            sources.write_json(Path(tmp)/"active.json", {"snapshot": "../outside"})
            with self.assertRaisesRegex(ValueError, "Invalid snapshot identifier"):
                sources.active_folder()

    def test_failed_live_harvest_preserves_active_snapshot(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {"URBAN_MCP_DATA": tmp}), patch.object(sources, "collect_pages", side_effect=RuntimeError("source unavailable")):
            pointer=Path(tmp)/"active.json"
            sources.write_json(pointer, {"snapshot": "previous-good"})
            with self.assertRaisesRegex(RuntimeError, "source unavailable"):
                sources.harvest_live()
            self.assertEqual(json.loads(pointer.read_text())["snapshot"], "previous-good")
            receipt=next((Path(tmp)/"sources").glob("*/harvest.json"))
            self.assertFalse(json.loads(receipt.read_text())["complete"])

    def test_invalid_snapshot_is_not_published_as_active(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);case=root/"case";case.mkdir();data=root/"data";data.mkdir()
            archive=data/"snapshot.zip"
            with zipfile.ZipFile(archive,"w") as z:
                z.writestr("harvest.json",json.dumps({"complete":False,"failed":["incomplete"],"sources":{}}))
            sources.write_json(case/"snapshot.lock.json",{"url":"https://github.com/polisplexity/urban-mcp/releases/download/test/snapshot.zip","snapshot":"new-invalid","bytes":archive.stat().st_size,"sha256":sources.digest(archive)})
            sources.write_json(data/"active.json",{"snapshot":"previous-good"})
            with patch.dict(os.environ,{"URBAN_MCP_DATA":str(data)}),patch.object(sources,"CASE",case):
                with self.assertRaisesRegex(ValueError,"acquisition failures"):
                    sources.harvest_snapshot()
            self.assertEqual(json.loads((data/"active.json").read_text())["snapshot"],"previous-good")


if __name__ == "__main__":
    unittest.main()
