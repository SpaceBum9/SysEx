import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts" / "trace_check.py"


class TraceCheckCliTests(unittest.TestCase):
    def test_fresh_compose(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(CLI)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 0, proc.stderr)
        payload = json.loads(proc.stdout)
        self.assertTrue(payload["verify"]["ok"])

    def test_bad_json_chain(self) -> None:
        packet = {"trace_id": "TR-not-hex", "content_sha256": "x"}
        proc = subprocess.run(
            [sys.executable, str(CLI)],
            cwd=ROOT,
            input=json.dumps(packet),
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(proc.returncode, 2)


if __name__ == "__main__":
    unittest.main()
