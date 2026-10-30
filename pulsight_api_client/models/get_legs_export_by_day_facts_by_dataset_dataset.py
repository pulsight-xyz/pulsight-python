from enum import StrEnum


class GetLegsExportByDayFactsByDatasetDataset(StrEnum):
    ACTIVITY = "activity"
    ACTIVITY_BASE = "activity_base"
    BUNDLES = "bundles"
    INSIDERS = "insiders"
    INSIDER_FLOWS = "insider_flows"
    MINTS = "mints"
    MINUTES = "minutes"

    def __str__(self) -> str:
        return str(self.value)
