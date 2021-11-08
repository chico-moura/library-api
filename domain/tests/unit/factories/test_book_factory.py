from unittest import TestCase
from uuid import uuid4

from domain.entities.book.dtos.bookDTO import BookDTO


class TestBookFactory(TestCase):
    def test_from_book_dto_WHEN_called_THEN_returns_book_matching_given_dto(self) -> None:
        expected_id = uuid4()


        book_dto = BookDTO(

        )
