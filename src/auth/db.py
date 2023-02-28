from datetime import datetime
from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Column, String, Boolean, Integer, TIMESTAMP
from database import get_async_session, Base
from .mail import get_verification_code


class User(SQLAlchemyBaseUserTable[int], Base):
    id: int = Column(Integer, primary_key=True, index=True)
    username: str = Column(
        String(length=320), unique=True, index=True, nullable=False)
    email: str = Column(
        String(length=320), unique=True, index=True, nullable=False)
    hashed_password: str = Column(String(length=1024), nullable=False)
    bio: str = Column(String, nullable=True)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)
    added = Column(TIMESTAMP, default=datetime.utcnow)
    email_token = Column(String, default=get_verification_code)


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
