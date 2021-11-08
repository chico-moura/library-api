from factory import Factory, Faker

from domain.entities.book.value_objects.book_publication_year import BookPublicationYear


class BookPublicationYearTestFactory(Factory):
    class Meta:
        model = BookPublicationYear

    value = Faker(
        'numerify',
        text='19##'
    )
