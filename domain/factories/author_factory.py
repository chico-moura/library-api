from domain.entities import Author
from domain.entities.author.value_objects import AuthorId, AuthorName


class AuthorFactory:
    @staticmethod
    def create_new(name: str) -> Author:
        return Author(
            id=AuthorId(),
            name=AuthorName(name)
        )
