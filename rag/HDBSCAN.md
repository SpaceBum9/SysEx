# HDBSCAN vs DBSCAN

DBSCAN: one eps and min_samples. Dense core, density-reachable border, noise. Fails when clusters have different densities.
HDBSCAN: mutual reachability + condensed cluster tree over a range of eps. Picks stable clusters; min_cluster_size instead of a global eps. Handles variable density better; still leaves noise.
Neither is an IVF coarse list. Not in src/ivf.py.
