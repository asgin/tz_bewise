from typing import Generator
from fastapi import Depends, FastAPI
from fastapi.responses import JSONResponse
from src.db.database import get_db
from src.db.models import Question
import requests

app = FastAPI(
    title="tz_bewise",
)

@app.post("/questions")
def create_question(questions_num: int, db: Generator = Depends(get_db)) -> JSONResponse:
    flag = False
    while flag == False:
        questions = requests.get(f"https://jservice.io/api/random?count={questions_num}").json()
        questions_id = [i['id'] for i in questions]
        value = db.query(Question).filter(Question.question_id.in_(questions_id)).all()
        if len(value) != 0:
            flag = False
        else:
            if len(questions) == 0:
                return {}
            else:
                db.add_all([Question(question_id=i['id'], question_text=i['question'], answer_text=i['answer'], date_created_question=i['created_at']) for i in questions])
                db.commit()
                return {"last_question:": questions[-1]}