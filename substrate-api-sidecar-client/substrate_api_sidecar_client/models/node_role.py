from enum import Enum


class NodeRole(str, Enum):
    AUTHORITY = "Authority"
    FULL = "Full"
    LIGHTCLIENT = "LightClient"
    SENTRY = "Sentry"

    def __str__(self) -> str:
        return str(self.value)
