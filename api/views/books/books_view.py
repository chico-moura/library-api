from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from api.repositories.django_book_repository import DjangoBookRepository
from api.serializers.book_creation_dto_serializer import BookCreationDTOSerializer
from api.serializers.book_dto_serializer import BookDTOSerializer
from domain.entities.book.dtos.list_books_input_dto import ListBooksInputDTO
from domain.repositories import BookRepository
from domain.services.book.create_book_service import CreateBookService
from domain.services.book.list_books_service import ListBooksService


class BooksView(APIView):
    __book_repository: BookRepository
    __list_books_service: ListBooksService

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__book_repository = DjangoBookRepository()
        self.__list_books_service = ListBooksService(self.__book_repository)

    def get(self, request: Request) -> Response:
        query_params = request.query_params.dict()
        list_books_input_dto = ListBooksInputDTO(
            **{query_key: query_value for query_key, query_value in query_params.items()}
        )

        book_dtos = self.__list_books_service.execute(list_books_input_dto)

        books_dto_serializer = BookDTOSerializer(book_dtos, many=True)
        return Response(
            data=books_dto_serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request: Request) -> Response:
        book_creation_dto_serializer = BookCreationDTOSerializer(data=request.data)
        book_creation_dto_serializer.is_valid(raise_exception=True)
        book_creation_dto = book_creation_dto_serializer.validated_data
        create_book_service = CreateBookService(self.__book_repository)

        book_dto = create_book_service.execute(book_creation_dto)

        book_dto_serializer = BookDTOSerializer(book_dto)

        return Response(
            data=book_dto_serializer.data,
            status=status.HTTP_201_CREATED
        )
