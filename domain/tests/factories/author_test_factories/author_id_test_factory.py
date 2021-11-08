from factory import Factory, Faker

from domain.entities.author.value_objects.author_id import AuthorId


class AuthorIdTestFactory(Factory):
    class Meta:
        model = AuthorId

    value = Faker('uuid4')
