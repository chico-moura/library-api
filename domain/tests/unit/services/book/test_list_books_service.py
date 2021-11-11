from unittest import TestCase
from uuid import uuid4

from mockito import when, mock, unstub

from domain.repositories import BookRepository
from domain.tests.factories import BookTestFactory
from domain.services.book.list_books_service import ListBooksService
from domain.entities.book.dtos.book_dto import BookDTO
from domain.entities.book.dtos.list_books_input_dto import ListBooksInputDTO


class TestListBooksService(TestCase):
    def setUp(self) -> None:
        raw_book_id = uuid4()
        self.book = BookTestFactory.build(id__value=raw_book_id, authors=[])
        self.book_repository = mock(BookRepository)
        when(self.book_repository).filter_by(...).thenReturn([self.book])
        return super().setUp()

    def tearDown(self) -> None:
        unstub()
        return super().tearDown()

    def test_execute_WHEN_called_THEN_returns_book_dto(self) -> None:
        name = 'Fake name'
        edition = 'Fake Edition'
        publication_year = '2021'
        author_id = uuid4()
        dto = ListBooksInputDTO(
            name=name,
            edition=edition,
            publication_year=publication_year,
            author_id=author_id
        )
        list_books_service = ListBooksService(self.book_repository)

        result_book_dtos = list_books_service.execute(dto)

        expected_book_dtos = [BookDTO(
            id=self.book.id.value,
            name=self.book.name.value,
            edition=self.book.edition.value,
            publication_year=self.book.publication_year.value,
            authors=[]
        )]
        self.assertEqual(expected_book_dtos, result_book_dtos)
