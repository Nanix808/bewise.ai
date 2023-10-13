"""CRUD Operations"""
from sqlalchemy.ext.asyncio import AsyncSession
import requests

from .shemas import Questions
from .models import Questions as DBQuestions


class QuestionsCRUD:
    """CRUD Operations"""

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    def create_questions(self, num: int) -> Questions:
        """Create and ADD Questions"""
        all_id = self.get_all_id()
        all_new_questions = self.get_questions_serialize_recursive(num, all_id)
        for questions in all_new_questions:
            crete_obj = DBQuestions(**questions.model_dump())
            self.db_session.add(crete_obj)
        self.db_session.commit()
        return all_new_questions[-1]

    def get_all_id(self) -> set:
        """GET ALL ID FROM DB"""
        return {a[0] for a in self.db_session.query(DBQuestions.id).all()}

    def get_questions_serialize_recursive(self, num: int, all_id: set) -> list:
        """Recursive method -- request url"""
        url = f'https://jservice.io/api/random?count={num}'
        response = requests.get(url, timeout=5)
        res = []
        for questions in response.json():
            if questions['id'] in all_id:
                print("Repeat")
                res.append(self.get_questions_serialize_recursive(1, all_id)[0])
                continue
            res.append(Questions(**questions))
        return res
