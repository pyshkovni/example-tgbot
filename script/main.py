# модуль запуска скрипта


# TODO - установите требуемые библиотеки через pip install
import asyncio
from classes import ScriptClass
from concurrent.futures import ThreadPoolExecutor


_executor = ThreadPoolExecutor(1)


async def main():
    # Пример асинхронного вызова метода класса
    instance = ScriptClass()
    await loop.run_in_executor(_executor, instance.method)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
