from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorMintWindowStats")


@_attrs_define
class PulsightInternalCoreDomainAggregatorMintWindowStats:
    """
    Attributes:
        buy_swap_count (int | Unset):
        buy_volume_sol (int | Unset): SOL spent buying, in lamports.
        buy_volume_usd (int | Unset):
        net_buy_sol (int | Unset): buy_volume_sol - sell_volume_sol, in lamports.
        net_buy_usd (int | Unset):
        pool_sol (int | Unset): The reference pool's latest quote-side depth, in lamports.
        pool_usd (int | Unset):
        price_change_pct (float | Unset): (close - open) / open × 100 over the window.
        sell_swap_count (int | Unset):
        sell_volume_sol (int | Unset): SOL received from sells, in lamports.
        sell_volume_usd (int | Unset):
        swap_count (int | Unset):
        total_fees_sol (int | Unset): Total network fees paid trading the mint in the window, in lamports:
            tx fees (base + priority) plus MEV tips over its trades.
        total_fees_usd (int | Unset):
        volume_sol (int | Unset): Total SOL traded (buy + sell), in lamports.
        volume_usd (int | Unset): The Usd twins are the same figures on the trades' USD stamps
            (micro-USD), never lamports converted by a later rate.
    """

    buy_swap_count: int | Unset = UNSET
    buy_volume_sol: int | Unset = UNSET
    buy_volume_usd: int | Unset = UNSET
    net_buy_sol: int | Unset = UNSET
    net_buy_usd: int | Unset = UNSET
    pool_sol: int | Unset = UNSET
    pool_usd: int | Unset = UNSET
    price_change_pct: float | Unset = UNSET
    sell_swap_count: int | Unset = UNSET
    sell_volume_sol: int | Unset = UNSET
    sell_volume_usd: int | Unset = UNSET
    swap_count: int | Unset = UNSET
    total_fees_sol: int | Unset = UNSET
    total_fees_usd: int | Unset = UNSET
    volume_sol: int | Unset = UNSET
    volume_usd: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buy_swap_count = self.buy_swap_count

        buy_volume_sol = self.buy_volume_sol

        buy_volume_usd = self.buy_volume_usd

        net_buy_sol = self.net_buy_sol

        net_buy_usd = self.net_buy_usd

        pool_sol = self.pool_sol

        pool_usd = self.pool_usd

        price_change_pct = self.price_change_pct

        sell_swap_count = self.sell_swap_count

        sell_volume_sol = self.sell_volume_sol

        sell_volume_usd = self.sell_volume_usd

        swap_count = self.swap_count

        total_fees_sol = self.total_fees_sol

        total_fees_usd = self.total_fees_usd

        volume_sol = self.volume_sol

        volume_usd = self.volume_usd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if buy_swap_count is not UNSET:
            field_dict["buy_swap_count"] = buy_swap_count
        if buy_volume_sol is not UNSET:
            field_dict["buy_volume_sol"] = buy_volume_sol
        if buy_volume_usd is not UNSET:
            field_dict["buy_volume_usd"] = buy_volume_usd
        if net_buy_sol is not UNSET:
            field_dict["net_buy_sol"] = net_buy_sol
        if net_buy_usd is not UNSET:
            field_dict["net_buy_usd"] = net_buy_usd
        if pool_sol is not UNSET:
            field_dict["pool_sol"] = pool_sol
        if pool_usd is not UNSET:
            field_dict["pool_usd"] = pool_usd
        if price_change_pct is not UNSET:
            field_dict["price_change_pct"] = price_change_pct
        if sell_swap_count is not UNSET:
            field_dict["sell_swap_count"] = sell_swap_count
        if sell_volume_sol is not UNSET:
            field_dict["sell_volume_sol"] = sell_volume_sol
        if sell_volume_usd is not UNSET:
            field_dict["sell_volume_usd"] = sell_volume_usd
        if swap_count is not UNSET:
            field_dict["swap_count"] = swap_count
        if total_fees_sol is not UNSET:
            field_dict["total_fees_sol"] = total_fees_sol
        if total_fees_usd is not UNSET:
            field_dict["total_fees_usd"] = total_fees_usd
        if volume_sol is not UNSET:
            field_dict["volume_sol"] = volume_sol
        if volume_usd is not UNSET:
            field_dict["volume_usd"] = volume_usd

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        buy_swap_count = d.pop("buy_swap_count", UNSET)

        buy_volume_sol = d.pop("buy_volume_sol", UNSET)

        buy_volume_usd = d.pop("buy_volume_usd", UNSET)

        net_buy_sol = d.pop("net_buy_sol", UNSET)

        net_buy_usd = d.pop("net_buy_usd", UNSET)

        pool_sol = d.pop("pool_sol", UNSET)

        pool_usd = d.pop("pool_usd", UNSET)

        price_change_pct = d.pop("price_change_pct", UNSET)

        sell_swap_count = d.pop("sell_swap_count", UNSET)

        sell_volume_sol = d.pop("sell_volume_sol", UNSET)

        sell_volume_usd = d.pop("sell_volume_usd", UNSET)

        swap_count = d.pop("swap_count", UNSET)

        total_fees_sol = d.pop("total_fees_sol", UNSET)

        total_fees_usd = d.pop("total_fees_usd", UNSET)

        volume_sol = d.pop("volume_sol", UNSET)

        volume_usd = d.pop("volume_usd", UNSET)

        pulsight_internal_core_domain_aggregator_mint_window_stats = cls(
            buy_swap_count=buy_swap_count,
            buy_volume_sol=buy_volume_sol,
            buy_volume_usd=buy_volume_usd,
            net_buy_sol=net_buy_sol,
            net_buy_usd=net_buy_usd,
            pool_sol=pool_sol,
            pool_usd=pool_usd,
            price_change_pct=price_change_pct,
            sell_swap_count=sell_swap_count,
            sell_volume_sol=sell_volume_sol,
            sell_volume_usd=sell_volume_usd,
            swap_count=swap_count,
            total_fees_sol=total_fees_sol,
            total_fees_usd=total_fees_usd,
            volume_sol=volume_sol,
            volume_usd=volume_usd,
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
