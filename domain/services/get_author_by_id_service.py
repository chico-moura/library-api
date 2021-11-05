from uuid import UUID

from domain.entities.author.dtos.author_dto import AuthorDTO
from domain.entities.author.value_objects.author_id import AuthorId
from domain.repositories.author_repository import AuthorRepository


class GetAuthorByIdService:
    __author_repository: AuthorRepository

    def __init__(self, author_repository: AuthorRepository) -> None:
        self.__author_repository = author_repository

    def execute(self, raw_id: UUID) -> AuthorDTO:
        author_id = AuthorId(raw_id)
        author = self.__author_repository.get_by_id(author_id)
        return AuthorDTO.from_entity(author)
