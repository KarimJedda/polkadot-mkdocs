from enum import Enum


class TransactionDispatchErrorErrorType(str, Enum):
    ARITHMETICERROR = "ArithmeticError"
    BADORIGIN = "BadOrigin"
    CANNOTLOOKUP = "CannotLookup"
    CONSUMERREMAINING = "ConsumerRemaining"
    CORRUPTION = "Corruption"
    EXHAUSTED = "Exhausted"
    MODULEERROR = "ModuleError"
    NOPROVIDERS = "NoProviders"
    OTHER = "Other"
    ROOTNOTALLOWED = "RootNotAllowed"
    TOKENERROR = "TokenError"
    TOOMANYCONSUMERS = "TooManyConsumers"
    TRANSACTIONALERROR = "TransactionalError"
    UNAVAILABLE = "Unavailable"

    def __str__(self) -> str:
        return str(self.value)
