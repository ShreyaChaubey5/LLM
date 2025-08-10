from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.document_parser import parse_and_chunk
from app.services.embeddings import embed_and_store_chunks

router = APIRouter()

@router.post("/document")
async def upload_document(file: UploadFile = File(...)):
    """Upload a PDF/Doc/Email, parse it, chunk it, embed and store vectors."""
    content = await file.read()
    try:
        chunks = parse_and_chunk(content, filename=file.filename)
        if not chunks:
            raise HTTPException(status_code=400, detail="No text extracted from file")

        embed_and_store_chunks(chunks)
        return {"status": "ok", "stored_chunks": len(chunks)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
