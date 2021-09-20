import datetime
from typing import Optional, List

from pydantic import BaseModel, UUID4


class UserForChat(BaseModel):
    id: UUID4
    username: str


class UserForMessage(BaseModel):
    id: UUID4


class MessagesForConvs(BaseModel):
    text: str
    user: UserForChat
    date_created: datetime.datetime


class ConversationOut(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    users: List[UserForChat]
    messages: List[MessagesForConvs]


class ConversationCreate(BaseModel):
    title: str
    description: str
