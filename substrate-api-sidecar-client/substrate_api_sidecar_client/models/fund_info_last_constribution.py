from enum import Enum


class FundInfoLastConstribution(str, Enum):
    ENDING = "ending"
    PREENDING = "preEnding"

    def __str__(self) -> str:
        return str(self.value)
