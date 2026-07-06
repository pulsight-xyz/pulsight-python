from enum import Enum


class PulsightInternalCoreDomainSubscriptionSubscriptionTier(str, Enum):
    TIER_ENTERPRISE = "enterprise"
    TIER_FREE = "free"
    TIER_ONE = "tier1"
    TIER_THREE = "tier3"
    TIER_TWO = "tier2"

    def __str__(self) -> str:
        return str(self.value)
