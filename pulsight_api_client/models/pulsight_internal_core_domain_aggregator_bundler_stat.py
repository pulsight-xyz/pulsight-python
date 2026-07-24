from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_aggregator_bundler_entry import (
        PulsightInternalCoreDomainAggregatorBundlerEntry,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorBundlerStat")


@_attrs_define
class PulsightInternalCoreDomainAggregatorBundlerStat:
    """
    Attributes:
        available (bool | Unset):
        count (int | Unset):
        total_initial_pct (float | Unset):
        total_pct (float | Unset):
        wallets (list[PulsightInternalCoreDomainAggregatorBundlerEntry] | Unset):
    """

    available: bool | Unset = UNSET
    count: int | Unset = UNSET
    total_initial_pct: float | Unset = UNSET
    total_pct: float | Unset = UNSET
    wallets: list[PulsightInternalCoreDomainAggregatorBundlerEntry] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available = self.available

        count = self.count

        total_initial_pct = self.total_initial_pct

        total_pct = self.total_pct

        wallets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wallets, Unset):
            wallets = []
            for wallets_item_data in self.wallets:
                wallets_item = wallets_item_data.to_dict()
                wallets.append(wallets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available is not UNSET:
            field_dict["available"] = available
        if count is not UNSET:
            field_dict["count"] = count
        if total_initial_pct is not UNSET:
            field_dict["total_initial_pct"] = total_initial_pct
        if total_pct is not UNSET:
            field_dict["total_pct"] = total_pct
        if wallets is not UNSET:
            field_dict["wallets"] = wallets

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_domain_aggregator_bundler_entry import (
            PulsightInternalCoreDomainAggregatorBundlerEntry,
        )

        d = dict(src_dict)
        available = d.pop("available", UNSET)

        count = d.pop("count", UNSET)

        total_initial_pct = d.pop("total_initial_pct", UNSET)

        total_pct = d.pop("total_pct", UNSET)

        _wallets = d.pop("wallets", UNSET)
        wallets: list[PulsightInternalCoreDomainAggregatorBundlerEntry] | Unset = UNSET
        if _wallets is not UNSET:
            wallets = []
            for wallets_item_data in _wallets:
                wallets_item = (
                    PulsightInternalCoreDomainAggregatorBundlerEntry.from_dict(
                        wallets_item_data
                    )
                )

                wallets.append(wallets_item)

        pulsight_internal_core_domain_aggregator_bundler_stat = cls(
            available=available,
            count=count,
            total_initial_pct=total_initial_pct,
            total_pct=total_pct,
            wallets=wallets,
        )

        pulsight_internal_core_domain_aggregator_bundler_stat.additional_properties = d
        return pulsight_internal_core_domain_aggregator_bundler_stat

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
