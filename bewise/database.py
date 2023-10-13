from typing import Generator
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine

from settings import settings


Base = declarative_base()
engine = create_engine(settings.DATABASE_URL_psycopg)
session_maker = sessionmaker(engine, expire_on_commit=False)


def get_db() -> Generator:
    try:
        session: Session = session_maker()
        yield session
    finally:
        session.close()


def create_db():
    Base.metadata.create_all(bind=engine, checkfirst=True)
