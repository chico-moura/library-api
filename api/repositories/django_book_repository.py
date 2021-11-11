from typing import Optional, List

from rest_framework.generics import get_object_or_404

from api.models.book_model import BookModel
from domain.entities.author.value_objects.author_id import AuthorId
from domain.entities.book.book import Book
from domain.entities.book.value_objects.book_edition import BookEdition
from domain.entities.book.value_objects.book_id import BookId
from domain.entities.book.value_objects.book_name import BookName
from domain.entities.book.value_objects.book_publication_year import BookPublicationYear
from domain.exceptions.book.book_not_found_exception import BookNotFoundException
from domain.repositories.book_repository import BookRepository


class DjangoBookRepository(BookRepository):
    def save(self, *books: Book) -> None:
        for book in books:
            book_model = BookModel.from_entity(book)
            book_model.save()

    def get_all(self) -> List[Book]:
        pass

    def get_by_id(self, id_: BookId) -> Book:
        book_model = self.__get_book_model_by_id(id_)
        return book_model.to_entity()

    def delete(self, id_: BookId) -> None:
        book_model: BookModel = self.__get_book_model_by_id(id_)
        book_model.delete()

    def get_by_attributes(
        self,
        name: Optional[BookName],
        edition: Optional[BookEdition],
        publication_year: Optional[BookPublicationYear],
        authors: Optional[List[AuthorId]]
    ) -> List[Book]:
        pass

    @staticmethod
    def __get_book_model_by_id(id_: BookId) -> BookModel:
        try:
            return BookModel.objects.get(pk=id_.value)
        except BookModel.DoesNotExist as error:
            exception_message = f'Book not found for given id(id_.value)'
            raise BookNotFoundException(exception_message) from error
