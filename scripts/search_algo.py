#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from search_algo import run, run_many  # noqa: E402


def main() -> None:
    p = argparse.ArgumentParser(prog="search_algo")
    p.add_argument("text", nargs="*", default=["garas"])
    p.add_argument("--algo", default="brute")
    p.add_argument("--batch", action="store_true")
    args = p.parse_args()
    queries = args.text or ["garas"]
    if args.batch:
        out = run_many(args.algo, queries)
    else:
        out = run(args.algo, " ".join(queries))
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
