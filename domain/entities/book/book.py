from typing import List

from domain.entities.author.value_objects.author_id import AuthorId
from domain.entities.book.value_objects.book_edition import BookEdition
from domain.entities.book.value_objects.book_id import BookId
from domain.entities.book.value_objects.book_name import BookName
from domain.entities.book.value_objects.book_publication_year import BookPublicationYear


class Book:
    __id: BookId
    __name: BookName
    __edition: BookEdition
    __publication_year: BookPublicationYear
    __authors: List[AuthorId]

    def __init__(
        self,
        id_: BookId,
        name: BookName,
        edition: BookEdition,
        publication_year: BookPublicationYear,
        authors: List[AuthorId]
    ) -> None:
        self.__id = id_
        self.__name = name
        self.__edition = edition
        self.__publication_year = publication_year
        self.__authors = authors

