# HNSW tips

Fix M and efConstruction first on a rebuild. Then only sweep efSearch at query time.
Normalize vectors if using cosine. Keep the graph in RAM. Cap k. Quantize if RAM binds.
Do not raise efSearch to hide a bad M. SysEx does not run HNSW.
