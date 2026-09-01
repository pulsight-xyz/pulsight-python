from enum import StrEnum


class PulsightInternalCoreUsecasesBacktestSide(StrEnum):
    SIDE_BUY = "buy"
    SIDE_SELL = "sell"

    def __str__(self) -> str:
        return str(self.value)
