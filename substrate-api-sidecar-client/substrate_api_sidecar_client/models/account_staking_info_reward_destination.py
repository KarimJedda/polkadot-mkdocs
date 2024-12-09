from enum import Enum


class AccountStakingInfoRewardDestination(str, Enum):
    CONTROLLER = "Controller"
    STAKED = "Staked"
    STASH = "Stash"

    def __str__(self) -> str:
        return str(self.value)
