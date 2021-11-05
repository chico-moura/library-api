from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.author_output_dto_serializer import AuthorOutputDTOSerializer
from domain.repositories.author_repository import AuthorRepository
from domain.services.author.list_authors_service import ListAuthorsService
from api.repositories.django_author_repository import DjangoAuthorRepository

# TODO: Integrated test mocking DB


class AuthorView(APIView):
    __author_repository: AuthorRepository

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__author_repository = DjangoAuthorRepository()

    def get(self, request: Request) -> Response:
        list_authors_service = ListAuthorsService(self.__author_repository)
        authors = list_authors_service.execute()
        serializer = AuthorOutputDTOSerializer(authors, many=True)
        return Response(serializer.data)
