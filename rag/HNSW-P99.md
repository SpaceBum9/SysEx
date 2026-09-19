# p99 latency

Measure end-to-end, not mean. Warm cache separately from cold.
HNSW levers: lower efSearch until recall floor; cap k; keep graph in RAM; avoid GC/alloc in the hop loop.
Tails often come from page faults, noisy neighbors, huge efSearch on hard queries.
Adaptive efSearch: start small, raise only if the candidate heap is unstable.
SysEx has no p99 SLO. rag_vec is offline over small md.
