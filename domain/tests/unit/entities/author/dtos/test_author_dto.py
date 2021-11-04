import uuid
from unittest import TestCase

from domain.entities.author.author import Author
from domain.entities.author.dtos.author_output_dto import AuthorOutputDTO
from domain.entities.author.value_objects.author_id import AuthorId
from domain.entities.author.value_objects.author_name import AuthorName


class TestAuthorDTO(TestCase):
    def test_from_entity_WHEN_called_with_author_THEN_returns_author_dto_with_string_representation_of_author_id(self) -> None:
        author_name = AuthorName('Fake Name')
        author_id = AuthorId(uuid.uuid4())
        author = Author(id=author_id, name=author_name)
        expected_stringified_id = author_id.value

        author_dto = AuthorOutputDTO.from_entity(author)

        self.assertEqual(expected_stringified_id, author_dto.id)

    def test_from_entity_WHEN_called_with_author_THEN_returns_author_dto_with_same_name(self) -> None:
        author_name = AuthorName('Fake Name')
        author_id = AuthorId(uuid.uuid4())
        author = Author(id=author_id, name=author_name)
        expected_name = author_name.value

        author_dto = AuthorOutputDTO.from_entity(author)

        self.assertEqual(expected_name, author_dto.name)

    def test_to_entity_WHEN_called_THEN_returns_author_with_same_id(self) -> None:
        expected_id = uuid.uuid4()
        raw_name = 'Fake Name'
        author_dto = AuthorOutputDTO(id=expected_id, name=raw_name)

        author = author_dto.to_entity()

        self.assertEqual(expected_id, author.id.value)

    def test_to_entity_WHEN_called_THEN_returns_author_with_same_name(self) -> None:
        expected_name = 'Fake Name'
        raw_id = uuid.uuid4()
        author_dto = AuthorOutputDTO(id=raw_id, name=expected_name)

        author = author_dto.to_entity()

        self.assertEqual(expected_name, author.name.value)
