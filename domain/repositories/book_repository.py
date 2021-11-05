from abc import ABC, abstractmethod
from typing import List

from domain.entities.author.value_objects.author_id import AuthorId
from domain.entities.book.book import Book
from domain.entities.book.value_objects.book_edition import BookEdition
from domain.entities.book.value_objects.book_id import BookId
from domain.entities.book.value_objects.book_name import BookName
from domain.entities.book.value_objects.book_publication_year import BookPublicationYear


class BookRepository(ABC):
    @abstractmethod
    def save(self, book: Book) -> None:
        pass

    @abstractmethod
    def get(self,
            id_: BookId,
            name: BookName,
            edition: BookEdition,
            publication_year: BookPublicationYear,
            authors: List[AuthorId]
    ) -> List[Book]:
        pass
