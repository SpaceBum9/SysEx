"""scripts/rag_vec.py brute and --ivf."""

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts" / "rag_vec.py"


class RagVecCliTests(unittest.TestCase):
    def test_brute_and_ivf(self) -> None:
        brute = subprocess.run(
            [sys.executable, str(CLI), "HNSW"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        ivf = subprocess.run(
            [sys.executable, str(CLI), "--ivf", "HNSW"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(brute.returncode, 0, brute.stderr)
        self.assertEqual(ivf.returncode, 0, ivf.stderr)
        self.assertTrue(json.loads(brute.stdout))
        self.assertTrue(json.loads(ivf.stdout))


if __name__ == "__main__":
    unittest.main()
