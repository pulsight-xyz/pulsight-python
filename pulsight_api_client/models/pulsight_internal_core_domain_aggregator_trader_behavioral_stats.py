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

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorTraderBehavioralStats")


@_attrs_define
class PulsightInternalCoreDomainAggregatorTraderBehavioralStats:
    """
    Attributes:
        active_hours_count (int | Unset):
        avg_buy_count_per_token (float | Unset):
        avg_holding_time_secs (float | Unset):
        avg_price_impact_bps (float | Unset): Mean price impact of the wallet's own fills, in basis points.
        avg_reactivity_secs (float | Unset):
        avg_sell_count_per_token (float | Unset):
        avg_trade_size_lamports (float | Unset): AvgTradeSizeLamports is TotalVolumeLamports over the window's swap
            count — the wallet's typical clip. It is what makes the price-impact
            figures below legible: impact is size against pool depth, so the two
            are read together.
        median_buy_count_per_token (float | Unset):
        median_holding_time_secs (float | Unset):
        median_price_impact_bps (float | Unset): Median price impact of the wallet's own fills, in basis points.
        median_reactivity_secs (float | Unset):
        median_sell_count_per_token (float | Unset):
        oldest_trade_at (str | Unset):
        price_impact_swaps (int | Unset): Swap legs the two impact figures were measured over. 0 = not measured.
        profit_per_trade_lamports (float | Unset):
        pubkey (str | Unset):
        rebalancing_ratio (float | Unset):
        total_volume_lamports (int | Unset): TotalVolumeLamports is the window's traded value in lamports, both
            sides. It reads the QUOTE side of each row (with non-WSOL quotes
            projected through `swaps.quote_lamports`) — see the adapter's
            swapQuoteLamportsExpr for why a plain `sum(amount_in)` is not that.
        window (PulsightInternalCoreDomainAggregatorWindow | Unset):
    """

    active_hours_count: int | Unset = UNSET
    avg_buy_count_per_token: float | Unset = UNSET
    avg_holding_time_secs: float | Unset = UNSET
    avg_price_impact_bps: float | Unset = UNSET
    avg_reactivity_secs: float | Unset = UNSET
    avg_sell_count_per_token: float | Unset = UNSET
    avg_trade_size_lamports: float | Unset = UNSET
    median_buy_count_per_token: float | Unset = UNSET
    median_holding_time_secs: float | Unset = UNSET
    median_price_impact_bps: float | Unset = UNSET
    median_reactivity_secs: float | Unset = UNSET
    median_sell_count_per_token: float | Unset = UNSET
    oldest_trade_at: str | Unset = UNSET
    price_impact_swaps: int | Unset = UNSET
    profit_per_trade_lamports: float | Unset = UNSET
    pubkey: str | Unset = UNSET
    rebalancing_ratio: float | Unset = UNSET
    total_volume_lamports: int | Unset = UNSET
    window: PulsightInternalCoreDomainAggregatorWindow | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_hours_count = self.active_hours_count

        avg_buy_count_per_token = self.avg_buy_count_per_token

        avg_holding_time_secs = self.avg_holding_time_secs

        avg_price_impact_bps = self.avg_price_impact_bps

        avg_reactivity_secs = self.avg_reactivity_secs

        avg_sell_count_per_token = self.avg_sell_count_per_token

        avg_trade_size_lamports = self.avg_trade_size_lamports

        median_buy_count_per_token = self.median_buy_count_per_token

        median_holding_time_secs = self.median_holding_time_secs

        median_price_impact_bps = self.median_price_impact_bps

        median_reactivity_secs = self.median_reactivity_secs

        median_sell_count_per_token = self.median_sell_count_per_token

        oldest_trade_at = self.oldest_trade_at

        price_impact_swaps = self.price_impact_swaps

        profit_per_trade_lamports = self.profit_per_trade_lamports

        pubkey = self.pubkey

        rebalancing_ratio = self.rebalancing_ratio

        total_volume_lamports = self.total_volume_lamports

        window: str | Unset = UNSET
        if not isinstance(self.window, Unset):
            window = self.window.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active_hours_count is not UNSET:
            field_dict["active_hours_count"] = active_hours_count
        if avg_buy_count_per_token is not UNSET:
            field_dict["avg_buy_count_per_token"] = avg_buy_count_per_token
        if avg_holding_time_secs is not UNSET:
            field_dict["avg_holding_time_secs"] = avg_holding_time_secs
        if avg_price_impact_bps is not UNSET:
            field_dict["avg_price_impact_bps"] = avg_price_impact_bps
        if avg_reactivity_secs is not UNSET:
            field_dict["avg_reactivity_secs"] = avg_reactivity_secs
        if avg_sell_count_per_token is not UNSET:
            field_dict["avg_sell_count_per_token"] = avg_sell_count_per_token
        if avg_trade_size_lamports is not UNSET:
            field_dict["avg_trade_size_lamports"] = avg_trade_size_lamports
        if median_buy_count_per_token is not UNSET:
            field_dict["median_buy_count_per_token"] = median_buy_count_per_token
        if median_holding_time_secs is not UNSET:
            field_dict["median_holding_time_secs"] = median_holding_time_secs
        if median_price_impact_bps is not UNSET:
            field_dict["median_price_impact_bps"] = median_price_impact_bps
        if median_reactivity_secs is not UNSET:
            field_dict["median_reactivity_secs"] = median_reactivity_secs
        if median_sell_count_per_token is not UNSET:
            field_dict["median_sell_count_per_token"] = median_sell_count_per_token
        if oldest_trade_at is not UNSET:
            field_dict["oldest_trade_at"] = oldest_trade_at
        if price_impact_swaps is not UNSET:
            field_dict["price_impact_swaps"] = price_impact_swaps
        if profit_per_trade_lamports is not UNSET:
            field_dict["profit_per_trade_lamports"] = profit_per_trade_lamports
        if pubkey is not UNSET:
            field_dict["pubkey"] = pubkey
        if rebalancing_ratio is not UNSET:
            field_dict["rebalancing_ratio"] = rebalancing_ratio
        if total_volume_lamports is not UNSET:
            field_dict["total_volume_lamports"] = total_volume_lamports
        if window is not UNSET:
            field_dict["window"] = window

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        active_hours_count = d.pop("active_hours_count", UNSET)

        avg_buy_count_per_token = d.pop("avg_buy_count_per_token", UNSET)

        avg_holding_time_secs = d.pop("avg_holding_time_secs", UNSET)

        avg_price_impact_bps = d.pop("avg_price_impact_bps", UNSET)

        avg_reactivity_secs = d.pop("avg_reactivity_secs", UNSET)

        avg_sell_count_per_token = d.pop("avg_sell_count_per_token", UNSET)

        avg_trade_size_lamports = d.pop("avg_trade_size_lamports", UNSET)

        median_buy_count_per_token = d.pop("median_buy_count_per_token", UNSET)

        median_holding_time_secs = d.pop("median_holding_time_secs", UNSET)

        median_price_impact_bps = d.pop("median_price_impact_bps", UNSET)

        median_reactivity_secs = d.pop("median_reactivity_secs", UNSET)

        median_sell_count_per_token = d.pop("median_sell_count_per_token", UNSET)

        oldest_trade_at = d.pop("oldest_trade_at", UNSET)

        price_impact_swaps = d.pop("price_impact_swaps", UNSET)

        profit_per_trade_lamports = d.pop("profit_per_trade_lamports", UNSET)

        pubkey = d.pop("pubkey", UNSET)

        rebalancing_ratio = d.pop("rebalancing_ratio", UNSET)

        total_volume_lamports = d.pop("total_volume_lamports", UNSET)

        _window = d.pop("window", UNSET)
        window: PulsightInternalCoreDomainAggregatorWindow | Unset
        if isinstance(_window, Unset):
            window = UNSET
        else:
            window = PulsightInternalCoreDomainAggregatorWindow(_window)

        pulsight_internal_core_domain_aggregator_trader_behavioral_stats = cls(
            active_hours_count=active_hours_count,
            avg_buy_count_per_token=avg_buy_count_per_token,
            avg_holding_time_secs=avg_holding_time_secs,
            avg_price_impact_bps=avg_price_impact_bps,
            avg_reactivity_secs=avg_reactivity_secs,
            avg_sell_count_per_token=avg_sell_count_per_token,
            avg_trade_size_lamports=avg_trade_size_lamports,
            median_buy_count_per_token=median_buy_count_per_token,
            median_holding_time_secs=median_holding_time_secs,
            median_price_impact_bps=median_price_impact_bps,
            median_reactivity_secs=median_reactivity_secs,
            median_sell_count_per_token=median_sell_count_per_token,
            oldest_trade_at=oldest_trade_at,
            price_impact_swaps=price_impact_swaps,
            profit_per_trade_lamports=profit_per_trade_lamports,
            pubkey=pubkey,
            rebalancing_ratio=rebalancing_ratio,
            total_volume_lamports=total_volume_lamports,
            window=window,
        )

        pulsight_internal_core_domain_aggregator_trader_behavioral_stats.additional_properties = d
        return pulsight_internal_core_domain_aggregator_trader_behavioral_stats

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
