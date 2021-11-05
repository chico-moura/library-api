from rest_framework_dataclasses.serializers import DataclassSerializer

from domain.entities.author.dtos.author_dto import AuthorDTO


class AuthorOutputDTOSerializer(DataclassSerializer):
    class Meta:
        dataclass = AuthorDTO
