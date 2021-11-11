from uuid import UUID

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from api.exceptions.books.book_not_found_api_exception import BookNotFoundAPIException

from api.repositories.django_book_repository import DjangoBookRepository
from api.serializers.book_dto_serializer import BookDTOSerializer
from domain.entities.book.dtos.get_book_by_id_dto import GetBookByIdDTO
from domain.exceptions.book.book_not_found_exception import BookNotFoundException
from domain.services.book.get_book_by_id_service import GetBookByIdService


class BookDetailsView(APIView):
    __get_book_by_id_service: GetBookByIdService

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        book_repository = DjangoBookRepository()
        self.__get_book_by_id_service = GetBookByIdService(book_repository)

    def get(self, request: Request, book_id: UUID) -> Response:
        try:
            get_book_by_id_dto = GetBookByIdDTO(book_id)
            book_dto = self.__get_book_by_id_service.execute(get_book_by_id_dto)
        except BookNotFoundException as error:
            raise BookNotFoundAPIException from error

        serializer = BookDTOSerializer(book_dto)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

