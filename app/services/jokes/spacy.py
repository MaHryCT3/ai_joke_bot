import ru_core_news_lg
from sklearn import metrics

from app.config import settings
from app.domains.joke import Joke
from app.repositories.alchemy.joke import JokeAlchemyRepository
from app.services.jokes.abstract import AbstractJokeGetter
from utils.singleton import Singleton


nlp = ru_core_news_lg.load()


class SpacyJokeGetter(Singleton, AbstractJokeGetter):
    """
    Класс для получения шуток используя библиотеку spacy и векторы.

    https://spacy.io/.
    """

    MIN_MATCH_PERCENT: float = settings.MIN_PERCENT_FOR_JOKE

    def __init__(self) -> None:
        self.available_jokes = JokeAlchemyRepository().list()

        self._nlp_jokes = [nlp(joke.text) for joke in self.available_jokes]
        self._joke_vectors = [joke.vector.reshape((1, 300)) for joke in self._nlp_jokes]

    def get_joke(self, phrase: str) -> Joke | None:
        nlp_phrase = nlp(phrase.lower())

        phrase_vector = nlp_phrase.vector.reshape((1, 300))
        match_percents = [
            metrics.pairwise.cosine_similarity(phrase_vector, joke_vector) for joke_vector in self._joke_vectors
        ]

        max_match_percent = max(match_percents)
        print(max_match_percent)
        if max_match_percent >= self.MIN_MATCH_PERCENT:
            return self.available_jokes[match_percents.index(max_match_percent)]
