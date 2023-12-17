from aiogram import Bot, Dispatcher

from app.config import settings
from app.entrypoint import *  # noqa
from app.handlers.middlewares import ErrorHandler
from app.handlers.router import handlers_router


dispatcher = Dispatcher()
dispatcher.message.middleware.register(ErrorHandler())
dispatcher.include_router(handlers_router)

bot = Bot(token=settings.TELEGRAM_TOKEN)
