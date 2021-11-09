from domain.entities import Author
from domain.entities.author.dtos import AuthorDTO


# FIXME: can I compare instances of different classes this way with testfixtures? how?


def compare_author_with_author_dto(author: Author, author_dto: AuthorDTO) -> str or None:
    name_match = author.name.value == author_dto.name
    id_match = author.id.value == author_dto.id

    if not name_match or not id_match:
        return f'Author {author.name.value} != AuthorDTO {author_dto.name}'
