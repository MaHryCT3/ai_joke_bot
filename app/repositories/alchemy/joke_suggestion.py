from app.domains.joke_suggestion import JokeSuggestion
from app.repositories.alchemy.base import BaseAlchemyRepository


class JokeSuggestionAlchemyRepository(BaseAlchemyRepository[JokeSuggestion]):
    domain_model: JokeSuggestion = JokeSuggestion

    def get_by_text(self, text: str) -> JokeSuggestion | None:
        return (
            self.session.query(self.domain_model)
            .filter(self.domain_model.text == text)
            .first()
        )

    def get_next_suggestion(self) -> JokeSuggestion | None:
        return (
            self.session.query(self.domain_model)
            .filter(self.domain_model.is_approved == False)
            .first()
        )
