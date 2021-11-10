from typing import List

from django.shortcuts import get_object_or_404

from domain.entities.author import Author
from domain.entities.author.value_objects import AuthorId
from domain.repositories import AuthorRepository

from api.models import AuthorModel


class DjangoAuthorRepository(AuthorRepository):
    def save(self, *authors: Author) -> None:
        for author in authors:
            model = AuthorModel.from_author(author)
            model.save()

    def get_by_id(self, id_: AuthorId) -> Author:
        model: AuthorModel = get_object_or_404(AuthorModel, pk=id_.value)
        return model.to_author()

    def get_all(self) -> List[Author]:
        models = AuthorModel.objects.all()
        return [model.to_author() for model in models]
