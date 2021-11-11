from unittest import TestCase
from uuid import uuid4

from domain.entities.author.value_objects import AuthorId
from domain.entities.book.dtos.list_books_input_dto import ListBooksInputDTO
from domain.entities.book.value_objects import BookEdition, BookName, BookPublicationYear


class TestListBooksInputDTO(TestCase):
    def test_to_data_WHEN_called_THEN_returns_dict_version_of_dto(self):
        name = 'Fake name'
        edition = 'Fake Edition'
        publication_year = '2021'
        author_id = uuid4()
        list_books_input_dto = ListBooksInputDTO(
            name=name,
            edition=edition,
            publication_year=publication_year,
            author_id=author_id
        )

        result_data = list_books_input_dto.to_data()
        expected_data = {
            'name': BookName(name),
            'edition': BookEdition(edition),
            'publication_year': BookPublicationYear(publication_year),
            'author_id': AuthorId(author_id)
        }
        self.assertEqual(expected_data, result_data)
