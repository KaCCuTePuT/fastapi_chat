from fastapi import HTTPException

from src.conversations.models import Conversation
from src.user.models import User


class Permission:

    @staticmethod
    def is_conv_member(user: User, my_conv: Conversation) -> bool:
        list_of_id = [u['id'] for u in my_conv.dict()['users']]
        if user.user_id in list_of_id:
            return True
        else:
            raise HTTPException(status_code=403, detail='Вы не являетесь членом беседы')

    @staticmethod
    def is_conv_creator(user: User, my_conv: Conversation) -> bool:
        if user.user_id == my_conv.creator.id:
            return True
        else:
            raise HTTPException(status_code=403, detail='Вы не являетесь создателем беседы')
