from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from app.services.joke_moderations import JokesModeration

router = Router()

class AddJokeStates(StatesGroup):
    add_joke = State()


@router.message(F.text.startswith("добавить шутку"))
async def add_joke_enter(message: Message, state: FSMContext):
    await state.set_state(AddJokeStates.add_joke)
    return await message.answer("Хорошо, пришли свою шутку")


@router.message(AddJokeStates.add_joke)
async def add_joke_to_moderate(message: Message, state: FSMContext):
    joke_moderation = JokesModeration()
    joke_text = message.text

    if joke_moderation.is_joke_exists(joke_text):
        return await message.answer("Такая шутка уже существует")
    elif joke_moderation.is_suggestion_exists(joke_text):
        return await message.answer("Такую шутку уже предложили, попробую другую")

    await joke_moderation.add_joke_to_moderate(joke_text, message.from_user.id)

    await state.clear()
    await message.answer(
        "Хорошо, твоя шутка отправлена на модерацию. Я сообщу тебе как только она будет рассмотрена"
    )
