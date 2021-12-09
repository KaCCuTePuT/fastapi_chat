from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect

from src.messages.models import Message
from src.user.models import User
from src.user.services import get_current_user
from .models import Conversation
from .schemas import ConversationCreate
from src.conversations.ws_connection_manager import manager
from src.conversations.services import get_current_websocket_user

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


@conv_router.websocket("/ws/{conv_id}/{token}")
async def conversation_websocket(
        websocket: WebSocket,
        conv_id: int,
        token: str,
):
    user = get_current_websocket_user(token)

    await manager.connect(conv_id, user, websocket)
    try:
        while True:
            message_text = await websocket.receive_text()
            await Message.objects.create(
                user=user.user_id,
                text=message_text,
                conversation=conv_id
            )
            await manager.broadcast()

    except WebSocketDisconnect:
        manager.disconnect(user)
