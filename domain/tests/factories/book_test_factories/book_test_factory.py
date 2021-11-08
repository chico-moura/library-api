from uuid import uuid4

from factory import Factory, Faker, SubFactory

from domain.entities.author.value_objects.author_id import AuthorId
from domain.entities.book.book import Book
from domain.tests.factories.book_test_factories.book_edition_test_factory import BookEditionTestFactory
from domain.tests.factories.book_test_factories.book_id_test_factory import BookIdTestFactory
from domain.tests.factories.book_test_factories.book_name_test_factory import BookNameTestFactory
from domain.tests.factories.book_test_factories.book_publication_year_test_factory import BookPublicationYearTestFactory


class BookTestFactory(Factory):
    class Meta:
        model = Book

    id = SubFactory(BookIdTestFactory)
    name = SubFactory(BookNameTestFactory)
    edition = SubFactory(BookEditionTestFactory)
    publication_year = SubFactory(BookPublicationYearTestFactory)
    authors = Faker(
        'random_elements',
        elements=[AuthorId(uuid4()) for _ in range(5)],
        unique=True
    )

