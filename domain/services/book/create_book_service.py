from domain.entities.book.dtos import BookDTO
from domain.entities.book.dtos.book_creation_dto import BookCreationDTO
from domain.repositories import BookRepository


class CreateBookService:
    __book_repository: BookRepository

    def __init__(self, book_repository: BookRepository) -> None:
        self.__book_repository = book_repository

    def execute(self, book_creation_dto: BookCreationDTO) -> BookDTO:
        book = book_creation_dto.to_entity()
        self.__book_repository.save(book)
        return BookDTO.from_entity(book)
