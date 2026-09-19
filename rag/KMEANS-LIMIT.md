# k-means limits

Assumes spherical equal-variance blobs. Fails on elongated, nested, or unequal clusters.
Needs k chosen ahead. Init can strand empty lists (src/ivf.py keeps stale centroid then).
Lloyd is a local min. Outliers pull means. Cosine-on-sparse TF-IDF is not the textbook L2 ball.
On tens of rag files the coarse lists add miss risk vs brute rag_vec.
