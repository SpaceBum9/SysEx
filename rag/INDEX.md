# Vector index

SysEx index = rebuild TF-IDF over rag/*.md in process (src/rag_vec.py).
No Pinecone, Weaviate, Chroma, Qdrant, OpenAI embeddings.
No stored ANN. Optional local dump rag/.index.json is gitignored if added later.
Re-index = run query() again. execute=false.
