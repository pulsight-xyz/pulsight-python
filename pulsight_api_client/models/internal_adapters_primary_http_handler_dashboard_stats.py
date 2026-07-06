from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.internal_adapters_primary_http_handler_best_run_ref import (
        InternalAdaptersPrimaryHttpHandlerBestRunRef,
    )


T = TypeVar("T", bound="InternalAdaptersPrimaryHttpHandlerDashboardStats")


@_attrs_define
class InternalAdaptersPrimaryHttpHandlerDashboardStats:
    """
    Attributes:
        aggregate_sim_pnl_sol (float | Unset):
        backtested_trades (int | Unset):
        best_run (InternalAdaptersPrimaryHttpHandlerBestRunRef | Unset):
        running_backtests (int | Unset):
        strategies_with_runs (int | Unset):
        total_strategies (int | Unset):
    """

    aggregate_sim_pnl_sol: float | Unset = UNSET
    backtested_trades: int | Unset = UNSET
    best_run: InternalAdaptersPrimaryHttpHandlerBestRunRef | Unset = UNSET
    running_backtests: int | Unset = UNSET
    strategies_with_runs: int | Unset = UNSET
    total_strategies: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aggregate_sim_pnl_sol = self.aggregate_sim_pnl_sol

        backtested_trades = self.backtested_trades

        best_run: dict[str, Any] | Unset = UNSET
        if not isinstance(self.best_run, Unset):
            best_run = self.best_run.to_dict()

        running_backtests = self.running_backtests

        strategies_with_runs = self.strategies_with_runs

        total_strategies = self.total_strategies

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aggregate_sim_pnl_sol is not UNSET:
            field_dict["aggregate_sim_pnl_sol"] = aggregate_sim_pnl_sol
        if backtested_trades is not UNSET:
            field_dict["backtested_trades"] = backtested_trades
        if best_run is not UNSET:
            field_dict["best_run"] = best_run
        if running_backtests is not UNSET:
            field_dict["running_backtests"] = running_backtests
        if strategies_with_runs is not UNSET:
            field_dict["strategies_with_runs"] = strategies_with_runs
        if total_strategies is not UNSET:
            field_dict["total_strategies"] = total_strategies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.internal_adapters_primary_http_handler_best_run_ref import (
            InternalAdaptersPrimaryHttpHandlerBestRunRef,
        )

        d = dict(src_dict)
        aggregate_sim_pnl_sol = d.pop("aggregate_sim_pnl_sol", UNSET)

        backtested_trades = d.pop("backtested_trades", UNSET)

        _best_run = d.pop("best_run", UNSET)
        best_run: InternalAdaptersPrimaryHttpHandlerBestRunRef | Unset
        if isinstance(_best_run, Unset):
            best_run = UNSET
        else:
            best_run = InternalAdaptersPrimaryHttpHandlerBestRunRef.from_dict(_best_run)

        running_backtests = d.pop("running_backtests", UNSET)

        strategies_with_runs = d.pop("strategies_with_runs", UNSET)

        total_strategies = d.pop("total_strategies", UNSET)

        internal_adapters_primary_http_handler_dashboard_stats = cls(
            aggregate_sim_pnl_sol=aggregate_sim_pnl_sol,
            backtested_trades=backtested_trades,
            best_run=best_run,
            running_backtests=running_backtests,
            strategies_with_runs=strategies_with_runs,
            total_strategies=total_strategies,
        )

        internal_adapters_primary_http_handler_dashboard_stats.additional_properties = d
        return internal_adapters_primary_http_handler_dashboard_stats

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
