from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


def get_add_joke_inline_keyboard() -> InlineKeyboardBuilder:
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text='Добавить шутку', callback_data='add_joke')
    return keyboard


def get_clear_state_inline_button(button_name: str = 'Отменить') -> InlineKeyboardBuilder:
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text=button_name, callback_data='cancel')
    return keyboard


def get_add_joke_reply_keyboard() -> ReplyKeyboardBuilder:
    keyboard = ReplyKeyboardBuilder()

    keyboard.button(text='Добавить шутку')
    keyboard.adjust()
    return keyboard
