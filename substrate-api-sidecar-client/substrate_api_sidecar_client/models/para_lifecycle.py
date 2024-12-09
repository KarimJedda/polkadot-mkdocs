from enum import Enum


class ParaLifecycle(str, Enum):
    DOWNGRADINGPARACHAIN = "downgradingParachain"
    OFFBOARDINGPARACHAIN = "offboardingParachain"
    OFFBOARDINGPARATHREAD = "offboardingParathread"
    ONBOARDING = "onboarding"
    PARACHAIN = "parachain"
    PARATHREAD = "parathread"
    UPGRADINGPARATHREAD = "upgradingParathread"

    def __str__(self) -> str:
        return str(self.value)
