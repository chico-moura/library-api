from unittest import TestCase

from mockito import when, mock, verify

from domain.repositories import BookRepository
from domain.services.book.create_book_service import CreateBookService
from domain.tests.factories import BookTestFactory
from domain.tests.factories.book_test_factories.book_creation_dto_test_factory import BookCreationDTOTestFactory


class TestCreateBookService(TestCase):
    def test_execute_WHEN_called_THEN_calls_repository_save_with_book_created_from_dto(self) -> None:
        book_creation_dto = BookCreationDTOTestFactory.build()
        book = BookTestFactory.build()
        book_repository = mock(BookRepository)
        when(book_creation_dto).to_entity().thenReturn(book)
        when(book_repository).save(book)
        create_book_service = CreateBookService(book_repository)

        create_book_service.execute(book_creation_dto)

        verify(book_repository).save(book)
