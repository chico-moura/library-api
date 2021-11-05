from django.test import TestCase

from api.models import AuthorDTOModel
from api.repositories.django_author_repository import DjangoAuthorRepository
from api.tests.factories.author_factory import AuthorFactory
from domain.entities.author.dtos.author_dto import AuthorDTO


class TestDjangoAuthorRepository(TestCase):
    default_author_name: str

    def setUp(self) -> None:
        self.default_author_name = 'Author Default Name'

    def test_save_WHEN_called_with_one_author_THEN_save_given_authors_dto_in_database(self) -> None:
        author = AuthorFactory.new(self.default_author_name)
        author_dto = AuthorDTO.from_entity(author)
        repository = DjangoAuthorRepository()

        repository.save(author)

        saved_dto = AuthorDTOModel.objects.get(id=author.id.value)
        self.assertEqual(author_dto, saved_dto)
