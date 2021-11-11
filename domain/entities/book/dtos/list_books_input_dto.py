from dataclasses import dataclass, field, asdict
from typing import Dict, Optional
from uuid import UUID


@dataclass
class ListBooksInputDTO:
    name: Optional[str] = field(default=None)
    edition: Optional[str] = field(default=None)
    publication_year: Optional[str] = field(default=None)
    author_id: Optional[UUID] = field(default=None)

    def to_data(self) -> Dict:
        return asdict(self)
