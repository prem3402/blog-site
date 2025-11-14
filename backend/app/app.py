from fastapi import FastAPI, Response
from app.db import create_db_and_tables

from app.routers import blogs

from app.models import Blogs

app = FastAPI()


@app.on_event("startup")
def on_start():
    create_db_and_tables()


@app.get("/")
def index():
    return {"ping": "pong"}


app.include_router(blogs.router)
