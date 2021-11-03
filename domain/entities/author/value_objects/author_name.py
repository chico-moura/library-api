from dataclasses import dataclass

from domain.exceptions.value_objects.author_name_exceptions.author_name_too_long_exception import \
    AuthorNameTooLongException
from domain.exceptions.value_objects.author_name_exceptions.author_name_too_short_exception import \
    AuthorNameTooShortException
from shared.value_object import ValueObject


@dataclass(frozen=True)
class AuthorName(ValueObject):
    value: str

    def validate(self) -> None:
        self.__validate_max_length()
        self.__validate_min_length()

    def __validate_max_length(self) -> None:
        max_length = 250

        if len(self.value) > max_length:
            raise AuthorNameTooLongException

    def __validate_min_length(self) -> None:
        min_length = 2

        if len(self.value) < min_length:
            raise AuthorNameTooShortException
