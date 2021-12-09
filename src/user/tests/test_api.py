import pytest
from httpx import AsyncClient

from config import test_settings


@pytest.mark.asyncio
async def test_creating_user():
    async with AsyncClient(**test_settings.HTTPX_CLIENT_SETTINGS) as ac:
        response = await ac.post('', json=test_settings.DATA_FOR_GETTING_TOKEN1)
    assert response.status_code == 200
