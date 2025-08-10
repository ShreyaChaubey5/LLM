import faiss
import numpy as np

# In-memory FAISS index
embedding_dim = 384  # all-MiniLM-L6-v2 embedding size
index = faiss.IndexFlatL2(embedding_dim)
documents = []

def upsert_embeddings(text_chunks, embeddings):
    """
    Store embeddings and corresponding text chunks in FAISS.
    """
    global documents
    index.add(np.array(embeddings).astype('float32'))
    documents.extend(text_chunks)

def query_embeddings(query_embedding, top_k=5):
    """
    Search for the most similar chunks.
    """
    if index.ntotal == 0:
        return []
    D, I = index.search(np.array([query_embedding]).astype('float32'), top_k)
    return [documents[i] for i in I[0]]
