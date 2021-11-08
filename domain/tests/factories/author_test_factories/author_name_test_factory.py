from factory import Factory, Faker

from domain.entities.author.value_objects.author_name import AuthorName


class AuthorNameTestFactory(Factory):
    class Meta:
        model = AuthorName

    value = Faker('name')
