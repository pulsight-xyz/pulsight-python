from enum import StrEnum


class PulsightInternalCoreDomainTraderTagSource(StrEnum):
    TAG_SOURCE_AGGREGATOR = "aggregator"
    TAG_SOURCE_COMPUTED = "computed"
    TAG_SOURCE_MANUAL = "manual"

    def __str__(self) -> str:
        return str(self.value)
