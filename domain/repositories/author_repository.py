from abc import ABC, abstractmethod

from domain.entities.author.author import Author


class AuthorRepository(ABC):
    @abstractmethod
    def save(self, author: Author) -> None:
        pass
