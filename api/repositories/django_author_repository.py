from api.models import AuthorModel
from domain.entities.author.author import Author
from domain.repositories.author_repository import AuthorRepository


# TODO: make integration test with bank
# TODO: research djangorestframework-dataclasses
class DjangoAuthorRepository(AuthorRepository):
    def save(self, author: Author) -> None:
        author_model = AuthorModel.from_entity(author)
        author_model.save()
