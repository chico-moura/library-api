from domain.entities.author.author import Author
from domain.entities.author.value_objects.author_id import AuthorId
from domain.entities.author.value_objects.author_name import AuthorName


# FIXME: use factory_boy


class AuthorFactory:
    @staticmethod
    def new(name: str) -> Author:
        author_name = AuthorName(name)
        author_id = AuthorId()
        return Author(name=author_name, id=author_id)
