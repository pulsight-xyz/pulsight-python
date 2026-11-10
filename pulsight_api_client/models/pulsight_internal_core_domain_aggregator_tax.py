from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreDomainAggregatorTax")


@_attrs_define
class PulsightInternalCoreDomainAggregatorTax:
    """
    Attributes:
        buy_bps (int | Unset): BuyBps is the tax a buy pays, SwapFeeBps plus TransferFeeBps. Absent
            while either is unknown: the tax is then at least TransferFeeBps.
        dex (str | Unset): Dex is Pool's venue slug, same vocabulary as `?dex=`.
        holder_rewards (bool | Unset): HolderRewards reports that the creator share inside SwapFeeBps is paid
            to the coin's holders: the mint is a pump.fun holder-rewards coin and
            the pool is its own pump.fun curve or PumpSwap pool. Never set on a
            listing row, whose pool is not named.
        pool (str | Unset): Pool is the pool SwapFeeBps was read from: on the token page's row the
            mint's reference pool, the one its price is read from. Omitted on a
            listing row and on a market row, which is its own pool.
        sell_bps (int | Unset): SellBps is the tax a sell pays, on the same components as BuyBps.
        swap_fee_at (str | Unset): SwapFeeAt is the minute SwapFeeBps was recorded in. Omitted on a
            listing row.
        swap_fee_bps (int | Unset): SwapFeeBps is the pool's swap fee, the venue's whole schedule (LP,
            protocol, creator and partner shares): the highest fee its trades
            recorded in the latest minute that recorded one. Absent when no trade
            on the pool ever recorded a fee — unknown, never free.
        transfer_fee_bps (int | Unset): TransferFeeBps is the mint's Token-2022 transfer fee, the higher of its
            current and scheduled rate with its per-transfer cap not applied; 0 for
            a mint without one. Absent until the mint account has been read.
    """

    buy_bps: int | Unset = UNSET
    dex: str | Unset = UNSET
    holder_rewards: bool | Unset = UNSET
    pool: str | Unset = UNSET
    sell_bps: int | Unset = UNSET
    swap_fee_at: str | Unset = UNSET
    swap_fee_bps: int | Unset = UNSET
    transfer_fee_bps: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buy_bps = self.buy_bps

        dex = self.dex

        holder_rewards = self.holder_rewards

        pool = self.pool

        sell_bps = self.sell_bps

        swap_fee_at = self.swap_fee_at

        swap_fee_bps = self.swap_fee_bps

        transfer_fee_bps = self.transfer_fee_bps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if buy_bps is not UNSET:
            field_dict["buy_bps"] = buy_bps
        if dex is not UNSET:
            field_dict["dex"] = dex
        if holder_rewards is not UNSET:
            field_dict["holder_rewards"] = holder_rewards
        if pool is not UNSET:
            field_dict["pool"] = pool
        if sell_bps is not UNSET:
            field_dict["sell_bps"] = sell_bps
        if swap_fee_at is not UNSET:
            field_dict["swap_fee_at"] = swap_fee_at
        if swap_fee_bps is not UNSET:
            field_dict["swap_fee_bps"] = swap_fee_bps
        if transfer_fee_bps is not UNSET:
            field_dict["transfer_fee_bps"] = transfer_fee_bps

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        buy_bps = d.pop("buy_bps", UNSET)

        dex = d.pop("dex", UNSET)

        holder_rewards = d.pop("holder_rewards", UNSET)

        pool = d.pop("pool", UNSET)

        sell_bps = d.pop("sell_bps", UNSET)

        swap_fee_at = d.pop("swap_fee_at", UNSET)

        swap_fee_bps = d.pop("swap_fee_bps", UNSET)

        transfer_fee_bps = d.pop("transfer_fee_bps", UNSET)

        pulsight_internal_core_domain_aggregator_tax = cls(
            buy_bps=buy_bps,
            dex=dex,
            holder_rewards=holder_rewards,
            pool=pool,
            sell_bps=sell_bps,
            swap_fee_at=swap_fee_at,
            swap_fee_bps=swap_fee_bps,
            transfer_fee_bps=transfer_fee_bps,
        )

        pulsight_internal_core_domain_aggregator_tax.additional_properties = d
        return pulsight_internal_core_domain_aggregator_tax

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
