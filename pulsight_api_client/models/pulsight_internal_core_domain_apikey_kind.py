from enum import Enum


class PulsightInternalCoreDomainApikeyKind(str, Enum):
    KIND_BOT = "bot"
    KIND_USER = "user"

    def __str__(self) -> str:
        return str(self.value)
