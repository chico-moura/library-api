from os import path

from api.exceptions.managment_commands_exceptions.file_does_not_have_csv_extension_exception import \
    FileDoesNotHaveCSVExtensionException
from api.exceptions.managment_commands_exceptions.file_not_found import FileNotFoundException
from api.management.management_enum import ManagementEnum


class CSVValidationService:
    @staticmethod
    def excecute(file_path: str) -> None:
        CSVValidationService.validate_extension(file_path)

    @staticmethod
    def validate_extension(file_name: str) -> None:
        extension = file_name.split('.')[-1]

        if extension != ManagementEnum.CSV_EXTENSION.value:
            raise FileDoesNotHaveCSVExtensionException()

    @staticmethod
    def validate_existence(file_path: str) -> None:
        if not path.exists(file_path):
            raise FileNotFoundException()
