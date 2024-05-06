from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from .schemas import UserCreate, UserUpdate
from ...db.model import User


async def create_user(db: AsyncSession, user_data: UserCreate) -> User:
    db_user = User(email=user_data.email, hashed_password=user_data.password, name=user_data.name)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()


def update_user(db: Session, user_id: int, user: UserUpdate) -> User:
    db_user = get_user(db, user_id)
    if db_user:
        db_user.email = user.email
        db_user.name = user.name
        db.commit()
        db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
