from __future__ import annotations
from dataclasses import dataclass
from uuid import UUID

from domain.entities.author.author import Author
from domain.entities.author.value_objects.author_id import AuthorId
from domain.entities.author.value_objects.author_name import AuthorName


@dataclass
class AuthorDTO:
    id: str
    name: str

    @classmethod
    def from_entity(cls, author: Author) -> AuthorDTO:
        id_ = author.id.value.hex
        name = author.name.value

        return cls(id=id_, name=name)

    def to_entity(self) -> Author:
        raw_id = UUID(self.id)
        author_id = AuthorId(raw_id)
        author_name = AuthorName(self.name)

        return Author(id=author_id, name=author_name)
