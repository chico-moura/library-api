from unittest import TestCase
from mockito import when, unstub

from domain.entities.author.value_objects import AuthorName
from domain.exceptions.value_objects.author_name_exceptions.author_name_too_long_exception import \
    AuthorNameTooLongException
from domain.exceptions.value_objects.author_name_exceptions.author_name_too_short_exception import \
    AuthorNameTooShortException
from domain.settings import AuthorSettings


# FIXME: should test __init__, not save. no one cares about validate()

class TestAuthorName(TestCase):
    def tearDown(self) -> None:
        unstub()

    def test_init_WHEN_called_with_valid_name_THEN_assigns_given_name_to_value(self) -> None:
        expected_value = 'Author Name'

        author_name = AuthorName(expected_value)

        self.assertEqual(expected_value, author_name.value)

    def test_validate_WHEN_author_name_is_too_long_THEN_raises_author_name_too_long_exception(self) -> None:
        max_size = AuthorSettings.NAME_MAX_LENGTH
        name = 'a' * (max_size + 1)
        when(AuthorName).__post_init__()
        author_name = AuthorName(name)

        with self.assertRaises(AuthorNameTooLongException):
            author_name.validate()

    def test_validate_WHEN_author_name_is_not_too_long_THEN_does_not_raises_author_name_too_long_exception(self) -> None:
        max_size = AuthorSettings.NAME_MAX_LENGTH
        name = 'a' * max_size
        when(AuthorName).__post_init__()
        author_name = AuthorName(name)

        try:
            author_name.validate()

        except AuthorNameTooLongException:
            self.fail('AuthorNameTooLongException raised unexpectedly')

    def test_validate_WHEN_author_name_is_too_short_THEN_raises_author_name_too_short_exception(self) -> None:
        min_size = AuthorSettings.NAME_MIN_LENGTH
        name = 'a' * (min_size - 1)
        when(AuthorName).__post_init__()
        author_name = AuthorName(name)

        with self.assertRaises(AuthorNameTooShortException):
            author_name.validate()

    def test_validate_WHEN_author_name_is_not_too_short_THEN_does_not_raises_author_name_too_short_exception(self) -> None:
        min_size = AuthorSettings.NAME_MIN_LENGTH
        name = 'a' * min_size
        when(AuthorName).__post_init__()
        author_name = AuthorName(name)

        try:
            author_name.validate()

        except AuthorNameTooShortException:
            self.fail('AuthorNameTooShortException raised unexpectedly')
