from uuid import uuid4

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from testfixtures.django import compare

from api.models.book_model import BookModel
from api.tests.factories.book_model_test_factory import BookModelTestFactory


class TestBookDetailsView(APITestCase):
    def test_get_WHEN_book_is_found_THEN_returns_status_200(self) -> None:
        book_model: BookModel = BookModelTestFactory.create()
        url = reverse('book_details', kwargs={'book_id': book_model.id})

        response = self.client.get(
            path=url,
        )

        expected_status = status.HTTP_200_OK
        actual_status = response.status_code
        self.assertEqual(expected_status, actual_status)

    def test_get_WHEN_book_is_found_THEN_returns_payload(self) -> None:
        book_model: BookModel = BookModelTestFactory.create()
        url = reverse('book_details', kwargs={'book_id': book_model.id})

        response = self.client.get(
            path=url,
        )

        expected_payload = {
            'id': str(book_model.id),
            'name': book_model.name,
            'edition': book_model.edition,
            'publication_year': book_model.publication_year,
            'authors': [str(author.id) for author in book_model.authors.all()]
        }
        actual_payload = response.json()
        compare(expected_payload, actual_payload)

    def test_get_WHEN_book_is_not_found_THEN_returns_status_404(self) -> None:
        book_id = uuid4()
        url = reverse('book_details', kwargs={'book_id': book_id})

        response = self.client.get(
            path=url,
        )

        expected_status = status.HTTP_404_NOT_FOUND
        actual_status = response.status_code
        self.assertEqual(expected_status, actual_status)

    def test_put_WHEN_book_found_THEN_returns_status_code_200(self):
        pass

    def test_put_WHEN_book_found_THEN_returns_payload_with_updated_book(self):
        pass

    def test_put_WHEN_book_not_found_THEN_returns_status_code_404(self):
        book_model: BookModel = BookModelTestFactory.build()
        update_book_data={
            'name': book_model.name,
            'edition': book_model.edition,
            'publication_year': book_model.publication_year,
            'authors': []
        }
        url = reverse('book_details', kwargs={'book_id': book_model.id})

        response = self.client.put(
            path=url,
            data=update_book_data
        )

        expected_status = status.HTTP_404_NOT_FOUND
        self.assertEqual(expected_status, response.status_code)
