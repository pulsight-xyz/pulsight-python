from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorHop")


@_attrs_define
class PulsightInternalCoreDomainAggregatorHop:
    """
    Attributes:
        dex (str | Unset):
        mint_in_id (int | Unset):
        mint_out_id (int | Unset):
        pool (str | Unset):
        pool_id (int | Unset):
    """

    dex: str | Unset = UNSET
    mint_in_id: int | Unset = UNSET
    mint_out_id: int | Unset = UNSET
    pool: str | Unset = UNSET
    pool_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dex = self.dex

        mint_in_id = self.mint_in_id

        mint_out_id = self.mint_out_id

        pool = self.pool

        pool_id = self.pool_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dex is not UNSET:
            field_dict["dex"] = dex
        if mint_in_id is not UNSET:
            field_dict["mint_in_id"] = mint_in_id
        if mint_out_id is not UNSET:
            field_dict["mint_out_id"] = mint_out_id
        if pool is not UNSET:
            field_dict["pool"] = pool
        if pool_id is not UNSET:
            field_dict["pool_id"] = pool_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        dex = d.pop("dex", UNSET)

        mint_in_id = d.pop("mint_in_id", UNSET)

        mint_out_id = d.pop("mint_out_id", UNSET)

        pool = d.pop("pool", UNSET)

        pool_id = d.pop("pool_id", UNSET)

        pulsight_internal_core_domain_aggregator_hop = cls(
            dex=dex,
            mint_in_id=mint_in_id,
            mint_out_id=mint_out_id,
            pool=pool,
            pool_id=pool_id,
        )

        pulsight_internal_core_domain_aggregator_hop.additional_properties = d
        return pulsight_internal_core_domain_aggregator_hop

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
