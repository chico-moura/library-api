from rest_framework_dataclasses.serializers import DataclassSerializer

from domain.entities.author.dtos.author_output_dto import AuthorOutputDTO


class AuthorOutputDTOSerializer(DataclassSerializer):
    class Meta:
        dataclass = AuthorOutputDTO
