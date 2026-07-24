from enum import Enum


class PulsightInternalCoreDomainWebhookType(str, Enum):
    TYPE_DISCORD = "discord"
    TYPE_TELEGRAM = "telegram"

    def __str__(self) -> str:
        return str(self.value)
