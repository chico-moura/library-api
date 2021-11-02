import uuid
from dataclasses import dataclass
from typing import Optional


@dataclass(init=False)
class AuthorId:
    value: uuid.UUID

    def __init__(self, value: Optional[uuid.UUID] = None) -> None:
        self.value = value or uuid.uuid4()
