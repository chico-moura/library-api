from factory import Factory, Faker

from domain.entities.author.dtos.author_dto import AuthorDTO


class AuthorDTOTestFactory(Factory):
    class Meta:
        model = AuthorDTO

    id = Faker('uuid4')
    name = Faker('name')
