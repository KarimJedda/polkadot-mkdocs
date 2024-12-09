from enum import Enum


class RuntimeDispatchInfoClass(str, Enum):
    MANDATORY = "Mandatory"
    NORMAL = "Normal"
    OPERATIONAL = "Operational"

    def __str__(self) -> str:
        return str(self.value)
