from dataclasses import dataclass

from domain.entities.value_object import ValueObject


@dataclass(frozen=True)
class BookEdition(ValueObject):
    MAX_SIZE = 10
    MIN_SIZE = 1

    value: str

    def validate(self) -> None:
        pass
