from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorMintActivityPoint")


@_attrs_define
class PulsightInternalCoreDomainAggregatorMintActivityPoint:
    """
    Attributes:
        fees_lamports (int | Unset):
        swaps (int | Unset):
        ts (int | Unset):
    """

    fees_lamports: int | Unset = UNSET
    swaps: int | Unset = UNSET
    ts: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fees_lamports = self.fees_lamports

        swaps = self.swaps

        ts = self.ts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fees_lamports is not UNSET:
            field_dict["fees_lamports"] = fees_lamports
        if swaps is not UNSET:
            field_dict["swaps"] = swaps
        if ts is not UNSET:
            field_dict["ts"] = ts

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        fees_lamports = d.pop("fees_lamports", UNSET)

        swaps = d.pop("swaps", UNSET)

        ts = d.pop("ts", UNSET)

        pulsight_internal_core_domain_aggregator_mint_activity_point = cls(
            fees_lamports=fees_lamports,
            swaps=swaps,
            ts=ts,
        )

        pulsight_internal_core_domain_aggregator_mint_activity_point.additional_properties = d
        return pulsight_internal_core_domain_aggregator_mint_activity_point

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
