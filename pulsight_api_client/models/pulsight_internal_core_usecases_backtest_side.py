from enum import Enum


class PulsightInternalCoreUsecasesBacktestSide(str, Enum):
    SIDE_BUY = "buy"
    SIDE_SELL = "sell"

    def __str__(self) -> str:
        return str(self.value)
