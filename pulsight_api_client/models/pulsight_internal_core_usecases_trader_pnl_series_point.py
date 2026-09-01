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
        cashback (int | Unset):
        day (str | Unset):
        failed_cost (int | Unset):
        failed_txs (int | Unset):
        fees (int | Unset): Costs of the day (lamports): per-tx fees, tips, and failed-tx burn,
            plus the day's CLAIMED pump cashback (cash basis, the one positive
            component), with `net = profit - fees - tips - failed_cost +
            cashback`. The charts plot NET as the headline series; `profit` stays
            as the flat/gross component.
        net (int | Unset):
        profit (int | Unset):
        success_rate (float | Unset):
        tips (int | Unset):
        txs (int | Unset): Txs is the day's landed transaction count; FailedTxs the failed-tx
            ledger's failed swaps+arbs+other. SuccessRate divides the OBSERVED
            landed count (failed-tx-watched hours only, CA 000096) by
            observed+failed — nil when no hour of the day was observed, so
            pre-ledger history reads "not measured" rather than a fake 100%.
    """

    cashback: int | Unset = UNSET
    day: str | Unset = UNSET
    failed_cost: int | Unset = UNSET
    failed_txs: int | Unset = UNSET
    fees: int | Unset = UNSET
    net: int | Unset = UNSET
    profit: int | Unset = UNSET
    success_rate: float | Unset = UNSET
    tips: int | Unset = UNSET
    txs: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cashback = self.cashback

        day = self.day

        failed_cost = self.failed_cost

        failed_txs = self.failed_txs

        fees = self.fees

        net = self.net

        profit = self.profit

        success_rate = self.success_rate

        tips = self.tips

        txs = self.txs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cashback is not UNSET:
            field_dict["cashback"] = cashback
        if day is not UNSET:
            field_dict["day"] = day
        if failed_cost is not UNSET:
            field_dict["failed_cost"] = failed_cost
        if failed_txs is not UNSET:
            field_dict["failed_txs"] = failed_txs
        if fees is not UNSET:
            field_dict["fees"] = fees
        if net is not UNSET:
            field_dict["net"] = net
        if profit is not UNSET:
            field_dict["profit"] = profit
        if success_rate is not UNSET:
            field_dict["success_rate"] = success_rate
        if tips is not UNSET:
            field_dict["tips"] = tips
        if txs is not UNSET:
            field_dict["txs"] = txs

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        cashback = d.pop("cashback", UNSET)

        day = d.pop("day", UNSET)

        failed_cost = d.pop("failed_cost", UNSET)

        failed_txs = d.pop("failed_txs", UNSET)

        fees = d.pop("fees", UNSET)

        net = d.pop("net", UNSET)

        profit = d.pop("profit", UNSET)

        success_rate = d.pop("success_rate", UNSET)

        tips = d.pop("tips", UNSET)

        txs = d.pop("txs", UNSET)

        pulsight_internal_core_usecases_trader_pnl_series_point = cls(
            cashback=cashback,
            day=day,
            failed_cost=failed_cost,
            failed_txs=failed_txs,
            fees=fees,
            net=net,
            profit=profit,
            success_rate=success_rate,
            tips=tips,
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
