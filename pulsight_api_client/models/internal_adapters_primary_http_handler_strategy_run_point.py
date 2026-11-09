from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalAdaptersPrimaryHttpHandlerStrategyRunPoint")


@_attrs_define
class InternalAdaptersPrimaryHttpHandlerStrategyRunPoint:
    """
    Attributes:
        backtest_id (str | Unset):
        created_at (str | Unset): CreatedAt is when the run was submitted, the key the series is
            ordered by.
        roi_pct (float | Unset):
        time_from (str | Unset): TimeFrom and TimeTo bound the window the run replayed.
        time_to (str | Unset):
        total_pnl_sol (float | Unset): TotalPnlSol is the run's summary.total_pnl_sol, not a running sum.
    """

    backtest_id: str | Unset = UNSET
    created_at: str | Unset = UNSET
    roi_pct: float | Unset = UNSET
    time_from: str | Unset = UNSET
    time_to: str | Unset = UNSET
    total_pnl_sol: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        backtest_id = self.backtest_id

        created_at = self.created_at

        roi_pct = self.roi_pct

        time_from = self.time_from

        time_to = self.time_to

        total_pnl_sol = self.total_pnl_sol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if backtest_id is not UNSET:
            field_dict["backtest_id"] = backtest_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if roi_pct is not UNSET:
            field_dict["roi_pct"] = roi_pct
        if time_from is not UNSET:
            field_dict["time_from"] = time_from
        if time_to is not UNSET:
            field_dict["time_to"] = time_to
        if total_pnl_sol is not UNSET:
            field_dict["total_pnl_sol"] = total_pnl_sol

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        backtest_id = d.pop("backtest_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        roi_pct = d.pop("roi_pct", UNSET)

        time_from = d.pop("time_from", UNSET)

        time_to = d.pop("time_to", UNSET)

        total_pnl_sol = d.pop("total_pnl_sol", UNSET)

        internal_adapters_primary_http_handler_strategy_run_point = cls(
            backtest_id=backtest_id,
            created_at=created_at,
            roi_pct=roi_pct,
            time_from=time_from,
            time_to=time_to,
            total_pnl_sol=total_pnl_sol,
        )

        internal_adapters_primary_http_handler_strategy_run_point.additional_properties = d
        return internal_adapters_primary_http_handler_strategy_run_point

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
