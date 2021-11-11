from uuid import UUID

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from api.exceptions.books.book_not_found_api_exception import BookNotFoundAPIException
from api.repositories.django_book_repository import DjangoBookRepository
from api.serializers.book_dto_serializer import BookDTOSerializer
from domain.entities.book.dtos.delete_book_dto import DeleteBookDTO
from domain.entities.book.dtos.get_book_by_id_dto import GetBookByIdDTO
from domain.exceptions.book.book_not_found_exception import BookNotFoundException
from domain.services.book.delete_book_service import DeleteBookService
from domain.services.book.get_book_by_id_service import GetBookByIdService
from domain.services.book.update_book_service import UpdateBookService


class BookDetailsView(APIView):
    __get_book_by_id_service: GetBookByIdService
    __delete_book_service: DeleteBookService

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        book_repository = DjangoBookRepository()
        self.__get_book_by_id_service = GetBookByIdService(book_repository)
        self.__update_book_service = UpdateBookService(book_repository)
        self.__delete_book_service = DeleteBookService(book_repository)


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

    def put(self, request: Request, book_id: UUID) -> Response:
        try:
            book_data = {'id':book_id, **request.data}
            input_book_dto_serializer = BookDTOSerializer(data=book_data)
            input_book_dto_serializer.is_valid(raise_exception=True)
            input_book_dto = input_book_dto_serializer.save()
            output_book_dto = self.__update_book_service.execute(input_book_dto)

        except BookNotFoundException as error:
            raise BookNotFoundAPIException from error

        output_serializer = BookDTOSerializer(output_book_dto)
        return Response(
            data=output_serializer.data,
            status=status.HTTP_200_OK
        )

    def delete(self, request: Request, book_id: UUID) -> Response:
        delete_book_dto = DeleteBookDTO(id=book_id)

        try:
            self.__delete_book_service.execute(delete_book_dto)

        except BookNotFoundException as error:
            raise BookNotFoundAPIException from error

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )


