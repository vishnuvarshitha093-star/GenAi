from pydantic import BaseModel, EmailStr

from app.models.enums import RoleEnum


class UserCreate(BaseModel):
    email: EmailStr
    full_name: str
    password: str
    role: RoleEnum = RoleEnum.USER


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    role: RoleEnum

    class Config:
        from_attributes = True
