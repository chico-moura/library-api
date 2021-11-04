from rest_framework_dataclasses.serializers import DataclassSerializer

from domain.entities.author.dtos.author_input_dto import AuthorInputDTO


class AuthorInputDTOSerializer(DataclassSerializer):
    class Meta:
        dataclass = AuthorInputDTO
