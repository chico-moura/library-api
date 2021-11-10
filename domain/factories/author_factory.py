from uuid import UUID

from domain.entities import Author
from domain.entities.author.value_objects import AuthorId, AuthorName


class AuthorFactory:
    @staticmethod
    def build_new(name: str) -> Author:
        return Author(
            id=AuthorId(),
            name=AuthorName(name)
        )

    @staticmethod
    def build_existing(id_: UUID, name: str) -> Author:
        return Author(
            id=AuthorId(id_),
            name=AuthorName(name)
        )
