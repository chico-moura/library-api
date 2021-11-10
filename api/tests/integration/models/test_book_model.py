from django.test import TestCase

from api.models.book_model import BookModel
from api.repositories.django_author_repository import DjangoAuthorRepository
from api.repositories.django_book_repository import DjangoBookRepository
from api.tests.factories.book_model_test_factory import BookModelTestFactory
from domain.tests.factories import BookTestFactory, AuthorTestFactory


# FIXME: is this test ok?
# TODO: isort

class TestBookModel(TestCase):
    def test_from_entity_WHEN_called_with_book_THEN_returns_book_model_with_matching_attributes(self) -> None:
        author_repository = DjangoAuthorRepository()
        book_repository = DjangoBookRepository()
        author = AuthorTestFactory.build()
        author_repository.save(author)
        book = BookTestFactory.build(authors=[author.id])
        book_repository.save(book)
        expected_attributes = [
            book.id.value,
            book.name.value,
            book.edition.value,
            book.publication_year.value,
            [author_id.value for author_id in book.authors]
        ]

        model = BookModel.from_entity(book)

        actual_attributes = [
            model.id,
            model.name,
            model.edition,
            model.publication_year,
            [author.id for author in model.authors.all()]
        ]
        self.assertEqual(expected_attributes, actual_attributes)

    def test_to_entity_WHEN_called_THEN_returns_book_with_matching_attributes(self) -> None:
        model: BookModel = BookModelTestFactory.create()
        expected_attributes = [
            model.id,
            model.name,
            model.edition,
            model.publication_year,
        ]

        book = model.to_entity()

        actual_attributes = [
            book.id.value,
            book.name.value,
            book.edition.value,
            book.publication_year.value,
        ]
        self.assertEqual(expected_attributes, actual_attributes)
