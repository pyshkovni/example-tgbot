__all__ = [
    'register_message_handlers'
]


# Работа c Router - https://docs.aiogram.dev/en/v3.14.0/dispatcher/router.html
# Пример работы с Router через декораторы @router - https://mastergroosha.github.io/aiogram-3-guide/routers/
# Пример работы с Router через функцию сборщик https://stackoverflow.com/questions/77809738/how-to-connect-a-router-in-aiogram-3-x-x#:~:text=1-,Answer,-Sorted%20by%3A


from aiogram import types, Router, filters, F
from .keyboard import keyboard_continue  # импорт из клавиатур
from .callbacks import callback_message  # импорт из коллбека


async def command_start_handler(message: types.Message):
    """Команда start"""
    await message.answer(text="Привет!", reply_markup=keyboard_continue)


async def command_help_handler(message: types.Message):
    """Команда help"""
    await message.answer(text="Справка!...")


# Здесь описывается маршрутизация
async def register_message_handlers(router: Router):
    """Маршрутизация обработчиков"""
    router.message.register(command_start_handler, filters.Command(commands=["start"]))
    router.callback_query.register(callback_message, F.data.endswith("_continue"))
