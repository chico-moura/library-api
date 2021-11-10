from rest_framework_dataclasses.serializers import DataclassSerializer

from domain.entities.book.dtos.book_creation_dto import BookCreationDTO


class BookCreationDTOSerializer(DataclassSerializer):
    class Meta:
        model = BookCreationDTO
