# example-tgbot
Aiogram3 tgbot example (with some bugs)

## Installation

1. Create virtual environment
 
2. Download python package aiogram

```Bash
pip install aiogram
```

3. Start project

```
python3 main.py
```

## Материал

* Дополнительный гайд по aiogram https://mastergroosha.github.io/aiogram-3-guide/quickstart/
* Дополнительный гайд по асинхронному бэкенду https://habr.com/ru/companies/kts/articles/598575/
* Для создания бота необходимо получить token в telegram https://t.me/BotFather
* Бот принимает команды, например /start. Создадим хендлер - обработчик сообщений, и будем возвращать сообщение, указанное в функции подробнее о конструкции async/await - https://docs-python.ru/tutorial/sintaksis-async-await-python/
* Запуск процесса поллинга новых апдейтов. Существует 2 способа получить уведомления:
  * `webhook` — инициатором запроса выступает Телеграм. Когда пользователь пишет боту, Телеграм делает запрос на URL, который вы установите с помощью метода setwebhook.
  * `long polling` — инициатором является ваше приложение. Оно обращается к Telegram API и получает уведомления или ожидает, если уведомлений нет.