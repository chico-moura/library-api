from __future__ import annotations
from django.db import models

from domain.settings import AuthorSettings


class AuthorModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=AuthorSettings.NAME_MAX_LENGTH)
