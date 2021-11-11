from uuid import uuid4
from django.test import TestCase
from testfixtures.django import compare

from api.models.book_model import BookModel
from api.repositories.django_book_repository import DjangoBookRepository
from api.tests.factories.book_model_test_factory import BookModelTestFactory
from domain.entities.book.book import Book
from domain.entities.book.value_objects.book_id import BookId
from domain.entities.book.value_objects.book_name import BookName
from domain.exceptions.book.book_not_found_exception import BookNotFoundException
from domain.factories import BookFactory
from domain.tests.factories import BookIdTestFactory
from domain.tests.factories.book_test_factories.book_test_factory import BookTestFactory


class TestDjangoBookRepository(TestCase):
    def test_get_by_id_WHEN_called_THEN_retrieves_given_book_from_database(self) -> None:
        book_model: BookModel = BookModelTestFactory.create()
        book_id = BookIdTestFactory.build(value=book_model.id)
        django_book_repository = DjangoBookRepository()

        actual_book = django_book_repository.get_by_id(book_id)

        expected_book = BookFactory.build_existing(
            id_=book_model.id,
            name=book_model.name,
            edition=book_model.edition,
            publication_year=book_model.publication_year,
            authors=[author.id for author in book_model.authors.all()]
        )
        compare(expected_book, actual_book)

    def test_get_by_id_WHEN_book_does_not_exist_THEN_raises_book_not_found_exception(self) -> None:
        unexisting_book_id = BookId(uuid4())
        django_book_repository = DjangoBookRepository()

        with self.assertRaises(BookNotFoundException):
            django_book_repository.get_by_id(unexisting_book_id)

    def test_delete_WHEN_book_exists_THEN_deletes_given_book_model(self) -> None:
        book_model: BookModel = BookModelTestFactory.create()
        book_id = BookId(book_model.id)
        django_book_repository = DjangoBookRepository()

        django_book_repository.delete(book_id)

        book_exists = BookModel.objects.filter(pk=book_id.value).exists()
        self.assertFalse(book_exists)

    def test_delete_WHEN_book_does_not_exists_THEN_raises_book_not_found_exception(self) -> None:
        unexisting_book_id = BookId(uuid4())
        django_book_repository = DjangoBookRepository()

        with self.assertRaises(BookNotFoundException):
            django_book_repository.delete(unexisting_book_id)

    def test_filter_by_WHEN_filtering_by_name_THEN_returns_books_that_matches_name(self) -> None:
        book_name = BookName('Fake name')
        book_authors = []
        book_models = BookModelTestFactory.create_batch(1, name=book_name.value, authors=book_authors)
        django_book_repository = DjangoBookRepository()

        result_books = django_book_repository.filter_by(name=book_name)

        expected_books = [BookTestFactory.build(
            id__value=book_models[0].id,
            name__value=book_models[0].name,
            edition__value=book_models[0].edition,
            publication_year__value=book_models[0].publication_year,
            authors=book_authors,
        )]
        compare(expected_books, result_books)
