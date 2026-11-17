from enum import StrEnum


class PulsightInternalCoreDomainTraderSimilarityLabel(StrEnum):
    SIMILARITY_ALIKE = "alike"
    SIMILARITY_DIFFERENT = "different"
    SIMILARITY_SOMEWHAT_ALIKE = "somewhat_alike"
    SIMILARITY_VERY_ALIKE = "very_alike"

    def __str__(self) -> str:
        return str(self.value)
