from rest_framework_dataclasses.serializers import DataclassSerializer

from domain.entities.book.dtos import BookDTO


class BookDTOSerializer(DataclassSerializer):
    class Meta:
        dataclass = BookDTO
