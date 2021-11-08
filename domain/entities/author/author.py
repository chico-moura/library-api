from dataclasses import dataclass

from domain.entities.author.value_objects import AuthorId, AuthorName


@dataclass(frozen=True)
class Author:
    id: AuthorId
    name: AuthorName
