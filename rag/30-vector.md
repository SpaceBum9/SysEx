# Vector store

Active: in-memory TF-IDF over rag/*.md (src/rag_vec.py). Cosine. No persistence.
Not wired: Pinecone, Weaviate, Qdrant Cloud, OpenAI embeddings. Those are vendor_live.
Later local-only options if an operator machine installs them: sqlite-vec, faiss-cpu, chroma file mode. Still no keys in git.
Keyword path remains src/rag_query.py.
