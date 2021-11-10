from __future__ import annotations

from dataclasses import dataclass
from typing import List
from uuid import UUID

from domain.entities.book.book import Book
from domain.factories import BookFactory


@dataclass
class BookDTO:
    id: UUID
    name: str
    edition: str
    publication_year: str
    authors: List[UUID]

    def to_entity(self) -> Book:
        return BookFactory.build_existing(
            id_=self.id,
            name=self.name,
            edition=self.edition,
            publication_year=self.publication_year,
            authors=self.authors
        )

    @classmethod
    def from_entity(cls, book: Book) -> BookDTO:
        return cls(
            id=book.id.value,
            name=book.name.value,
            edition=book.edition.value,
            publication_year=book.publication_year.value,
            authors=[author_id.value for author_id in book.authors]
        )
