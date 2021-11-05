from dataclasses import dataclass

from domain.entities.value_object import ValueObject


@dataclass(frozen=True)
class BookEdition(ValueObject):
    value: str

    def validate(self) -> None:
        pass
