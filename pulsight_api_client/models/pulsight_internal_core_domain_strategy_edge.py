from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pulsight_internal_core_domain_strategy_edge_port import (
    PulsightInternalCoreDomainStrategyEdgePort,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainStrategyEdge")


@_attrs_define
class PulsightInternalCoreDomainStrategyEdge:
    """
    Attributes:
        from_ (str | Unset):
        port (PulsightInternalCoreDomainStrategyEdgePort | Unset):
        to (str | Unset):
    """

    from_: str | Unset = UNSET
    port: PulsightInternalCoreDomainStrategyEdgePort | Unset = UNSET
    to: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_

        port: str | Unset = UNSET
        if not isinstance(self.port, Unset):
            port = self.port.value

        to = self.to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if port is not UNSET:
            field_dict["port"] = port
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_ = d.pop("from", UNSET)

        _port = d.pop("port", UNSET)
        port: PulsightInternalCoreDomainStrategyEdgePort | Unset
        if isinstance(_port, Unset):
            port = UNSET
        else:
            port = PulsightInternalCoreDomainStrategyEdgePort(_port)

        to = d.pop("to", UNSET)

        pulsight_internal_core_domain_strategy_edge = cls(
            from_=from_,
            port=port,
            to=to,
        )

        pulsight_internal_core_domain_strategy_edge.additional_properties = d
        return pulsight_internal_core_domain_strategy_edge

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
