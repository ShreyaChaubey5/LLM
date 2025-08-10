from pydantic import BaseModel
from typing import List

class ClauseRef(BaseModel):
    id: str
    score: float = None

class DecisionOut(BaseModel):
    decision: str
    justification: str
    referenced_clauses: List[ClauseRef]
