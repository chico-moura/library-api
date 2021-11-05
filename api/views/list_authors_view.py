from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from api.serializers.author_output_dto_serializer import AuthorOutputDTOSerializer
from api.views.base_author_view import BaseAuthorView
from domain.services.author.list_authors_service import ListAuthorsService


class ListAuthorsView(BaseAuthorView):
    def get(self, request: Request) -> Response:
        list_authors_service = ListAuthorsService(self._author_repository)
        dtos = list_authors_service.execute()
        serializer = AuthorOutputDTOSerializer(dtos, many=True)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )
