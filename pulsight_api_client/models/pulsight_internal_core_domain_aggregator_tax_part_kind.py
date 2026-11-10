from enum import StrEnum


class PulsightInternalCoreDomainAggregatorTaxPartKind(StrEnum):
    CASHBACK = "cashback"
    CREATOR = "creator"
    FUND = "fund"
    HOLDER_REWARDS = "holder_rewards"
    LP = "lp"
    PLATFORM = "platform"
    PROTOCOL = "protocol"

    def __str__(self) -> str:
        return str(self.value)
