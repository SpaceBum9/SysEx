import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAG = ROOT / "rag"
MANIFEST = RAG / "MANIFEST.json"


class ManifestTests(unittest.TestCase):
    def test_manifest_covers_numbered_rag_chunks(self) -> None:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
        chunks = data["chunks"]

        self.assertEqual(len(chunks), len(set(chunks)), "manifest contains duplicate chunks")

        missing_files = [chunk for chunk in chunks if not (ROOT / chunk).is_file()]
        self.assertEqual(missing_files, [], "manifest references missing files")

        numbered_paths = sorted(
            f"rag/{path.name}" for path in RAG.glob("[0-9][0-9]-*.md")
        )
        missing_from_manifest = sorted(set(numbered_paths) - set(chunks))
        self.assertEqual(
            missing_from_manifest,
            [],
            "numbered RAG chunks are missing from the manifest",
        )

        numbers = sorted(int(Path(path).name[:2]) for path in numbered_paths)
        self.assertEqual(
            numbers,
            list(range(numbers[0], numbers[-1] + 1)),
            "numbered RAG chunk sequence has a gap",
        )


if __name__ == "__main__":
    unittest.main()
