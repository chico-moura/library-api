from unittest import TestCase
import uuid

from domain.entities.author.value_objects.author_id import AuthorId


class TestAuthorId(TestCase):
    def test_init_WHEN_called_with_uuid_THEN_assigns_given_uuid_to_value(self) -> None:
        expected_uuid = uuid.uuid4()

        author_id = AuthorId(expected_uuid)

        self.assertEqual(expected_uuid, author_id.value)

    def test_init_WHEN_called_without_uuid_THEN_assigns_uuid_to_value(self) -> None:
        author_id = AuthorId()

        self.assertIsInstance(author_id.value, uuid.UUID)
