from factory import Factory, Faker

from domain.entities.author.dtos import AuthorCreationDTO


class AuthorCreationDTOTestFactory(Factory):
    class Meta:
        model = AuthorCreationDTO

    name = Faker('name')
