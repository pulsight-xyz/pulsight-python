from enum import Enum


class PulsightInternalCoreDomainStrategyVenueID(str, Enum):
    DEFAULT_VENUE = "solana"
    VENUE_HYPERLIQUID = "hyperliquid"
    VENUE_POLYMARKET = "polymarket"
    VENUE_SOLANA = "solana"

    def __str__(self) -> str:
        return str(self.value)
