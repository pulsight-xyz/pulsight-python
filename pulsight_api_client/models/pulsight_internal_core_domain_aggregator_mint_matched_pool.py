from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorMintMatchedPool")


@_attrs_define
class PulsightInternalCoreDomainAggregatorMintMatchedPool:
    """
    Attributes:
        address (str | Unset): Address is the pool's address.
        base (bool | Unset): Base is true when the row's mint is the pool's base token, the side
            the pool prices; false when it is the pool's quote.
        dex (str | Unset): Dex is the pool's venue slug, same vocabulary as `?dex=`.
    """

    address: str | Unset = UNSET
    base: bool | Unset = UNSET
    dex: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        base = self.base

        dex = self.dex

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if base is not UNSET:
            field_dict["base"] = base
        if dex is not UNSET:
            field_dict["dex"] = dex

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        address = d.pop("address", UNSET)

        base = d.pop("base", UNSET)

        dex = d.pop("dex", UNSET)

        pulsight_internal_core_domain_aggregator_mint_matched_pool = cls(
            address=address,
            base=base,
            dex=dex,
        )

        pulsight_internal_core_domain_aggregator_mint_matched_pool.additional_properties = d
        return pulsight_internal_core_domain_aggregator_mint_matched_pool

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
