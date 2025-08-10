import uuid
import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from services.text_extractor import extract_text
from services.chunker import chunk_text
from services.embedder import get_embeddings
from services.vector_store import upsert_embeddings
from services.retriever import retrieve_relevant_chunks
from services.llm_reasoner import generate_decision
from models.query_models import UploadResponse, QueryRequest, QueryResponse

app = FastAPI(title="LLM Retrieval API")

# Allow CORS for frontend dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace "*" with your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploaded_docs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Store mapping of file_id -> document name (for reference)
file_registry = {}

@app.post("/upload", response_model=UploadResponse)
async def upload_file(file: UploadFile = File(...)):
    try:
        ext = os.path.splitext(file.filename)[-1].lower()
        if ext not in [".pdf", ".doc", ".docx", ".txt"]:
            raise HTTPException(status_code=400, detail="Unsupported file type.")

        # Save file locally
        file_id = str(uuid.uuid4())
        file_path = os.path.join(UPLOAD_DIR, f"{file_id}{ext}")
        with open(file_path, "wb") as f:
            f.write(await file.read())

        # Extract text
        text = extract_text(file_path)

        # Chunk text
        chunks = chunk_text(text)

        # Embed chunks
        embeddings = get_embeddings(chunks)

        # Store embeddings in Pinecone
        upsert_embeddings(embeddings, chunks, file_id)

        # Save mapping
        file_registry[file_id] = file.filename

        return UploadResponse(file_id=file_id, message="File uploaded and indexed successfully.")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/query", response_model=QueryResponse)
async def query_doc(request: QueryRequest):
    try:
        if not request.file_id:
            raise HTTPException(status_code=400, detail="file_id is required.")

        # Retrieve relevant chunks
        relevant_chunks = retrieve_relevant_chunks(request.query)

        # Get decision from LLM
        result = generate_decision(request.query, relevant_chunks)

        return QueryResponse(**result)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
async def root():
    return {"message": "LLM Retrieval API is running"}
