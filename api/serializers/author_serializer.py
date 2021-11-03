from rest_framework_dataclasses.serializers import DataclassSerializer

from domain.entities.author.dtos.author_dto import AuthorDTO


class AuthorDTOSerializer(DataclassSerializer):
    class Meta:
        dataclass = AuthorDTO
