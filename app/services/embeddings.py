"""Wrapper for Gemini/Google Embeddings (text-embedding-004)."""
from app.config.settings import settings

try:
    import google.generativeai as genai
    genai.configure(api_key=settings.GOOGLE_API_KEY)
except Exception:
    genai = None

try:
    import pinecone
    pinecone.init(api_key=settings.PINECONE_API_KEY, environment=settings.PINECONE_ENV)
    pinecone_index = pinecone.Index(settings.PINECONE_INDEX)
except Exception:
    pinecone = None
    pinecone_index = None


def embed_text(text: str):
    if genai is None:
        raise RuntimeError("google.generativeai library not available or GOOGLE_API_KEY not set")

    # Use the correct Gemini embedding API
    resp = genai.embed_content(
        model="models/text-embedding-004",  # correct model path
        content=text
    )

    return resp["embedding"]


def embed_and_store_chunks(chunks: list):
    if pinecone_index is None:
        raise RuntimeError("Pinecone index not initialized — check PINECONE_API_KEY and PINECONE_ENV")

    vectors = []
    for chunk in chunks:
        emb = embed_text(chunk['text'])
        vectors.append((chunk['id'], emb, chunk['meta']))

    pinecone_index.upsert(vectors)
    return True


def embed_query(query: str):
    return embed_text(query)



