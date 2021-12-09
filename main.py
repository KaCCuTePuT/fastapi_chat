from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import database


from config.base_settings import ORIGINS
from src.user.api import user_router
from src.conversations.api import conv_router
from src.friends.api import friends_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

# metadata.create_all(engine)
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
app.include_router(friends_router)

