from pydantic import BaseModel
from typing import Any, Optional


class UserCreate(BaseModel):
    phone: str
    verification_code1: str
    verification_code2: str


class UserOut(BaseModel):
    id: int
    username: Optional[str] = None
    phone: str
    avatar: Optional[str] = None


class TokenPayload(BaseModel):
    user_id: int = None
