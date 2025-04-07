import pytest
from unittest.mock import AsyncMock
from aiogram.types import Message
from handlers.handlers import command_start_handler


@pytest.mark.asyncio
async def test_command_start_handler():
    # Создаем mock-объект Message
    mock_message = AsyncMock(spec=Message)
    mock_message.answer = AsyncMock()

    # Вызываем хендлер
    await command_start_handler(mock_message)

    # Проверяем, что message.answer был вызван один раз с ожидаемым текстом
    mock_message.answer.assert_called_once_with(text="Привет!")
