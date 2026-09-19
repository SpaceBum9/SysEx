# Hierarchical alternatives

Agglomerative: start as n leaves, merge closest pair (single/complete/average/Ward) into a dendrogram. Cut later; k need not be chosen first.
Divisive: split top-down. Rare in ANN coarse lists.
Vs k-means: no spherical assumption as strong; O(n^2) naive; Ward is closest to variance min.
Other skips: GMM (soft ellipses), DBSCAN (density, no k), BIRCH (streaming trees).
SysEx IVF stays Lloyd. HAC not wired.
