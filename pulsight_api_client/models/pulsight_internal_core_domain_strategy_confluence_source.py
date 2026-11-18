from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainStrategyConfluenceSource")


@_attrs_define
class PulsightInternalCoreDomainStrategyConfluenceSource:
    """
    Attributes:
        group_id (str | Unset): GroupID is the favorites group, or "ungrouped".
        synced_at (str | Unset): SyncedAt is when the wallets were taken from the group.
    """

    group_id: str | Unset = UNSET
    synced_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_id = self.group_id

        synced_at = self.synced_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if synced_at is not UNSET:
            field_dict["synced_at"] = synced_at

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        group_id = d.pop("group_id", UNSET)

        synced_at = d.pop("synced_at", UNSET)

        pulsight_internal_core_domain_strategy_confluence_source = cls(
            group_id=group_id,
            synced_at=synced_at,
        )

        pulsight_internal_core_domain_strategy_confluence_source.additional_properties = d
        return pulsight_internal_core_domain_strategy_confluence_source

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
