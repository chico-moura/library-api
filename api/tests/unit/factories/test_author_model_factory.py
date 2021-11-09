from unittest import TestCase

from api.factories.author_model_factory import AuthorModelFactory
from api.tests.factories.author_model_test_factory import AuthorModelTestFactory


class TestAuthorFactory(TestCase):
    def test_author_from_model_WHEN_called_THEN_return_author_with_given_author_id(self) -> None:
        model = AuthorModelTestFactory.create()

        author = AuthorModelFactory.author_from_model(model)

        self.assertEqual(model.id, author.id.value)
