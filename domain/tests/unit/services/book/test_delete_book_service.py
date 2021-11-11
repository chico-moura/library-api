from unittest import TestCase
from uuid import uuid4

from mockito import mock, when, verify

from domain.entities.book.dtos.delete_book_dto import DeleteBookDTO
from domain.entities.book.value_objects import BookId
from domain.repositories import BookRepository
from domain.services.book.delete_book_service import DeleteBookService


class TestDeleteBookService(TestCase):
    def test_execute_WHEN_called_THEN_calls_repository_delete(self) -> None:
        delete_book_dto = DeleteBookDTO(uuid4())
        book_id = BookId(delete_book_dto.id)
        book_repository = mock(BookRepository)
        delete_book_service = DeleteBookService(book_repository)
        when(book_repository).delete(book_id)

        delete_book_service.execute(delete_book_dto)

        verify(book_repository).delete(book_id)
