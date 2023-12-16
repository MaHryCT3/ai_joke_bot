import dataclasses


@dataclasses.dataclass
class Joke:
    text: str
    author_telegram_id: int | None = None
