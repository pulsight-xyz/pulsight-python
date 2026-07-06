from enum import Enum


class PulsightInternalCoreUsecasesBacktestSelectionMetric(str, Enum):
    SEL_METRIC_LIQUIDITY_SOL = "liquidity_sol"
    SEL_METRIC_PRICE_CHANGE_PCT = "price_change_pct"
    SEL_METRIC_SWAP_COUNT = "swap_count"
    SEL_METRIC_VOLUME_SOL = "volume_sol"

    def __str__(self) -> str:
        return str(self.value)
