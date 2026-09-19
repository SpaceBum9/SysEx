# Vector DB alternatives

Pinecone Weaviate Qdrant Chroma Milvus pgvector LanceDB = hosted or extra daemon.
FAISS Annoy ScaNN = local libs, still a vendor bind for SysEx.
open_store() only accepts memory. Others raise vendor_live=false.
Retrieval for rag stays rag_vec / ivf / rag_query.
