#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from bilo import load, lookup, scan  # noqa: E402


def main() -> None:
    p = argparse.ArgumentParser(prog="bilo")
    p.add_argument("text", nargs="*", default=["GARAS"])
    p.add_argument("--all", action="store_true")
    args = p.parse_args()
    if args.all:
        out = list(load().values())
    elif len(args.text) == 1 and lookup(args.text[0]):
        out = lookup(args.text[0])
    else:
        out = scan(" ".join(args.text))
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
