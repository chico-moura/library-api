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
        return BookFactory.build_new(
            name=self.name,
            edition=self.edition,
            publication_year=self.publication_year,
            authors=self.authors
        )
