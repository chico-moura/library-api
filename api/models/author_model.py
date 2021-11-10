from __future__ import annotations
from django.db import models

from domain.entities import Author
from domain.entities.author.value_objects import AuthorName
from domain.factories import AuthorFactory


class AuthorModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=AuthorName.MAX_LENGTH)

    @classmethod
    def from_author(cls, author: Author) -> AuthorModel:
        return cls(
            id=author.id.value,
            name=author.name.value
        )

    def to_author(self) -> Author:
        return AuthorFactory.build_existing(
            id_=self.id,
            name=self.name
        )
