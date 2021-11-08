import os
import pathlib
from io import TextIOWrapper
from typing import BinaryIO, List
from unittest import TestCase

from mockito import unstub
from domain.entities.author.dtos.author_input_dto import AuthorCreationDTO
from domain.entities.authors_csv_file.authors_csv_file import AuthorsCSVFile


class TestAuthorsCSVFile(TestCase):
    file: BinaryIO
    names: List[str]
    author_csv_file: AuthorsCSVFile

    def setUp(self) -> None:
        example_file_name = 'example_authors_csv_file.csv'
        this_directory = pathlib.Path(__file__).parent.resolve()
        example_file_path = f'{this_directory}/{example_file_name}'
        self.file = open(example_file_path, 'rb')

        wrapper = TextIOWrapper(self.file)
        self.author_csv_file = AuthorsCSVFile(wrapper)

        self.names = ['Foo bar', 'Bar foo']

    def tearDown(self) -> None:
        self.file.close()
        unstub()

    def foo(self):
        print(self.file.name)

    def test_names_WHEN_called_THEN_returns_list_of_names_in_file(self) -> None:
        expected_result = self.names

        actual_result = self.author_csv_file.authors_names

        self.assertEqual(expected_result, actual_result)

    def test_to_dto_collection_WHEN_called_THEN_returns_dtos(self) -> None:
        expected_result = [AuthorCreationDTO(name) for name in self.names]

        actual_result = self.author_csv_file.to_dto_collection()

        self.assertEqual(expected_result, actual_result)

    def test_length_WHEN_called_THEN_returns_number_of_data_lines_in_file(self) -> None:
        expected_result = len(self.names)

        actual_result = self.author_csv_file.length

        self.assertEqual(expected_result, actual_result)

    def test_to_dto_collection_WHEN_length_property_is_used_before_THEN_still_returns_dtos(self) -> None:
        length = self.author_csv_file.length
        expected_result = [AuthorCreationDTO(name) for name in self.names]

        actual_result = self.author_csv_file.to_dto_collection()

        self.assertEqual(expected_result, actual_result)

