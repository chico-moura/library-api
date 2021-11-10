from mockito import when, unstub
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.tests.factories.author_model_test_factory import AuthorModelTestFactory

from api.models import AuthorModel


class TestAuthorsViews(APITestCase):
    def tearDown(self) -> None:
        unstub()

    def test_get_WHEN_called_THEN_return_response_with_status_200(self) -> None:
        models = [AuthorModelTestFactory.create() for _ in range(3)]
        when(AuthorModel.objects).all().thenReturn(models)
        url = reverse('authors')
        expected_status = status.HTTP_200_OK

        response = self.client.get(url)

        actual_status = response.status_code
        self.assertEqual(expected_status, actual_status)

    def test_get_WHEN_called_THEN_return_response_with_authors_data(self) -> None:
        pass
