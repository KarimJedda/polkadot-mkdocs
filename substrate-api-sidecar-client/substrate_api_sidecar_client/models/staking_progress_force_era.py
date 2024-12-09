from enum import Enum


class StakingProgressForceEra(str, Enum):
    FORCEALWAYS = "ForceAlways"
    FORCENEW = "ForceNew"
    FORCENONE = "ForceNone"
    NOTFORCING = "NotForcing"

    def __str__(self) -> str:
        return str(self.value)
