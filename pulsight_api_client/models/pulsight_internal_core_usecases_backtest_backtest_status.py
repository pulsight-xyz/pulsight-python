from enum import Enum


class PulsightInternalCoreUsecasesBacktestBacktestStatus(str, Enum):
    BACKTEST_STATUS_CANCELLED = "cancelled"
    BACKTEST_STATUS_DONE = "done"
    BACKTEST_STATUS_FAILED = "failed"
    BACKTEST_STATUS_PENDING = "pending"
    BACKTEST_STATUS_RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
