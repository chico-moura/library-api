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

    def test_get_WHEN_called_THEN_return_response_with_authors_data(self) -> None:
        authors = [
            AuthorFactory.new(name='Author 1'),
            AuthorFactory.new(name='Author 2')
        ]
        # FIXME: why can't I generalize AuthorRepository? when(AuthorRepository)
        when(DjangoAuthorRepository).get_all().thenReturn(authors)
        authors_view = AuthorsView()
        request = Request(HttpRequest())
        expected_ids = [author.id.value for author in authors]

        response = authors_view.get(request)

        actual_ids = [UUID(data['id']) for data in response.data]
        self.assertEqual(expected_ids, actual_ids)
