import uuid
from dataclasses import dataclass


@dataclass(frozen=True)
class BookId:
    value: uuid.UUID
