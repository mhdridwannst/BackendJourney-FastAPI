from pydantic import BaseModel, EmailStr, Field
from pydantic import ConfigDict


class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    email: EmailStr
    age: int = Field(ge=17, le=100)


class UserUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=50)
    email: EmailStr | None = None
    age: int | None = Field(default=None, ge=17, le=100)


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: EmailStr
    age: int
