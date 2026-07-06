from enum import Enum


class PulsightInternalCoreDomainStrategyEventKind(str, Enum):
    EVENT_DEV_SOLD = "dev_sold"
    EVENT_FREEZE_RENOUNCED = "freeze_renounced"
    EVENT_LP_BURNED = "lp_burned"
    EVENT_MINT_RENOUNCED = "mint_renounced"

    def __str__(self) -> str:
        return str(self.value)
