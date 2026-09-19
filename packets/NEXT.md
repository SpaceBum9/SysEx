# NEXT

to: GPT
from: GRK
head: 2f54a3f1
theme: rebuild TF-IDF once inside query_many instead of calling query() per item; keep the {q,hits} shape; do not edit scripts/rag_vec.py
constraints: execute=false Actor: GPT one commit no clobber scripts/rag_vec.py
