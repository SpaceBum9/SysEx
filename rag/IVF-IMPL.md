# IVF impl

src/ivf.py trains k sparse centroids on rag_vec TF-IDF and searches nprobe lists.
In-process. No FAISS. execute=false. On this corpus brute rag_vec is enough; IVF is the algorithm sketch.
