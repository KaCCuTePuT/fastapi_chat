import ormar

from fastapi_users.db import OrmarBaseUserModel, OrmarUserDatabase

from db import MainMeta
from user.schemas import UserDB


class User(OrmarBaseUserModel):
    class Meta(MainMeta):
        pass

    username = ormar.String(unique=True, nullable=False, max_length=100)
    phone = ormar.String(unique=True, nullable=False, min_length=11, max_length=11)


user_db = OrmarUserDatabase(UserDB, User)
