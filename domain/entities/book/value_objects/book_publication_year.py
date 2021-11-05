from dataclasses import dataclass

from domain.entities.value_object import ValueObject


@dataclass(frozen=True)
class BookPublicationYear(ValueObject):
    value: str

    def validate(self) -> None:
        pass
