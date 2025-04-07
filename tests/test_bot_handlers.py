import pytest
from unittest.mock import AsyncMock
from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from handlers.handlers import command_start_handler, command_help_handler
from fixtures import mock_router, mock_message


@pytest.mark.asyncio
async def test_command_start_handler(mock_router, mock_message):
    await command_start_handler(mock_message)  # запуск хендлера с mock-сообщения
    assert mock_message.answer.called, "message.answer не был вызван"  # Проверка, что message.answer был вызван

    called_args, called_kwargs = mock_message.answer.call_args  # Получаем аргументы, с которыми был вызван message.answer. Проверить print(called_args, called_kwargs)

    assert called_kwargs["text"] == "Привет!"  # Проверяем текст сообщения

    markup = called_kwargs.get("reply_markup")  # Проверяем наличие inline-клавиатуры
    assert isinstance(markup, InlineKeyboardMarkup), "reply_markup не является InlineKeyboardMarkup"

    buttons = markup.inline_keyboard  # Проверяем содержимое клавиатуры
    assert len(buttons) == 1, "Ожидалась одна строка с кнопками"
    assert len(buttons[0]) == 1, "Ожидалась одна кнопка в строке"
    button = buttons[0][0]
    assert button.text == "Далее"
    assert button.callback_data == "button_continue"


@pytest.mark.asyncio
async def test_command_help_handler(mock_router, mock_message):
    mock_message = AsyncMock(spec=Message)  # Создаем mock-объект Message
    mock_message.answer = AsyncMock()

    await command_help_handler(mock_message)  # Вызываем хендлер

    mock_message.answer.assert_called_once_with(text="Справка!...")  # Проверяем, что message.answer был вызван один раз с ожидаемым текстом
