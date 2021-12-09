from typing import Optional

from pydantic import BaseModel
from src.user.schemas import UserOut


class MessageOut(BaseModel):
    id: Optional[int] = None
    text: str
    user: UserOut
    date_created: str


class MessageCreate(BaseModel):
    text: str
    conversation: int
