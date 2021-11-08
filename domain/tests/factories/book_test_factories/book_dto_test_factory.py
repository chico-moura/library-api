from factory import Factory, Faker
from uuid import uuid4

from domain.entities.book.dtos.bookDTO import BookDTO


class BookDTOTestFactory(Factory):
    class Meta:
        model = BookDTO

    id = Faker(
        'uuid4'
    )
    name = Faker(
        'company'
    )
    edition = Faker(
        'numerify',
        text='#'
    )
    publication_year = Faker(
        'numerify',
        text='19##'
    )
    authors = Faker(
        'random_elements',
        elements=[uuid4() for _ in range(5)],
        unique=True
    )
