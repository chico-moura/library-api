from abc import ABC, abstractmethod
from typing import List

from domain.entities.author.author import Author
from domain.entities.author.value_objects.author_id import AuthorId


class AuthorRepository(ABC):
    @abstractmethod
    def save(self, *authors: Author) -> None:
        pass

    @abstractmethod
    def get_by_id(self, author_id: AuthorId) -> Author:
        pass

    @abstractmethod
    def get_all(self) -> List[Author]:
        pass
