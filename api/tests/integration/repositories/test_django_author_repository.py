from django.test import TestCase

from api.factories.author_model_factory import AuthorModelFactory
from api.models import AuthorModel
from api.repositories.django_author_repository import DjangoAuthorRepository
from domain.tests.factories import AuthorTestFactory


class TestDjangoAuthorRepository(TestCase):
    def test_save_WHEN_called_with_one_author_THEN_save_given_authors_in_database(self) -> None:
        author = AuthorTestFactory.build()
        expected_attributes = [
            author.id.value,
            author.name.value
        ]
        repository = DjangoAuthorRepository()

        repository.save(author)

        model = AuthorModel.objects.get(id=author.id.value)
        actual_attributes = [
            model.id,
            model.name
        ]
        self.assertEqual(expected_attributes, actual_attributes)

    def test_save_WHEN_called_with_more_than_one_author_THEN_save_all_given_authors_in_database(self) -> None:
        expected_authors = [AuthorTestFactory.build() for _ in range(2)]
        repository = DjangoAuthorRepository()

        repository.save(*expected_authors)

        actual_authors = []
        for expected_author in expected_authors:
            model = AuthorModel.objects.get(id=expected_author.id.value)
            actual_author = AuthorModelFactory.author_from_model(model)
            actual_authors.append(actual_author)
        self.assertEqual(expected_authors, expected_authors)

    def test_get_by_id_WHEN_called_THEN_returns_author_with_given_id(self) -> None:
        expected_author = AuthorTestFactory.build()
        model = AuthorModelFactory.model_from_author(expected_author)
        model.save()
        repository = DjangoAuthorRepository()

        actual_author = repository.get_by_id(expected_author.id)

        self.assertEqual(expected_author, actual_author)

    def test_get_all_WHEN_called_THEN_return_all_authors(self) -> None:
        expected_authors = [AuthorTestFactory.build() for _ in range(2)]
        for expected_author in expected_authors:
            model = AuthorModelFactory.model_from_author(expected_author)
            model.save()
        repository = DjangoAuthorRepository()

        actual_authors = repository.get_all()

        self.assertEqual(expected_authors, actual_authors)

