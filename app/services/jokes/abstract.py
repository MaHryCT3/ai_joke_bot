from abc import ABC, abstractmethod

from app.domains.joke import Joke


class AbstractJokeGetter(ABC):
    """
    Абстрактный для получения шуток.
    """

    @abstractmethod
    def get_joke(self, phrase: str) -> Joke | None:
        ...
