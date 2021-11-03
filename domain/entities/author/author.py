from dataclasses import dataclass

from domain.entities.author.value_objects.author_id import AuthorId
from domain.entities.author.value_objects.author_name import AuthorName


@dataclass(frozen=True)
class Author:
    id: AuthorId
    name: AuthorName
