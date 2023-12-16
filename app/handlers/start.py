from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message):
    answer_text = "Привет. Я бот, шутки присылаю"
    return await message.answer(answer_text)
