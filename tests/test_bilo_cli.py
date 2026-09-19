import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts" / "bilo.py"


class BiloCliTests(unittest.TestCase):
    def test_lookup(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(CLI), "ATM"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        row = json.loads(proc.stdout)
        self.assertEqual(row["token"], "ATM")
        self.assertFalse(row["claims_external_state"])


if __name__ == "__main__":
    unittest.main()
