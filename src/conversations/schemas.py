from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserForChat(BaseModel):
    id: int
    username: Optional[str] = None
    phone: str


class UserForMessage(BaseModel):
    id: int


class MessagesForConvs(BaseModel):
    text: str
    user: UserForChat
    date_created: datetime


class ConversationOut(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    users: list[UserForChat]
    messages: list[MessagesForConvs]


class ConversationCreate(BaseModel):
    title: str
    description: str
