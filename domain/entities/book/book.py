from dataclasses import dataclass
from typing import List

from domain.entities.author.value_objects.author_id import AuthorId
from domain.entities.book.value_objects.book_edition import BookEdition
from domain.entities.book.value_objects.book_id import BookId
from domain.entities.book.value_objects.book_name import BookName
from domain.entities.book.value_objects.book_publication_year import BookPublicationYear


@dataclass(frozen=True)
class Book:
    id: BookId
    name: BookName
    edition: BookEdition
    publication_year: BookPublicationYear
    authors: List[AuthorId]
