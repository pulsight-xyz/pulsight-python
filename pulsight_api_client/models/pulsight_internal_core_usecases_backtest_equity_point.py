from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PulsightInternalCoreUsecasesBacktestEquityPoint")


@_attrs_define
class PulsightInternalCoreUsecasesBacktestEquityPoint:
    """
    Attributes:
        balance_sol (float | Unset):
        ts (str | Unset):
    """

    balance_sol: float | Unset = UNSET
    ts: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        balance_sol = self.balance_sol

        ts = self.ts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if balance_sol is not UNSET:
            field_dict["balance_sol"] = balance_sol
        if ts is not UNSET:
            field_dict["ts"] = ts

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        balance_sol = d.pop("balance_sol", UNSET)

        ts = d.pop("ts", UNSET)

        pulsight_internal_core_usecases_backtest_equity_point = cls(
            balance_sol=balance_sol,
            ts=ts,
        )

        pulsight_internal_core_usecases_backtest_equity_point.additional_properties = d
        return pulsight_internal_core_usecases_backtest_equity_point

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
