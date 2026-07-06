from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorCreatedMintRow")


@_attrs_define
class PulsightInternalCoreDomainAggregatorCreatedMintRow:
    """
    Attributes:
        decimals (int | Unset):
        first_seen_ts (str | Unset): FirstSeenTS proxies "created at" — the create-tx and first buy land in
            the same flush window. nil for fixture-only edge cases.
        graduated (bool | Unset): Graduated is true iff the mint has any `mint_migrations` row.
        graduation_target_dex (str | Unset): GraduationTargetDex is the most-recent migration's to_dex; nil when not
            graduated.
        logo_uri (str | Unset):
        mint (str | Unset):
        name (str | Unset):
        symbol (str | Unset):
    """

    decimals: int | Unset = UNSET
    first_seen_ts: str | Unset = UNSET
    graduated: bool | Unset = UNSET
    graduation_target_dex: str | Unset = UNSET
    logo_uri: str | Unset = UNSET
    mint: str | Unset = UNSET
    name: str | Unset = UNSET
    symbol: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        decimals = self.decimals

        first_seen_ts = self.first_seen_ts

        graduated = self.graduated

        graduation_target_dex = self.graduation_target_dex

        logo_uri = self.logo_uri

        mint = self.mint

        name = self.name

        symbol = self.symbol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if decimals is not UNSET:
            field_dict["decimals"] = decimals
        if first_seen_ts is not UNSET:
            field_dict["first_seen_ts"] = first_seen_ts
        if graduated is not UNSET:
            field_dict["graduated"] = graduated
        if graduation_target_dex is not UNSET:
            field_dict["graduation_target_dex"] = graduation_target_dex
        if logo_uri is not UNSET:
            field_dict["logo_uri"] = logo_uri
        if mint is not UNSET:
            field_dict["mint"] = mint
        if name is not UNSET:
            field_dict["name"] = name
        if symbol is not UNSET:
            field_dict["symbol"] = symbol

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        decimals = d.pop("decimals", UNSET)

        first_seen_ts = d.pop("first_seen_ts", UNSET)

        graduated = d.pop("graduated", UNSET)

        graduation_target_dex = d.pop("graduation_target_dex", UNSET)

        logo_uri = d.pop("logo_uri", UNSET)

        mint = d.pop("mint", UNSET)

        name = d.pop("name", UNSET)

        symbol = d.pop("symbol", UNSET)

        pulsight_internal_core_domain_aggregator_created_mint_row = cls(
            decimals=decimals,
            first_seen_ts=first_seen_ts,
            graduated=graduated,
            graduation_target_dex=graduation_target_dex,
            logo_uri=logo_uri,
            mint=mint,
            name=name,
            symbol=symbol,
        )

        pulsight_internal_core_domain_aggregator_created_mint_row.additional_properties = d
        return pulsight_internal_core_domain_aggregator_created_mint_row

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
