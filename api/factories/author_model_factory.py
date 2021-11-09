from uuid import UUID

from api.models import AuthorModel

from domain.entities import Author
from domain.entities.author.value_objects import AuthorId, AuthorName


class AuthorModelFactory:
    @staticmethod
    def author_from_model(model: AuthorModel) -> Author:
        author = Author(
            id=AuthorId(model.id),
            name=AuthorName(model.name)
        )
        return author

    @staticmethod
    def model_from_author(author: Author) -> AuthorModel:
        model = AuthorModel(
            id=author.id.value,
            name=author.name.value
        )
        return model
