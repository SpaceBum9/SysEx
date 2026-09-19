#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from rag_vec import query  # noqa: E402
from ivf import search, train  # noqa: E402


def main() -> None:
    p = argparse.ArgumentParser(prog="rag_vec")
    p.add_argument("text", nargs="*", default=["garas", "a4b"])
    p.add_argument("--ivf", action="store_true")
    p.add_argument("--k", type=int, default=4)
    p.add_argument("--nprobe", type=int, default=2)
    args = p.parse_args()
    q = " ".join(args.text)
    if args.ivf:
        out = search(q, train(k=args.k), nprobe=args.nprobe)
    else:
        out = query(q)
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
