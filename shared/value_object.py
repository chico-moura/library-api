from abc import ABC, abstractmethod


class ValueObject(ABC):
    def __post_init__(self):
        self.validate()

    @abstractmethod
    def validate(self) -> None:
        pass
