from factory import Factory, Faker

from domain.entities.author.dtos.author_input_dto import AuthorCreationDTO


class AuthorCreationDTOTestFactory(Factory):
    class Meta:
        model = AuthorCreationDTO

    name = Faker('name')
