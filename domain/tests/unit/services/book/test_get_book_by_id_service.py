from unittest import TestCase
from uuid import uuid4

from mockito import when, mock, unstub

from domain.repositories import BookRepository
from domain.tests.factories import BookTestFactory
from domain.services.book.get_book_by_id_service import GetBookByIdService
from domain.entities.book.dtos.book_dto import BookDTO
from domain.entities.book.dtos.get_book_by_id_dto import GetBookByIdDTO
from domain.tests.factories.author_test_factories.author_test_factory import AuthorTestFactory


class TestGetBookByIdService(TestCase):
    def setUp(self) -> None:
        raw_book_id = uuid4()
        authors = AuthorTestFactory.build_batch(2)
        author_ids = [authors[0].id, authors[1].id]
        self.book = BookTestFactory.build(id__value=raw_book_id, authors=author_ids)
        self.book_repository = mock(BookRepository)
        self.dto = GetBookByIdDTO(self.book.id.value)
        when(self.dto).to_book_id().thenReturn(self.book.id)
        when(self.book_repository).get_by_id(self.book.id).thenReturn(self.book)
        return super().setUp()

    def tearDown(self) -> None:
        unstub()
        return super().tearDown()

    def test_execute_WHEN_called_THEN_returns_book_dto(self) -> None:
        get_book_by_id_service = GetBookByIdService(self.book_repository)

        result_book_dto = get_book_by_id_service.execute(self.dto)

        expected_book_dto = BookDTO(
            id=self.book.id.value,
            name=self.book.name.value,
            edition=self.book.edition.value,
            publication_year=self.book.publication_year.value,
            authors=[self.book.authors[0].value, self.book.authors[1].value]
        )
        self.assertEqual(expected_book_dto, result_book_dto)
