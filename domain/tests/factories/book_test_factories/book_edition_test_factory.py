from factory import Factory, Faker

from domain.entities.book.value_objects.book_edition import BookEdition


class BookEditionTestFactory(Factory):
    class Meta:
        model = BookEdition

    value = Faker(
        'numerify',
        text='#'
    )
