from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


# TODO: -> JSON reponse
# TODO: Integrated test mocking DB
# TODO: Finish endpoint
# TODO: CSV (django commands & pure python) (is CSV part of domain)

from domain.entities.author.dtos.author_dto import AuthorDTO
from domain.repositories.author_repository import AuthorRepository
from domain.services.save_author_service import SaveAuthorService
from api.repositories.django_author_repository import DjangoAuthorRepository


class AuthorView(APIView):
    __author_repository: AuthorRepository

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__author_repository = DjangoAuthorRepository()

    def post(self, request: Request, *args, **kwargs) -> Response:
        save_author_service = SaveAuthorService(self.__author_repository)

        # TODO: create serializer
        dto = AuthorDTO(name="roberto")

        save_author_service.execute(dto)

        return Response()
