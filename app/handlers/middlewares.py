from collections.abc import Awaitable, Callable
from typing import Any

from aiogram import BaseMiddleware
from aiogram.types import Message
from sqlalchemy.orm import Session

from app.config import settings
from app.db.engine import engine


class SessionMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: dict[str, Any],
    ) -> Any:
        with Session(engine, expire_on_commit=False) as session:
            data['session'] = session
            return await handler(event, data)


class ErrorHandler(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: dict[str, Any],
    ) -> Any:
        try:
            return await handler(event, data)
        except Exception as e:
            await event.answer(text='Что-то пошло не так. Мы уже разбираемся с этой ошибкой.')
            await event.bot.send_message(settings.ERROR_LOG_CHAT_ID, text=str(e))
