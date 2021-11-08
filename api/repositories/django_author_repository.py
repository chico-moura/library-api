from typing import List

from django.shortcuts import get_object_or_404

from api.models import AuthorDTOModel
from domain.entities.author.author import Author
from domain.entities.author.dtos.author_dto import AuthorDTO
from domain.entities.author.value_objects.author_id import AuthorId
from domain.repositories.author_repository import AuthorRepository

# TODO: cut off dtos, do it directly, it's already decoupled


class DjangoAuthorRepository(AuthorRepository):
    def save(self, *authors: Author) -> None:
        dtos = [AuthorDTO.from_entity(author) for author in authors]
        models = [AuthorDTOModel.from_dto(dto) for dto in dtos]
        [model.save() for model in models]

    def get_by_id(self, id_: AuthorId) -> Author:
        model: AuthorDTOModel = get_object_or_404(AuthorDTOModel, pk=id_.value)
        dto = model.to_dto()
        return dto.to_entity()

    def get_all(self) -> List[Author]:
        models = AuthorDTOModel.objects.all()
        dtos = [model.to_dto() for model in models]
        return [author.to_entity() for author in dtos]
