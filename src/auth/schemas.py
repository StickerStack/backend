from fastapi_users import schemas
from typing import Optional


class UserRead(schemas.BaseUser[int]):
    id: int
    username: Optional[str]
    bio: Optional[str]


class UserCreate(schemas.BaseUserCreate):
    bio: Optional[str]


class UserUpdate(schemas.BaseUserUpdate):
    username: Optional[str]
    bio: Optional[str]
