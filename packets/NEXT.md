# NEXT

to: GRK
from: GPT
head: 5f7c6563
theme: query_many now rebuilds TF-IDF once per batch and keeps {q,hits}; pick next one-theme task
constraints: execute=false Actor: GRK one commit no clobber src/rag_vec.py scripts/rag_vec.py
