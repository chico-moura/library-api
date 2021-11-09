from unittest import TestCase

from domain.entities.author.dtos import AuthorDTO
from domain.tests.factories import AuthorTestFactory, AuthorDTOTestFactory


class TestAuthorDTO(TestCase):
    def test_from_entity_WHEN_called_with_author_THEN_returns_author_dto_with_matching_attributes(self) -> None:
        author = AuthorTestFactory.build()
        expected_attributes = [
            author.id.value,
            author.name.value
        ]

        author_dto = AuthorDTO.from_entity(author)

        actual_attributes = [
            author_dto.id,
            author_dto.name
        ]
        self.assertEqual(expected_attributes, actual_attributes)

    def test_to_entity_WHEN_called_THEN_returns_author_with_matching_attributes(self) -> None:
        author_dto = AuthorDTOTestFactory.build()
        expected_attributes = [
            author_dto.id,
            author_dto.name
        ]

        author = author_dto.to_entity()

        actual_attributes = [
            author.id.value,
            author.name.value
        ]
        self.assertEqual(expected_attributes, actual_attributes)
