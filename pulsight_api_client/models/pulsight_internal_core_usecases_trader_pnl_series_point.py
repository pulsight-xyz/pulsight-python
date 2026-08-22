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
        day (str | Unset):
        failed_cost (int | Unset):
        fees (int | Unset): Costs of the day (lamports): per-tx fees, tips, and failed-tx burn,
            with `net = profit - fees - tips - failed_cost`. The charts plot NET
            as the headline series; `profit` stays as the flat/gross component.
        net (int | Unset):
        profit (int | Unset):
        tips (int | Unset):
    """

    day: str | Unset = UNSET
    failed_cost: int | Unset = UNSET
    fees: int | Unset = UNSET
    net: int | Unset = UNSET
    profit: int | Unset = UNSET
    tips: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day = self.day

        failed_cost = self.failed_cost

        fees = self.fees

        net = self.net

        profit = self.profit

        tips = self.tips

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if day is not UNSET:
            field_dict["day"] = day
        if failed_cost is not UNSET:
            field_dict["failed_cost"] = failed_cost
        if fees is not UNSET:
            field_dict["fees"] = fees
        if net is not UNSET:
            field_dict["net"] = net
        if profit is not UNSET:
            field_dict["profit"] = profit
        if tips is not UNSET:
            field_dict["tips"] = tips

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        day = d.pop("day", UNSET)

        failed_cost = d.pop("failed_cost", UNSET)

        fees = d.pop("fees", UNSET)

        net = d.pop("net", UNSET)

        profit = d.pop("profit", UNSET)

        tips = d.pop("tips", UNSET)

        pulsight_internal_core_usecases_trader_pnl_series_point = cls(
            day=day,
            failed_cost=failed_cost,
            fees=fees,
            net=net,
            profit=profit,
            tips=tips,
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
