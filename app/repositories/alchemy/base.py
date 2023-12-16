from abc import ABC
from dataclasses import asdict
from typing import Generic, TypeVar

from sqlalchemy.orm import Session

from app.db.engine import engine
from app.repositories.abstract import AbstractRepository

DomainModel = TypeVar("DomainModel")


class BaseAlchemyRepository(AbstractRepository, Generic[DomainModel], ABC):
    domain_model: DomainModel

    def __init__(self, session: Session | None = None):
        self.session = session or Session(engine, expire_on_commit=False)

    def get(self, id: int) -> DomainModel | None:
        return (
            self.session.query(self.domain_model)
            .filter(self.domain_model.id == id)
            .first()
        )

    def list(self) -> list[DomainModel]:
        return self.session.query(self.domain_model).all()

    def create(self, domain: DomainModel) -> DomainModel:
        self.session.add(domain)
        self.session.commit()
        self.session.refresh(domain)
        return domain

    def update(self, id: int, updated_domain: DomainModel) -> DomainModel:
        database_instance = self.get(id)

        for key, value in asdict(updated_domain).items():
            setattr(database_instance, key, value)

        self.session.add(database_instance)
        self.session.commit()
        self.session.refresh(database_instance)

        return database_instance

    def detele(self, id: int) -> None:
        database_instance = self.get(id)
        self.session.delete(database_instance)
