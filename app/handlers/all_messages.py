from aiogram import Router
from aiogram.types import Message

from app.handlers.keyboards import get_add_joke_inline_keyboard
from app.services.jokes.exceptions import NotSupportedLanguageException
from app.services.jokes.spacy import SpacyJokeGetter


router = Router()


@router.message()
async def all_messages_handler(message: Message):
    if not message.text:
        return await message.answer(
            'Попробуй еще еще раз, ты можешь написать любую фразу или слово и я попробую подобрать шутку.'
        )

    joke = SpacyJokeGetter().get_joke(message.text)
    if not joke:
        return await message.answer(
            'Я не смог подобрать подходящую шутку, но ты можешь добавить свою!',
            reply_markup=get_add_joke_inline_keyboard().as_markup(),
        )

    return await message.answer(joke.text)
