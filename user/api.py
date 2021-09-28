from fastapi import APIRouter

from .schemas import UserCreate
from .services import create_user, create_token


user_router = APIRouter(tags=["auth"])


@user_router.post('/auth')
async def my_auth(user: UserCreate):
    if user.verification_code1 == user.verification_code2:
        new_user = await create_user(user)
        my_token = create_token(new_user.id)
        return my_token
    else:
        return 'Коды не совпадают'
