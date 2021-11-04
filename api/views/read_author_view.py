from uuid import UUID

from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from api.repositories.django_author_repository import DjangoAuthorRepository
from api.serializers.author_output_dto_serializer import AuthorOutputDTOSerializer
from domain.repositories.author_repository import AuthorRepository
from domain.services.get_author_by_id_service import GetAuthorByIdService


class ReadAuthorView(APIView):
    __author_repository: AuthorRepository

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, *kwargs)
        self.__author_repository = DjangoAuthorRepository()

    def get(self, request: Request, raw_id: str) -> Response:
        get_author_by_id_service = GetAuthorByIdService(self.__author_repository)
        author_dto = get_author_by_id_service.execute(UUID(raw_id))
        serializer = AuthorOutputDTOSerializer(data=author_dto)

        if serializer.is_valid():
            return Response(
                data=serializer.validated_data,
                status=status.HTTP_200_OK
            )
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
