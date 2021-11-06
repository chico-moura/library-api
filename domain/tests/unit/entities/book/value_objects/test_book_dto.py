from unittest import TestCase

from domain.entities.book.dtos.bookDTO import BookDTO
from domain.tests.factories.book_dto_factory import BookDTOFactory
from domain.tests.factories.book_factory import BookFactory


class TestBookDTO(TestCase):
    def test_to_entity_WHEN_called_THEN_returns_book_with_matching_attributes(self) -> None:
        dto = BookDTOFactory.get_random('Book name')
        expected_values = [
            dto.id,
            dto.name,
            dto.edition,
            dto.publication_year,
            dto.authors
        ]

        book = dto.to_entity()

        actual_values = [
            book.id.value,
            book.name.value,
            book.edition.value,
            book.publication_year.value,
            [author_id.value for author_id in book.authors]
        ]
        self.assertEqual(expected_values, actual_values)

    def test_from_entity_WHEN_called_with_book_THEN_returns_dto_with_matching_attributes(self) -> None:
        book = BookFactory.get_random('Book name')
        expected_values = [
            book.id.value,
            book.name.value,
            book.edition.value,
            book.publication_year.value,
            [author_id.value for author_id in book.authors]
        ]

        dto = BookDTO.from_entity(book)

        actual_values = [
            dto.id,
            dto.name,
            dto.edition,
            dto.publication_year,
            dto.authors
        ]
        self.assertEqual(expected_values, actual_values)
