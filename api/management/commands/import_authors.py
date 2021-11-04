import argparse
import csv
from django.core.management import BaseCommand, CommandParser

from api.repositories.django_author_repository import DjangoAuthorRepository
from domain.entities.author.author import Author
from domain.entities.author.dtos.author_output_dto import AuthorOutputDTO
from domain.entities.author.value_objects.author_id import AuthorId
from domain.entities.author.value_objects.author_name import AuthorName
from domain.services.save_author_service import SaveAuthorService


class Command(BaseCommand):
    __CSV_FILE: str = 'csv_file'
    __SAVE_AUTHOR_SERVICE: SaveAuthorService

    help = 'Import authors from a CSV file to database.'

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        author_repository = DjangoAuthorRepository()
        self.__SAVE_AUTHOR_SERVICE = SaveAuthorService(author_repository)

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            self.__CSV_FILE,
            type=argparse.FileType('r')
        )

    def handle(self, *args, **options) -> None:
        csv_file = options[self.__CSV_FILE]
        author_reader = csv.reader(csv_file)

        for row in author_reader:
            raw_name = ''.join(row)
            author_id = AuthorId()
            author_name = AuthorName(raw_name)

            author = Author(
                id=author_id,
                name=author_name
            )
            author_dto = AuthorOutputDTO.from_entity(author)

            self.__SAVE_AUTHOR_SERVICE.execute(author_dto)
