from enum import StrEnum


class PulsightInternalCoreUsecasesBacktestCapitalModel(StrEnum):
    CAPITAL_MODEL_PORTFOLIO = "portfolio"
    CAPITAL_MODEL_UNLIMITED = "unlimited"

    def __str__(self) -> str:
        return str(self.value)
