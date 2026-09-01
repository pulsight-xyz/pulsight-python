from enum import StrEnum


class PulsightInternalCoreUsecasesBacktestTradeSource(StrEnum):
    TRADE_SOURCE_COPY_BUY = "copy_buy"
    TRADE_SOURCE_COPY_SELL = "copy_sell"
    TRADE_SOURCE_EMIT_BUY = "emit_buy"
    TRADE_SOURCE_EMIT_SELL = "emit_sell"
    TRADE_SOURCE_SCOPE_EXIT = "scope_exit"

    def __str__(self) -> str:
        return str(self.value)
