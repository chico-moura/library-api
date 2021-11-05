from unittest import TestCase
from unittest.mock import create_autospec

from domain.entities.author.author import Author
from domain.entities.author.dtos.author_dto import AuthorDTO
from domain.repositories.author_repository import AuthorRepository
from domain.services.save_author_service import SaveAuthorService


class TestSaveAuthorService(TestCase):
    def test_execute_WHEN_called_THEN_calls_author_repository_save_with_respective_author(self) -> None:
        author_repository = create_autospec(AuthorRepository)
        author_dto = create_autospec(AuthorDTO)
        author: Author = create_autospec(Author)
        author_dto.to_entity.return_value = author
        save_author_service = SaveAuthorService(author_repository)

        save_author_service.execute(author_dto)

        author_repository.save.assert_called_with(author)
