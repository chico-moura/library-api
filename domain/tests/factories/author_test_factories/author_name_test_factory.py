from factory import Factory, Faker

from domain.entities.author.value_objects import AuthorName


class AuthorNameTestFactory(Factory):
    class Meta:
        model = AuthorName

    value = Faker('name')
