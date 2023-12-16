from app.domains.joke import Joke
from app.repositories.alchemy.base import BaseAlchemyRepository


class JokeAlchemyRepository(BaseAlchemyRepository[Joke]):
    domain_model = Joke

    def get_by_text(self, text: str) -> Joke | None:
        return (
            self.session.query(self.domain_model)
            .filter(self.domain_model.text == text)
            .first()
        )
