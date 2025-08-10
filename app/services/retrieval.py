"""Retrieve top-k matches from Pinecone."""
from app.config.settings import settings

try:
    import pinecone
    pinecone.init(api_key=settings.PINECONE_API_KEY, environment=settings.PINECONE_ENV)
    index = pinecone.Index(settings.PINECONE_INDEX)
except Exception:
    index = None

def retrieve_top_k(query_embedding, top_k: int = 5):
    if index is None:
        raise RuntimeError("Pinecone index not initialized")
    res = index.query(vector=query_embedding, top_k=top_k, include_metadata=True)
    matches = []
    for m in res['matches']:
        matches.append({
            'id': m['id'],
            'score': m['score'],
            'meta': m.get('metadata', {}),
        })
    return matches
