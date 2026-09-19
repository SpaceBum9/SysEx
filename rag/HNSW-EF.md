# efSearch

Dynamic candidate list size during HNSW query (layer 0 especially).
Must be >= k. Larger efSearch: more neighbors expanded, higher recall, more distance computations.
efConstruction is the build-time analog; usually larger than efSearch.
SysEx rag_vec has no efSearch.
