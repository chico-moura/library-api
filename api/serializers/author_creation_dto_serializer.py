from rest_framework_dataclasses.serializers import DataclassSerializer

from domain.entities.author.dtos import AuthorCreationDTO


class AuthorCreationDTOSerializer(DataclassSerializer):
    class Meta:
        dataclass = AuthorCreationDTO
