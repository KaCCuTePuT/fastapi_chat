from conversations.models import Conversation
from user.models import User


async def is_conv_member(user: User, my_conv: Conversation) -> bool:
    list_of_id = [u['id'] for u in my_conv.dict()['users']]
    return user.user_id in list_of_id


async def is_conv_creator(user: User, my_conv: Conversation) -> bool:
    return user.user_id == my_conv.creator.id
