from typing import Optional, Union, Dict

import ormar
from db import MainMeta

from src.user.models import User


class Friend(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    user: Optional[Union[User, Dict]] = ormar.ForeignKey(User, related_name="user")
    friend: Optional[Union[User, Dict]] = ormar.ForeignKey(User, related_name="subscriber")
