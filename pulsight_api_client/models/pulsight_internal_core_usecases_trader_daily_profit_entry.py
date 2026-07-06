from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreUsecasesTraderDailyProfitEntry")


@_attrs_define
class PulsightInternalCoreUsecasesTraderDailyProfitEntry:
    """
    Attributes:
        date (str | Unset):
        total_profit (float | Unset):
    """

    date: str | Unset = UNSET
    total_profit: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        total_profit = self.total_profit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if total_profit is not UNSET:
            field_dict["total_profit"] = total_profit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date", UNSET)

        total_profit = d.pop("total_profit", UNSET)

        pulsight_internal_core_usecases_trader_daily_profit_entry = cls(
            date=date,
            total_profit=total_profit,
        )

        pulsight_internal_core_usecases_trader_daily_profit_entry.additional_properties = d
        return pulsight_internal_core_usecases_trader_daily_profit_entry

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
