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
    from ..models.pulsight_internal_core_domain_aggregator_holder_entry import (
        PulsightInternalCoreDomainAggregatorHolderEntry,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorRiskCohort")


@_attrs_define
class PulsightInternalCoreDomainAggregatorRiskCohort:
    """
    Attributes:
        bundlers (list[PulsightInternalCoreDomainAggregatorBundlerEntry] | Unset):
        group (str | Unset):
        wallets (list[PulsightInternalCoreDomainAggregatorHolderEntry] | Unset):
    """

    bundlers: list[PulsightInternalCoreDomainAggregatorBundlerEntry] | Unset = UNSET
    group: str | Unset = UNSET
    wallets: list[PulsightInternalCoreDomainAggregatorHolderEntry] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bundlers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bundlers, Unset):
            bundlers = []
            for bundlers_item_data in self.bundlers:
                bundlers_item = bundlers_item_data.to_dict()
                bundlers.append(bundlers_item)

        group = self.group

        wallets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wallets, Unset):
            wallets = []
            for wallets_item_data in self.wallets:
                wallets_item = wallets_item_data.to_dict()
                wallets.append(wallets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bundlers is not UNSET:
            field_dict["bundlers"] = bundlers
        if group is not UNSET:
            field_dict["group"] = group
        if wallets is not UNSET:
            field_dict["wallets"] = wallets

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.pulsight_internal_core_domain_aggregator_bundler_entry import (
            PulsightInternalCoreDomainAggregatorBundlerEntry,
        )
        from ..models.pulsight_internal_core_domain_aggregator_holder_entry import (
            PulsightInternalCoreDomainAggregatorHolderEntry,
        )

        d = dict(src_dict)
        _bundlers = d.pop("bundlers", UNSET)
        bundlers: list[PulsightInternalCoreDomainAggregatorBundlerEntry] | Unset = UNSET
        if _bundlers is not UNSET:
            bundlers = []
            for bundlers_item_data in _bundlers:
                bundlers_item = (
                    PulsightInternalCoreDomainAggregatorBundlerEntry.from_dict(
                        bundlers_item_data
                    )
                )

                bundlers.append(bundlers_item)

        group = d.pop("group", UNSET)

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

        pulsight_internal_core_domain_aggregator_risk_cohort = cls(
            bundlers=bundlers,
            group=group,
            wallets=wallets,
        )

        pulsight_internal_core_domain_aggregator_risk_cohort.additional_properties = d
        return pulsight_internal_core_domain_aggregator_risk_cohort

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
