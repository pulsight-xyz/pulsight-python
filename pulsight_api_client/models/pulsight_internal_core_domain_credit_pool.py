from enum import StrEnum


class PulsightInternalCoreDomainCreditPool(StrEnum):
    POOL_API = "api"

    def __str__(self) -> str:
        return str(self.value)
