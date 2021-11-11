from dataclasses import dataclass
from uuid import UUID

from domain.entities.book.value_objects.book_id import BookId


@dataclass
class GetBookByIdDTO:
    raw_book_id: UUID

    def to_book_id(self) -> BookId:
        return BookId(self.raw_book_id)
