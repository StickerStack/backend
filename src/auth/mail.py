from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel
from random import randbytes
from hashlib import sha256


# class EmailSchema(BaseModel):
#     email: EmailStr


# conf = ConnectionConfig(
#     MAIL_USERNAME="",
#     MAIL_PASSWORD="",
#     MAIL_FROM="",
#     MAIL_PORT=25,
#     MAIL_SERVER="",
#     MAIL_FROM_NAME="",
#     MAIL_STARTTLS=False,
#     MAIL_SSL_TLS=True,
#     USE_CREDENTIALS=True,
#     VALIDATE_CERTS=True
# )


# async def send_email_ver(
#     email: EmailStr,
#     url: str
# ):
#     html = f"<p>{url}</p>"

#     message = MessageSchema(
#         subject="Fastapi-Mail module",
#         recipients=[email],
#         body=html,
#         subtype=MessageType.html)

#     fm = FastMail(conf)
#     await fm.send_message(message)


def get_verification_code():
    token = randbytes(10)
    hashedCode = sha256()
    hashedCode.update(token)
    verification_code = hashedCode.hexdigest()
    return verification_code
