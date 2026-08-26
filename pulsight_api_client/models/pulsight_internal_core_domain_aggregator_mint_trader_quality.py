from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorMintTraderQuality")


@_attrs_define
class PulsightInternalCoreDomainAggregatorMintTraderQuality:
    """
    Attributes:
        classified (int | Unset):
        fresh (int | Unset):
        organic (int | Unset):
        ruggy (int | Unset):
        traders (int | Unset):
    """

    classified: int | Unset = UNSET
    fresh: int | Unset = UNSET
    organic: int | Unset = UNSET
    ruggy: int | Unset = UNSET
    traders: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        classified = self.classified

        fresh = self.fresh

        organic = self.organic

        ruggy = self.ruggy

        traders = self.traders

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if classified is not UNSET:
            field_dict["classified"] = classified
        if fresh is not UNSET:
            field_dict["fresh"] = fresh
        if organic is not UNSET:
            field_dict["organic"] = organic
        if ruggy is not UNSET:
            field_dict["ruggy"] = ruggy
        if traders is not UNSET:
            field_dict["traders"] = traders

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        classified = d.pop("classified", UNSET)

        fresh = d.pop("fresh", UNSET)

        organic = d.pop("organic", UNSET)

        ruggy = d.pop("ruggy", UNSET)

        traders = d.pop("traders", UNSET)

        pulsight_internal_core_domain_aggregator_mint_trader_quality = cls(
            classified=classified,
            fresh=fresh,
            organic=organic,
            ruggy=ruggy,
            traders=traders,
        )

        pulsight_internal_core_domain_aggregator_mint_trader_quality.additional_properties = d
        return pulsight_internal_core_domain_aggregator_mint_trader_quality

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
