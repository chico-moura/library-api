from dataclasses import dataclass
from typing import List
from uuid import UUID

from domain.entities import Book
from domain.factories import BookFactory


@dataclass
class BookCreationDTO:
    name: str
    edition: str
    publication_year: str
    authors: List[UUID]

    def to_entity(self) -> Book:
        return BookFactory
