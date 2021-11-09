from __future__ import annotations
from django.db import models

from domain.entities.author.value_objects import AuthorName


class AuthorModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=AuthorName.MAX_LENGTH)
