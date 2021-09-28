from fastapi import FastAPI
from db import database, metadata, engine


from user.api import user_router
from conversations.api import conv_router
from messages.api import message_router
app = FastAPI()


metadata.create_all(engine)
app.state.database = database


@app.on_event('startup')
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event('shutdown')
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()

app.include_router(user_router)
app.include_router(conv_router)
app.include_router(message_router)

