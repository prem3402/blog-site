from app.models import Users
from fastapi import APIRouter, status, HTTPException
from app.schema import User, UserResponse
from app.db import SessionDep

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(user: User, session: SessionDep):
    db_user = Users(**user.model_dump())
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@router.get("/{id}", response_model=UserResponse)
def get_user(id: int, session: SessionDep):
    user = session.get(Users, id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"The user with id {id} not found!",
        )
    return user

