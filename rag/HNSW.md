# HNSW

Hierarchical Navigable Small World (Malkov, Yashunin). ANN over vectors.
Layers: sparse long links on top, dense short links at layer 0.
Insert: sample max layer exponentially; greedy search per layer; link up to M neighbors.
Query: enter top layer, greedy to local min, descend. efSearch widens the candidate list.
Not exact kNN. Recall vs latency tradeoff.
SysEx rag_vec does not use HNSW. Corpus is tens of md files; brute TF-IDF cosine is enough.
