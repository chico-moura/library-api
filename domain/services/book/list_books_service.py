from typing import List

from domain.entities import Book
from domain.repositories import BookRepository


class ListBooksService:
    __book_repository: BookRepository

    def __init__(self, book_repository: BookRepository) -> None:
        self.__book_repository = book_repository

    def execute(self) -> List[Book]:
        books = self.__book_repository.g
