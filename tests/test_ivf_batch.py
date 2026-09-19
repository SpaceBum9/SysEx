"""Batch IVF: one train, many queries."""

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
CLI = ROOT / "scripts" / "rag_vec.py"

from ivf import search_many, train  # noqa: E402


class IvfBatchTests(unittest.TestCase):
    def test_search_many_shares_index(self) -> None:
        idx = train(k=4, rounds=2)
        rows = search_many(["HNSW", "GARAS"], index=idx, nprobe=2)
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["q"], "HNSW")
        self.assertTrue(rows[0]["hits"])

    def test_cli_batch(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(CLI), "--ivf", "--batch", "HNSW", "GARAS"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertEqual(len(payload), 2)
        self.assertIn("hits", payload[0])


if __name__ == "__main__":
    unittest.main()
