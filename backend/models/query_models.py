from pydantic import BaseModel
from typing import List, Optional

# Response after uploading a file
class UploadResponse(BaseModel):
    file_id: str
    message: str

# Request body for querying
class QueryRequest(BaseModel):
    query: str
    file_id: Optional[str] = None  # ID to link with stored document embeddings

# Response after querying
class QueryResponse(BaseModel):
    decision: str
    clauses: List[str]
    justification: List[str]
