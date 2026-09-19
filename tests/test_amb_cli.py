import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts" / "amb.py"


class AmbCliTests(unittest.TestCase):
    def test_batch(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(CLI), "--lang", "en", "--batch", "virus galaxy", "read health"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        rows = json.loads(proc.stdout)
        self.assertEqual(len(rows), 2)
        self.assertFalse(rows[0]["snapshot"]["claims_external_state"])


if __name__ == "__main__":
    unittest.main()
