#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from packet import compose  # noqa: E402


def main() -> None:
    p = argparse.ArgumentParser(prog="compose")
    p.add_argument("text", nargs="*", default=["health"])
    p.add_argument("--verb", default="sync")
    p.add_argument("--lang", default="de")
    args = p.parse_args()
    packet = compose(" ".join(args.text), verb=args.verb, lang=args.lang)
    print(json.dumps(packet, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
