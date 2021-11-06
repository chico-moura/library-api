from random import randrange
from uuid import uuid4

from domain.entities.book.dtos.bookDTO import BookDTO


class BookDTOFactory:
    @classmethod
    def get_random(cls, name: str) -> BookDTO:
        return BookDTO(
            id=uuid4(),
            name=name,
            edition=str(randrange(1, 10)),
            publication_year=str(randrange(500, 2021)),
            authors=[uuid4() for _ in range(randrange(1, 4))]
        )
