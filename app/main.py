from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import upload, query
from app.config.settings import settings

app = FastAPI(title="Bajaj LLM Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173/"],  # adjust for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router, prefix="/upload", tags=["upload"])
app.include_router(query.router, prefix="/query", tags=["query"])

@app.get("/")
async def root():
    return {"status": "up", "service": "bajaj-llm-backend"}
