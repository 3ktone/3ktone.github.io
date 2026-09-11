import importlib.util
from pathlib import Path
import tempfile
import unittest


SCRIPT = Path(__file__).parents[1] / "scripts" / "check_legacy_urls.py"
SPEC = importlib.util.spec_from_file_location("check_legacy_urls", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Unable to load {SCRIPT}")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class LegacyUrlCandidatesTest(unittest.TestCase):
    def test_directory_requires_index_file(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            (root / "tags").mkdir()
            candidate = MODULE.candidates(root, "/tags/")
            self.assertEqual(candidate, [root / "tags" / "index.html"])
            self.assertFalse(any(path.is_file() for path in candidate))

    def test_root_resolves_to_index(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            (root / "index.html").write_text("ok", encoding="utf-8")
            candidate = MODULE.candidates(root, "/")
            self.assertEqual(candidate, [root / "index.html"])
            self.assertTrue(candidate[0].is_file())

    def test_root_resolves_to_index_when_build_path_contains_dot(self):
        with tempfile.TemporaryDirectory(prefix="review.build.") as directory:
            root = Path(directory).resolve()
            (root / "index.html").write_text("ok", encoding="utf-8")
            candidate = MODULE.candidates(root, "/")
            self.assertEqual(candidate, [root / "index.html"])
            self.assertTrue(candidate[0].is_file())

    def test_file_url_requires_file(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            asset = root / "assets" / "example.html"
            asset.parent.mkdir()
            asset.write_text("ok", encoding="utf-8")
            self.assertEqual(MODULE.candidates(root, "/assets/example.html"), [asset])

    def test_encoded_traversal_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            self.assertEqual(MODULE.candidates(root, "/%2e%2e/secret.txt"), [])


if __name__ == "__main__":
    unittest.main()
