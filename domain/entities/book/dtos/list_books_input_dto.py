from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, Optional
from uuid import UUID
from domain.entities.author.value_objects.author_id import AuthorId
from domain.entities.book.value_objects.book_edition import BookEdition

from domain.entities.book.value_objects.book_name import BookName
from domain.entities.book.value_objects.book_publication_year import BookPublicationYear


@dataclass
class ListBooksInputDTO:
    name: Optional[str] = field(default=None)
    edition: Optional[str] = field(default=None)
    publication_year: Optional[str] = field(default=None)
    author_id: Optional[UUID] = field(default=None)

    def to_data(self) -> Dict:
        return {
            'name': BookName(self.name) if self.name else None,
            'edition': BookEdition(self.edition) if self.edition else None,
            'publication_year': BookPublicationYear(self.publication_year) if self.publication_year else None,
            'author_id': AuthorId(self.author_id) if self.author_id else None,
        }
