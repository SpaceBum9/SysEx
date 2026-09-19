#!/usr/bin/env python3
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from rag_vec import query  # noqa: E402

print(json.dumps(query(" ".join(sys.argv[1:]) or "garas a4b"), ensure_ascii=False, indent=2))
