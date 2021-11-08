import pytest
import settings
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_creating_conv_without_token():
    data = {
        "title": "testTitle",
        "description": "testDesc"
    }
    async with AsyncClient(**settings.HTTPX_CLIENT_SETTINGS) as ac:
        response = await ac.post('/conv/create', json=data)
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_creating_conv_with_token():
    data = {
        "title": "testTitle",
        "description": "testDesc"
    }
    async with AsyncClient(**settings.HTTPX_CLIENT_SETTINGS) as ac:
        token_response = await ac.post('/auth', json=settings.DATA_FOR_GETTING_TOKEN1)
        token = token_response.json().get('access_token')
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response = await ac.post('/conv/create', json=data, headers=headers)
    assert response.status_code == 201
    assert response.json() == f'Беседа testTitle была создана'


@pytest.mark.asyncio
async def test_retrieving_conv_without_token():
    async with AsyncClient(**settings.HTTPX_CLIENT_SETTINGS) as ac:
        response = await ac.post('/conv/retrieve/1')
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_retrieving_conv_with_token():
    async with AsyncClient(**settings.HTTPX_CLIENT_SETTINGS) as ac:
        token_response = await ac.post('/auth', json=settings.DATA_FOR_GETTING_TOKEN1)
        token = token_response.json().get('access_token')
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response = await ac.post('/conv/retrieve/1', headers=headers)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_retrieving_conv_by_non_creator():
    async with AsyncClient(**settings.HTTPX_CLIENT_SETTINGS) as ac:
        token_response = await ac.post('/auth', json=settings.DATA_FOR_GETTING_TOKEN2)
        token = token_response.json().get('access_token')
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response = await ac.post('/conv/retrieve/1', headers=headers)
    assert response.status_code == 403
    assert response.json() == {'detail': 'Вы не являетесь членом беседы'}


@pytest.mark.asyncio
async def test_updating_conv_by_non_creator():
    data = {
        "title": "testTitleUpdate",
        "description": "testDescUpdate"
    }
    async with AsyncClient(**settings.HTTPX_CLIENT_SETTINGS) as ac:
        token_response = await ac.post('/auth', json=settings.DATA_FOR_GETTING_TOKEN2)
        token = token_response.json().get('access_token')
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response = await ac.put('/conv/update/1', json=data, headers=headers)
    assert response.status_code == 403
    assert response.json() == {'detail': 'Вы не являетесь создателем беседы'}


@pytest.mark.asyncio
async def test_updating_conv_without_token():
    data = {
        "title": "testTitleUpdate",
        "description": "testDescUpdate"
    }
    async with AsyncClient(**settings.HTTPX_CLIENT_SETTINGS) as ac:
        response = await ac.put('/conv/update/1', json=data)
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_updating_conv():
    data = {
        "title": "testTitleUpdate",
        "description": "testDescUpdate"
    }
    async with AsyncClient(**settings.HTTPX_CLIENT_SETTINGS) as ac:
        token_response = await ac.post('/auth', json=settings.DATA_FOR_GETTING_TOKEN1)
        token = token_response.json().get('access_token')
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response = await ac.put('/conv/update/1', json=data, headers=headers)
    assert response.status_code == 200
    assert response.json() == 'Беседа была изменена'


@pytest.mark.asyncio
async def test_deleting_conv_without_token():
    async with AsyncClient(**settings.HTTPX_CLIENT_SETTINGS) as ac:
        response = await ac.delete('/conv/delete/1')
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_deleting_conv_by_non_creator():
    async with AsyncClient(**settings.HTTPX_CLIENT_SETTINGS) as ac:
        token_response = await ac.post('/auth', json=settings.DATA_FOR_GETTING_TOKEN2)
        token = token_response.json().get('access_token')
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response = await ac.delete('/conv/delete/1', headers=headers)
    assert response.status_code == 403
    assert response.json() == {'detail': 'Вы не являетесь создателем беседы'}


@pytest.mark.asyncio
async def test_deleting_conv():
    async with AsyncClient(**settings.HTTPX_CLIENT_SETTINGS) as ac:
        token_response = await ac.post('/auth', json=settings.DATA_FOR_GETTING_TOKEN1)
        token = token_response.json().get('access_token')
        headers = {
            'Authorization': f'Bearer {token}'
        }
        response = await ac.delete('/conv/delete/1', headers=headers)
    assert response.status_code == 200
    assert response.json() == 'Беседа была удалена'



