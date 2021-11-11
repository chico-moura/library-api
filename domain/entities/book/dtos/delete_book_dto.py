from dataclasses import dataclass
from uuid import UUID


@dataclass
class DeleteBookDTO:
    id: UUID
