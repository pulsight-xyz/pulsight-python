from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_aggregator_holder_entry import (
        PulsightInternalCoreDomainAggregatorHolderEntry,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorCohortStat")


@_attrs_define
class PulsightInternalCoreDomainAggregatorCohortStat:
    """
    Attributes:
        available (bool | Unset): false = signal not computable yet
        count (int | Unset):
        total_pct (float | Unset): % of circulating
        wallets (list[PulsightInternalCoreDomainAggregatorHolderEntry] | Unset):
    """

    available: bool | Unset = UNSET
    count: int | Unset = UNSET
    total_pct: float | Unset = UNSET
    wallets: list[PulsightInternalCoreDomainAggregatorHolderEntry] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available = self.available

        count = self.count

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
        if total_pct is not UNSET:
            field_dict["total_pct"] = total_pct
        if wallets is not UNSET:
            field_dict["wallets"] = wallets

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_domain_aggregator_holder_entry import (
            PulsightInternalCoreDomainAggregatorHolderEntry,
        )

        d = dict(src_dict)
        available = d.pop("available", UNSET)

        count = d.pop("count", UNSET)

        total_pct = d.pop("total_pct", UNSET)

        _wallets = d.pop("wallets", UNSET)
        wallets: list[PulsightInternalCoreDomainAggregatorHolderEntry] | Unset = UNSET
        if _wallets is not UNSET:
            wallets = []
            for wallets_item_data in _wallets:
                wallets_item = (
                    PulsightInternalCoreDomainAggregatorHolderEntry.from_dict(
                        wallets_item_data
                    )
                )

                wallets.append(wallets_item)

        pulsight_internal_core_domain_aggregator_cohort_stat = cls(
            available=available,
            count=count,
            total_pct=total_pct,
            wallets=wallets,
        )

        pulsight_internal_core_domain_aggregator_cohort_stat.additional_properties = d
        return pulsight_internal_core_domain_aggregator_cohort_stat

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
