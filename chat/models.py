from typing import List

import ormar
import datetime

from db import MainMeta
from user.models import User


class Conversation(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=255)
    description: str = ormar.Text()
    user: List[User] = ormar.ManyToMany(User)


class Message(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    text: str = ormar.Text(nullable=False)
    user: User = ormar.ForeignKey(User)
    conversation: Conversation = ormar.ForeignKey(Conversation)
    date_created: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)

