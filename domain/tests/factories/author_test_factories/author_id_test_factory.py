from factory import Factory, Faker

from domain.entities.author.value_objects import AuthorId


class AuthorIdTestFactory(Factory):
    class Meta:
        model = AuthorId

    value = Faker('uuid4')
