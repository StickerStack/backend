from auth.auth import auth_backend
from auth.db import User
from auth.manager import get_user_manager
from database import get_async_session
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_users import FastAPIUsers
from sqlalchemy import update, select
from sqlalchemy.ext.asyncio import AsyncSession
from auth.models import user


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()


router = APIRouter(
    prefix='/auth',
    tags=['verify']
)


@router.get('/verifyemail/{token}')
async def verify_email(
    token: str,
    session: AsyncSession = Depends(get_async_session)
):
    query = select(user).where(user.c.email_token == token)
    result = await session.execute(query)
    if result.one_or_none():
        verify_query = update(user).where(user.c.email_token == token).values(
            is_verified=True
        )
        await session.execute(verify_query)
        await session.commit()
        return {
            "status": "success",
            "message": "Account verified successfully"
        }
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Invalid verification code"
    )
