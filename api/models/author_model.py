from __future__ import  annotations

from django.db import models
from django.db.models import Model

from domain.entities.author.author import Author


class AuthorModel(Model):
    id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=120)

    @classmethod
    def from_entity(cls, author: Author) -> AuthorModel:
        return AuthorModel(id=author.id.value, name=author.name.value)
