from fastapi import Depends, APIRouter

from user.services import get_current_user
from user.models import User
from .models import Message
from .schemas import MessageCreate
from conversations.models import Conversation
from conversations.schemas import ConversationOut


message_router = APIRouter(prefix='/message', tags=['chat'])


@message_router.post('/create/{conv_id}', status_code=201)
async def create_message(
        conv_id,
        msg: MessageCreate,
        user: User = Depends(get_current_user)
):
    my_conv = await Conversation.objects.prefetch_related('users').get(id=conv_id)
    list_of_id = [u['id'] for u in my_conv.dict()['users']]
    if user.user_id in list_of_id:
        await Message.objects.create(
            user=user.user_id,
            text=msg.text,
            conversation=msg.conversation
        )
    else:
        return 'Пользователя нет в беседе'
    return 'Cообщение было создано'


