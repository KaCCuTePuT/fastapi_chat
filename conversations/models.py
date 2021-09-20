import ormar

from typing import List

from db import MainMeta
from user.models import User


class Conversation(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=255)
    description: str = ormar.Text()
    creator: User = ormar.ForeignKey(User, related_name='created_convs')
    users: List[User] = ormar.ManyToMany(User, related_name='my_convs')




