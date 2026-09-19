# HNSW vs IVF

HNSW: graph. Greedy walk on layered NSW. Good recall at mid-size. RAM-heavy. Incremental insert ok.
IVF: inverted file. Train k coarse centroids, assign each vector to a list, search nprobe lists then brute those lists. Often + PQ. Cheaper RAM, needs a train set, worse if clusters drift.
Combo exists (IVF-HNSW coarse).
SysEx uses neither.
