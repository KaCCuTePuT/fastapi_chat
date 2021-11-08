import pytest
from httpx import AsyncClient

import settings


@pytest.mark.asyncio
async def test_creating_user():
    async with AsyncClient(**settings.HTTPX_CLIENT_SETTINGS) as ac:
        response = await ac.post('', json=settings.DATA_FOR_GETTING_TOKEN1)
    assert response.status_code == 200
