from dataclasses import dataclass

from domain.entities.value_object import ValueObject


@dataclass(frozen=True)
class BookPublicationYear(ValueObject):
    MIN_SIZE = 1
    MAX_SIZE = 4

    value: str

    def validate(self) -> None:
        pass
