from sqlmodel import Field, SQLModel
from datetime import datetime
from sqlalchemy import Column, TIMESTAMP, func


class Blogs(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str
    content: str
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        sa_column=Column(TIMESTAMP(timezone=True), server_default=func.now()),
    )
