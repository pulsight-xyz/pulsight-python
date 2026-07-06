from enum import Enum


class PulsightInternalCoreDomainTraderTagSource(str, Enum):
    TAG_SOURCE_AGGREGATOR = "aggregator"
    TAG_SOURCE_COMPUTED = "computed"
    TAG_SOURCE_MANUAL = "manual"

    def __str__(self) -> str:
        return str(self.value)
