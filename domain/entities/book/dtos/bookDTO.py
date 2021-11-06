from __future__ import annotations

from dataclasses import dataclass
from typing import List
from uuid import UUID

from domain.entities.author.value_objects.author_id import AuthorId
from domain.entities.book.book import Book
from domain.entities.book.value_objects.book_edition import BookEdition
from domain.entities.book.value_objects.book_id import BookId
from domain.entities.book.value_objects.book_name import BookName
from domain.entities.book.value_objects.book_publication_year import BookPublicationYear


@dataclass
class BookDTO:
    id: UUID
    name: str
    edition: str
    publication_year: str
    authors: List[UUID]

    def to_entity(self) -> Book:
        book_id = BookId(self.id)
        book_name = BookName(self.name)
        book_edition = BookEdition(self.edition)
        book_publication_year = BookPublicationYear(self.publication_year)
        book_authors = [AuthorId(id_) for id_ in self.authors]

        return Book(
            id=book_id,
            name=book_name,
            edition=book_edition,
            publication_year=book_publication_year,
            authors=book_authors
        )

    @classmethod
    def from_entity(cls, book: Book) -> BookDTO:
        raw_ids = [author_id.value for author_id in book.authors]

        return cls(
            id=book.id.value,
            name=book.name.value,
            edition=book.edition.value,
            publication_year=book.publication_year.value,
            authors=raw_ids
        )
