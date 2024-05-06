from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    name: str


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    name: str | None = None


class UserRead(UserBase):
    id: int

    class Config:
        from_attributes = True
