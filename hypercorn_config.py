import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve

from main import app

config = Config()
config.bind = ["localhost:8000"]

asyncio.run(serve(app, config))
