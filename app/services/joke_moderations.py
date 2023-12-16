from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.domains.joke import Joke
from app.domains.joke_suggestion import JokeSuggestion
from app.repositories.alchemy.joke import JokeAlchemyRepository
from app.repositories.alchemy.joke_suggestion import \
    JokeSuggestionAlchemyRepository
from aiogram.client.bot import Bot
from app.config import settings

class JokeModerationCallback(CallbackData, prefix="moderation"):
    joke_id: int
    is_approve: bool

class JokesModeration:
    """
    Класс полностью отвеачет за модерацию шуток
    """

    def __init__(self):
        self.joke_repository = JokeAlchemyRepository()
        self.joke_suggestion_repository = JokeSuggestionAlchemyRepository()

    def is_joke_exists(self, text: str) -> bool:
        return bool(self.joke_repository.get_by_text(text))

    def is_suggestion_exists(self, text: str) -> bool:
        return bool(self.joke_suggestion_repository.get_by_text(text))

    def get_next_suggestion(self) -> JokeSuggestion:
        return self.joke_suggestion_repository.get_next_suggestion()

    async def accept_joke(self, joke_suggestion_id: int) -> None:
        joke_suggestion = self.joke_suggestion_repository.get(joke_suggestion_id)
        joke_suggestion.is_approved = True
        self.joke_suggestion_repository.update(joke_suggestion.id, joke_suggestion)

        joke = self._get_joke_from_suggestion(joke_suggestion)
        self.joke_repository.create(joke)

        await self._send_approve_message_to_user(joke_suggestion)

    async def decline_joke(self, joke_suggestion_id: int) -> None:
        joke_suggestion = self.joke_suggestion_repository.get(joke_suggestion_id)
        joke_suggestion.is_approved = False
        self.joke_suggestion_repository.update(joke_suggestion.id, joke_suggestion)

        await self._send_decline_message_to_user(joke_suggestion)

    async def add_joke_to_moderate(self, joke_text: str, telegram_id: int) -> None:
        joke_suggestion = JokeSuggestion(
            text=joke_text,
            telegram_id=telegram_id,
            is_approved=None,
        )
        joke_suggestion = self.joke_suggestion_repository.create(joke_suggestion)

        await self._send_message_to_moderation_chat(joke_suggestion)

    async def _send_message_to_moderation_chat(self, joke_suggestion: JokeSuggestion):
        bot = Bot(token=settings.TELEGRAM_TOKEN)

        message = joke_suggestion.text

        keyboard_builder = InlineKeyboardBuilder()
        keyboard_builder.button(text='✅ Принять', callback_data=JokeModerationCallback(joke_id=joke_suggestion.id, is_approve=True).pack())
        keyboard_builder.button(text='❌ Отклонить', callback_data=JokeModerationCallback(joke_id=joke_suggestion.id, is_approve=False).pack())

        await bot.send_message(
            chat_id=settings.MODERATION_CHAT_ID,
            text=message,
            reply_markup=keyboard_builder.as_markup()
        )

    async def _send_approve_message_to_user(self, joke_suggestion: JokeSuggestion):
        bot = Bot(token=settings.TELEGRAM_TOKEN)

        message = f'Поздравляем! Ваша шутка была одобрена: {joke_suggestion.text}'

        await bot.send_message(
            joke_suggestion.telegram_id,
            text=message,
        )

    async def _send_decline_message_to_user(self, joke_suggestion: JokeSuggestion):
        bot = Bot(token=settings.TELEGRAM_TOKEN)

        message = f'К сожалению, ваша шутка не прошла модерацию: {joke_suggestion.text}'

        await bot.send_message(
            joke_suggestion.telegram_id,
            text=message,
        )

    def _get_joke_from_suggestion(self, joke_suggestion: JokeSuggestion) -> Joke:
        return Joke(
            text=joke_suggestion.text,
            author_telegram_id=joke_suggestion.telegram_id,
        )