from csv import DictReader
from io import TextIOWrapper
from typing import List

from domain.entities.author.dtos.author_input_dto import AuthorCreationDTO


# FIXME: send me to api layer or make service receives file path


class AuthorsCSVFile:
    __file: TextIOWrapper
    __dict_reader: DictReader

    def __init__(self, file: TextIOWrapper) -> None:
        self.__file = file
        self.__dict_reader = DictReader(file)

    @property
    def authors_names(self) -> List[str]:
        return [row['name'] for row in self.__dict_reader]

    @property
    def length(self) -> int:
        reader_as_list = list(self.__dict_reader)
        self._reset_reader()
        return len(reader_as_list)

    def to_dto_collection(self) -> List[AuthorCreationDTO]:
        return [AuthorCreationDTO(name=name) for name in self.authors_names]

    def _reset_reader(self) -> None:
        self.__file.seek(0)
        self.__dict_reader = DictReader(self.__file)
