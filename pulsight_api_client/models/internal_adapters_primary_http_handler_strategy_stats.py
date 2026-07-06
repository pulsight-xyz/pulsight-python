from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InternalAdaptersPrimaryHttpHandlerStrategyStats")


@_attrs_define
class InternalAdaptersPrimaryHttpHandlerStrategyStats:
    """
    Attributes:
        draft (bool | Unset):
        equity_points (list[float] | Unset): EquityPoints is the cumulative-P&L curve across the most
            recent ≤20 `done` runs, ordered ascending by finished_at.
            Each element is the running sum of `summary.total_pnl_sol`
            through that run, so a frontend <polyline> over these points
            renders the dashboard sparkline directly.
        last_run_at (str | Unset):
        last_run_pnl_sol (float | Unset):
        last_run_status (str | Unset):
        last_run_trades (int | Unset):
        last_run_win_rate_pct (float | Unset):
        total_runs (int | Unset):
    """

    draft: bool | Unset = UNSET
    equity_points: list[float] | Unset = UNSET
    last_run_at: str | Unset = UNSET
    last_run_pnl_sol: float | Unset = UNSET
    last_run_status: str | Unset = UNSET
    last_run_trades: int | Unset = UNSET
    last_run_win_rate_pct: float | Unset = UNSET
    total_runs: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        draft = self.draft

        equity_points: list[float] | Unset = UNSET
        if not isinstance(self.equity_points, Unset):
            equity_points = self.equity_points

        last_run_at = self.last_run_at

        last_run_pnl_sol = self.last_run_pnl_sol

        last_run_status = self.last_run_status

        last_run_trades = self.last_run_trades

        last_run_win_rate_pct = self.last_run_win_rate_pct

        total_runs = self.total_runs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if draft is not UNSET:
            field_dict["draft"] = draft
        if equity_points is not UNSET:
            field_dict["equity_points"] = equity_points
        if last_run_at is not UNSET:
            field_dict["last_run_at"] = last_run_at
        if last_run_pnl_sol is not UNSET:
            field_dict["last_run_pnl_sol"] = last_run_pnl_sol
        if last_run_status is not UNSET:
            field_dict["last_run_status"] = last_run_status
        if last_run_trades is not UNSET:
            field_dict["last_run_trades"] = last_run_trades
        if last_run_win_rate_pct is not UNSET:
            field_dict["last_run_win_rate_pct"] = last_run_win_rate_pct
        if total_runs is not UNSET:
            field_dict["total_runs"] = total_runs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        draft = d.pop("draft", UNSET)

        equity_points = cast(list[float], d.pop("equity_points", UNSET))

        last_run_at = d.pop("last_run_at", UNSET)

        last_run_pnl_sol = d.pop("last_run_pnl_sol", UNSET)

        last_run_status = d.pop("last_run_status", UNSET)

        last_run_trades = d.pop("last_run_trades", UNSET)

        last_run_win_rate_pct = d.pop("last_run_win_rate_pct", UNSET)

        total_runs = d.pop("total_runs", UNSET)

        internal_adapters_primary_http_handler_strategy_stats = cls(
            draft=draft,
            equity_points=equity_points,
            last_run_at=last_run_at,
            last_run_pnl_sol=last_run_pnl_sol,
            last_run_status=last_run_status,
            last_run_trades=last_run_trades,
            last_run_win_rate_pct=last_run_win_rate_pct,
            total_runs=total_runs,
        )

        internal_adapters_primary_http_handler_strategy_stats.additional_properties = d
        return internal_adapters_primary_http_handler_strategy_stats

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
