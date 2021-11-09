from typing import List

from django.shortcuts import get_object_or_404

from api.factories.author_model_factory import AuthorModelFactory
from domain.entities.author import Author
from domain.entities.author.value_objects import AuthorId
from domain.repositories import AuthorRepository

from api.models import AuthorModel


class DjangoAuthorRepository(AuthorRepository):
    def save(self, *authors: Author) -> None:
        for author in authors:
            model = AuthorModelFactory.model_from_author(author)
            model.save()

    def get_by_id(self, id_: AuthorId) -> Author:
        model: AuthorModel = get_object_or_404(AuthorModel, pk=id_.value)
        return AuthorModelFactory.author_from_model(model)

    def get_all(self) -> List[Author]:
        models = AuthorModel.objects.all()
        return [AuthorModelFactory.author_from_model(model) for model in models]
