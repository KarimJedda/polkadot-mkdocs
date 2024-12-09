from enum import Enum


class OnboardingAs(str, Enum):
    PARACHAIN = "parachain"
    PARATHREAD = "parathread"

    def __str__(self) -> str:
        return str(self.value)
