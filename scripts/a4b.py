#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from a4b import route, route_many  # noqa: E402


def main() -> None:
    p = argparse.ArgumentParser(prog="a4b")
    p.add_argument("text", nargs="*", default=["read health"])
    p.add_argument("--batch", action="store_true")
    args = p.parse_args()
    items = args.text or ["read health"]
    if args.batch:
        out = route_many(items)
    else:
        out = route(" ".join(items))
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
