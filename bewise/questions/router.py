from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from .shemas import NumQuestins
from .service import QuestionsCRUD


questions_router = APIRouter()
      
        
@questions_router.post("/add", status_code=201)
def create_resume(body: NumQuestins, db : Session = Depends(get_db)) -> NumQuestins:
    with db as session:
        with session.begin():
            num = body.num
            if num:
                questions_crud = QuestionsCRUD(session)
                response = questions_crud.create_questions(num=num)
            return response