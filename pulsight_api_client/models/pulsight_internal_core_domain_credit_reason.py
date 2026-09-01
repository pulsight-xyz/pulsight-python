from enum import StrEnum


class PulsightInternalCoreDomainCreditReason(StrEnum):
    REASON_ADJUST = "adjust"
    REASON_CONSUME = "consume"
    REASON_GRANT = "grant"
    REASON_REFERRAL_BONUS = "referral_bonus"
    REASON_REFUND = "refund"

    def __str__(self) -> str:
        return str(self.value)
