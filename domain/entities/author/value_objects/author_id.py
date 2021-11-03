import uuid
from dataclasses import dataclass, field

from domain.entities.value_object import ValueObject


@dataclass(frozen=True)
class AuthorId2(ValueObject):
    value: uuid.UUID = field(default_factory=uuid.uuid4)

    def validate(self) -> None:
        pass
