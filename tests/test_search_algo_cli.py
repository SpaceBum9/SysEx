import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts" / "search_algo.py"


class SearchAlgoCliTests(unittest.TestCase):
    def test_brute_batch(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(CLI), "--algo", "brute", "--batch", "GARAS", "HNSW"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertEqual(len(payload), 2)

    def test_hnsw_fails(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(CLI), "--algo", "hnsw", "GARAS"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertNotEqual(proc.returncode, 0)


if __name__ == "__main__":
    unittest.main()
