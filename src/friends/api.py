from fastapi import APIRouter, Depends

from src.user.models import User
from .models import Friend
from src.user.services import get_current_user
from .schemas import FriendCreateAndDelete, FriendList
from .crud import CRUDFriend
from ..conversations.models import Conversation

friends_router = APIRouter(prefix='/friends', tags=['friends'])


@friends_router.post('/add', status_code=201)
async def add_friend(
        friend: FriendCreateAndDelete,
        user: User = Depends(get_current_user)
):
    await CRUDFriend.create(friend, user)
    my_user = await User.objects.get(id=user.user_id)
    my_friend = await User.objects.get(phone=friend.phone)
    new_conv = await Conversation.objects.create(
        title=friend.phone,
        description=friend.phone,
        creator=my_user
    )
    await new_conv.users.add(my_user)
    await new_conv.users.add(my_friend)


@friends_router.delete('/delete/{db_id}', status_code=200)
async def add_friend(
        db_id,
        user: User = Depends(get_current_user)
):
    return await CRUDFriend.delete(db_id)


@friends_router.post('/me', response_model=list[FriendList])
async def my_friends_list(user: User = Depends(get_current_user)):
    return await Friend.objects.select_related(
        ['user', 'friend']
    ).filter(user=user.user_id).all()

