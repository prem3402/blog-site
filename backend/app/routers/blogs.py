from fastapi import APIRouter, HTTPException, status, Response
from app.db import SessionDep
from app.models import Blogs
from sqlmodel import select
from app.schema import BlogCreate, BlogsResponse
from typing import List

router = APIRouter(prefix="/blogs", tags=["Blogs"])


@router.get("/", response_model=List[BlogsResponse])
def get_blogs(session: SessionDep):

    blogs = session.exec(select(Blogs)).all()

    return blogs


@router.get("/{id}", response_model=BlogsResponse)
def get_blog(id: int, session: SessionDep):
    blog = session.get(Blogs, id)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found!",
        )

    return blog


@router.post("/", response_model=BlogsResponse, status_code=status.HTTP_201_CREATED)
def create_blog(blog: BlogCreate, session: SessionDep):

    db_blog = Blogs(**blog.model_dump())

    session.add(db_blog)
    session.commit()
    session.refresh(db_blog)
    return db_blog


@router.delete("/{id}")
def delete_blog(id: int, session: SessionDep):
    post = session.get(Blogs, id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The blog with id {id} not found!",
        )
    session.delete(post)
    session.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=BlogsResponse)
def update_blog(id: int, blog: BlogCreate, session: SessionDep):
    db_blog = session.get(Blogs, id)
    if not db_blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The blog with id {id} not found",
        )
    db_blog.title = blog.title
    db_blog.content = blog.content
    session.commit()
    session.refresh(db_blog)
    return db_blog
