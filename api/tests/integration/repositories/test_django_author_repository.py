from django.test import TestCase

from api.models import AuthorDTOModel
from api.repositories.django_author_repository import DjangoAuthorRepository
from api.tests.factories.author_factory import AuthorFactory
from domain.entities.author.dtos.author_dto import AuthorDTO


class TestDjangoAuthorRepository(TestCase):
    def test_save_WHEN_called_with_one_author_THEN_save_given_authors_dto_in_database(self) -> None:
        raw_name = 'Author Default Name'
        author = AuthorFactory.new(name=raw_name)
        expected_dto = AuthorDTO.from_entity(author)
        repository = DjangoAuthorRepository()

        repository.save(author)

        model = AuthorDTOModel.objects.get(id=author.id.value)
        actual_dto = model.to_dto()
        self.assertEqual(expected_dto, actual_dto)

    def test_save_WHEN_called_with_more_than_one_author_THEN_save_all_given_authors_dtos_in_database(self) -> None:
        names = ['Author 1', 'Author 2']
        authors = [AuthorFactory.new(name) for name in names]
        expected_dtos = [AuthorDTO.from_entity(author) for author in authors]
        repository = DjangoAuthorRepository()

        repository.save(authors[0], authors[1])

        models = [AuthorDTOModel.objects.get(id=author.id.value) for author in authors]
        actual_dtos = [model.to_dto() for model in models]
        self.assertEqual(expected_dtos, actual_dtos)

    def test_get_by_id_WHEN_called_THEN_returns_author_with_given_id(self) -> None:
        name = 'Author Name'
        expected_author = AuthorFactory.new(name=name)
        repository = DjangoAuthorRepository()
        repository.save(expected_author)

        actual_author = repository.get_by_id(expected_author.id)

        self.assertEqual(expected_author, actual_author)

    def test_get_all_WHEN_called_THEN_return_all_authors(self) -> None:
        names = ['Author 1', 'Author 2']
        expected_authors = [AuthorFactory.new(name) for name in names]
        repository = DjangoAuthorRepository()
        repository.save(expected_authors[0], expected_authors[1])

        actual_authors = repository.get_all()

        self.assertEqual(expected_authors, actual_authors)

