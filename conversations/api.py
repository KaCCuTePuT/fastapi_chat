from fastapi import APIRouter, Depends

from user.models import User
from user.services import get_current_user
from services import is_conv_member, is_conv_creator
from .models import Conversation
from .schemas import ConversationCreate, ConversationOut

conv_router = APIRouter(prefix='/conv', tags=['chat'])


@conv_router.post('/create', status_code=201)
async def create_conversation(
        conv: ConversationCreate,
        user: User = Depends(get_current_user)
):
    my_user = await User.objects.get(id=user.user_id)
    new_conv = await Conversation.objects.create(
        title=conv.title,
        description=conv.description,
        creator=my_user
    )
    await new_conv.users.add(my_user)
    return f'Беседа {conv.title} была создана'


@conv_router.post('/retrieve/{conv_id}', response_model=ConversationOut, status_code=200)
async def create_conversation(
        conv_id,
        user: User = Depends(get_current_user)
):
    my_conv = await Conversation.objects.select_related(['messages__user', 'users']).get(id=conv_id)
    if is_conv_member(user, my_conv):
        return my_conv


@conv_router.post('/update/{conv_id}', status_code=200)
async def change_conversation(
    conv_id,
    conv: ConversationCreate,
    user: User = Depends(get_current_user)
):
    my_conv = await Conversation.objects.get(id=conv_id)
    if is_conv_creator(user, my_conv):
        await my_conv.update(
            title=conv.title,
            description=conv.description
        )
    else:
        return 'Вы не являетесь создателем беседы'
    return 'Беседа была изменена'


@conv_router.post('/delete/{conv_id}', status_code=200)
async def delete_conversation(
    conv_id,
    user: User = Depends(get_current_user)
):
    my_conv = await Conversation.objects.select_related('messages').get(id=conv_id)
    if is_conv_creator(user, my_conv):
        await my_conv.messages.clear(keep_reversed=False)
        await my_conv.delete()
    else:
        return 'Вы не являетесь создателем беседы'
    return 'Беседа была удалена'








