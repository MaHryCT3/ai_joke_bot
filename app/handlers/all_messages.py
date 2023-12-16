from aiogram import Router
from aiogram.types import Message

from app.services.jokes.exceptions import NotSupportedLanguageException
from app.services.jokes.spacy import SpacyJokeGetter


router = Router()


@router.message()
async def all_messages_handler(message: Message):
    try:
        joke = SpacyJokeGetter().get_joke(message.text)
    except NotSupportedLanguageException:
        return await message.answer('Извини, я тебя не понимаю. Я поддерживаю только русский язык.')

    if not joke:
        return await message.answer(
            'Я не смог подобрать подходящую шутку, но ты можешь добавить свою!',
        )

    return await message.answer(joke.text)
