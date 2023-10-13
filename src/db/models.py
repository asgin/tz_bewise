from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, nullable=False)
    question_text = Column(String, nullable=False)
    answer_text = Column(String, nullable=False)
    date_created_question = Column(String, nullable=False)