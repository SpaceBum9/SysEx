# k-means

Partition n points into k groups. Iterate: assign each point to nearest centroid, replace centroid by the mean of its group. Stop after rounds or when assignments stabilize.
Objective: minimize within-cluster sum of squares (Lloyd). Sensitive to init and to k.
SysEx src/ivf.py uses a few Lloyd rounds on sparse TF-IDF with cosine assign, not L2.
