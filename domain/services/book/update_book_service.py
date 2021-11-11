from domain.entities.book.dtos import BookDTO
from domain.repositories import BookRepository


class UpdateBookService:
    __book_repository: BookRepository

    def __init__(self, book_repository: BookRepository) -> None:
        self.__book_repository = book_repository

    def execute(self, book_dto: BookDTO) -> BookDTO:
        book = book_dto.to_entity()
        self.__book_repository.get_by_id(book.id)
        self.__book_repository.save(book)
        return BookDTO.from_entity(book)
