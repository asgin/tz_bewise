from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import *
from typing import Generator

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)
session = sessionmaker(bind=engine)

def get_db() -> Generator:
    db = session()
    try:
        yield db
    finally:
        db.close()