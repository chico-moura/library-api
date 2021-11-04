from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import AuthorModel
from api.serializers.author_dto_serializer import AuthorDTOSerializer
from domain.entities.author.dtos.author_output_dto import AuthorOutputDTO
from domain.repositories.author_repository import AuthorRepository
from domain.services.save_author_service import SaveAuthorService
from api.repositories.django_author_repository import DjangoAuthorRepository

# TODO: -> JSON reponse
# TODO: Integrated test mocking DB
# TODO: Finish endpoint
# TODO: CSV (django commands & pure python) (is CSV part of domain)


class AuthorView(APIView):
    __author_repository: AuthorRepository

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__author_repository = DjangoAuthorRepository()

    def get(self, request: Request) -> Response:
        authors = AuthorModel.objects.all()
        serializer = AuthorDTOSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request: Request, *args, **kwargs) -> Response:
        # FIXME: DTO serializer? Or entity serializer?
        serializer = AuthorDTOSerializer(data=request.data)

        if serializer.is_valid():
            author_dto = serializer.save()
            save_author_service = SaveAuthorService(self.__author_repository)

            save_author_service.execute(author_dto)

            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
