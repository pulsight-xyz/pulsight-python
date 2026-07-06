from enum import Enum


class PulsightInternalCoreDomainAggregatorTimeframe(str, Enum):
    TIMEFRAME_15_M = "15m"
    TIMEFRAME_15_S = "15s"
    TIMEFRAME_1_M = "1m"
    TIMEFRAME_1_S = "1s"
    TIMEFRAME_30_M = "30m"
    TIMEFRAME_30_S = "30s"
    TIMEFRAME_5_M = "5m"
    TIMEFRAME_5_S = "5s"

    def __str__(self) -> str:
        return str(self.value)
