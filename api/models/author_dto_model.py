from __future__ import annotations
from django.db import models

from domain.entities.author.dtos.author_dto import AuthorDTO
from domain.settings import AuthorSettings


class AuthorDTOModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=AuthorSettings.NAME_MAX_LENGTH)

    @classmethod
    def from_dto(cls, author_dto: AuthorDTO) -> AuthorDTOModel:
        return AuthorDTOModel(
            id=author_dto.id,
            name=author_dto.name
        )

    def to_dto(self) -> AuthorDTO:
        return AuthorDTO(
            id=self.id,
            name=self.name
        )
