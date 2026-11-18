from enum import StrEnum


class PulsightInternalCoreDomainStrategyConfluenceMetric(StrEnum):
    CONFLUENCE_BUYERS = "buyers"
    CONFLUENCE_HOLDERS = "holders"
    CONFLUENCE_SELLERS = "sellers"

    def __str__(self) -> str:
        return str(self.value)
