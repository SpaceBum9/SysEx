import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from garas import classify, decide  # noqa: E402
from packet import compose  # noqa: E402
from rc import next_slot  # noqa: E402


class PacketTests(unittest.TestCase):
    def test_observe_packet(self) -> None:
        p = compose("read health", verb="sync")
        self.assertTrue(p["trace_verify"]["ok"])
        self.assertFalse(p["execute"])
        self.assertEqual(p["garas"]["intent_class"], "OBSERVE")
        self.assertEqual(p["atm"]["status"], "accepted")

    def test_bilo_scan_is_in_packet(self) -> None:
        p = compose("hold GARAS execute", verb="sync")
        tokens = {row["token"] for row in p["bilo"]}
        self.assertIn("HOLD", tokens)
        self.assertIn("GARAS", tokens)
        self.assertTrue(all(row["claims_external_state"] is False for row in p["bilo"]))

    def test_execute_denied(self) -> None:
        p = compose("go", verb="execute")
        self.assertEqual(p["garas"]["decision"], "deny")
        self.assertEqual(p["atm"]["status"], "denied")
        self.assertEqual(classify("execute now"), "EXECUTE")

    def test_money_class(self) -> None:
        self.assertEqual(decide("transfer funds")["intent_class"], "MONEY")

    def test_nikita_on_wheel(self) -> None:
        self.assertEqual(next_slot(0)["slot"], "NIKITA")


if __name__ == "__main__":
    unittest.main()
