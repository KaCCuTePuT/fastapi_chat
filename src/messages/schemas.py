from typing import Optional

from pydantic import BaseModel


class MessageOut(BaseModel):
    id: Optional[int] = None
    text: str
    user: str
    date_created: str


class MessageCreate(BaseModel):
    text: str
    conversation: int