from enum import Enum


class TransactionValidityErrorErrorType(str, Enum):
    UNIMPLEMENTED = "Unimplemented"
    VERSIONEDCONVERSIONFAILED = "VersionedConversionFailed"

    def __str__(self) -> str:
        return str(self.value)
