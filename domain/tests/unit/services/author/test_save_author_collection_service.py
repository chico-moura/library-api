from unittest import TestCase

from mockito import mock, when, unstub, verify

from domain.entities.author import Author
from domain.entities.author.dtos import AuthorCreationDTO
from domain.repositories import AuthorRepository
from domain.services import SaveAuthorCollectionService


class TestSaveAuthorCollectionService(TestCase):
    def tearDown(self) -> None:
        unstub()

    def test_execute_WHEN_called_THEN_calls_repository_save_with_authors_created_from_given_dtos(self) -> None:
        author_repository = mock(AuthorRepository)
        author_creation_dtos = [mock(AuthorCreationDTO) for _ in range(3)]
        authors = [mock(Author) for _ in author_creation_dtos]
        when(author_repository).save(*authors)
        [when(author_creation_dtos[index]).to_entity().thenReturn(authors[index]) for index in range(len(author_creation_dtos))]
        save_author_collection_service = SaveAuthorCollectionService(author_repository)

        save_author_collection_service.execute(author_creation_dtos)

        verify(author_repository).save(*authors)
