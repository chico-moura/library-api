from factory import Factory, SubFactory

from domain.entities import Author

from domain.tests.factories.author_test_factories import AuthorIdTestFactory
from domain.tests.factories.author_test_factories.author_name_test_factory import AuthorNameTestFactory


class AuthorTestFactory(Factory):
    class Meta:
        model = Author

    id = SubFactory(AuthorIdTestFactory)
    name = SubFactory(AuthorNameTestFactory)
