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
        return BookFactory.from_book_dto(self)

    @classmethod
    def from_entity(cls, book: Book) -> BookDTO:
        pass
