import dataclasses


@dataclasses.dataclass
class JokeSuggestion:
    text: str
    telegram_id: int
    is_approved: bool | None = None
    id: int | None = None
