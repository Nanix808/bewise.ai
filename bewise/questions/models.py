""" Models from DB"""
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column

from bewise.database import Base


class Questions(Base):
    """ Models Questions"""
    __tablename__ = 'questions'
    id : Mapped[int] = mapped_column(primary_key=True)
    answer : Mapped[str]
    question : Mapped[str]
    created_at: Mapped[datetime]
