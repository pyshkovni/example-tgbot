__all__ = [
    "User",
    "Base",
]

# Про ORM-паттерн асинхронного sqlalchemy и модели
# https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html#synopsis-orm

# декларативная модель базы данных python
# https://metanit.com/python/database/3.2.php
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, DATE, Integer, VARCHAR, Text
from datetime import datetime

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_table"
    # TODO - Описать модель таблицы пользователей
    # Таблица пользователей
    #   userid - индентификатор пользователя telegram
    #   username - имя пользователя telegram
    #   tutorcode - код преподавателя, чтобы поделиться для студента (если преподавателя)
    #   subscribe - имя преподавателя, на которого подписан слушатель (если слушатель)
    #   extra - доп колонка
    pass
