from factory import Factory, Faker

from domain.entities.book.value_objects.book_name import BookName


class BookNameTestFactory(Factory):
    class Meta:
        model = BookName

    value = Faker('company')
