from typing import List
from uuid import UUID

from domain.entities.author.value_objects import AuthorId
from domain.entities.book import Book
from domain.entities.book.dtos.book_creation_dto import BookCreationDTO
from domain.entities.book.value_objects import BookEdition, BookId, BookName, BookPublicationYear


class BookFactory:
    @staticmethod
    def build(
            name: str,
            edition: str,
            publication_year: str,
            authors: List[UUID]
    ) -> Book:
        return Book(
            id=BookId(),

        )

    @staticmethod
    def from_book_dto(book_dto) -> Book:
        return Book(
            id=BookId(book_dto.id),
            name=BookName(book_dto.name),
            edition=BookEdition(book_dto.edition),
            publication_year=BookPublicationYear(book_dto.publication_year),
            authors=[AuthorId(raw_id) for raw_id in book_dto.authors]
        )

    @staticmethod
    def from_book_creation_dto(book_creation_dto: BookCreationDTO) -> Book:
        return Book(
            id=BookId(),
            name=BookName(book_creation_dto.name),
            edition=BookEdition(book_creation_dto.edition),
            publication_year=BookPublicationYear(book_creation_dto.publication_year),
            authors=[AuthorId(raw_id) for raw_id in book_creation_dto.authors]
        )
