from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorMintBundled")


@_attrs_define
class PulsightInternalCoreDomainAggregatorMintBundled:
    """
    Attributes:
        initial_pct (float | Unset):
        wallets (int | Unset):
    """

    initial_pct: float | Unset = UNSET
    wallets: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        initial_pct = self.initial_pct

        wallets = self.wallets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if initial_pct is not UNSET:
            field_dict["initial_pct"] = initial_pct
        if wallets is not UNSET:
            field_dict["wallets"] = wallets

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        initial_pct = d.pop("initial_pct", UNSET)

        wallets = d.pop("wallets", UNSET)

        pulsight_internal_core_domain_aggregator_mint_bundled = cls(
            initial_pct=initial_pct,
            wallets=wallets,
        )

        pulsight_internal_core_domain_aggregator_mint_bundled.additional_properties = d
        return pulsight_internal_core_domain_aggregator_mint_bundled

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
