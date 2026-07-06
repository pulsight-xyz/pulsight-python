from enum import Enum


class PulsightInternalCoreDomainStrategyComparisonOp(str, Enum):
    COMPARISON_EQ = "eq"
    COMPARISON_GT = "gt"
    COMPARISON_GTE = "gte"
    COMPARISON_LT = "lt"
    COMPARISON_LTE = "lte"

    def __str__(self) -> str:
        return str(self.value)
