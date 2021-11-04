from django.shortcuts import get_object_or_404

from api.models import AuthorModel
from domain.entities.author.author import Author
from domain.entities.author.dtos.author_output_dto import AuthorOutputDTO
from domain.entities.author.value_objects.author_id import AuthorId
from domain.repositories.author_repository import AuthorRepository


# TODO: make integration test with bank

class DjangoAuthorRepository(AuthorRepository):
    def save(self, author: Author) -> None:
        author_dto = AuthorOutputDTO.from_entity(author)
        author_model = AuthorModel.from_dto(author_dto)
        author_model.save()

    def get_by_id(self, id_: AuthorId) -> Author:
        model: AuthorModel = get_object_or_404(AuthorModel, pk=id_.value)
        dto = model.to_dto()
        return dto.to_entity()
