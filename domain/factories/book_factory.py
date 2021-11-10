from typing import List
from uuid import UUID

from domain.entities.author.value_objects import AuthorId
from domain.entities.book import Book
from domain.entities.book.value_objects import BookEdition, BookId, BookName, BookPublicationYear


class BookFactory:
    @staticmethod
    def build_new(
            name: str,
            edition: str,
            publication_year: str,
            authors: List[UUID]
    ) -> Book:
        return Book(
            id=BookId(),
            name=BookName(name),
            edition=BookEdition(edition),
            publication_year=BookPublicationYear(publication_year),
            authors=[AuthorId(raw_id) for raw_id in authors]
        )

    @staticmethod
    def build_existing(
            id_: UUID,
            name: str,
            edition: str,
            publication_year: str,
            authors: List[UUID]
    ) -> Book:
        return Book(
            id=BookId(id_),
            name=BookName(name),
            edition=BookEdition(edition),
            publication_year=BookPublicationYear(publication_year),
            authors=[AuthorId(raw_id) for raw_id in authors]
        )
