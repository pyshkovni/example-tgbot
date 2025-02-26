from aiogram import Bot, Dispatcher


bot = Bot(token="YOUR TOKEN")
dp = Dispatcher()


@dp.message(text='/start')
def process_start_command(message):
    return message.answer("Привет!")


@dp.message()
def echo_message(message):
    return message.answer(message.text)


async def main():
    return dp.start_polling(bot)


if __name__ == "__main__":
    dp.run_polling()
