#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from rag_query import query, query_many  # noqa: E402


def main() -> None:
    p = argparse.ArgumentParser(prog="rag_query")
    p.add_argument("text", nargs="*", default=["garas"])
    p.add_argument("--batch", action="store_true")
    args = p.parse_args()
    if args.batch:
        out = query_many(args.text or ["garas"])
    else:
        out = query(" ".join(args.text) or "garas")
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
