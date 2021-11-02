from dataclasses import dataclass


@dataclass(frozen=True)
class BookName:
    value: str
