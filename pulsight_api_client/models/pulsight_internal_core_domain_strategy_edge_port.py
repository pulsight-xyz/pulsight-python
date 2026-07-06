from enum import Enum


class PulsightInternalCoreDomainStrategyEdgePort(str, Enum):
    EDGE_PORT_COND = "cond"
    EDGE_PORT_DEFAULT = "default"
    EDGE_PORT_ELSE = "else"
    EDGE_PORT_THEN = "then"

    def __str__(self) -> str:
        return str(self.value)
