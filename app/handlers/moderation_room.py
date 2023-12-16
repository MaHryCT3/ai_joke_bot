from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from app.services.joke_moderations import JokeModerationCallback, JokesModeration

router = Router()


@router.callback_query(JokeModerationCallback.filter(F.is_approve == True))
async def approve_joke_handle(query: CallbackQuery, callback_data: JokeModerationCallback):
    joke_moderation = JokesModeration()

    await joke_moderation.accept_joke(callback_data.joke_id)

    await query.answer("Шутка одобрена")
    await query.message.delete()


@router.callback_query(JokeModerationCallback.filter(F.is_approve == False))
async def decline_joke_handle(query: CallbackQuery, callback_data: JokeModerationCallback):
    joke_moderation = JokesModeration()

    await joke_moderation.decline_joke(callback_data.joke_id)

    await query.answer("Шутка отклонена")
    await query.message.delete()
