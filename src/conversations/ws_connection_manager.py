from fastapi import WebSocket
from fastapi.encoders import jsonable_encoder

from src.base.permissions import Permission
from src.conversations.models import Conversation
from src.messages.models import Message


class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[WebSocket] = dict()

    async def connect(self, conv_id, user, websocket: WebSocket):
        await websocket.accept()
        if user.user_id not in self.active_connections:
            self.active_connections.update({user.user_id: websocket})
        my_conv = await Conversation.objects.select_related(['messages__user', 'users']).get(id=conv_id)
        if Permission.is_conv_member(user, my_conv):
            messages = await Message.objects.select_related('user').all(conversation=conv_id)
            await websocket.send_json(jsonable_encoder(messages))

    def disconnect(self, user):
        self.active_connections.pop(user.user_id, None)

    async def broadcast(self):
        last_message = await Message.objects.select_related('user').get()
        for connection in self.active_connections.values():
            await connection.send_json(jsonable_encoder(last_message))
            print(jsonable_encoder(last_message))


manager = ConnectionManager()
