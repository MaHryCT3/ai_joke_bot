from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message

from app.handlers.keyboards import get_clear_state_inline_button
from app.services.joke_moderations import JokesModeration


router = Router()


class AddJokeStates(StatesGroup):
    add_joke = State()


@router.message(Command('add_joke'))
@router.message(F.text.lower() == 'добавить шутку')
@router.callback_query(F.data == 'add_joke')
async def add_joke_enter(message: Message | CallbackQuery, state: FSMContext):
    await state.set_state(AddJokeStates.add_joke)

    await message.bot.send_message(
        message.from_user.id,
        'Хорошо, отправь свою шутку',
        reply_markup=get_clear_state_inline_button().as_markup(),
    )


@router.message(AddJokeStates.add_joke)
async def add_joke_to_moderate(message: Message, state: FSMContext):
    joke_moderation = JokesModeration()
    joke_text = message.text

    if joke_moderation.is_joke_exists(joke_text):
        return await message.answer('Такая шутка уже существует')
    elif joke_moderation.is_suggestion_exists(joke_text):
        return await message.answer('Такую шутку уже предложили, попробую другую')

    await joke_moderation.add_joke_to_moderate(joke_text, message.from_user.id)

    await state.clear()
    await message.answer('Хорошо, твоя шутка отправлена на модерацию. Я сообщу тебе как только она будет рассмотрена')
