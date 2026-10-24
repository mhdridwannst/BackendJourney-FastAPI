from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.auth import LoginRequest, Token
from app.security import create_access_token
from app.services import user_service

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=Token)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = user_service.authenticate_user(db, data.email, data.password)
    if user is None:
        raise HTTPException(
            status_code=401, detail="Email atau password salah")
    return Token(access_token=create_access_token(user.id))
