import pytest
from httpx import AsyncClient

import settings

@pytest.mark.asyncio
async def test_creating_message():
    data_for_creating_conv = {
        "title": "testTitle",
        "description": "testDesc"
    }
    data_for_creating_message = {
        "text": "testMessage",
        "conversation": "1"
    }
    async with AsyncClient(**settings.HTTPX_CLIENT_SETTINGS) as ac:
        token_response = await ac.post('/auth', json=settings.DATA_FOR_GETTING_TOKEN1)
        token = token_response.json().get('access_token')
        headers = {
            'Authorization': f'Bearer {token}'
        }
        # Сначала создадим беседу
        await ac.post('/conv/create', json=data_for_creating_conv, headers=headers)
        response_creating_message = await ac.post('/message/create/1', json=data_for_creating_message, headers=headers)
    assert response_creating_message.status_code == 201


@pytest.mark.asyncio
async def test_creating_message_without_token():
    data_for_creating_message = {
        "text": "testMessage",
        "conversation": "1"
    }
    async with AsyncClient(**settings.HTTPX_CLIENT_SETTINGS) as ac:
        response_creating_message = await ac.post('/message/create/1', json=data_for_creating_message)
    assert response_creating_message.status_code == 401


@pytest.mark.asyncio
async def test_creating_message_by_non_member():
    data_for_creating_message = {
        "text": "testMessage",
        "conversation": "1"
    }
    async with AsyncClient(**settings.HTTPX_CLIENT_SETTINGS) as ac:
        token_response = await ac.post('/auth', json=settings.DATA_FOR_GETTING_TOKEN1)
        token = token_response.json().get('access_token')
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response_creating_message = await ac.post('/message/create/1', json=data_for_creating_message, headers=headers)
    assert response_creating_message.status_code == 201
