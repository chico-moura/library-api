from random import randrange
from typing import List
from uuid import uuid4

import factory
from factory import Faker
from factory.django import DjangoModelFactory

from api.models.book_model import BookModel
from api.tests.factories.author_model_test_factory import AuthorModelTestFactory
from domain.entities.author.value_objects import AuthorId


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
    def authors(self, create: bool, extracted: List[AuthorId], *args, **kwargs) -> None:
        if not create:
            return

        if extracted:
            self.save()
            authors = [AuthorModelTestFactory.create(id=author_id.value) for author_id in extracted]
            self.authors.set(authors)
