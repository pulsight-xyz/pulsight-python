from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorMintWindowStats")


@_attrs_define
class PulsightInternalCoreDomainAggregatorMintWindowStats:
    """
    Attributes:
        buy_swap_count (int | Unset):
        buy_volume_sol (int | Unset): SOL spent buying, in lamports.
        net_buy_sol (int | Unset): buy_volume_sol - sell_volume_sol, in lamports.
        pool_sol (int | Unset): Most recent virtual_sol (pool size) observed in the window, in lamports.
        price_change_pct (float | Unset): (close - open) / open × 100 over the window.
        sell_swap_count (int | Unset):
        sell_volume_sol (int | Unset): SOL received from sells, in lamports.
        swap_count (int | Unset):
        volume_sol (int | Unset): Total SOL traded (buy + sell), in lamports.
    """

    buy_swap_count: int | Unset = UNSET
    buy_volume_sol: int | Unset = UNSET
    net_buy_sol: int | Unset = UNSET
    pool_sol: int | Unset = UNSET
    price_change_pct: float | Unset = UNSET
    sell_swap_count: int | Unset = UNSET
    sell_volume_sol: int | Unset = UNSET
    swap_count: int | Unset = UNSET
    volume_sol: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buy_swap_count = self.buy_swap_count

        buy_volume_sol = self.buy_volume_sol

        net_buy_sol = self.net_buy_sol

        pool_sol = self.pool_sol

        price_change_pct = self.price_change_pct

        sell_swap_count = self.sell_swap_count

        sell_volume_sol = self.sell_volume_sol

        swap_count = self.swap_count

        volume_sol = self.volume_sol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if buy_swap_count is not UNSET:
            field_dict["buy_swap_count"] = buy_swap_count
        if buy_volume_sol is not UNSET:
            field_dict["buy_volume_sol"] = buy_volume_sol
        if net_buy_sol is not UNSET:
            field_dict["net_buy_sol"] = net_buy_sol
        if pool_sol is not UNSET:
            field_dict["pool_sol"] = pool_sol
        if price_change_pct is not UNSET:
            field_dict["price_change_pct"] = price_change_pct
        if sell_swap_count is not UNSET:
            field_dict["sell_swap_count"] = sell_swap_count
        if sell_volume_sol is not UNSET:
            field_dict["sell_volume_sol"] = sell_volume_sol
        if swap_count is not UNSET:
            field_dict["swap_count"] = swap_count
        if volume_sol is not UNSET:
            field_dict["volume_sol"] = volume_sol

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        buy_swap_count = d.pop("buy_swap_count", UNSET)

        buy_volume_sol = d.pop("buy_volume_sol", UNSET)

        net_buy_sol = d.pop("net_buy_sol", UNSET)

        pool_sol = d.pop("pool_sol", UNSET)

        price_change_pct = d.pop("price_change_pct", UNSET)

        sell_swap_count = d.pop("sell_swap_count", UNSET)

        sell_volume_sol = d.pop("sell_volume_sol", UNSET)

        swap_count = d.pop("swap_count", UNSET)

        volume_sol = d.pop("volume_sol", UNSET)

        pulsight_internal_core_domain_aggregator_mint_window_stats = cls(
            buy_swap_count=buy_swap_count,
            buy_volume_sol=buy_volume_sol,
            net_buy_sol=net_buy_sol,
            pool_sol=pool_sol,
            price_change_pct=price_change_pct,
            sell_swap_count=sell_swap_count,
            sell_volume_sol=sell_volume_sol,
            swap_count=swap_count,
            volume_sol=volume_sol,
        )

        pulsight_internal_core_domain_aggregator_mint_window_stats.additional_properties = d
        return pulsight_internal_core_domain_aggregator_mint_window_stats

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
