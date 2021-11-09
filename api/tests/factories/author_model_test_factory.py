from factory import Factory, Faker

from api.models import AuthorModel


class AuthorModelTestFactory(Factory):
    class Meta:
        model = AuthorModel

    id = Faker('uuid4')
    name = Faker('name')
