"""scripts/compose.py --verb matches packet."""

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts" / "compose.py"


class ComposeCliTests(unittest.TestCase):
    def _run(self, *args: str) -> dict:
        proc = subprocess.run(
            [sys.executable, str(CLI), *args],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        return json.loads(proc.stdout)

    def test_sync_json(self) -> None:
        packet = self._run("read", "health", "--verb", "sync")
        self.assertEqual(packet["verb"], "sync")
        self.assertFalse(packet["execute"])
        self.assertIn("garas", packet)

    def test_execute_denied(self) -> None:
        packet = self._run("read", "health", "--verb", "execute")
        self.assertEqual(packet["verb"], "execute")
        self.assertFalse(packet["execute"])
        self.assertEqual(packet["atm"]["status"], "denied")
        self.assertEqual(packet["garas"]["decision"], "deny")


if __name__ == "__main__":
    unittest.main()
