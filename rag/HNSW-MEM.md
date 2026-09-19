# HNSW memory

Cost ~ vectors + M links per node on layer 0 + sparse upper layers.
Lower M and scalar quantize vectors if RAM binds. Preallocate neighbor arrays; no per-hop malloc.
Do not store full dense distance matrices. mmap the vector blob; keep the graph hot.
SysEx does not allocate an HNSW heap.
