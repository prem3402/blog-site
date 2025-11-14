from pydantic import BaseModel
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
