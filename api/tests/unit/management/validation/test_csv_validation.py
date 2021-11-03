from unittest import TestCase

from api.exceptions.managment_commands_exceptions.file_does_not_have_csv_extension_exception import \
    FileDoesNotHaveCSVExtensionException
from api.management.validation.csv_validation import CSVValidationService


class TestCSVValidation(TestCase):
    def test_validate_extension_WHEN_file_name_has_write_extension_THEN_does_not_raise_exceptions(self) -> None:
        file_name = 'foo.csv'

        try:
            CSVValidationService.validate_extension(file_name)

        except Exception:
            self.fail('Exception called unexpectedly')

    def test_validate_extension_WHEN_file_name_has_different_extension_THEN_raises_file_does_not_have_csv_extension_exception(self) -> None:
        file_name = 'foo.json'

        with self.assertRaises(FileDoesNotHaveCSVExtensionException):
            CSVValidationService.validate_extension(file_name)

    def test_validate_extension_WHEN_file_name_has_no_extension_THEN_raises_file_does_not_have_csv_extension_exception(self) -> None:
        file_name = 'foo'

        with self.assertRaises(FileDoesNotHaveCSVExtensionException):
            CSVValidationService.validate_extension(file_name)
