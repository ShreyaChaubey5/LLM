import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY", "")
    PINECONE_API_KEY: str = os.getenv("PINECONE_API_KEY", "")
    PINECONE_ENV: str = os.getenv("PINECONE_ENV", "")
    PINECONE_INDEX: str = os.getenv("PINECONE_INDEX", "policy-index")
    MONGO_URI: str = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    EMBEDDING_MODEL: str = os.getenv("EMBEDDING_MODEL", "text-embedding-004")
    REASONING_MODEL: str = os.getenv("REASONING_MODEL", "gemini-pro")
    MAX_CHUNK_CHARS: int = int(os.getenv("MAX_CHUNK_CHARS", "2000"))

settings = Settings()
