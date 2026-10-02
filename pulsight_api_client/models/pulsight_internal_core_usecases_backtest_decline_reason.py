from enum import StrEnum


class PulsightInternalCoreUsecasesBacktestDeclineReason(StrEnum):
    DECLINE_COOLDOWN = "cooldown"
    DECLINE_EXPOSURE_CAP = "exposure_cap"
    DECLINE_MAX_BUYS_PER_POSITION = "max_buys_per_position"
    DECLINE_NON_SOL_QUOTE = "non_sol_quote"
    DECLINE_NO_BRACKET = "no_bracket"
    DECLINE_POOL_NOT_SIMULATED = "pool_not_simulated"
    DECLINE_RATE_LIMITED = "rate_limited"
    DECLINE_REVERTED = "reverted"
    DECLINE_SIZE_OUT_OF_RANGE = "size_out_of_range"
    DECLINE_UNMIRRORED = "unmirrored"
    DECLINE_UNPRICED = "unpriced"
    DECLINE_ZERO_SIZE = "zero_size"

    def __str__(self) -> str:
        return str(self.value)
