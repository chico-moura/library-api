from unittest import TestCase

from mockito import mock, unstub, when, verify

from domain.entities.book.dtos import BookDTO
from domain.repositories import BookRepository
from domain.services.book.update_book_service import UpdateBookService
from domain.tests.factories import BookDTOTestFactory


class TestUpdateBookService(TestCase):
    def setUp(self) -> None:
        self.book_dto: BookDTO = BookDTOTestFactory.build()
        self.book = self.book_dto.to_entity()
        self.book_repository: BookRepository = mock(BookRepository)

        when(self.book_repository).save(...)
        when(self.book_repository).get_by_id(self.book.id).thenReturn(self.book)

    def tearDown(self) -> None:
        unstub()

    def test_execute_WHEN_called_THEN_calls_repository_save(self) -> None:
        update_book_service = UpdateBookService(self.book_repository)

        update_book_service.execute(self.book_dto)

        verify(self.book_repository).save(self.book)

    def test_execute_WHEN_called_THEN_calls_repository_get_by_id(self) -> None:
        update_book_service = UpdateBookService(self.book_repository)

        update_book_service.execute(self.book_dto)

        verify(self.book_repository).get_by_id(self.book.id)
