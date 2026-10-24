from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

from app.models.user import User
from app.schemas.user import UserCreate


def create_user(db: Session, data: UserCreate) -> User:
    user = User(**data.model_dump())
    db.add(user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Email sudah terdaftar")
    db.refresh(user)
    return user


def update_user(db: Session, user: User, data: dict) -> User:
    for key, value in data.items():
        setattr(user, key, value)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Email sudah terdaftar")
    db.refresh(user)
    return user


def delete_user(db: Session, user: User) -> None:
    db.delete(user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409, detail="User masih memiliki order dan tidak bisa dihapus"
        )


def list_users(db: Session) -> list[User]:
    return list(db.scalars(select(User)).order_by(User.id).all())


def get_user(db: Session, user_id: int) -> User | None:
    return db.get(User, user_id)
