from factory import Faker
from factory.django import DjangoModelFactory

from api.models import AuthorModel


class AuthorModelTestFactory(DjangoModelFactory):
    class Meta:
        model = AuthorModel

    id = Faker('uuid4')
    name = Faker('name')
