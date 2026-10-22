from fastapi import APIRouter

from app.schemas.user import UserCreate
from app.services import user_service

router = APIRouter()


@router.post("/users", status_code=201)
def create_user(user: UserCreate):
    return user_service.create_user(user)
