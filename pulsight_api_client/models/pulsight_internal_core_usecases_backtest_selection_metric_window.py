from enum import Enum


class PulsightInternalCoreUsecasesBacktestSelectionMetricWindow(str, Enum):
    SEL_WINDOW_12_H = "12h"
    SEL_WINDOW_1_H = "1h"
    SEL_WINDOW_30_M = "30m"
    SEL_WINDOW_5_M = "5m"
    SEL_WINDOW_6_H = "6h"

    def __str__(self) -> str:
        return str(self.value)
