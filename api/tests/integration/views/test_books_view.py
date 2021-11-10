from uuid import uuid4

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from testfixtures import compare

from api.tests.factories.author_model_test_factory import AuthorModelTestFactory


class TestBooksView(TestCase):
    def test_post_WHEN_called_with_valid_data_THEN_returns_status_201(self) -> None:
        author_id = uuid4()
        payload = {
            'name': 'fake name',
            'edition': '1',
            'publication_year': '2121',
            'authors': [str(author_id)]
        }
        url = reverse('books')
        AuthorModelTestFactory.create(id=author_id)

        response = self.client.post(
            path=url,
            data=payload
        )

        expected_status = status.HTTP_201_CREATED
        actual_status = response.status_code
        self.assertEqual(expected_status, actual_status)

    def test_post_WHEN_called_with_valid_data_THEN_returns_payload(self) -> None:
        author_id = uuid4()
        payload = {
            'name': 'fake name',
            'edition': '1',
            'publication_year': '2121',
            'authors': [str(author_id)]
        }
        url = reverse('books')
        AuthorModelTestFactory.create(id=author_id)

        response = self.client.post(
            path=url,
            data=payload
        )

        expected_payload = payload
        actual_payload = response.json()
        actual_payload.pop('id')
        compare(expected_payload, actual_payload)

    def test_post_WHEN_called_with_invalid_data_THEN_returns_status_400(self) -> None:
        author_id = uuid4()
        payload = {
            'name': 'fake name',
        }
        url = reverse('books')
        AuthorModelTestFactory.create(id=author_id)

        response = self.client.post(
            path=url,
            data=payload
        )

        expected_status = status.HTTP_400_BAD_REQUEST
        actual_status = response.status_code
        self.assertEqual(expected_status, actual_status)
