"""This routers"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from bewise.database import get_db
from .shemas import NumQuestins, Questions
from .service import QuestionsCRUD


questions_router = APIRouter()

@questions_router.post("/add", status_code=201, response_model = Questions)
def create_resume(body: NumQuestins, db : Session = Depends(get_db)) -> Questions:
    """router add Questions"""
    with db as session:
        with session.begin():
            num = body.num
            if num:
                questions_crud = QuestionsCRUD(session)
                response = questions_crud.create_questions(num=num)
                print(response)
            return response
