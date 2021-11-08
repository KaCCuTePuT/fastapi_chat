from pydantic import BaseModel

from src.user.schemas import UserOut


class FriendCreateAndDelete(BaseModel):
    phone: str


class FriendList(BaseModel):
    id: int
    friend: UserOut
