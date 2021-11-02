from enum import Enum
import csv
from django.core.management import BaseCommand, CommandParser


class CommandEnum(Enum):
    AUTHORS_CSV_FILE = 'authors_csv_file'


class Command(BaseCommand):
    help = 'Import authors from a CSV file to database.'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            CommandEnum.AUTHORS_CSV_FILE.value,
        )

    def handle(self, *args, **options):
        csv_file = options[CommandEnum.AUTHORS_CSV_FILE.value]
        
        self.stdout.write(csv_file)
