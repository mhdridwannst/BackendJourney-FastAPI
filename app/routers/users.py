from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.services import user_service


router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", status_code=201, response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)


@router.get("/", response_model=list[UserRead])
def list_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return user_service.list_users(db)


@router.get("/me", response_model=UserRead)
def read_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user),):
    if current_user.id != user_id:
        raise HTTPException(
            status_code=403, detail="Hanya pemilik yang boleh mengambil data user!")
    user = user_service.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")
    return user


@router.patch("/{user_id}", response_model=UserRead)
def patch_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user),):
    if current_user.id != user_id:
        raise HTTPException(
            status_code=403, detail="Tidak boleh mengubah akun orang lain!")
    user = user_service.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")

    update_dict = user_data.model_dump(exclude_unset=True)
    if not update_dict:
        raise HTTPException(
            status_code=400, detail="Tidak ada data yang diberikan untuk diperbarui")

    return user_service.update_user(db, user, update_dict)


@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user),):
    if current_user.id != user_id:
        raise HTTPException(
            status_code=403, detail="Tidak boleh menghapus akun orang lain!")
    user = user_service.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")
    user_service.delete_user(db, user)
