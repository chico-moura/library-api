from api.exceptions.managment_commands_exceptions.file_does_not_have_csv_extension_exception import \
    FileDoesNotHaveCSVExtensionException
from api.management.management_enum import ManagementEnum


class CSVValidationService:
    @staticmethod
    def validate_extension(file_name: str) -> None:
        extension = file_name.split('.')[-1]
        if extension != ManagementEnum.CSV_EXTENSION:
            raise FileDoesNotHaveCSVExtensionException()
