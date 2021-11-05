from typing import List

from domain.entities.author.dtos.author_input_dto import AuthorCreationDTO
from domain.services.author.base_author_service import BaseAuthorService


class SaveAuthorCollectionService(BaseAuthorService):
    def execute(self, author_creation_dtos: List[AuthorCreationDTO]) -> None:
        authors = [dto.to_entity() for dto in author_creation_dtos]
        self._author_repository.save(*authors)
