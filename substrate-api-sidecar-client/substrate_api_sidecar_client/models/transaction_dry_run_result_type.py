from enum import Enum


class TransactionDryRunResultType(str, Enum):
    DISPATCHERROR = "DispatchError"
    DISPATCHOUTCOME = "DispatchOutcome"
    TRANSACTIONVALIDITYERROR = "TransactionValidityError"

    def __str__(self) -> str:
        return str(self.value)
