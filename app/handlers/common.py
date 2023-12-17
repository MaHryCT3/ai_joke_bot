from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery


router = Router()


@router.callback_query(F.data == 'cancel')
async def clear_state(query: CallbackQuery, state: FSMContext):
    await state.clear()
    await query.message.delete()
    await query.answer(text='Можешь продолжать пользоваться ботом')
