# version1.1.0
import logging
import asyncio
from aiogram import Bot, Dispatcher,types
from config import TOKEN
from handlers import register_message_handlers, bot_commands


# Настройка логирования
logging.basicConfig(level=logging.INFO)


async def main():
    """
    Основная функция для установки конфигурации бота.
    Для создания бота необходимо получить token в telegram https://t.me/BotFather
    и добавить полученный токен в файл .env
    """

    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # Здесь функция для вызова хендлеров из handlers.py
    await register_message_handlers(dp)

    # Здесь вызов меню с командами бота
    await bot.set_my_commands(bot_commands, types.BotCommandScopeDefault())

    # Запуск бота в polling-режиме
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
