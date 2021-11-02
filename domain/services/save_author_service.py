from domain.entities.author.dtos.author_dto import AuthorDTO
from domain.repositories.author_repository import AuthorRepository


class SaveAuthorService:
    """
    Asks for repository to save author.

    Recieves an AuthorDTO, instantiate author from it, and passes to repository's method save
    """
    __author_repository: AuthorRepository

    def __init__(self, author_repository: AuthorRepository) -> None:
        self.__author_repository = author_repository

    def execute(self, author_dto: AuthorDTO) -> None:
        author = author_dto.to_entity()
        self.__author_repository.save(author)
