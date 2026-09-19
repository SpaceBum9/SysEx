# Tune efSearch for recall

Hold out queries with exact kNN labels. Sweep efSearch: k, 2k, 16, 32, 64, 128, 256.
Plot recall@k vs latency. Stop at first efSearch that meets the recall floor with acceptable p99.
If the curve plateaus below target: raise M / efConstruction and rebuild; efSearch alone cannot fix a sparse graph.
Do not set efSearch in SysEx. No HNSW runtime.
