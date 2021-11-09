from dataclasses import dataclass

from domain.entities.author.author import Author
from domain.factories import AuthorFactory


@dataclass
class AuthorCreationDTO:
    name: str

    def to_entity(self) -> Author:
        return AuthorFactory.create_new(
            name=self.name
        )

