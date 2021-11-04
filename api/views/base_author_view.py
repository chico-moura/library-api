from rest_framework.views import APIView

from api.repositories.django_author_repository import DjangoAuthorRepository
from domain.repositories.author_repository import AuthorRepository


class BaseAuthorView(APIView):
    _author_repository: AuthorRepository

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._author_repository = DjangoAuthorRepository()
