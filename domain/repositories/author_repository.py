from abc import ABC, abstractmethod

from domain.entities.author.author import Author
from domain.entities.author.value_objects.author_id import AuthorId


class AuthorRepository(ABC):
    @abstractmethod
    def save(self, author: Author) -> None:
        pass

    @abstractmethod
    def get_by_id(self, author_id: AuthorId) -> Author:
        pass
