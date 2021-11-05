from dataclasses import dataclass

from domain.entities.author.author import Author
from domain.entities.author.value_objects.author_id import AuthorId
from domain.entities.author.value_objects.author_name import AuthorName


@dataclass
class AuthorCreationDTO:
    name: str

    def to_entity(self) -> Author:
        author_id = AuthorId()
        author_name = AuthorName(self.name)

        return Author(
            id=author_id,
            name=author_name
        )
