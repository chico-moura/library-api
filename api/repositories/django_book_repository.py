from typing import Dict, Optional, List

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

    def filter_by(
        self,
        *,
        name: Optional[BookName] = None,
        edition: Optional[BookEdition] = None,
        publication_year: Optional[BookPublicationYear] = None,
        author_id: Optional[AuthorId] = None
    ) -> List[Book]:
        filter_arguments = self.__prepare_filter_arguments(name, edition, publication_year, author_id)
        book_models = BookModel.objects.filter(**filter_arguments)

        return [book_model.to_entity() for book_model in book_models]

    @staticmethod
    def __get_book_model_by_id(id_: BookId) -> BookModel:
        try:
            return BookModel.objects.get(pk=id_.value)
        except BookModel.DoesNotExist as error:
            exception_message = f'Book not found for given id(id_.value)'
            raise BookNotFoundException(exception_message) from error

    @staticmethod
    def __prepare_filter_arguments(
        name: Optional[BookName] = None,
        edition: Optional[BookEdition] = None,
        publication_year: Optional[BookPublicationYear] = None,
        author_id: Optional[AuthorId] = None
    ) -> Dict:
        arguments_data = {
            'name': name.value if name else None,
            'edition': edition.value if edition else None,
            'publication_year': publication_year.value if publication_year else None,
            'author_id': author_id.value if author_id else None,
        }
        return {
            filter_key: filter_value for filter_key, filter_value in arguments_data.items() if filter_value is not None
        }
