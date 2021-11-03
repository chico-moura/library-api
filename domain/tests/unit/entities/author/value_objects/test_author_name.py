from unittest import TestCase

from mockito import when, unstub

from domain.entities.author.value_objects.author_name import AuthorName
from domain.exceptions.value_objects.author_name_exceptions.author_name_too_long_exception import \
    AuthorNameTooLongException
from domain.exceptions.value_objects.author_name_exceptions.author_name_too_short_exception import \
    AuthorNameTooShortException


class TestAuthorName(TestCase):
    def tearDown(self) -> None:
        unstub()

    def test_validate_WHEN_author_name_is_too_long_THEN_raises_author_name_too_long_exception(self) -> None:
        name = 'a' * 300
        when(AuthorName).__post_init__()
        author_name = AuthorName(name)

        with self.assertRaises(AuthorNameTooLongException):
            author_name.validate()

    def test_validate_WHEN_author_name_is_not_too_long_THEN_does_not_raises_author_name_too_long_exception(self) -> None:
        name = 'a' * 100
        when(AuthorName).__post_init__()
        author_name = AuthorName(name)

        try:
            author_name.validate()

        except AuthorNameTooLongException:
            self.fail('AuthorNameTooLongException raised unexpectedly')

    def test_validate_WHEN_author_name_is_too_short_THEN_raises_author_name_too_short_exception(self) -> None:
        name = ''
        when(AuthorName).__post_init__()
        author_name = AuthorName(name)

        with self.assertRaises(AuthorNameTooShortException):
            author_name.validate()

    def test_validate_WHEN_author_name_is_not_too_short_THEN_does_not_raises_author_name_too_short_exception(self) -> None:
        name = 'a' * 100
        when(AuthorName).__post_init__()
        author_name = AuthorName(name)

        try:
            author_name.validate()

        except AuthorNameTooShortException:
            self.fail('AuthorNameTooShortException raised unexpectedly')
