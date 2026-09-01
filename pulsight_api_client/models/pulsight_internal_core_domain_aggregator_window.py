from enum import StrEnum


class PulsightInternalCoreDomainAggregatorWindow(StrEnum):
    WINDOW_1_D = "1d"
    WINDOW_30_D = "30d"
    WINDOW_3_M = "3m"
    WINDOW_7_D = "7d"
    WINDOW_ALL = "all"

    def __str__(self) -> str:
        return str(self.value)
