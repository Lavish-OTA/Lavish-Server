from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from .crud import create_user, get_user, update_user, delete_user
from .schemas import UserCreate, UserRead, UserUpdate
from ..dependencies import get_current_user, get_db

user_router = APIRouter()


@user_router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user_endpoint(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db, user)


@user_router.get("/{user_id}", response_model=UserRead)
def read_user(user_id: int, current_user: UserRead = Depends(get_current_user)):
    """Retrieve a specific user"""
    return get_user(user_id)


@user_router.put("/{user_id}", response_model=UserRead)
def update_user_endpoint(user_id: int, user: UserUpdate, current_user: UserRead = Depends(get_current_user)):
    """Update an existing user"""
    return update_user(user_id, user)


@user_router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_endpoint(user_id: int, current_user: UserRead = Depends(get_current_user)):
    """Delete a user"""
    delete_user(user_id)
    return {"message": "User deleted successfully"}
