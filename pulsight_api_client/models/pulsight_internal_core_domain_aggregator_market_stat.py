from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorMarketStat")


@_attrs_define
class PulsightInternalCoreDomainAggregatorMarketStat:
    """
    Attributes:
        concentration (float | Unset): top-pool volume share, 0..1
        pool_count (int | Unset):
        total_liquidity_usd (float | Unset):
    """

    concentration: float | Unset = UNSET
    pool_count: int | Unset = UNSET
    total_liquidity_usd: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        concentration = self.concentration

        pool_count = self.pool_count

        total_liquidity_usd = self.total_liquidity_usd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if concentration is not UNSET:
            field_dict["concentration"] = concentration
        if pool_count is not UNSET:
            field_dict["pool_count"] = pool_count
        if total_liquidity_usd is not UNSET:
            field_dict["total_liquidity_usd"] = total_liquidity_usd

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        concentration = d.pop("concentration", UNSET)

        pool_count = d.pop("pool_count", UNSET)

        total_liquidity_usd = d.pop("total_liquidity_usd", UNSET)

        pulsight_internal_core_domain_aggregator_market_stat = cls(
            concentration=concentration,
            pool_count=pool_count,
            total_liquidity_usd=total_liquidity_usd,
        )

        pulsight_internal_core_domain_aggregator_market_stat.additional_properties = d
        return pulsight_internal_core_domain_aggregator_market_stat

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
