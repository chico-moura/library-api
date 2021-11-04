from rest_framework_dataclasses.serializers import DataclassSerializer

from domain.entities.author.dtos.author_output_dto import AuthorOutputDTO


# FIXME: DTOSerializer? Or AuthorSerializer?
class AuthorDTOSerializer(DataclassSerializer):
    class Meta:
        dataclass = AuthorOutputDTO
