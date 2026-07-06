from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorMintMigration")


@_attrs_define
class PulsightInternalCoreDomainAggregatorMintMigration:
    """
    Attributes:
        destination_pool (str | Unset):
        from_dex (str | Unset):
        mint (str | Unset):
        slot (int | Unset):
        source (str | Unset): Source ∈ {"observed","inferred"} (CHECK constraint).
        timestamp (str | Unset):
        to_dex (str | Unset):
    """

    destination_pool: str | Unset = UNSET
    from_dex: str | Unset = UNSET
    mint: str | Unset = UNSET
    slot: int | Unset = UNSET
    source: str | Unset = UNSET
    timestamp: str | Unset = UNSET
    to_dex: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination_pool = self.destination_pool

        from_dex = self.from_dex

        mint = self.mint

        slot = self.slot

        source = self.source

        timestamp = self.timestamp

        to_dex = self.to_dex

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if destination_pool is not UNSET:
            field_dict["destination_pool"] = destination_pool
        if from_dex is not UNSET:
            field_dict["from_dex"] = from_dex
        if mint is not UNSET:
            field_dict["mint"] = mint
        if slot is not UNSET:
            field_dict["slot"] = slot
        if source is not UNSET:
            field_dict["source"] = source
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if to_dex is not UNSET:
            field_dict["to_dex"] = to_dex

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        destination_pool = d.pop("destination_pool", UNSET)

        from_dex = d.pop("from_dex", UNSET)

        mint = d.pop("mint", UNSET)

        slot = d.pop("slot", UNSET)

        source = d.pop("source", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        to_dex = d.pop("to_dex", UNSET)

        pulsight_internal_core_domain_aggregator_mint_migration = cls(
            destination_pool=destination_pool,
            from_dex=from_dex,
            mint=mint,
            slot=slot,
            source=source,
            timestamp=timestamp,
            to_dex=to_dex,
        )

        pulsight_internal_core_domain_aggregator_mint_migration.additional_properties = d
        return pulsight_internal_core_domain_aggregator_mint_migration

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
