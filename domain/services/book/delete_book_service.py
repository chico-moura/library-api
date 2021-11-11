from api.models.book_model import BookModel
from domain.entities.book.dtos.delete_book_dto import DeleteBookDTO
from domain.entities.book.value_objects import BookId
from domain.repositories import BookRepository


class DeleteBookService:
    __book_repository: BookRepository

    def __init__(self, book_repository: BookRepository) -> None:
        self.__book_repository = book_repository

    def execute(self, delete_book_dto: DeleteBookDTO) -> None:
        book_id = BookId(delete_book_dto.id)
        book = self.__book_repository.get_by_id(book_id)

