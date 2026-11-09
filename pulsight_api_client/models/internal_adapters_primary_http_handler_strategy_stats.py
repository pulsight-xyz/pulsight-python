from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.internal_adapters_primary_http_handler_strategy_run_point import (
        InternalAdaptersPrimaryHttpHandlerStrategyRunPoint,
    )


T = TypeVar("T", bound="InternalAdaptersPrimaryHttpHandlerStrategyStats")


@_attrs_define
class InternalAdaptersPrimaryHttpHandlerStrategyStats:
    """
    Attributes:
        draft (bool | Unset):
        last_run_at (str | Unset): LastRunAt is when that run finished, or when it was submitted
            while it has not finished.
        last_run_pnl_sol (float | Unset): LastRunPnlSol is that run's summary.total_pnl_sol; null until
            the run has a summary.
        last_run_status (str | Unset): LastRunStatus is the status of the newest run by created_at,
            whatever its outcome.
        last_run_trades (int | Unset): LastRunTrades is that run's summary.trades: every fill, buys
            included.
        last_run_win_rate_pct (float | Unset): LastRunWinRatePct is that run's wins / (wins + losses) × 100, the
            win rate the run page shows; null until the run has closed a trade.
        run_points (list[InternalAdaptersPrimaryHttpHandlerStrategyRunPoint] | Unset): RunPoints is one point per `done`
            run among the newest 20 by
            created_at, in ascending created_at order. Each point carries
            that run's own total_pnl_sol, never a running sum: runs differ
            in window and scope, so their PnL does not add up to an equity.
        total_runs (int | Unset):
    """

    draft: bool | Unset = UNSET
    last_run_at: str | Unset = UNSET
    last_run_pnl_sol: float | Unset = UNSET
    last_run_status: str | Unset = UNSET
    last_run_trades: int | Unset = UNSET
    last_run_win_rate_pct: float | Unset = UNSET
    run_points: list[InternalAdaptersPrimaryHttpHandlerStrategyRunPoint] | Unset = UNSET
    total_runs: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        draft = self.draft

        last_run_at = self.last_run_at

        last_run_pnl_sol = self.last_run_pnl_sol

        last_run_status = self.last_run_status

        last_run_trades = self.last_run_trades

        last_run_win_rate_pct = self.last_run_win_rate_pct

        run_points: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.run_points, Unset):
            run_points = []
            for run_points_item_data in self.run_points:
                run_points_item = run_points_item_data.to_dict()
                run_points.append(run_points_item)

        total_runs = self.total_runs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if draft is not UNSET:
            field_dict["draft"] = draft
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
        if run_points is not UNSET:
            field_dict["run_points"] = run_points
        if total_runs is not UNSET:
            field_dict["total_runs"] = total_runs

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.internal_adapters_primary_http_handler_strategy_run_point import (
            InternalAdaptersPrimaryHttpHandlerStrategyRunPoint,
        )

        d = dict(src_dict)
        draft = d.pop("draft", UNSET)

        last_run_at = d.pop("last_run_at", UNSET)

        last_run_pnl_sol = d.pop("last_run_pnl_sol", UNSET)

        last_run_status = d.pop("last_run_status", UNSET)

        last_run_trades = d.pop("last_run_trades", UNSET)

        last_run_win_rate_pct = d.pop("last_run_win_rate_pct", UNSET)

        _run_points = d.pop("run_points", UNSET)
        run_points: list[InternalAdaptersPrimaryHttpHandlerStrategyRunPoint] | Unset = (
            UNSET
        )
        if _run_points is not UNSET:
            run_points = []
            for run_points_item_data in _run_points:
                run_points_item = (
                    InternalAdaptersPrimaryHttpHandlerStrategyRunPoint.from_dict(
                        run_points_item_data
                    )
                )

                run_points.append(run_points_item)

        total_runs = d.pop("total_runs", UNSET)

        internal_adapters_primary_http_handler_strategy_stats = cls(
            draft=draft,
            last_run_at=last_run_at,
            last_run_pnl_sol=last_run_pnl_sol,
            last_run_status=last_run_status,
            last_run_trades=last_run_trades,
            last_run_win_rate_pct=last_run_win_rate_pct,
            run_points=run_points,
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
