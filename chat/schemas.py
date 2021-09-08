from typing import Optional, List

from pydantic import BaseModel
# from ..user.schemas import User


class UserForChat(BaseModel):
    username: str


class ConversationOut(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    user: List[str]


class ConversationCreate(BaseModel):
    title: str
    description: str
    # user: UserForChat


class MessageOut(BaseModel):
    id: Optional[int] = None
    text: str
    user: str
    date_created: str


class MessageCreate(BaseModel):
    text: str
    conversation: int
