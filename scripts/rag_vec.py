#!/usr/bin/env python3
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from rag_vec import query  # noqa: E402
from ivf import search, train  # noqa: E402

args = [a for a in sys.argv[1:] if a != "--ivf"]
use_ivf = "--ivf" in sys.argv[1:]
q = " ".join(args) or "garas a4b"
if use_ivf:
    out = search(q, train())
else:
    out = query(q)
print(json.dumps(out, ensure_ascii=False, indent=2))
