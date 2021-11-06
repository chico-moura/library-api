from random import randrange
from uuid import uuid4

from domain.entities.author.value_objects.author_id import AuthorId
from domain.entities.book.book import Book
from domain.entities.book.value_objects.book_edition import BookEdition
from domain.entities.book.value_objects.book_id import BookId
from domain.entities.book.value_objects.book_name import BookName
from domain.entities.book.value_objects.book_publication_year import BookPublicationYear


class BookFactory:
    @classmethod
    def get_random(cls, raw_name: str) -> Book:
        raw_id = uuid4()
        raw_edition = str(randrange(1, 10))
        raw_publication_year = str(randrange(500, 2021))
        raw_author_ids = [uuid4() for _ in range(randrange(1, 4))]

        return Book(
            id=BookId(raw_id),
            name=BookName(raw_name),
            edition=BookEdition(raw_edition),
            publication_year=BookPublicationYear(raw_publication_year),
            authors=[AuthorId(raw_id) for raw_id in raw_author_ids]
        )
