from unittest import TestCase

from testfixtures import compare

from domain.entities import Book
from domain.factories import BookFactory
from domain.tests.factories import BookTestFactory


class TestBookFactory(TestCase):
    def test_create_existing_WHEN_called_THEN_returns_book_with_given_attributes(self) -> None:
        expected_book: Book = BookTestFactory.build()

        actual_book = BookFactory.build_existing(
            id_=expected_book.id.value,
            name=expected_book.name.value,
            edition=expected_book.edition.value,
            publication_year=expected_book.publication_year.value,
            authors=[author_id.value for author_id in expected_book.authors]
        )

        compare(expected_book, actual_book)
