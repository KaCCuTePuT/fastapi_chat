import ormar

from db import MainMeta


class User(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    username: str = ormar.String(max_length=100, unique=True, nullable=True)
    phone: str = ormar.String(max_length=12, unique=True)
    avatar = ormar.String(max_length=500, nullable=True)
    is_superuser = ormar.Boolean(default=False, nullable=False)
