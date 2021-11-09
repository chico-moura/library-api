from mockito import when, unstub
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.factories.author_model_factory import AuthorModelFactory
from domain.tests.factories import AuthorTestFactory

from api.models import AuthorModel


class TestAuthorsViews(APITestCase):
    def tearDown(self) -> None:
        unstub()

    def test_get_WHEN_called_THEN_return_response_with_status_200(self) -> None:
        models = []
        for _ in range(3):
            author = AuthorTestFactory.build()
            model = AuthorModelFactory.model_from_author(author)
            models.append(model)

        when(AuthorModel.objects).all().thenReturn(models)
        url = reverse('authors')
        expected_status = status.HTTP_200_OK

        response = self.client.get(url)

        actual_status = response.status_code
        self.assertEqual(expected_status, actual_status)

    def test_get_WHEN_called_THEN_return_response_with_authors_data(self) -> None:
        pass
