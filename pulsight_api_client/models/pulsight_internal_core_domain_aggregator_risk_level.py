from enum import StrEnum


class PulsightInternalCoreDomainAggregatorRiskLevel(StrEnum):
    RISK_DANGER = "danger"
    RISK_WARN = "warn"

    def __str__(self) -> str:
        return str(self.value)
