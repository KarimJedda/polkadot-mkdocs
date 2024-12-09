from enum import Enum


class OperationPhaseVariant(str, Enum):
    APPLYEXTRINSIC = "applyExtrinsic"
    FINALCHECKS = "finalChecks"
    INITIALCHECKS = "initialChecks"
    ONFINALIZE = "onFinalize"
    ONINITIALIZE = "onInitialize"

    def __str__(self) -> str:
        return str(self.value)
