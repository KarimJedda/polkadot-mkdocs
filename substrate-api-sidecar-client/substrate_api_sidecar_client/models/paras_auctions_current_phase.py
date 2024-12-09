from enum import Enum


class ParasAuctionsCurrentPhase(str, Enum):
    ENDPERIOD = "endPeriod"
    STARTPERIOD = "startPeriod"
    VRFDELAY = "vrfDelay"

    def __str__(self) -> str:
        return str(self.value)
