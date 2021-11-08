from unittest import TestCase

from mockito import mock, when, unstub, verify

from domain.entities.author.author import Author
from domain.entities.author.dtos.author_input_dto import AuthorCreationDTO
from domain.repositories.author_repository import AuthorRepository
from domain.services.author.save_author_collection_service import SaveAuthorCollectionService


class TestSaveAuthorCollectionService(TestCase):
    def tearDown(self) -> None:
        unstub()

    # FIXME: shrink it

    def test_execute_WHEN_called_THEN_calls_repository_save_with_authors_created_from_given_dtos(self) -> None:
        dto1 = mock(AuthorCreationDTO)
        dto2 = mock(AuthorCreationDTO)
        author1 = mock(Author)
        author2 = mock(Author)
        when(dto1).to_entity().thenReturn(author1)
        when(dto2).to_entity().thenReturn(author2)
        author_repository = mock(AuthorRepository)
        when(author_repository).save(author1, author2)
        author_dtos = [dto1, dto2]
        save_author_collection_service = SaveAuthorCollectionService(author_repository)

        save_author_collection_service.execute(author_dtos)

        verify(author_repository).save(author1, author2)
