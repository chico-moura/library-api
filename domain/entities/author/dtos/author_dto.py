from dataclasses import dataclass
from typing import Optional

from domain.entities.author.author import Author
from domain.entities.author.value_objects.author_id import AuthorId
from domain.entities.author.value_objects.author_name import AuthorName


@dataclass
class AuthorDTO:
    name: str
    id: Optional[str] = None

    def to_entity(self) -> Author:
        name = AuthorName(self.name)
        id_ = AuthorId(self.id)
        return Author(id_=id_, name=name)
