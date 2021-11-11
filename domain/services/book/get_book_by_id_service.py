from domain.entities.book.dtos import BookDTO
from domain.entities.book.dtos.get_book_by_id_dto import GetBookByIdDTO
from domain.repositories import BookRepository


class GetBookByIdService:
    __book_repository: BookRepository

    def __init__(self, book_repository: BookRepository) -> None:
        self.__book_repository = book_repository

    def execute(self, dto: GetBookByIdDTO) -> BookDTO:
        book_id = dto.to_book_id()
        book = self.__book_repository.get_by_id(book_id)

        return BookDTO.from_entity(book)
