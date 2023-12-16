from abc import ABC, abstractmethod
from typing import Any


class AbstractRepository(ABC):
    domain_model: Any  # FIXME: Dataclass Protocol

    @abstractmethod
    def get(self, id):
        ...

    @abstractmethod
    def list(self):
        ...

    @abstractmethod
    def create(self, domain):
        ...

    @abstractmethod
    def update(self, id, domain):
        ...

    @abstractmethod
    def detele(self, id):
        ...
