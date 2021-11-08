from unittest import TestCase

from domain.entities.book.dtos import BookDTO
from domain.factories import BookFactory
from domain.tests.factories import BookDTOTestFactory


class TestBookFactory(TestCase):
    def test_from_book_dto_WHEN_called_THEN_returns_book_matching_given_dto(self) -> None:
        book_dto: BookDTO = BookDTOTestFactory.build()
        expected_attributes = [
            book_dto.id,
            book_dto.name,
            book_dto.edition,
            book_dto.publication_year,
            book_dto.authors
        ]

        book = BookFactory.from_book_dto(book_dto)

        actual_attributes = [
            book.id.value,
            book.name.value,
            book.edition.value,
            book.publication_year.value,
            [author_id.value for author_id in book.authors]
        ]
        self.assertEqual(expected_attributes, actual_attributes)
