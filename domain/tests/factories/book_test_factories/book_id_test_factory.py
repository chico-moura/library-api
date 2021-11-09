from factory import Factory, Faker

from domain.entities.book.value_objects import BookId


class BookIdTestFactory(Factory):
    class Meta:
        model = BookId

    value = Faker('uuid4', cast_to=None)
