from enum import Enum


class PulsightInternalCoreDomainCreditPool(str, Enum):
    POOL_API = "api"

    def __str__(self) -> str:
        return str(self.value)
