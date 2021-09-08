from typing import Optional

from fastapi import APIRouter, Depends, Header, Request

from .models import Conversation, Message
from .schemas import ConversationCreate, ConversationOut, MessageCreate
from user.models import User
from user.routers import fastapi_users

chat_router = APIRouter(prefix='/chat', tags=['chat'])


@chat_router.post('/create_conv', status_code=201)
async def create_conversation(
        conv: ConversationCreate,
        user: User = Depends(fastapi_users.current_user())
):
    my_user = await User.objects.get(id=user.id)
    new_conv = await Conversation.objects.create(
        title=conv.title,
        description=conv.description
    )
    await new_conv.user.add(my_user)
    return new_conv


@chat_router.post('/create_message', status_code=201)
async def create_message(
        msg: MessageCreate,
        user: User = Depends(fastapi_users.current_user())
):
    new_msg = await Message.objects.create(
        user=user.id,
        text=msg.text,
        conversation=msg.conversation
    )
    return new_msg

