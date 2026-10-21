from enum import StrEnum


class GetLegsExportByDayFactsByDatasetDataset(StrEnum):
    BUNDLES = "bundles"
    INSIDERS = "insiders"
    MINTS = "mints"
    MINUTES = "minutes"

    def __str__(self) -> str:
        return str(self.value)
