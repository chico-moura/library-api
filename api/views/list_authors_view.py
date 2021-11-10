from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from api.serializers.author_dto_serializer import AuthorDTOSerializer
from api.views.base_author_view import BaseAuthorView
from domain.services.author.list_authors_service import ListAuthorsService


class ListAuthorsView(BaseAuthorView):
    __list_authors_service: ListAuthorsService

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__list_authors_service = ListAuthorsService(self._author_repository)

    def get(self, request: Request) -> Response:
        dtos = self.__list_authors_service.execute()
        serializer = AuthorDTOSerializer(dtos, many=True)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )
