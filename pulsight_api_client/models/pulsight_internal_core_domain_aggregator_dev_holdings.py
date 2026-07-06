from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorDevHoldings")


@_attrs_define
class PulsightInternalCoreDomainAggregatorDevHoldings:
    """
    Attributes:
        balance_raw (str | Unset): Creator's raw token balance (NUMERIC → decimal string).
        creator (str | Unset): Creator wallet (mirrors MintRow.Creator).
        percent_of_supply (float | Unset): Percentage of supply held by the creator, 0..=100.
        supply_raw (str | Unset): Mint's on-chain total supply (same encoding).
    """

    balance_raw: str | Unset = UNSET
    creator: str | Unset = UNSET
    percent_of_supply: float | Unset = UNSET
    supply_raw: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        balance_raw = self.balance_raw

        creator = self.creator

        percent_of_supply = self.percent_of_supply

        supply_raw = self.supply_raw

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if balance_raw is not UNSET:
            field_dict["balance_raw"] = balance_raw
        if creator is not UNSET:
            field_dict["creator"] = creator
        if percent_of_supply is not UNSET:
            field_dict["percent_of_supply"] = percent_of_supply
        if supply_raw is not UNSET:
            field_dict["supply_raw"] = supply_raw

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        balance_raw = d.pop("balance_raw", UNSET)

        creator = d.pop("creator", UNSET)

        percent_of_supply = d.pop("percent_of_supply", UNSET)

        supply_raw = d.pop("supply_raw", UNSET)

        pulsight_internal_core_domain_aggregator_dev_holdings = cls(
            balance_raw=balance_raw,
            creator=creator,
            percent_of_supply=percent_of_supply,
            supply_raw=supply_raw,
        )

        pulsight_internal_core_domain_aggregator_dev_holdings.additional_properties = d
        return pulsight_internal_core_domain_aggregator_dev_holdings

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
