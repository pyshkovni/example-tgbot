import pytest
from aiogram import Router
from aiogram.types import Message
from handlers.handlers import command_start_handler, command_help_handler
from unittest.mock import AsyncMock


@pytest.fixture
def mock_router():
    """Mock-роутер"""
    router = Router()
    router.message.register(command_start_handler)
    router.message.register(command_help_handler)
    return router


@pytest.fixture
def mock_message():
    """Mock-сообщение"""
    mock_msg = AsyncMock(spec=Message)
    mock_msg.answer = AsyncMock()
    return mock_msg
