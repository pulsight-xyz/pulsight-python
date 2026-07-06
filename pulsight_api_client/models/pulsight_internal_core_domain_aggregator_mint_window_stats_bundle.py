from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_aggregator_mint_stats_by_window import (
        PulsightInternalCoreDomainAggregatorMintStatsByWindow,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorMintWindowStatsBundle")


@_attrs_define
class PulsightInternalCoreDomainAggregatorMintWindowStatsBundle:
    """
    Attributes:
        as_of (str | Unset):
        mint (str | Unset):
        stats (PulsightInternalCoreDomainAggregatorMintStatsByWindow | Unset):
    """

    as_of: str | Unset = UNSET
    mint: str | Unset = UNSET
    stats: PulsightInternalCoreDomainAggregatorMintStatsByWindow | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        as_of = self.as_of

        mint = self.mint

        stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if as_of is not UNSET:
            field_dict["as_of"] = as_of
        if mint is not UNSET:
            field_dict["mint"] = mint
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pulsight_internal_core_domain_aggregator_mint_stats_by_window import (
            PulsightInternalCoreDomainAggregatorMintStatsByWindow,
        )

        d = dict(src_dict)
        as_of = d.pop("as_of", UNSET)

        mint = d.pop("mint", UNSET)

        _stats = d.pop("stats", UNSET)
        stats: PulsightInternalCoreDomainAggregatorMintStatsByWindow | Unset
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = PulsightInternalCoreDomainAggregatorMintStatsByWindow.from_dict(
                _stats
            )

        pulsight_internal_core_domain_aggregator_mint_window_stats_bundle = cls(
            as_of=as_of,
            mint=mint,
            stats=stats,
        )

        pulsight_internal_core_domain_aggregator_mint_window_stats_bundle.additional_properties = d
        return pulsight_internal_core_domain_aggregator_mint_window_stats_bundle

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
