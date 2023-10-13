"""Pydantic shemas"""
from datetime import datetime
from pydantic import BaseModel


class NumQuestins(BaseModel):
    """Count request questions"""
    num: int = 1


class Questions(BaseModel):
    """Validate Questions"""
    id: int
    answer: str
    question: str
    created_at: datetime | None
