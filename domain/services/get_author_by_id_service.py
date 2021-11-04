from uuid import UUID

from domain.entities.author.dtos.author_output_dto import AuthorOutputDTO
from domain.entities.author.value_objects.author_id import AuthorId
from domain.repositories.author_repository import AuthorRepository


class GetAuthorByIdService:
    __author_repository: AuthorRepository

    def __init__(self, author_repository: AuthorRepository) -> None:
        self.__author_repository = author_repository

    def execute(self, raw_id: UUID) -> AuthorOutputDTO:
        author_id = AuthorId(raw_id)
        author = self.__author_repository.get_by_id(author_id)
        return AuthorOutputDTO.from_entity(author)
