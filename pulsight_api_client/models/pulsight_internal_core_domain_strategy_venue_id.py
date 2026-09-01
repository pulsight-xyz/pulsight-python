from enum import StrEnum


class PulsightInternalCoreDomainStrategyVenueID(StrEnum):
    VENUE_HYPERLIQUID = "hyperliquid"
    VENUE_POLYMARKET = "polymarket"
    VENUE_SOLANA = "solana"

    def __str__(self) -> str:
        return str(self.value)
