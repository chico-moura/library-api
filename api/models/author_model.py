from __future__ import annotations
from django.db import models
from django.db.models import Model

from domain.entities.author.dtos.author_dto import AuthorDTO
from domain.settings import AuthorSettings


class AuthorModel(Model):
    id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=AuthorSettings.NAME_MAX_LENGTH)

    @classmethod
    def from_dto(cls, author_dto: AuthorDTO) -> AuthorModel:
        return AuthorModel(
            id=author_dto.id,
            name=author_dto.name
        )
