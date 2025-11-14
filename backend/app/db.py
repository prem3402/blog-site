from sqlmodel import create_engine, Session, SQLModel
from typing import Annotated
from fastapi import Depends

URL = "postgresql://postgres:root@localhost/blog"
engine = create_engine(URL)


def get_session():
    with Session(engine) as session:
        yield session


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


SessionDep = Annotated[Session, Depends(get_session)]
