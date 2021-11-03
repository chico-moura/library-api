from unittest import TestCase

from api.exceptions.managment_commands_exceptions.file_does_not_have_csv_extension_exception import \
    FileDoesNotHaveCSVExtensionException
from api.exceptions.managment_commands_exceptions.file_not_found import FileNotFoundException
from api.management.validation.csv_validation import CSVValidationService


class TestCSVValidation(TestCase):
    def test_validate_extension_WHEN_file_name_has_write_extension_THEN_does_not_raise_file_does_not_have_csv_extension_exception(self) -> None:
        file_name = 'foo.csv'

        try:
            CSVValidationService.validate_extension(file_name)

        except FileDoesNotHaveCSVExtensionException:
            self.fail('FileDoesNotHaveCSVExtensionException raised unexpectedly')

    def test_validate_extension_WHEN_file_name_has_different_extension_THEN_raises_file_does_not_have_csv_extension_exception(self) -> None:
        file_name = 'foo.json'

        with self.assertRaises(FileDoesNotHaveCSVExtensionException):
            CSVValidationService.validate_extension(file_name)

    def test_validate_extension_WHEN_file_name_has_no_extension_THEN_raises_file_does_not_have_csv_extension_exception(self) -> None:
        file_name = 'foo'

        with self.assertRaises(FileDoesNotHaveCSVExtensionException):
            CSVValidationService.validate_extension(file_name)

    def test_validate_existence_WHEN_file_exists_THEN_does_not_raise_file_not_found_exception(self) -> None:
        file_path = __file__

        try:
            CSVValidationService.validate_existence(file_path)

        except FileNotFoundException:
            self.fail('FileNotFoundException raised unexpectedly')

    def test_validate_existence_WHEN_file_does_not_exists_THEN_does_not_raise_file_not_found_exception(self) -> None:
        file_path = 'fake_path'

        with self.assertRaises(FileNotFoundException):
            CSVValidationService.validate_existence(file_path)


