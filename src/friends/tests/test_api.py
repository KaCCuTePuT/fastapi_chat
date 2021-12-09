import pytest
from httpx import AsyncClient

from config import test_settings


# В тестовой бд уже есть 2 пользователя

@pytest.mark.asyncio
async def test_adding_friend_without_token():
    data = {
        "phone": "70009998877"
    }
    async with AsyncClient(**test_settings.HTTPX_CLIENT_SETTINGS) as ac:
        response_creating_message = await ac.post('/friends/add', json=data)
    assert response_creating_message.status_code == 401


@pytest.mark.asyncio
async def test_adding_friend_does_not_exist():
    data = {
        "phone": "70009998800"
    }
    async with AsyncClient(**test_settings.HTTPX_CLIENT_SETTINGS) as ac:
        token_response = await ac.post('/auth', json=test_settings.DATA_FOR_GETTING_TOKEN1)
        token = token_response.json().get('access_token')
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response_adding_friend = await ac.post('/friends/add', json=data, headers=headers)
    assert response_adding_friend.status_code == 404


@pytest.mark.asyncio
async def test_adding_me_as_friend():
    data = {
        "phone": "79991234567"
    }
    async with AsyncClient(**test_settings.HTTPX_CLIENT_SETTINGS) as ac:
        token_response = await ac.post('/auth', json=test_settings.DATA_FOR_GETTING_TOKEN1)
        token = token_response.json().get('access_token')
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response_adding_friend = await ac.post('/friends/add', json=data, headers=headers)
    assert response_adding_friend.status_code == 400


@pytest.mark.asyncio
async def test_adding_friend():
    data = {
        "phone": "70009998877"
    }
    async with AsyncClient(**test_settings.HTTPX_CLIENT_SETTINGS) as ac:
        token_response = await ac.post('/auth', json=test_settings.DATA_FOR_GETTING_TOKEN1)
        token = token_response.json().get('access_token')
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response_adding_friend = await ac.post('/friends/add', json=data, headers=headers)
    assert response_adding_friend.status_code == 201
    assert response_adding_friend.json() == 'Вы добавили 70009998877 в друзья'


@pytest.mark.asyncio
async def test_adding_friend_that_is_already_friend():
    data = {
        "phone": "70009998877"
    }
    async with AsyncClient(**test_settings.HTTPX_CLIENT_SETTINGS) as ac:
        token_response = await ac.post('/auth', json=test_settings.DATA_FOR_GETTING_TOKEN1)
        token = token_response.json().get('access_token')
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response_adding_friend = await ac.post('/friends/add', json=data, headers=headers)
    assert response_adding_friend.status_code == 400


@pytest.mark.asyncio
async def test_getting_friend_list_without_token():
    async with AsyncClient(**test_settings.HTTPX_CLIENT_SETTINGS) as ac:
        response_adding_friend = await ac.post('/friends/me',)
    assert response_adding_friend.status_code == 401


@pytest.mark.asyncio
async def test_getting_friend_list():

    async with AsyncClient(**test_settings.HTTPX_CLIENT_SETTINGS) as ac:
        token_response = await ac.post('/auth', json=test_settings.DATA_FOR_GETTING_TOKEN1)
        token = token_response.json().get('access_token')
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response_getting_friend_list = await ac.post('/friends/me', headers=headers)
    assert response_getting_friend_list.status_code == 200


@pytest.mark.asyncio
async def test_deleting_friend_without_token():
    async with AsyncClient(**test_settings.HTTPX_CLIENT_SETTINGS) as ac:
        response_deleting_friend = await ac.delete('/friends/delete/1')
    assert response_deleting_friend.status_code == 401


@pytest.mark.asyncio
async def test_deleting_friend_():
    async with AsyncClient(**test_settings.HTTPX_CLIENT_SETTINGS) as ac:
        token_response = await ac.post('/auth', json=test_settings.DATA_FOR_GETTING_TOKEN1)
        token = token_response.json().get('access_token')
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response_deleting_friend = await ac.delete('/friends/delete/1', headers=headers)
    assert response_deleting_friend.status_code == 200
