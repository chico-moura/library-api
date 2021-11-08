from factory import Factory, Faker

from domain.entities.book.value_objects import BookPublicationYear


class BookPublicationYearTestFactory(Factory):
    class Meta:
        model = BookPublicationYear

    value = Faker(
        'numerify',
        text='19##'
    )
