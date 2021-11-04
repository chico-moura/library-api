from __future__ import annotations
from dataclasses import dataclass
from uuid import UUID

from domain.entities.author.author import Author
from domain.entities.author.value_objects.author_id import AuthorId
from domain.entities.author.value_objects.author_name import AuthorName


@dataclass
class AuthorOutputDTO:
    id: UUID
    name: str

    @classmethod
    def from_entity(cls, author: Author) -> AuthorOutputDTO:
        return cls(
            id=author.id.value,
            name=author.name.value
        )

    def to_entity(self) -> Author:
        author_id = AuthorId(self.id)
        author_name = AuthorName(self.name)

        return Author(
            id=author_id,
            name=author_name
        )
