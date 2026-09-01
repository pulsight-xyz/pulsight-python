from enum import StrEnum


class PulsightInternalCoreDomainAggregatorTimeframe(StrEnum):
    TIMEFRAME_12_H = "12h"
    TIMEFRAME_15_M = "15m"
    TIMEFRAME_15_S = "15s"
    TIMEFRAME_1_H = "1h"
    TIMEFRAME_1_M = "1m"
    TIMEFRAME_1_S = "1s"
    TIMEFRAME_24_H = "24h"
    TIMEFRAME_2_H = "2h"
    TIMEFRAME_30_M = "30m"
    TIMEFRAME_30_S = "30s"
    TIMEFRAME_4_H = "4h"
    TIMEFRAME_5_M = "5m"
    TIMEFRAME_5_S = "5s"
    TIMEFRAME_6_H = "6h"

    def __str__(self) -> str:
        return str(self.value)
