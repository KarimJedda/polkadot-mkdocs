from enum import Enum


class BalanceLockReasons(str, Enum):
    ALL_2 = "All = 2"
    FEE_0 = "Fee = 0"
    MISC_1 = "Misc = 1"

    def __str__(self) -> str:
        return str(self.value)
