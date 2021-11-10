from unittest import TestCase
from uuid import uuid4

from domain.entities.book.dtos.get_book_by_id_dto import GetBookByIdDTO
from domain.entities.book.value_objects.book_id import BookId


class TestGetBookByIdDTO(TestCase):
    def test_to_book_id_WHEN_called_THEN_returns_book_id_instance(self):
        raw_book_id = uuid4()

        result_book_id = GetBookByIdDTO(raw_book_id).to_book_id()

        expected_book_id = BookId(raw_book_id)
        self.assertEqual(expected_book_id, result_book_id)
