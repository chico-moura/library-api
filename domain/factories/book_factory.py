from domain.entities.author.value_objects import AuthorId
from domain.entities.book import Book
from domain.entities.book.value_objects import BookEdition, BookId, BookName, BookPublicationYear


class BookFactory:
    @staticmethod
    def from_book_dto(book_dto) -> Book:
        book_id = BookId(book_dto.id)
        book_name = BookName(book_dto.name)
        book_edition = BookEdition(book_dto.edition)
        book_publication_year = BookPublicationYear(book_dto.publication_year)
        book_authors = [AuthorId(id_) for id_ in book_dto.authors]

        return Book(
            id=book_id,
            name=book_name,
            edition=book_edition,
            publication_year=book_publication_year,
            authors=book_authors
        )
