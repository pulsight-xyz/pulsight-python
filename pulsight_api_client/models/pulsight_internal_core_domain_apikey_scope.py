from enum import Enum


class PulsightInternalCoreDomainApikeyScope(str, Enum):
    SCOPE_BACKTEST_RUN = "backtest:run"
    SCOPE_DATA_READ = "data:read"
    SCOPE_STRATEGY_READ = "strategy:read"
    SCOPE_STRATEGY_WRITE = "strategy:write"

    def __str__(self) -> str:
        return str(self.value)
