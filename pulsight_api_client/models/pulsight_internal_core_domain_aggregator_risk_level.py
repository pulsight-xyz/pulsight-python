from enum import Enum


class PulsightInternalCoreDomainAggregatorRiskLevel(str, Enum):
    RISK_DANGER = "danger"
    RISK_WARN = "warn"

    def __str__(self) -> str:
        return str(self.value)
