from domain.entities.author.value_objects.author_id import AuthorId
from domain.entities.author.value_objects.author_name import AuthorName


# TODO: make stuff private and getters
class Author:
    id: AuthorId
    name: AuthorName

    def __init__(self, id_: AuthorId, name: AuthorName) -> None:
        self.id = id_
        self.name = name
