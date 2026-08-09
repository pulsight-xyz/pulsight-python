from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.pulsight_internal_core_domain_aggregator_window import (
    PulsightInternalCoreDomainAggregatorWindow,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorTraderPriceImpactStats")


@_attrs_define
class PulsightInternalCoreDomainAggregatorTraderPriceImpactStats:
    """
    Attributes:
        avg_price_impact_bps (float | Unset): AvgBps is the mean and MedianBps the p50 over the window's measurable
            legs. Both are reported because the population is heavy-tailed — a
            handful of large fills into thin curves dominate the mean while the
            median describes the wallet's ordinary fill.

            POINTERS, because 0 bps is a REAL answer (a wallet trading tiny size
            into deep pools) and "we could not measure it" must not read as it.
            Nil when Swaps is 0 — most often a wallet trading only concentrated
            liquidity, whose vault balances are not a curve.
        median_price_impact_bps (float | Unset):
        price_impact_swaps (int | Unset): Swaps is how many legs were measurable, and is what tells "measured 0"
            apart from "not measured" on the wire.
        pubkey (str | Unset):
        window (PulsightInternalCoreDomainAggregatorWindow | Unset):
    """

    avg_price_impact_bps: float | Unset = UNSET
    median_price_impact_bps: float | Unset = UNSET
    price_impact_swaps: int | Unset = UNSET
    pubkey: str | Unset = UNSET
    window: PulsightInternalCoreDomainAggregatorWindow | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        avg_price_impact_bps = self.avg_price_impact_bps

        median_price_impact_bps = self.median_price_impact_bps

        price_impact_swaps = self.price_impact_swaps

        pubkey = self.pubkey

        window: str | Unset = UNSET
        if not isinstance(self.window, Unset):
            window = self.window.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if avg_price_impact_bps is not UNSET:
            field_dict["avg_price_impact_bps"] = avg_price_impact_bps
        if median_price_impact_bps is not UNSET:
            field_dict["median_price_impact_bps"] = median_price_impact_bps
        if price_impact_swaps is not UNSET:
            field_dict["price_impact_swaps"] = price_impact_swaps
        if pubkey is not UNSET:
            field_dict["pubkey"] = pubkey
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        avg_price_impact_bps = d.pop("avg_price_impact_bps", UNSET)

        median_price_impact_bps = d.pop("median_price_impact_bps", UNSET)

        price_impact_swaps = d.pop("price_impact_swaps", UNSET)

        pubkey = d.pop("pubkey", UNSET)

        _window = d.pop("window", UNSET)
        window: PulsightInternalCoreDomainAggregatorWindow | Unset
        if isinstance(_window, Unset):
            window = UNSET
        else:
            window = PulsightInternalCoreDomainAggregatorWindow(_window)

        pulsight_internal_core_domain_aggregator_trader_price_impact_stats = cls(
            avg_price_impact_bps=avg_price_impact_bps,
            median_price_impact_bps=median_price_impact_bps,
            price_impact_swaps=price_impact_swaps,
            pubkey=pubkey,
            window=window,
        )

        pulsight_internal_core_domain_aggregator_trader_price_impact_stats.additional_properties = d
        return pulsight_internal_core_domain_aggregator_trader_price_impact_stats

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
