import ormar
import datetime

from db import MainMeta
from src.user.models import User
from src.conversations.models import Conversation


class Message(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    text: str = ormar.Text(nullable=False)
    user: User = ormar.ForeignKey(User)
    conversation: Conversation = ormar.ForeignKey(Conversation, related_name='messages')
    date_created: datetime.datetime = ormar.DateTime(default=datetime.datetime.now)
