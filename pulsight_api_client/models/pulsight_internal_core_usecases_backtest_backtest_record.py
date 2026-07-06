from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pulsight_internal_core_domain_aggregator_timeframe import (
    PulsightInternalCoreDomainAggregatorTimeframe,
)
from ..models.pulsight_internal_core_usecases_backtest_backtest_status import (
    PulsightInternalCoreUsecasesBacktestBacktestStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pulsight_internal_core_domain_strategy_strategy_def import (
        PulsightInternalCoreDomainStrategyStrategyDef,
    )
    from ..models.pulsight_internal_core_usecases_backtest_backtest_summary import (
        PulsightInternalCoreUsecasesBacktestBacktestSummary,
    )
    from ..models.pulsight_internal_core_usecases_backtest_token_scope import (
        PulsightInternalCoreUsecasesBacktestTokenScope,
    )


T = TypeVar("T", bound="PulsightInternalCoreUsecasesBacktestBacktestRecord")


@_attrs_define
class PulsightInternalCoreUsecasesBacktestBacktestRecord:
    """
    Attributes:
        created_at (str | Unset):
        error (str | Unset):
        finished_at (str | Unset):
        id (str | Unset):
        progress_note (str | Unset):
        progress_pct (int | Unset):
        scope (PulsightInternalCoreUsecasesBacktestTokenScope | Unset):
        started_at (str | Unset):
        starting_balance_sol (float | Unset):
        status (PulsightInternalCoreUsecasesBacktestBacktestStatus | Unset):
        strategy_id (str | Unset):
        strategy_snapshot (PulsightInternalCoreDomainStrategyStrategyDef | Unset):
        summary (PulsightInternalCoreUsecasesBacktestBacktestSummary | Unset):
        target_trader (str | Unset):
        time_from (str | Unset):
        time_to (str | Unset):
        timeframe (PulsightInternalCoreDomainAggregatorTimeframe | Unset):
        user_id (str | Unset):
    """

    created_at: str | Unset = UNSET
    error: str | Unset = UNSET
    finished_at: str | Unset = UNSET
    id: str | Unset = UNSET
    progress_note: str | Unset = UNSET
    progress_pct: int | Unset = UNSET
    scope: PulsightInternalCoreUsecasesBacktestTokenScope | Unset = UNSET
    started_at: str | Unset = UNSET
    starting_balance_sol: float | Unset = UNSET
    status: PulsightInternalCoreUsecasesBacktestBacktestStatus | Unset = UNSET
    strategy_id: str | Unset = UNSET
    strategy_snapshot: PulsightInternalCoreDomainStrategyStrategyDef | Unset = UNSET
    summary: PulsightInternalCoreUsecasesBacktestBacktestSummary | Unset = UNSET
    target_trader: str | Unset = UNSET
    time_from: str | Unset = UNSET
    time_to: str | Unset = UNSET
    timeframe: PulsightInternalCoreDomainAggregatorTimeframe | Unset = UNSET
    user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        error = self.error

        finished_at = self.finished_at

        id = self.id

        progress_note = self.progress_note

        progress_pct = self.progress_pct

        scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()

        started_at = self.started_at

        starting_balance_sol = self.starting_balance_sol

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        strategy_id = self.strategy_id

        strategy_snapshot: dict[str, Any] | Unset = UNSET
        if not isinstance(self.strategy_snapshot, Unset):
            strategy_snapshot = self.strategy_snapshot.to_dict()

        summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()

        target_trader = self.target_trader

        time_from = self.time_from

        time_to = self.time_to

        timeframe: str | Unset = UNSET
        if not isinstance(self.timeframe, Unset):
            timeframe = self.timeframe.value

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if error is not UNSET:
            field_dict["error"] = error
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at
        if id is not UNSET:
            field_dict["id"] = id
        if progress_note is not UNSET:
            field_dict["progress_note"] = progress_note
        if progress_pct is not UNSET:
            field_dict["progress_pct"] = progress_pct
        if scope is not UNSET:
            field_dict["scope"] = scope
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if starting_balance_sol is not UNSET:
            field_dict["starting_balance_sol"] = starting_balance_sol
        if status is not UNSET:
            field_dict["status"] = status
        if strategy_id is not UNSET:
            field_dict["strategy_id"] = strategy_id
        if strategy_snapshot is not UNSET:
            field_dict["strategy_snapshot"] = strategy_snapshot
        if summary is not UNSET:
            field_dict["summary"] = summary
        if target_trader is not UNSET:
            field_dict["target_trader"] = target_trader
        if time_from is not UNSET:
            field_dict["time_from"] = time_from
        if time_to is not UNSET:
            field_dict["time_to"] = time_to
        if timeframe is not UNSET:
            field_dict["timeframe"] = timeframe
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pulsight_internal_core_domain_strategy_strategy_def import (
            PulsightInternalCoreDomainStrategyStrategyDef,
        )
        from ..models.pulsight_internal_core_usecases_backtest_backtest_summary import (
            PulsightInternalCoreUsecasesBacktestBacktestSummary,
        )
        from ..models.pulsight_internal_core_usecases_backtest_token_scope import (
            PulsightInternalCoreUsecasesBacktestTokenScope,
        )

        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        error = d.pop("error", UNSET)

        finished_at = d.pop("finished_at", UNSET)

        id = d.pop("id", UNSET)

        progress_note = d.pop("progress_note", UNSET)

        progress_pct = d.pop("progress_pct", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: PulsightInternalCoreUsecasesBacktestTokenScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = PulsightInternalCoreUsecasesBacktestTokenScope.from_dict(_scope)

        started_at = d.pop("started_at", UNSET)

        starting_balance_sol = d.pop("starting_balance_sol", UNSET)

        _status = d.pop("status", UNSET)
        status: PulsightInternalCoreUsecasesBacktestBacktestStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PulsightInternalCoreUsecasesBacktestBacktestStatus(_status)

        strategy_id = d.pop("strategy_id", UNSET)

        _strategy_snapshot = d.pop("strategy_snapshot", UNSET)
        strategy_snapshot: PulsightInternalCoreDomainStrategyStrategyDef | Unset
        if isinstance(_strategy_snapshot, Unset):
            strategy_snapshot = UNSET
        else:
            strategy_snapshot = PulsightInternalCoreDomainStrategyStrategyDef.from_dict(
                _strategy_snapshot
            )

        _summary = d.pop("summary", UNSET)
        summary: PulsightInternalCoreUsecasesBacktestBacktestSummary | Unset
        if isinstance(_summary, Unset):
            summary = UNSET
        else:
            summary = PulsightInternalCoreUsecasesBacktestBacktestSummary.from_dict(
                _summary
            )

        target_trader = d.pop("target_trader", UNSET)

        time_from = d.pop("time_from", UNSET)

        time_to = d.pop("time_to", UNSET)

        _timeframe = d.pop("timeframe", UNSET)
        timeframe: PulsightInternalCoreDomainAggregatorTimeframe | Unset
        if isinstance(_timeframe, Unset):
            timeframe = UNSET
        else:
            timeframe = PulsightInternalCoreDomainAggregatorTimeframe(_timeframe)

        user_id = d.pop("user_id", UNSET)

        pulsight_internal_core_usecases_backtest_backtest_record = cls(
            created_at=created_at,
            error=error,
            finished_at=finished_at,
            id=id,
            progress_note=progress_note,
            progress_pct=progress_pct,
            scope=scope,
            started_at=started_at,
            starting_balance_sol=starting_balance_sol,
            status=status,
            strategy_id=strategy_id,
            strategy_snapshot=strategy_snapshot,
            summary=summary,
            target_trader=target_trader,
            time_from=time_from,
            time_to=time_to,
            timeframe=timeframe,
            user_id=user_id,
        )

        pulsight_internal_core_usecases_backtest_backtest_record.additional_properties = d
        return pulsight_internal_core_usecases_backtest_backtest_record

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
