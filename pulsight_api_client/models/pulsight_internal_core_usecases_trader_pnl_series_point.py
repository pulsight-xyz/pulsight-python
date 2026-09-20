from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreUsecasesTraderPnlSeriesPoint")


@_attrs_define
class PulsightInternalCoreUsecasesTraderPnlSeriesPoint:
    """
    Attributes:
        arb_pnl (int | Unset): ArbPnl is the day's arbitrage take-home (tx-grain). It is
            ALREADY included in Profit and Net — exposed separately so the UI can
            show the split. Arb round-trip rows book zero realized PnL upstream,
            so the inclusion never double-counts.
        arb_pnl_usd (int | Unset):
        cashback (int | Unset):
        cashback_usd (int | Unset):
        day (str | Unset):
        failed_cost (int | Unset):
        failed_cost_usd (int | Unset):
        failed_txs (int | Unset):
        fees (int | Unset): Costs of the day (lamports): per-tx fees, tips, and failed-tx burn,
            against what pump paid the wallet that day — cashback CLAIMED and
            holder rewards RECEIVED, both cash basis — with `net = profit - fees
            - tips - failed_cost + cashback + holder_rewards` (profit already
            includes the arbitrage take-home). The charts plot NET as the headline
            series; `profit` stays as the flat/gross component.
        fees_usd (int | Unset):
        holder_reward_payouts (int | Unset):
        holder_rewards (int | Unset): HolderRewards is the day's holder-reward payouts valued in SOL, and
            HolderRewardPayouts how many payouts there were. A payout in a quote
            we cannot price in SOL adds nothing to the value but still counts, so
            a day can carry payouts with zero lamports.
        holder_rewards_usd (int | Unset):
        net (int | Unset):
        net_usd (int | Unset):
        profit (int | Unset):
        profit_usd (int | Unset): The Usd twins are the same day's figures on the trades' USD stamps
            (micro-USD).
        success_rate (float | Unset):
        tips (int | Unset):
        tips_usd (int | Unset):
        txs (int | Unset): Txs is the day's landed transaction count; FailedTxs the failed-tx
            ledger's failed swaps+arbs+other. SuccessRate divides the OBSERVED
            landed count (the `observed_hours` only) by observed+failed — nil
            when no hour of the day was observed, so unobserved history reads
            "not measured" rather than a fake 100%.
    """

    arb_pnl: int | Unset = UNSET
    arb_pnl_usd: int | Unset = UNSET
    cashback: int | Unset = UNSET
    cashback_usd: int | Unset = UNSET
    day: str | Unset = UNSET
    failed_cost: int | Unset = UNSET
    failed_cost_usd: int | Unset = UNSET
    failed_txs: int | Unset = UNSET
    fees: int | Unset = UNSET
    fees_usd: int | Unset = UNSET
    holder_reward_payouts: int | Unset = UNSET
    holder_rewards: int | Unset = UNSET
    holder_rewards_usd: int | Unset = UNSET
    net: int | Unset = UNSET
    net_usd: int | Unset = UNSET
    profit: int | Unset = UNSET
    profit_usd: int | Unset = UNSET
    success_rate: float | Unset = UNSET
    tips: int | Unset = UNSET
    tips_usd: int | Unset = UNSET
    txs: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        arb_pnl = self.arb_pnl

        arb_pnl_usd = self.arb_pnl_usd

        cashback = self.cashback

        cashback_usd = self.cashback_usd

        day = self.day

        failed_cost = self.failed_cost

        failed_cost_usd = self.failed_cost_usd

        failed_txs = self.failed_txs

        fees = self.fees

        fees_usd = self.fees_usd

        holder_reward_payouts = self.holder_reward_payouts

        holder_rewards = self.holder_rewards

        holder_rewards_usd = self.holder_rewards_usd

        net = self.net

        net_usd = self.net_usd

        profit = self.profit

        profit_usd = self.profit_usd

        success_rate = self.success_rate

        tips = self.tips

        tips_usd = self.tips_usd

        txs = self.txs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if arb_pnl is not UNSET:
            field_dict["arb_pnl"] = arb_pnl
        if arb_pnl_usd is not UNSET:
            field_dict["arb_pnl_usd"] = arb_pnl_usd
        if cashback is not UNSET:
            field_dict["cashback"] = cashback
        if cashback_usd is not UNSET:
            field_dict["cashback_usd"] = cashback_usd
        if day is not UNSET:
            field_dict["day"] = day
        if failed_cost is not UNSET:
            field_dict["failed_cost"] = failed_cost
        if failed_cost_usd is not UNSET:
            field_dict["failed_cost_usd"] = failed_cost_usd
        if failed_txs is not UNSET:
            field_dict["failed_txs"] = failed_txs
        if fees is not UNSET:
            field_dict["fees"] = fees
        if fees_usd is not UNSET:
            field_dict["fees_usd"] = fees_usd
        if holder_reward_payouts is not UNSET:
            field_dict["holder_reward_payouts"] = holder_reward_payouts
        if holder_rewards is not UNSET:
            field_dict["holder_rewards"] = holder_rewards
        if holder_rewards_usd is not UNSET:
            field_dict["holder_rewards_usd"] = holder_rewards_usd
        if net is not UNSET:
            field_dict["net"] = net
        if net_usd is not UNSET:
            field_dict["net_usd"] = net_usd
        if profit is not UNSET:
            field_dict["profit"] = profit
        if profit_usd is not UNSET:
            field_dict["profit_usd"] = profit_usd
        if success_rate is not UNSET:
            field_dict["success_rate"] = success_rate
        if tips is not UNSET:
            field_dict["tips"] = tips
        if tips_usd is not UNSET:
            field_dict["tips_usd"] = tips_usd
        if txs is not UNSET:
            field_dict["txs"] = txs

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        arb_pnl = d.pop("arb_pnl", UNSET)

        arb_pnl_usd = d.pop("arb_pnl_usd", UNSET)

        cashback = d.pop("cashback", UNSET)

        cashback_usd = d.pop("cashback_usd", UNSET)

        day = d.pop("day", UNSET)

        failed_cost = d.pop("failed_cost", UNSET)

        failed_cost_usd = d.pop("failed_cost_usd", UNSET)

        failed_txs = d.pop("failed_txs", UNSET)

        fees = d.pop("fees", UNSET)

        fees_usd = d.pop("fees_usd", UNSET)

        holder_reward_payouts = d.pop("holder_reward_payouts", UNSET)

        holder_rewards = d.pop("holder_rewards", UNSET)

        holder_rewards_usd = d.pop("holder_rewards_usd", UNSET)

        net = d.pop("net", UNSET)

        net_usd = d.pop("net_usd", UNSET)

        profit = d.pop("profit", UNSET)

        profit_usd = d.pop("profit_usd", UNSET)

        success_rate = d.pop("success_rate", UNSET)

        tips = d.pop("tips", UNSET)

        tips_usd = d.pop("tips_usd", UNSET)

        txs = d.pop("txs", UNSET)

        pulsight_internal_core_usecases_trader_pnl_series_point = cls(
            arb_pnl=arb_pnl,
            arb_pnl_usd=arb_pnl_usd,
            cashback=cashback,
            cashback_usd=cashback_usd,
            day=day,
            failed_cost=failed_cost,
            failed_cost_usd=failed_cost_usd,
            failed_txs=failed_txs,
            fees=fees,
            fees_usd=fees_usd,
            holder_reward_payouts=holder_reward_payouts,
            holder_rewards=holder_rewards,
            holder_rewards_usd=holder_rewards_usd,
            net=net,
            net_usd=net_usd,
            profit=profit,
            profit_usd=profit_usd,
            success_rate=success_rate,
            tips=tips,
            tips_usd=tips_usd,
            txs=txs,
        )

        pulsight_internal_core_usecases_trader_pnl_series_point.additional_properties = d
        return pulsight_internal_core_usecases_trader_pnl_series_point

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
