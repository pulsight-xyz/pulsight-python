from enum import Enum


class PulsightInternalCoreDomainAggregatorWindow(str, Enum):
    WINDOW_1_D = "1d"
    WINDOW_30_D = "30d"
    WINDOW_7_D = "7d"
    WINDOW_ALL = "all"

    def __str__(self) -> str:
        return str(self.value)
