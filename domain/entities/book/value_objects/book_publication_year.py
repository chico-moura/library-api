from dataclasses import dataclass


@dataclass(frozen=True)
class BookPublicationYear:
    value: str
