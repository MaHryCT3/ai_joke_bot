import ru_core_news_lg
import spacy_fastlang
from sklearn import metrics
from spacy.tokens import Doc

from app.domains.joke import Joke
from app.repositories.alchemy.joke import JokeAlchemyRepository
from app.services.jokes.abstract import AbstractJokeGetter
from app.services.jokes.exceptions import NotSupportedLanguageException
from utils.singleton import Singleton

nlp = ru_core_news_lg.load()
nlp.add_pipe("language_detector")


class SpacyJokeGetter(Singleton, AbstractJokeGetter):
    """
    Класс для получения шуток используя библиотеку spacy и векторы.

    https://spacy.io/.
    """

    AVAILABLE_LANGUAGES = ["ru"]
    MIN_MATCH_PERCENT: float = 0.15

    def __init__(self) -> None:
        self.available_jokes = JokeAlchemyRepository().list()

        self._nlp_jokes = [nlp(joke.text) for joke in self.available_jokes]
        self._joke_vectors = [joke.vector.reshape((1, 300)) for joke in self._nlp_jokes]

    def get_joke(self, phrase: str) -> Joke | None:
        nlp_phrase = nlp(phrase.lower())
        self._validate_language(nlp_phrase)

        phrase_vector = nlp_phrase.vector.reshape((1, 300))
        match_percents = [
            metrics.pairwise.cosine_similarity(phrase_vector, joke_vector)
            for joke_vector in self._joke_vectors
        ]

        max_match_percent = max(match_percents)
        print(max_match_percent)
        if max_match_percent >= self.MIN_MATCH_PERCENT:
            return self.available_jokes[match_percents.index(max_match_percent)]

    def _validate_language(self, nlp_phrase: Doc) -> None:
        """
        Проверяет, какой язык используется, если его нет в списке доступных возбуждает ошибку.
        """
        if nlp_phrase._.language not in self.AVAILABLE_LANGUAGES:
            raise NotSupportedLanguageException(
                f"Language {nlp_phrase._.language} is not supported"
            )
