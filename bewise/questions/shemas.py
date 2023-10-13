from pydantic import BaseModel
from datetime import datetime


class NumQuestins(BaseModel):
    num: int


class Questions(BaseModel):
    id: int
    answer: str
    question: str
    created_at: datetime | None
