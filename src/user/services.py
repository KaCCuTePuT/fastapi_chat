import jwt
from datetime import datetime, timedelta

from fastapi import HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from starlette.status import HTTP_403_FORBIDDEN
from .schemas import TokenPayload, UserCreate
from .models import User
import settings


reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/api/v1/login/access-token")


def create_token(user_id) -> dict:
    str_user_id = str(user_id)
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": create_access_token(
            data={"user_id": str_user_id}, expires_delta=access_token_expires
        ),
        "token_type": "Bearer",
    }


def create_access_token(data: dict, expires_delta: timedelta = None):
    """Создание токена"""
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire, "sub": settings.ACCESS_TOKEN_JWT_SUBJECT})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


async def create_user(user: UserCreate) -> User:
    _user = await User.objects.get_or_create(phone=user.phone)
    return _user


def get_current_user(token: str = Security(reusable_oauth2)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        token_data = TokenPayload(**payload)
    except jwt.PyJWTError:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials")
    return token_data
