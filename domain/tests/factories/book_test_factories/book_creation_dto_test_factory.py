from uuid import uuid4

from factory import Factory, Faker

from domain.entities.author.value_objects import AuthorId
from domain.entities.book.dtos.book_creation_dto import BookCreationDTO


class BookCreationDTOTestFactory(Factory):
    class Meta:
        model = BookCreationDTO

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
        elements=[AuthorId(uuid4()) for _ in range(5)],
        unique=True
    )
