from enum import IntEnum


class GetMintsHours(IntEnum):
    VALUE_1 = 1
    VALUE_6 = 6
    VALUE_24 = 24

    def __str__(self) -> str:
        return str(self.value)
