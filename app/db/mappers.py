from sqlalchemy.orm import registry

from app.db.models.joke import JokeTable
from app.db.models.joke_suggestions import JokeSuggestionTable
from app.domains.joke import Joke
from app.domains.joke_suggestion import JokeSuggestion


def start_mapping_table_from_domain():
    """
    Регистрирует доменные модели как сущность алхимии.
    Суть в том, что доменная модель никак не изменяет свою работу, но мы
    получаем возможность использовать ее как модель при выполнение запросов.
    Это упрощает работу т.к. не нужно перегонять из ОРМ модели в домен.
    """
    registrator = registry()

    registrator.map_imperatively(
        Joke,
        JokeTable.__table__,
    )

    registrator.map_imperatively(
        JokeSuggestion,
        JokeSuggestionTable.__table__,
    )
