# version1.1.0
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from config import TOKEN
from utils import setup_logger


bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def process_start_command(message):
    await message.answer("Привет!")
    logging.info(f"user {message.from_user.id} starts bot ")


@dp.message()
async def echo_message(message):
    await message.answer(message.text)
    logging.info(f"user {message.from_user.id} leaves unhandled message")


async def main():
    """
    Основная функция для установки конфигурации бота.
    Для создания бота необходимо получить token в telegram https://t.me/BotFather
    и добавить полученный токен в файл .env
    """
    
    # # Установить общий уровень логирования
    # logging.basicConfig(level=logging.DEBUG)

    # запуск логирования
    setup_logger(fname=__name__)

    # Запуск бота в polling-режиме
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
