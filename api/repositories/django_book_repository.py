from typing import Optional, List

from domain.entities.author.value_objects.author_id import AuthorId
from domain.entities.book.book import Book
from domain.entities.book.value_objects.book_edition import BookEdition
from domain.entities.book.value_objects.book_id import BookId
from domain.entities.book.value_objects.book_name import BookName
from domain.entities.book.value_objects.book_publication_year import BookPublicationYear
from domain.repositories.book_repository import BookRepository


class DjangoBookRepository(BookRepository):
    def save(self, book: Book) -> None:
        pass

    def get_by_id(self, id_: BookId) -> Book:
        pass

    def get_by_attributes(
        self,
        name: Optional[BookName],
        edition: Optional[BookEdition],
        publication_year: Optional[BookPublicationYear],
        authors: Optional[List[AuthorId]]
    ) -> List[Book]:
        pass
