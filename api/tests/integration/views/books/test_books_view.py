from uuid import uuid4

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from testfixtures import compare

from api.tests.factories.author_model_test_factory import AuthorModelTestFactory
from api.tests.factories.book_model_test_factory import BookModelTestFactory


class TestBooksView(APITestCase):
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
            data=payload,
            format='json'
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
            data=payload,
            format='json'
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
            data=payload,
            format='json'
        )

        expected_status = status.HTTP_400_BAD_REQUEST
        actual_status = response.status_code
        self.assertEqual(expected_status, actual_status)

    def test_get_WHEN_called_THEN_returns_status_code_200(self) -> None:
        url = reverse('books')

        response = self.client.get(
            path=url,
        )

        expected_status = status.HTTP_200_OK
        self.assertEqual(expected_status, response.status_code)

    def test_get_WHEN_filtering_by_name_THEN_returns_books_that_match_book_name(self) -> None:
        book_id = uuid4()
        book_name = 'Fake book name'
        book_authors = []
        book_model = BookModelTestFactory.create(id=book_id, name=book_name, authors=book_authors)
        url = reverse('books') + f'?name={book_name}'

        response = self.client.get(
            path=url,
        )

        expected_books_payload = [{
            'id': str(book_id),
            'name': book_name,
            'edition': book_model.edition,
            'publication_year': book_model.publication_year,
            'authors': book_authors
        }]
        compare(expected_books_payload, response.json())
