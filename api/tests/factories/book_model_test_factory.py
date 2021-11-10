from random import randrange
from uuid import uuid4

import factory
from factory import Faker
from factory.django import DjangoModelFactory

from api.models.book_model import BookModel
from api.tests.factories.author_model_test_factory import AuthorModelTestFactory


class BookModelTestFactory(DjangoModelFactory):
    class Meta:
        model = BookModel

    id = Faker(
        'uuid4',
        cast_to=None
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

    @factory.post_generation
    def authors(self, *args, **kwargs) -> None:
        self.save()
        amount = randrange(5)
        authors = []
        for _ in range(amount):
            author = AuthorModelTestFactory()
            author.save()
            authors.append(author)

        self.authors.set(authors)
