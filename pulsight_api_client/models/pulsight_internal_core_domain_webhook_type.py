from enum import StrEnum


class PulsightInternalCoreDomainWebhookType(StrEnum):
    TYPE_DISCORD = "discord"
    TYPE_TELEGRAM = "telegram"

    def __str__(self) -> str:
        return str(self.value)
