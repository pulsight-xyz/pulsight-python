from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorHolderEntry")


@_attrs_define
class PulsightInternalCoreDomainAggregatorHolderEntry:
    """
    Attributes:
        balance (str | Unset): raw base units (decimal string)
        is_bundler (bool | Unset):
        is_insider (bool | Unset):
        is_sniper (bool | Unset):
        label (str | Unset): Label/LabelType identify a known wallet (e.g. "Bybit"/"cex",
            "Pump.fun Fees"/"fee") from the admin-managed registry; empty when
            unknown.
        label_type (str | Unset):
        owner (str | Unset):
        pct_of_supply (float | Unset): % of circulating, 0..100
    """

    balance: str | Unset = UNSET
    is_bundler: bool | Unset = UNSET
    is_insider: bool | Unset = UNSET
    is_sniper: bool | Unset = UNSET
    label: str | Unset = UNSET
    label_type: str | Unset = UNSET
    owner: str | Unset = UNSET
    pct_of_supply: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        balance = self.balance

        is_bundler = self.is_bundler

        is_insider = self.is_insider

        is_sniper = self.is_sniper

        label = self.label

        label_type = self.label_type

        owner = self.owner

        pct_of_supply = self.pct_of_supply

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if balance is not UNSET:
            field_dict["balance"] = balance
        if is_bundler is not UNSET:
            field_dict["is_bundler"] = is_bundler
        if is_insider is not UNSET:
            field_dict["is_insider"] = is_insider
        if is_sniper is not UNSET:
            field_dict["is_sniper"] = is_sniper
        if label is not UNSET:
            field_dict["label"] = label
        if label_type is not UNSET:
            field_dict["label_type"] = label_type
        if owner is not UNSET:
            field_dict["owner"] = owner
        if pct_of_supply is not UNSET:
            field_dict["pct_of_supply"] = pct_of_supply

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        balance = d.pop("balance", UNSET)

        is_bundler = d.pop("is_bundler", UNSET)

        is_insider = d.pop("is_insider", UNSET)

        is_sniper = d.pop("is_sniper", UNSET)

        label = d.pop("label", UNSET)

        label_type = d.pop("label_type", UNSET)

        owner = d.pop("owner", UNSET)

        pct_of_supply = d.pop("pct_of_supply", UNSET)

        pulsight_internal_core_domain_aggregator_holder_entry = cls(
            balance=balance,
            is_bundler=is_bundler,
            is_insider=is_insider,
            is_sniper=is_sniper,
            label=label,
            label_type=label_type,
            owner=owner,
            pct_of_supply=pct_of_supply,
        )

        pulsight_internal_core_domain_aggregator_holder_entry.additional_properties = d
        return pulsight_internal_core_domain_aggregator_holder_entry

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
