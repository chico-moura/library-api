from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from api.repositories.django_book_repository import DjangoBookRepository
from api.serializers.book_creation_dto_serializer import BookCreationDTOSerializer
from api.serializers.book_dto_serializer import BookDTOSerializer
from domain.repositories import BookRepository
from domain.services.book.create_book_service import CreateBookService


class BooksView(APIView):
    __book_repository: BookRepository

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__book_repository = DjangoBookRepository()

    def get(self, request: Request) -> Response:
        ListBooksService

    def post(self, request: Request) -> Response:
        book_creation_dto_serializer = BookCreationDTOSerializer(request.data)

        if book_creation_dto_serializer.is_valid():
            book_creation_dto = book_creation_dto_serializer.validated_data
            create_book_service = CreateBookService(self.__book_repository)

            book_dto = create_book_service.execute(book_creation_dto)

            book_dto_serializer = BookDTOSerializer(book_dto)

            return Response(
                data=book_dto_serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            data=book_creation_dto_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

