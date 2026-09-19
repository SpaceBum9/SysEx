"""scripts/compose.py --verb matches packet."""

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts" / "compose.py"


class ComposeCliTests(unittest.TestCase):
    def test_sync_json(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(CLI), "read", "health", "--verb", "sync"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        packet = json.loads(proc.stdout)
        self.assertEqual(packet["verb"], "sync")
        self.assertFalse(packet["execute"])
        self.assertIn("garas", packet)


if __name__ == "__main__":
    unittest.main()
