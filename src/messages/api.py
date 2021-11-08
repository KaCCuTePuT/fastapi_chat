from fastapi import Depends, APIRouter

from src.user.services import get_current_user
from src.user.models import User
from src.base.permissions import Permission
from .models import Message
from .schemas import MessageCreate
from src.conversations.models import Conversation

message_router = APIRouter(prefix='/message', tags=['chat'])


@message_router.post('/create/{conv_id}', status_code=201)
async def create_message(
        conv_id,
        msg: MessageCreate,
        user: User = Depends(get_current_user)
):
    my_conv = await Conversation.objects.prefetch_related('users').get(id=conv_id)
    if Permission.is_conv_member(user, my_conv):
        await Message.objects.create(
            user=user.user_id,
            text=msg.text,
            conversation=msg.conversation
        )
    return 'Cообщение было создано'


