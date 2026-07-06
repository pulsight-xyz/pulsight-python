from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_strategy_node_kind import (
        PulsightInternalCoreDomainStrategyNodeKind,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainStrategyNode")


@_attrs_define
class PulsightInternalCoreDomainStrategyNode:
    """
    Attributes:
        id (str | Unset):
        kind (PulsightInternalCoreDomainStrategyNodeKind | Unset):
        label (str | Unset):
    """

    id: str | Unset = UNSET
    kind: PulsightInternalCoreDomainStrategyNodeKind | Unset = UNSET
    label: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kind: dict[str, Any] | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.to_dict()

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if kind is not UNSET:
            field_dict["kind"] = kind
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pulsight_internal_core_domain_strategy_node_kind import (
            PulsightInternalCoreDomainStrategyNodeKind,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _kind = d.pop("kind", UNSET)
        kind: PulsightInternalCoreDomainStrategyNodeKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = PulsightInternalCoreDomainStrategyNodeKind.from_dict(_kind)

        label = d.pop("label", UNSET)

        pulsight_internal_core_domain_strategy_node = cls(
            id=id,
            kind=kind,
            label=label,
        )

        pulsight_internal_core_domain_strategy_node.additional_properties = d
        return pulsight_internal_core_domain_strategy_node

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
