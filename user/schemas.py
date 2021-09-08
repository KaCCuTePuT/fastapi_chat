from fastapi_users import models


class User(models.BaseUser):
    username: str
    phone: str


class UserCreate(models.BaseUserCreate):
    username: str
    phone: str
    code: int


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass

