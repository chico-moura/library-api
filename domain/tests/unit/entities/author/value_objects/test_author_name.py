from unittest import TestCase

from domain.entities.author.value_objects import AuthorName
from domain.exceptions import ValidationException


class TestAuthorName(TestCase):
    def test_init_WHEN_called_with_valid_name_THEN_assigns_given_name_to_value(self) -> None:
        expected_value = 'Author Name'

        author_name = AuthorName(expected_value)

        self.assertEqual(expected_value, author_name.value)

    def test_init_WHEN_author_name_is_too_long_THEN_raises_validation_exception(self) -> None:
        length_too_long = 251

        name = 'a' * length_too_long

        with self.assertRaises(ValidationException):
            AuthorName(name)

    def test_init_WHEN_author_name_is_not_too_long_THEN_does_not_raises_validation_exception(self) -> None:
        acceptable_length = 250
        name = 'a' * acceptable_length

        try:
            AuthorName(name)

        except ValidationException:
            self.fail('AuthorNameTooLongException raised unexpectedly')

    def test_init_WHEN_author_name_is_too_short_THEN_raises_validation_exception(self) -> None:
        length_too_short = 1
        name = 'a' * length_too_short

        with self.assertRaises(ValidationException):
            AuthorName(name)

    def test_init_WHEN_author_name_is_not_too_short_THEN_does_not_raises_validation_exception(self) -> None:
        acceptable_length = 2
        name = 'a' * acceptable_length

        try:
            AuthorName(name)

        except ValidationException:
            self.fail('AuthorNameTooShortException raised unexpectedly')
