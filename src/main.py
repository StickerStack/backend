from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from auth.auth import auth_backend
from auth.db import User
from auth.schemas import UserCreate, UserRead, UserUpdate
from auth.manager import get_user_manager
from auth.router import router as auth_router
from exceptions import Initial500, initial500_exception_handler


app = FastAPI(title='StickerStack')

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["AUTH, поле username это почта пользователя"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Регистрация"],
)

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users, последние 3 ручки для админа"],
)

# app.include_router(
#     fastapi_users.get_reset_password_router(),
#     prefix="/auth",
#     tags=["auth"],
# )


app.include_router(auth_router)

app.add_exception_handler(Initial500, initial500_exception_handler)
