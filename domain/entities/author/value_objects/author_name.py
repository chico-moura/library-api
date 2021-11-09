from dataclasses import dataclass

from domain.exceptions import ValidationException
from domain.entities.value_object import ValueObject


@dataclass(frozen=True)
class AuthorName(ValueObject):
    MAX_LENGTH = 250
    MIN_LENGTH = 2

    value: str

    def validate(self) -> None:
        self.__validate_max_length()
        self.__validate_min_length()

    def __validate_max_length(self) -> None:
        value_length = len(self.value)
        if value_length > self.MAX_LENGTH:
            raise ValidationException(
                f'Author name too long: {self.value} (max length is {self.MAX_LENGTH}, has {value_length})'
            )

    def __validate_min_length(self) -> None:
        value_length = len(self.value)
        if value_length < self.MIN_LENGTH:
            raise ValidationException(
                f'Author name too short: {self.value} (min length is {self.MIN_LENGTH}, has {value_length})'
            )
