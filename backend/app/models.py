from sqlmodel import Field, SQLModel
from datetime import datetime
from sqlalchemy import Column, TIMESTAMP, func
from pydantic import EmailStr


class Blogs(SQLModel, table=True):
    __tablename__ = "blogs"
    id: int = Field(primary_key=True)
    title: str
    content: str
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(TIMESTAMP(timezone=True), server_default=func.now()),
    )


class Users(SQLModel, table=True):
    __tablename__ = "users"
    id: int = Field(primary_key=True)
    email: str = Field(unique=True)
    password: str
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(TIMESTAMP(timezone=True), server_default=func.now()),
    )
