import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts" / "a4b.py"


class A4bCliTests(unittest.TestCase):
    def test_batch(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(CLI), "--batch", "execute now", "read health"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        rows = json.loads(proc.stdout)
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["route"]["class"], "EXEC_BOUNDARY")
        self.assertFalse(rows[0]["route"]["grok_is_xai"])


if __name__ == "__main__":
    unittest.main()
