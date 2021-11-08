from uuid import UUID

from django.http import HttpRequest
from django.test import TestCase
from mockito import when, unstub
from rest_framework.request import Request

from api.repositories.django_author_repository import DjangoAuthorRepository
from api.tests.factories.author_factory import AuthorFactory
from api.views.authors_view import AuthorsView


class TestAuthorsViews(TestCase):
    def tearDown(self) -> None:
        unstub()

    # FIXME: tests must as less DRY as possible.
    # TODO: another test: response status
    def test_get_WHEN_called_THEN_return_response_with_authors_data(self) -> None:
        authors = [
            AuthorFactory.new(name='Author 1'),
            AuthorFactory.new(name='Author 2')
        ]
        # TODO: follow this example
        # when(AuthorDTOModel.objects).all().thenReturn(authors)
        when(DjangoAuthorRepository).get_all().thenReturn(authors)
        authors_view = AuthorsView()
        request = Request(HttpRequest())
        expected_ids = [author.id.value for author in authors]

        # TODO: use APITestCase from django to send an actual request instead of calling class method
        response = authors_view.get(request)

        # FIXME: make it compare all author data
        actual_ids = [UUID(data['id']) for data in response.data]
        self.assertEqual(expected_ids, actual_ids)
