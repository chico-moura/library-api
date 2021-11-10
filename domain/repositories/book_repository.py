from abc import ABC, abstractmethod
from typing import List, Optional

from domain.entities.author.value_objects.author_id import AuthorId
from domain.entities.book.book import Book
from domain.entities.book.value_objects.book_edition import BookEdition
from domain.entities.book.value_objects.book_id import BookId
from domain.entities.book.value_objects.book_name import BookName
from domain.entities.book.value_objects.book_publication_year import BookPublicationYear


class BookRepository(ABC):
    @abstractmethod
    def save(self, *book: Book) -> None:
        pass

    @abstractmethod
    def get_all(self) -> List[Book]:
        pass

    @abstractmethod
    def get_by_id(self, id_: BookId) -> Book:
        pass

    @abstractmethod
    def get_by_attributes(
        self,
        name: Optional[BookName],
        edition: Optional[BookEdition],
        publication_year: Optional[BookPublicationYear],
        authors: Optional[List[AuthorId]]
    ) -> List[Book]:
        pass
