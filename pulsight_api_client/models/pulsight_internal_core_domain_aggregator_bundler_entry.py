from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorBundlerEntry")


@_attrs_define
class PulsightInternalCoreDomainAggregatorBundlerEntry:
    """
    Attributes:
        balance (str | Unset):
        initial_balance (str | Unset):
        initial_pct_of_supply (float | Unset):
        label (str | Unset): Label/LabelType identify a known wallet (e.g. "Bybit"/"cex") from the
            admin-managed registry; empty when unknown. Same provenance as
            HolderEntry.Label.
        label_type (str | Unset):
        pct_of_supply (float | Unset):
        slot (int | Unset):
        wallet (str | Unset):
    """

    balance: str | Unset = UNSET
    initial_balance: str | Unset = UNSET
    initial_pct_of_supply: float | Unset = UNSET
    label: str | Unset = UNSET
    label_type: str | Unset = UNSET
    pct_of_supply: float | Unset = UNSET
    slot: int | Unset = UNSET
    wallet: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        balance = self.balance

        initial_balance = self.initial_balance

        initial_pct_of_supply = self.initial_pct_of_supply

        label = self.label

        label_type = self.label_type

        pct_of_supply = self.pct_of_supply

        slot = self.slot

        wallet = self.wallet

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if balance is not UNSET:
            field_dict["balance"] = balance
        if initial_balance is not UNSET:
            field_dict["initial_balance"] = initial_balance
        if initial_pct_of_supply is not UNSET:
            field_dict["initial_pct_of_supply"] = initial_pct_of_supply
        if label is not UNSET:
            field_dict["label"] = label
        if label_type is not UNSET:
            field_dict["label_type"] = label_type
        if pct_of_supply is not UNSET:
            field_dict["pct_of_supply"] = pct_of_supply
        if slot is not UNSET:
            field_dict["slot"] = slot
        if wallet is not UNSET:
            field_dict["wallet"] = wallet

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        balance = d.pop("balance", UNSET)

        initial_balance = d.pop("initial_balance", UNSET)

        initial_pct_of_supply = d.pop("initial_pct_of_supply", UNSET)

        label = d.pop("label", UNSET)

        label_type = d.pop("label_type", UNSET)

        pct_of_supply = d.pop("pct_of_supply", UNSET)

        slot = d.pop("slot", UNSET)

        wallet = d.pop("wallet", UNSET)

        pulsight_internal_core_domain_aggregator_bundler_entry = cls(
            balance=balance,
            initial_balance=initial_balance,
            initial_pct_of_supply=initial_pct_of_supply,
            label=label,
            label_type=label_type,
            pct_of_supply=pct_of_supply,
            slot=slot,
            wallet=wallet,
        )

        pulsight_internal_core_domain_aggregator_bundler_entry.additional_properties = d
        return pulsight_internal_core_domain_aggregator_bundler_entry

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
