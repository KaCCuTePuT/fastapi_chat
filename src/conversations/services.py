import jwt
from fastapi import HTTPException
from starlette.status import HTTP_403_FORBIDDEN

from config import base_settings
from src.user.schemas import TokenPayload


def get_current_websocket_user(token):

    try:
        payload = jwt.decode(token, base_settings.SECRET_KEY, algorithms=[base_settings.ALGORITHM])
        user = TokenPayload(**payload)
        return user
    except jwt.PyJWTError:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials")
