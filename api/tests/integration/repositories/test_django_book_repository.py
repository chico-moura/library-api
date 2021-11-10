from django.test import TestCase
from testfixtures.django import compare

from api.models.book_model import BookModel
from api.repositories.django_book_repository import DjangoBookRepository
from api.tests.factories.book_model_test_factory import BookModelTestFactory
from domain.factories import BookFactory
from domain.tests.factories import BookIdTestFactory


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
