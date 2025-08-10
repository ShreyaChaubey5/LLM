from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.embeddings import embed_query
from app.services.retrieval import retrieve_top_k
from app.services.reasoning import call_gemini_reasoner

router = APIRouter()

class QueryIn(BaseModel):
    query: str
    top_k: int = 5

@router.post("/")
async def handle_query(qin: QueryIn):
    try:
        q_emb = embed_query(qin.query)
        matches = retrieve_top_k(q_emb, top_k=qin.top_k)
        response = call_gemini_reasoner(qin.query, matches)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
