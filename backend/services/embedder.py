from sentence_transformers import SentenceTransformer

# Load a free, local embedding model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embeddings(text: str):
    """
    Generate embeddings for the given text using a local model.
    """
    return embedding_model.encode([text])[0].tolist()
