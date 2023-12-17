from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.handlers.keyboards import get_add_joke_reply_keyboard


router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message):
    answer_text = """Привет. Я бот, который сможет подобрать шутку на твою фразу.
Ты можешь это проверить прям сейчас, отправив сообщение!
Также ты сам можешь предложить свою шутку!
    """
    return await message.answer(answer_text, reply_markup=get_add_joke_reply_keyboard().as_markup(resize_keyboard=True))
