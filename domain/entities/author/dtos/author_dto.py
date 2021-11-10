from __future__ import annotations

from dataclasses import dataclass
from uuid import UUID

from domain.entities.author.author import Author
from domain.factories import AuthorFactory


@dataclass
class AuthorDTO:
    id: UUID
    name: str

    @classmethod
    def from_entity(cls, author: Author) -> AuthorDTO:
        return cls(
            id=author.id.value,
            name=author.name.value
        )

    def to_entity(self) -> Author:
        return AuthorFactory.build_existing(
            id_=self.id,
            name=self.name
        )
