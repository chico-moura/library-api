from dataclasses import dataclass

from domain.entities.value_object import ValueObject


@dataclass(frozen=True)
class BookName(ValueObject):
    MAX_SIZE = 250
    MIN_SIZE = 2

    value: str

    def validate(self) -> None:
        pass
