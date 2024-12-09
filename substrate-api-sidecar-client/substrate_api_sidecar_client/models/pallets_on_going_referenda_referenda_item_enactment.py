from enum import Enum


class PalletsOnGoingReferendaReferendaItemEnactment(str, Enum):
    AFTER = "after"
    AT = "at"

    def __str__(self) -> str:
        return str(self.value)
