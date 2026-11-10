from enum import StrEnum


class PulsightInternalCoreDomainAggregatorTaxSwapFeeSource(StrEnum):
    CONFIGURED = "configured"
    RECORDED = "recorded"

    def __str__(self) -> str:
        return str(self.value)
