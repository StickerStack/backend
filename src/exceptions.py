from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse


class Initial500(HTTPException):
    pass


def initial500_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Server Error"}
    )
