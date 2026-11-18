from enum import StrEnum


class PulsightInternalCoreDomainStrategyConfluenceCount(StrEnum):
    CONFLUENCE_COUNT_BUYS = "buys"
    CONFLUENCE_COUNT_ENTRIES = "entries"

    def __str__(self) -> str:
        return str(self.value)
