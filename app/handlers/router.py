from aiogram import Router

from app.handlers.all_messages import router as all_messages_router
from app.handlers.start import router as start_router
from app.handlers.add_joke import router as add_joke_router
from app.handlers.moderation_room import router as moderation_room_router

handlers_router = Router()

handlers_router.include_router(add_joke_router)
handlers_router.include_router(moderation_room_router)
handlers_router.include_router(start_router)
handlers_router.include_router(all_messages_router)
