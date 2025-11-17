from pydantic import BaseModel, EmailStr
from datetime import datetime


class BlogsBase(BaseModel):

    title: str
    content: str


class BlogCreate(BlogsBase):
    pass


class BlogsResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime


class User(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr
