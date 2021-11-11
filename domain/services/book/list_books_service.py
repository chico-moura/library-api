from typing import List

from domain.entities.book.dtos import BookDTO
from domain.entities.book.dtos.list_books_input_dto import ListBooksInputDTO
from domain.repositories import BookRepository


class ListBooksService:
    __book_repository: BookRepository

    def __init__(self, book_repository: BookRepository) -> None:
        self.__book_repository = book_repository

    def execute(self, dto: ListBooksInputDTO) -> List[BookDTO]:
        books = self.__book_repository.filter_by(**dto.to_data())

        return [BookDTO.from_entity(book) for book in books]
