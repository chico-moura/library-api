from __future__ import annotations

from django.db import models

from api.models import AuthorModel
from domain.entities import Book
from domain.entities.author.value_objects import AuthorId
from domain.entities.book.value_objects import BookName, BookEdition, BookPublicationYear
from domain.factories import BookFactory


class BookModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    name = models.CharField(max_length=BookName.MAX_SIZE)
    edition = models.CharField(max_length=BookEdition.MAX_SIZE)
    publication_year = models.CharField(max_length=BookPublicationYear.MAX_SIZE)
    authors = models.ManyToManyField(AuthorModel)

    @classmethod
    def from_entity(cls, book: Book) -> BookModel:
        model = cls(
            id=book.id.value,
            name=book.name.value,
            edition=book.edition.value,
            publication_year=book.publication_year.value,
        )
        model.save()    # FIXME: model.save() in middle of factory method
        authors = [AuthorModel.objects.get(pk=author_id.value) for author_id in book.authors]
        model.authors.set(authors)
        return model

    def to_entity(self) -> Book:
        return BookFactory.build_existing(
            id_=self.id,
            name=self.name,
            edition=self.edition,
            publication_year=self.publication_year,
            authors=[AuthorId(author.id) for author in self.authors.all()]
        )
