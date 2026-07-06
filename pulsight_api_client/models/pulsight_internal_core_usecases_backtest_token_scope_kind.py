from enum import Enum


class PulsightInternalCoreUsecasesBacktestTokenScopeKind(str, Enum):
    TOKEN_SCOPE_MINTS = "mints"
    TOKEN_SCOPE_MIRRORS_TRADED = "mirrors_traded"
    TOKEN_SCOPE_SINGLE_MINT = "single_mint"
    TOKEN_SCOPE_STANDALONE = "standalone"
    TOKEN_SCOPE_TRADER_TRADED = "trader_traded"

    def __str__(self) -> str:
        return str(self.value)
