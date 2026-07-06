from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_aggregator_mint_window_stats import (
        PulsightInternalCoreDomainAggregatorMintWindowStats,
    )


T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorMintStatsByWindow")


@_attrs_define
class PulsightInternalCoreDomainAggregatorMintStatsByWindow:
    """
    Attributes:
        field_1h (PulsightInternalCoreDomainAggregatorMintWindowStats | Unset):
        field_1m (PulsightInternalCoreDomainAggregatorMintWindowStats | Unset):
        field_24h (PulsightInternalCoreDomainAggregatorMintWindowStats | Unset):
        field_5m (PulsightInternalCoreDomainAggregatorMintWindowStats | Unset):
    """

    field_1h: PulsightInternalCoreDomainAggregatorMintWindowStats | Unset = UNSET
    field_1m: PulsightInternalCoreDomainAggregatorMintWindowStats | Unset = UNSET
    field_24h: PulsightInternalCoreDomainAggregatorMintWindowStats | Unset = UNSET
    field_5m: PulsightInternalCoreDomainAggregatorMintWindowStats | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_1h: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_1h, Unset):
            field_1h = self.field_1h.to_dict()

        field_1m: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_1m, Unset):
            field_1m = self.field_1m.to_dict()

        field_24h: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_24h, Unset):
            field_24h = self.field_24h.to_dict()

        field_5m: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_5m, Unset):
            field_5m = self.field_5m.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_1h is not UNSET:
            field_dict["1h"] = field_1h
        if field_1m is not UNSET:
            field_dict["1m"] = field_1m
        if field_24h is not UNSET:
            field_dict["24h"] = field_24h
        if field_5m is not UNSET:
            field_dict["5m"] = field_5m

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pulsight_internal_core_domain_aggregator_mint_window_stats import (
            PulsightInternalCoreDomainAggregatorMintWindowStats,
        )

        d = dict(src_dict)
        _field_1h = d.pop("1h", UNSET)
        field_1h: PulsightInternalCoreDomainAggregatorMintWindowStats | Unset
        if isinstance(_field_1h, Unset):
            field_1h = UNSET
        else:
            field_1h = PulsightInternalCoreDomainAggregatorMintWindowStats.from_dict(
                _field_1h
            )

        _field_1m = d.pop("1m", UNSET)
        field_1m: PulsightInternalCoreDomainAggregatorMintWindowStats | Unset
        if isinstance(_field_1m, Unset):
            field_1m = UNSET
        else:
            field_1m = PulsightInternalCoreDomainAggregatorMintWindowStats.from_dict(
                _field_1m
            )

        _field_24h = d.pop("24h", UNSET)
        field_24h: PulsightInternalCoreDomainAggregatorMintWindowStats | Unset
        if isinstance(_field_24h, Unset):
            field_24h = UNSET
        else:
            field_24h = PulsightInternalCoreDomainAggregatorMintWindowStats.from_dict(
                _field_24h
            )

        _field_5m = d.pop("5m", UNSET)
        field_5m: PulsightInternalCoreDomainAggregatorMintWindowStats | Unset
        if isinstance(_field_5m, Unset):
            field_5m = UNSET
        else:
            field_5m = PulsightInternalCoreDomainAggregatorMintWindowStats.from_dict(
                _field_5m
            )

        pulsight_internal_core_domain_aggregator_mint_stats_by_window = cls(
            field_1h=field_1h,
            field_1m=field_1m,
            field_24h=field_24h,
            field_5m=field_5m,
        )

        pulsight_internal_core_domain_aggregator_mint_stats_by_window.additional_properties = d
        return pulsight_internal_core_domain_aggregator_mint_stats_by_window

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
