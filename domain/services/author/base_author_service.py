from abc import ABC, abstractmethod
from sre_constants import ANY

from domain.repositories import AuthorRepository


class BaseAuthorService(ABC):
    _author_repository: AuthorRepository

    def __init__(self, author_repository: AuthorRepository) -> None:
        self._author_repository = author_repository

    @abstractmethod
    def execute(self, *args, **kwargs) -> ANY:
        pass
