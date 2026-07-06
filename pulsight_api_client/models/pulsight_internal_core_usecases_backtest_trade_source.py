from enum import Enum


class PulsightInternalCoreUsecasesBacktestTradeSource(str, Enum):
    TRADE_SOURCE_COPY_BUY = "copy_buy"
    TRADE_SOURCE_COPY_SELL = "copy_sell"
    TRADE_SOURCE_EMIT_BUY = "emit_buy"
    TRADE_SOURCE_EMIT_SELL = "emit_sell"

    def __str__(self) -> str:
        return str(self.value)
