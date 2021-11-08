from fastapi import HTTPException
from ormar import NoMatch

from src.friends.models import Friend
from src.user.models import User


class CRUDFriend:

    @staticmethod
    async def create(friend, user):
        try:
            my_friend = await User.objects.get(phone=friend.phone)
        except NoMatch:
            raise HTTPException(status_code=404, detail='Пользователь с таким номером не зарегистрирован')
        if my_friend.id == user.user_id:
            raise HTTPException(status_code=400, detail='Вы не можете добавить самого себя в друзья :)')
        new_friend = await Friend.objects.get_or_none(user=user.user_id, friend=my_friend)
        if new_friend:
            raise HTTPException(status_code=400, detail='Этот пользователь уже есть у вас в друзьях')
        else:
            await Friend.objects.create(user=user.user_id, friend=my_friend)
        return f'Вы добавили {friend.phone} в друзья'

    @staticmethod
    async def delete(db_id):
        db_friend = await Friend.objects.get(id=db_id)
        await db_friend.delete()
        return f'Пользователь был удален из друзей'
